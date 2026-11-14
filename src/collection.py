"""Query-level collection evidence. Empty responses are successes, not failures."""
from __future__ import annotations

from dataclasses import dataclass, field
from functools import wraps
from inspect import signature
from time import monotonic


@dataclass
class CollectionStats:
    source: str
    attempts: list[dict] = field(default_factory=list)
    context: dict = field(default_factory=dict)
    fatal_error: str | None = None
    skipped: bool = False

    def summary(self, papers=()) -> dict:
        # A recovered retry does not make a logical query fail.
        final = {a["query"]: a for a in self.attempts}
        failed = sum(a["status"] == "failed" for a in final.values())
        succeeded = len(final) - failed
        if self.skipped:
            status = "skipped"
        elif self.fatal_error or failed:
            status = "partial" if succeeded else "failed"
        elif not final:
            status = "unknown"
        else:
            status = "success"
        return {
            "source": self.source, "status": status,
            "queries_succeeded": succeeded, "queries_failed": failed,
            "request_attempts": len(self.attempts),
            "request_failures": sum(a["status"] == "failed" for a in self.attempts),
            "returned_records": sum(a.get("returned_records", 0) for a in final.values()),
            "collected_unique": len({p.get_id() for p in papers}),
            "context": self.context, "fatal_error": self.fatal_error,
            "attempts": self.attempts,
        }


def observed_query(fn):
    """Record final HTTP/parse outcomes, including failures caught by fetch()."""
    sig = signature(fn)

    @wraps(fn)
    def wrapped(self, *args, **kwargs):
        bound = sig.bind(self, *args, **kwargs)
        bound.apply_defaults()
        key = fn.__name__ + ":" + ",".join(
            f"{k}={v}" for k, v in bound.arguments.items() if k != "self"
        )
        started = monotonic()
        self._response_info = {}
        attempt = {"query": key}
        try:
            papers = fn(self, *args, **kwargs)
            attempt.update(status="success", parsed_records=len(papers), **self._response_info)
            return papers
        except Exception as exc:
            response = getattr(exc, "response", None)
            # Do not serialize exception strings: URLs/headers may contain credentials.
            attempt.update(status="failed", error_type=type(exc).__name__,
                           http_status=getattr(response, "status_code", None))
            raise
        finally:
            attempt["elapsed_seconds"] = round(monotonic() - started, 3)
            self.stats.attempts.append(attempt)
    return wrapped


def response_records(scraper, count: int, limit: int | None = None):
    scraper._response_info = {"returned_records": count,
                              "possibly_truncated": limit is not None and count >= limit}
