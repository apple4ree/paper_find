# paper_find

매일 주요 1티어 학회와 HuggingFace Papers에서 **Agent / Harness / Finance** 관련 논문을 자동 수집·정리하는 도구입니다.

## 수집 대상

| 구분 | 소스 |
|------|------|
| **학회** | AAAI, NeurIPS, ICML, ICLR, **CVPR**, KDD |
| **큐레이션** | [HuggingFace Daily Papers](https://huggingface.co/papers) |
| **컨퍼런스 DB** | OpenReview (ICLR · NeurIPS · ICML) |
| **CVPR 전용** | CVF Open Access (openaccess.thecvf.com) |
| **프리프린트** | arXiv (cs.AI · cs.LG · cs.CL · cs.CV · q-fin.*) |
| **통합 검색** | Semantic Scholar (AAAI · CVPR · KDD · 기타) |

## 토픽 키워드

- **Agent** — agent, multi-agent, autonomous agent, llm agent, agentic, tool-use, gui agent, web agent, …
- **Harness** — harness, lm eval, evaluation framework, benchmark suite, llm evaluation, …
- **Finance** — financial, trading, portfolio, stock market, fraud detection, algorithmic trading, finllm, …

## 중복 제거 방식

같은 논문이 여러 소스에서 수집되는 경우:
1. **arXiv ID** 기반 1차 중복 제거
2. **정규화된 제목** 기반 2차 중복 제거 (대소문자·구두점 무시)
3. 같은 논문이면 더 풍부한 메타데이터(초록, 저자, 학회명)를 유지

## 결과물

매일 `output/YYYY-MM-DD.md` 파일이 생성됩니다 (최신 결과는 `output/latest.md`).

예시 출력:

```
# Daily Paper Digest — 2025-04-14 (Monday)

## Agent  (12)

### CVPR
- **[Paper Title](url)** — Author A, Author B et al.
  - CVPR 2025 · CVF · 2025-04-13
  - Abstract snippet…

### NeurIPS
- **[Paper Title](url)** — Author A, Author B et al.
  - NeurIPS 2025 · 🤗 Featured · 2025-04-13
  - Abstract snippet…

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

# 특정 소스 제외 (빠른 실행)
python main.py --skip-arxiv             # arXiv 제외
python main.py --skip-cvf              # CVF 제외
python main.py --skip-openreview       # OpenReview 제외

# Semantic Scholar API 키 사용 (요청 한도 확대)
SS_API_KEY=<your_key> python main.py
```

## 자동 스케줄 (GitHub Actions)

`.github/workflows/daily_papers.yml`이 매일 **UTC 09:00 (KST 18:00)** 에 자동 실행되어 결과를 커밋합니다.

- 네트워크 오류 발생 시 30초 후 자동 재시도
- 수동 실행은 Actions 탭 → **Daily Paper Digest** → **Run workflow** 에서 가능

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
│   ├── processor.py           # 중복 제거(2단계) + 토픽 분류
│   ├── formatter.py           # Markdown 출력 포맷
│   └── scrapers/
│       ├── huggingface.py     # HuggingFace Daily Papers (API + HTML 폴백)
│       ├── openreview.py      # OpenReview (search + bulk 폴백)
│       ├── cvf.py             # CVF Open Access (CVPR 전용)
│       ├── semantic_scholar.py# Semantic Scholar (AAAI, CVPR, KDD 등)
│       └── arxiv.py           # arXiv 일별 제출 논문
├── output/
│   ├── latest.md              # 최신 결과
│   └── YYYY-MM-DD.md          # 날짜별 아카이브
└── .github/workflows/
    └── daily_papers.yml       # 일별 자동 실행 (재시도 포함)
```
