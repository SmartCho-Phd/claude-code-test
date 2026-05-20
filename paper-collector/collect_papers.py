import requests
import csv
import time
import os
from datetime import datetime

API_KEY = os.environ.get("SCOPUS_API_KEY", "")

QUERIES = [
    "generative AI",
    "large language model",
    "ChatGPT",
    "AI service",
    "artificial intelligence service",
]

START_YEAR = 2022
END_YEAR = 2025
MAX_RESULTS = 200  # 쿼리당 최대 수집 수

HEADERS = {
    "X-ELS-APIKey": API_KEY,
    "Accept": "application/json",
}

OUTPUT_FILE = "ssci_papers.csv"

CSV_FIELDS = [
    "title", "authors", "journal", "year", "doi",
    "cited_by", "scopus_id", "abstract", "query"
]


def search_scopus(query, start=0, count=25):
    url = "https://api.elsevier.com/content/search/scopus"
    params = {
        "query": f"{query} AND PUBYEAR > {START_YEAR - 1} AND PUBYEAR < {END_YEAR + 1}",
        "count": count,
        "start": start,
        "sort": "citedby-count",
        "field": "dc:title,dc:creator,prism:publicationName,prism:coverDate,"
                 "prism:doi,citedby-count,dc:identifier,dc:description",
    }
    resp = requests.get(url, headers=HEADERS, params=params, timeout=30)
    resp.raise_for_status()
    return resp.json()


def parse_entry(entry, query):
    year = ""
    date = entry.get("prism:coverDate", "")
    if date:
        year = date[:4]

    return {
        "title": entry.get("dc:title", ""),
        "authors": entry.get("dc:creator", ""),
        "journal": entry.get("prism:publicationName", ""),
        "year": year,
        "doi": entry.get("prism:doi", ""),
        "cited_by": entry.get("citedby-count", "0"),
        "scopus_id": entry.get("dc:identifier", ""),
        "abstract": entry.get("dc:description", ""),
        "query": query,
    }


def collect_papers():
    all_papers = {}  # scopus_id 기준 중복 제거

    for query in QUERIES:
        print(f"\n[검색] '{query}'")
        start = 0
        collected = 0

        while collected < MAX_RESULTS:
            try:
                data = search_scopus(query, start=start, count=25)
                results = data.get("search-results", {})
                total = int(results.get("opensearch:totalResults", 0))
                entries = results.get("entry", [])

                if not entries:
                    break

                for entry in entries:
                    paper = parse_entry(entry, query)
                    sid = paper["scopus_id"]
                    if sid and sid not in all_papers:
                        all_papers[sid] = paper
                        collected += 1

                print(f"  {start + len(entries)} / {min(total, MAX_RESULTS)} 수집 중...")

                if start + 25 >= min(total, MAX_RESULTS):
                    break

                start += 25
                time.sleep(0.5)  # API 요청 간격

            except requests.HTTPError as e:
                print(f"  HTTP 오류: {e}")
                break
            except Exception as e:
                print(f"  오류 발생: {e}")
                break

    return list(all_papers.values())


def save_csv(papers):
    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=CSV_FIELDS)
        writer.writeheader()
        writer.writerows(papers)
    print(f"\n저장 완료: {OUTPUT_FILE} ({len(papers)}편)")


if __name__ == "__main__":
    if not API_KEY:
        print("오류: SCOPUS_API_KEY 환경변수를 설정해주세요.")
        print("  Windows: $env:SCOPUS_API_KEY='your_key'")
        exit(1)

    print(f"수집 시작: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"기간: {START_YEAR} ~ {END_YEAR}")
    print(f"쿼리: {QUERIES}")

    papers = collect_papers()
    save_csv(papers)

    print(f"\n완료: 총 {len(papers)}편 수집")
