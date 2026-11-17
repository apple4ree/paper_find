# paper_find

매일 주요 1티어 학회와 HuggingFace Papers에서 **Agent / Harness / Finance** 관련 논문을 자동 수집·정리하는 도구입니다.

## 수집 대상

| 구분 | 소스 |
|------|------|
| **학회** | AAAI, NeurIPS, ICML, ICLR, CVPR, KDD |
| **큐레이션** | [HuggingFace Daily Papers](https://huggingface.co/papers) |
| **프리프린트** | arXiv (cs.AI · cs.LG · cs.CL · cs.CV · q-fin.*) |

## 토픽 키워드

- **Agent** — agent, multi-agent, autonomous agent, llm agent, agentic, tool-use, …
- **Harness** — harness, lm eval, evaluation framework, benchmark suite, …
- **Finance** — financial, trading, portfolio, stock market, fraud detection, algorithmic trading, …

## 결과물

매일 `output/YYYY-MM-DD.md` 파일이 생성됩니다 (최신 결과는 `output/latest.md`).

예시 출력:

```
# Daily Paper Digest — 2025-04-14 (Monday)
...
## Agent  (12)
### NeurIPS
- **[Paper Title](url)** — Author A, Author B et al.
  - NeurIPS 2024 · 🤗 Featured · 2025-04-13
  - Abstract snippet…
...
## Finance  (8)
### KDD
...
```

## 설치 및 실행

```bash
pip install -r requirements.txt

# 오늘 날짜 논문 수집
python main.py

# 특정 날짜 지정
python main.py --date 2025-04-10

# arXiv 제외 (빠른 실행)
python main.py --skip-arxiv

# Semantic Scholar API 키 사용 (요청 한도 확대)
SS_API_KEY=<your_key> python main.py
```

## 자동 스케줄 (GitHub Actions)

`.github/workflows/daily_papers.yml`이 매일 **UTC 09:00 (KST 18:00)** 에 실행을 예약합니다. 실제 시작 시각은 지연될 수 있습니다.

수동 실행은 Actions 탭 → **Daily Paper Digest** → **Run workflow** 에서 가능합니다.

### Secrets 설정 (선택)

| Secret | 설명 |
|--------|------|
| `SEMANTIC_SCHOLAR_API_KEY` | S2 API 키 (없어도 동작, 있으면 요청 한도 증가) |

## 프로젝트 구조

```
paper_find/
├── main.py                    # 진입점
├── requirements.txt
├── src/
│   ├── config.py              # 학회 목록, 키워드, 설정값
│   ├── models.py              # Paper 데이터 클래스
│   ├── processor.py           # 중복 제거 + 토픽 분류
│   ├── formatter.py           # Markdown 출력 포맷
│   └── scrapers/
│       ├── huggingface.py     # HuggingFace Daily Papers API
│       ├── semantic_scholar.py# Semantic Scholar 학회 논문
│       └── arxiv.py           # arXiv 일별 제출 논문
├── output/
│   ├── latest.md              # 최신 결과
│   └── YYYY-MM-DD.md          # 날짜별 아카이브
└── .github/workflows/
    └── daily_papers.yml       # 일별 자동 실행
```

## 수집 검증과 신규 논문 판별

보고서의 전체 논문 수는 **해당 실행에서 발견한 논문 수**입니다. 신규 발표 수가 아닙니다.
S2·OpenReview·HF 검색은 과거 논문도 발견하는 discovery 검색을 유지합니다.
`LOOKBACK_DAYS=3`은 중앙 날짜 분류와 arXiv 검색에 사용합니다. 과거 논문은 지우지 않고 별도 표시합니다.

매일 Markdown과 함께 `output/YYYY-MM-DD.json`을 저장합니다.

- `sources`: 성공/부분 실패/실패/skip/증거 부족 상태, 질의별 최종 결과, 재시도를 포함한 요청 실패 수, HTTP 상태, 응답 레코드 수, 파싱 후 수집 고유 수, 보고서 포함 수.
- `context`: 실제 검색 기간·학회 연도·HF fallback으로 사용한 날짜. HTTP 정상 0건과 오류로 인한 0건을 구분합니다.
- `papers`: 식별자, 관측 수집원, 발표일 근거, 최초 관측 보고서 날짜, 보고서 포함 여부. 토픽 필터에서 빠진 수집 결과도 이력에 보존합니다.
- `changes`: 전날 보고서 대비 added/existing/missing과 누적 이력 기준 first-seen을 분리합니다. 하루 빠졌다가 재등장한 논문은 added일 수 있지만 first-seen은 아닙니다.
- `changes_url`: 별도 URL 기준 변화 목록. arXiv 버전·OpenReview/DOI·동일 제목을 연결한 논문 식별 기준 변화와 다를 수 있습니다.

신규 발견 논문은 `recent` / `older` / `unknown`으로 나눕니다. future 날짜도 신규 발표에서 제외합니다.
`recent`는 목표 날짜까지 포함한 최근 3일 안의 확인 가능한 publication/submission 날짜가 필요합니다.
과거 학회 연도나 오래된 arXiv 월 식별자가 있으면 새 수집일·새 학회 발표일만으로 recent가 되지 않습니다.
OpenReview record 생성/수정 시각과 HF 외부 큐레이션 날짜는 발표일로 인정하지 않습니다.
같은 논문의 확인 가능한 발표일이 여럿이면 가장 이른 날짜를 보존합니다.

기존 Markdown만 있는 날짜는 URL·제목·표시된 날짜로 이력을 초기화합니다. 이 자료에는 원시 응답이나
토픽에서 제외된 논문이 없으므로 최초 관측은 **보존된 이력 안에서의 최초 관측**입니다.
직전 달력 날짜 자료가 없으면 전날 비교를 unavailable로 표시합니다. 과거 날짜를 재실행해도 미래 자료를
비교 기준으로 삼지 않고 `latest.md`를 과거 보고서로 덮어쓰지 않습니다.

### 급변 검증

기본 경보는 직전 날짜 대비 50% 이상 감소, 2배 이상 증가, 이전 보고서 논문의 50% 이상 미관측,
부분 실패/실패/상태 미확인입니다. 건수 비교는 이전 건수가 20 이상일 때만 수행합니다.
질의 결과가 API limit에 도달하면 페이지 누락 가능성도 경고합니다. 현재 검색은 기존의 첫 페이지를 유지하며,
전수 검색을 보장하지 않습니다. 검색 기간 변경과 요청 실패는 별도 증거로 표시하며 급변만으로 장애를 단정하지 않습니다.

```bash
python main.py --strict --drop-ratio 0.5 --spike-ratio 2.0 --min-baseline 20
python scripts/compare_reports.py output/2026-10-09.md output/2026-10-10.md
python -m unittest discover -s tests -v
```

`--strict`는 위 검증 실패 시 진단 JSON/Markdown 저장 후 exit 2를 반환합니다. 모든 활성 수집원에서
0건이면 strict 여부와 관계없이 exit 2이며 기존 `latest.md`를 보존합니다.
일별 Actions는 strict 검증을 사용합니다. 검증 실패 시에도 진단 artifact와 보고서를 저장·커밋한 뒤 실행을
실패로 표시합니다. 결과가 0건이 아니면 불완전 보고서도 상태 표시와 함께 최신 보고서가 될 수 있습니다.
skip은 명시적 제외이며 실패로 취급하지 않습니다. 경보는 원인 판정이 아니라 조사 신호입니다.

실제 2026-10-09~11 조사 근거는 [docs/collection-investigation-2026-10-12.md](docs/collection-investigation-2026-10-12.md)에 있습니다.
