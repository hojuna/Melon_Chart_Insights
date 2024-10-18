# EDA 프로젝트: [Melon Chart(2000~2024) crawling data]

## 1. 프로젝트 설명 (Project Description)
이 프로젝트는 멜론의 년도별 차트 데이터를 곡 정보와 함께 크롤링하여 분석하는 프로젝트입니다. 


<목적> 코드를 실제로 구현해 보면서 프로그래밍 실력 향상과 데이터 분석 실습을 목적으로 하고 있습니다

<기간 : 2024.10.09 ~ 2024.10.15>

---

## 2. 크롤링 설명 (Dataset Description)

[크롤링 실행 코드](https://github.com/hojuna/melon_chart_insights/blob/master/src/melon_crawling.py)

기본적으로 셀레니움을 사용하여 크롤링을 진행하였습니다. 

멜론은 년도 별 차트를 순위와 해당 노래의 정보를 크롤링하여 가져옵니다. 


노래의 정보는 'song_year','song_rank', 'singer', 'title','Genre', 'lyric'로 이루어져있습니다

---

## 3. 가사의 토큰화 (Installation)



한국어 형태소 분석기인 kiwi, okt, kkma, Hannanum을 사용하여 IU의 좋은날 가사를 토큰화(명사)해 비교해본 결과 실행 결과와 실행 기간을 비교 후 Hannanum을 사용하기로 결정하였습니다.

[토큰화 결과 비교](https://github.com/hojuna/melon_chart_insights/blob/master/notebooks/test_tokenizer.ipynb)



Hannanum을 통해 명사, 형용사, 동사를 추출하여 가사를 토큰화하여 "lyric_tokens" 열을 만들어 저장합니다.

[토큰화 실행 코드](https://github.com/hojuna/melon_chart_insights/blob/master/src/lyrics_tokenizer.py)

---

## 4. LDA (Latent Dirichlet Allocation)
토큰화된 가사 정보를 통해 LDA 모델을 학습하고 노래 가사의 토픽을 추출하고 분석에 활용합니다.

LDA의 결과 대로 나름대로 해석해 명칭을 지어보았습니다.


    "관계와 후회",         # Topic 0
    "고독과 그리움",       # Topic 1
    "불안과 거짓",         # Topic 2
    "삶과 감정",           # Topic 3
    "사랑의 끝과 소중함"   # Topic 4


![gensim_lda_result](https://github.com/user-attachments/assets/8ccb9ca7-c3db-4eb7-84ea-01adf5043f32)



[LDA 실행 코드](https://github.com/hojuna/melon_chart_insights/blob/master/notebooks/lda_analysis.ipynb)


---

## 5. EDA (Exploratory Data Analysis)

[EDA 실행 코드](https://github.com/hojuna/melon_chart_insights/blob/master/notebooks/EDA.ipynb)

-장르, 가수, 토픽을 메인으로 분석하였습니다.

-기본적으로 전체 년도의 장르 분포를 기본 막대차트로 시각화 했고


-년도 별 장르의 분포를 상위 5개의 장르를 기준으로 누적 막대차트로 나타냈습니다.


-자체적으로 트렌드 지수를 만들어 년도별 차트의 트렌드를 파악하였습니다.

<트렌드 지수는 2000~2023년도 장르의 평균 분포와 해당 년도의 장르의 분포 차이를 수치화 한 것을 의미한다.>


-데이터에 가수의 등장 횟수를 카운트하여 가수의 인기를 파악하였습니다.


-가장 오랫도록 차트에 있었던 가수를 찾기 위해 가수의 최대 연속 노래 순위를 찾아보았습니다.


-마지막으로 년도별 토픽의 분포와 토픽별로 가장 토픽 수치(퍼센트)가 높은 노래를 찾아보았습니다.

-토픽 별로 가장 흔한 장르와, 장르 별로 가장 흔한 토픽을 찾아 보았습니다.

---

### 6. 프로젝트 한계와 아쉬운 점

- 년도 별로 차트에 중복된 노래가 있다는 것을 늦게 인지하였습니다.

- 크롤링 다음으로 시간을 많이 쓴 토큰화와 LDA 모델의 결과가 만족스럽지 못했습니다.

- EDA를 조금 더 세부적으로 진행하고 싶었습니다.

- 음악을 가사로만 분석한다는 것의 한계를 느꼈습니다.

---

### 7. 프로젝트 구조

├── data/                   

│   ├── raw/                 # 크롤링한 원본 데이터

│   ├── token_data           # token화 작업을 한 데이터

│   ├── topic_data/             # 라벨링된 데이터

├── notebooks/               

│   ├── eda.ipynb            # EDA 코드

│   ├── wordcloud.ipynb      # Wordcloud 및 시각화 코드

│   ├── lda_analysis.ipynb   # LDA 주제 모델링 및 시각화 코드

│   ├── test_tokenizer.ipynb #형태소 분석기 성능 테스트 코드

└──  src/                     

    ├── melon_crawling.py          # 크롤링 관련 코드
    
    └──  lyrics_tokenizer.py          # 형태소 분석 및 데이터 전처리 코드

