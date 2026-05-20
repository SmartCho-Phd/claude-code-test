# Paper Collector

Scopus API를 활용하여 생성형 AI 및 AI 서비스 관련 SSCI급 논문을 자동 수집하는 스크립트입니다.

## 수집 조건
- 키워드: generative AI, large language model, ChatGPT, AI service 등
- 기간: 2022 ~ 2025
- 정렬: 피인용 수 기준
- 형식: CSV

## 사용법

### 1. 환경 설정
```
pip install requests
```

### 2. API 키 설정 (Windows PowerShell)
```
$env:SCOPUS_API_KEY="your_api_key_here"
```

### 3. 실행
```
python collect_papers.py
```

### 4. 결과
`ssci_papers.csv` 파일로 저장됩니다.

## 주의사항
- API 키는 절대 코드나 GitHub에 직접 입력하지 마세요.
- Scopus API는 기관 네트워크(학교 Wi-Fi 또는 VPN) 환경에서 전체 데이터 접근이 가능합니다.
