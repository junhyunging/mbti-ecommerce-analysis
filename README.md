# 🛒 MBTI 기반 이커머스 행동 분석 프로젝트

**BigQuery · Python · 데이터 분석 · 행동 로그 시뮬레이션**

MBTI 성향 정보를 기반으로 이커머스 고객 행동 로그를 직접 설계·생성하고,  
**BigQuery + Python**으로 퍼널·이탈·세그먼트·머신러닝 분석까지 수행한 데이터 분석 프로젝트입니다.

---

## 1. 프로젝트 개요

본 프로젝트는 **MBTI 성향에 따라 이커머스 환경에서 고객 행동이 어떻게 달라지는지**를 분석하기 위해 설계되었습니다.

실제 서비스 로그 구조를 참고하여  
Python 기반 **행동 로그 시뮬레이터**를 직접 구현하고,  
생성된 데이터를 **BigQuery에 적재 → SQL + Python 분석 → 시각화 → 머신러닝 모델링**로 구성했습니다.

---

## 2. 프로젝트 목표

- MBTI 성향과 **이커머스 행동 간 관계성** 탐구
- 성향별 **퍼널 전환율 (view → cart → checkout → purchase)** 분석
- **결제 이탈(checkout abandon)** 및 **고객 이탈(churn)** 원인 분석
- 심리 기반 고객 세그먼트 정의 및 **마케팅 인사이트 도출**
- BigQuery 기반 **대규모 로그 데이터 분석 실전 경험 확보**

---

## 3. 데이터 설계 및 구조

본 프로젝트는 실제 이커머스 로그 구조를 참고하여  
아래 **6개 핵심 테이블**로 구성되어 있습니다.

| 테이블      | 설명                                                 |
| ----------- | ---------------------------------------------------- |
| users       | 고객 기본 정보 및 MBTI 성향                          |
| sessions    | 방문 세션 정보 (체류시간, 디바이스, 캠페인 등)       |
| events      | 행동 로그 (view, add_to_cart, checkout, purchase 등) |
| orders      | 주문 헤더                                            |
| order_items | 주문 상세 상품                                       |
| products    | 상품 메타 정보                                       |

---

## 4. 기술 스택

### Data / Infra

- Python
- Google BigQuery
- BigQuery Standard SQL

### Analysis & Visualization

- Pandas
- Matplotlib / Seaborn
- Jupyter Notebook
- VSCode

### Machine Learning

- Scikit-learn
- LightGBM

---

## 5. 데이터 규모

| 테이블      | 건수        |
| ----------- | ----------- |
| users       | 5,000명     |
| sessions    | 약 15만 건  |
| events      | 약 650만 건 |
| orders      | 약 41만 건  |
| order_items | 약 78만 건  |
| products    | 600개       |

- 분석 기간: **2025-01-01 ~ 2025-06-30 (6개월)**

---

## 6. 분석 노트북 구성

### [01_basic_eda.ipynb](notebook/01_basic_eda.ipynb)

- BigQuery 적재 데이터 검증
- MBTI 분포 및 축(E/I, S/N, T/F, J/P)별 분포
- 고객 등급, 봇 트래픽, 이탈 현황 EDA

---

### [02_funnel_analysis.ipynb](notebook/02_funnel_analysis.ipynb)

- 전체 퍼널 전환율 분석
- MBTI별 퍼널 전환율 비교
- J/P 축별 결제 이탈률 분석
- T/F 축별 캠페인 반응 차이 분석

---

### [03_mbti_segments.ipynb](notebook/03_mbti_segments.ipynb)

- MBTI별 세션 행동 특성
- 시간대별 접속 패턴 (E/I 비교)
- MBTI별 이탈률 및 매출 기여도
- 심리 기반 고객 세그먼트 도출

---

### [04_ml_prediction.ipynb](notebook/04_ml_prediction.ipynb)

- 고객 이탈(churn) 예측 모델링
- **Data Leakage 문제 발견 및 해결**
- 첫 30일 행동 데이터로 재분석
- 행동 데이터만 vs MBTI 포함 모델 성능 비교
- **MBTI 추가 시 F1 4.9% 개선 확인**
- Feature Importance 분석 (S/N 축 가장 중요)

---

## 7. 주요 분석 질문 (Research Questions)

### 7.1 퍼널 분석

- view → cart 전환율이 가장 높은 MBTI는?
- cart → purchase 전환율이 가장 높은 성향은?
- checkout → purchase 결제 이탈률은 J/P 축에 따라 차이가 있는가?

### 7.2 세션 행동 분석

- MBTI별 평균 세션 체류시간 차이는?
- 외향형(E)과 내향형(I)의 시간대별 접속 패턴 차이는?
- 감성(T/F) 성향에 따른 캠페인 반응 차이는?

### 7.3 이탈 & VIP 분석

- VIP 고객의 매출 기여도는 어느 정도인가?
- MBTI별 고객 이탈률 차이는 존재하는가?
- 이탈 직전 고객의 공통 행동 패턴은 무엇인가?

### 7.4 머신러닝

- 행동 데이터만으로 이탈 예측이 가능한가?
- MBTI 정보를 추가했을 때 예측 성능은 개선되는가?

---

## 9. 가설 vs 실제 결과

| MBTI        | 가설                  | 실제 결과                 |
| ----------- | --------------------- | ------------------------- |
| ENFP / ESFP | 장바구니 ↑, 구매 지연 | (cart 많고 이탈 높음)     |
| ISTJ / INTJ | 신중한 구매, 전환율 ↑ | 전환율 낮지만 이탈도 낮음 |
| ESTP        | 즉흥 구매             | (전환율 65% 최고)         |
| ENTJ        | 빠른 의사결정         | (이탈률 6% 최저)          |

---

## 9. Data 설계 원칙

본 프로젝트의 데이터는 **분석 목적의 시뮬레이션 데이터**입니다.

- MBTI 성향은 결과를 강제하지 않음
- 행동 발생 **확률에만 간접적 영향**을 주도록 설계
- 로그 기반 분석을 통해 **MBTI 정보의 추가 설명력**을 검증하는 것이 목적

---

## 10. 프로젝트 구조

```text
mbti-ecommerce-analysis/
│
├── data/
├── src/
│   ├── bigquery_client.py
│   ├── utils.py
│
├── notebook/
│   ├── 01_basic_eda.ipynb
│   ├── 02_funnel_analysis.ipynb
│   ├── 03_mbti_segments.ipynb
│   └── 04_ml_prediction.ipynb
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Author

junhyung_ing (신준형)

---
