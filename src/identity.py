"""Conservative identities shared by deduplication and longitudinal comparison."""
import re
from urllib.parse import parse_qs, urlsplit, urlunsplit


def aliases(record):
    title = " ".join(record.get("title", "").casefold().split())
    result = {f"title:{title}"} if title else set()
    url = record.get("url", "")
    aid = record.get("arxiv_id")
    match = re.search(r"arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,5}(?:v\d+)?)", url)
    if not aid and match:
        aid = match.group(1)
    if aid:
        result.add("arxiv:" + re.sub(r"v\d+$", "", aid))
    if url:
        parts = urlsplit(url)
        host = (parts.hostname or "").lower()
        if host == "openreview.net":
            forum = parse_qs(parts.query).get("id", [])
            if forum:
                result.add("openreview:" + forum[0])
        elif host in ("doi.org", "dx.doi.org"):
            result.add("doi:" + parts.path.lstrip("/").casefold())
        elif host not in ("arxiv.org", "www.arxiv.org"):
            # Ignore URL fragments, preserve meaningful query parameters.
            result.add("url:" + urlunsplit(("https", host, parts.path.rstrip("/"), parts.query, "")))
    return result


def identity_groups(records):
    """Union all aliases, including title-only → arXiv metadata enrichment."""
    parent = list(range(len(records)))
    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i
    seen = {}
    for i, record in enumerate(records):
        for key in aliases(record) | set(record.get("aliases", [])):
            if key in seen:
                parent[find(i)] = find(seen[key])
            seen[key] = i
    groups = {}
    for i in range(len(records)):
        groups.setdefault(find(i), []).append(i)
    return list(groups.values())
