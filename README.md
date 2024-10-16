├── data/                    # 데이터 파일들을 저장하는 디렉터리
│   ├── raw/                 # 크롤링한 원본 데이터
│   ├── token_data           # token화 작업을 한 데이터
│   ├── labeled/             # 라벨링된 데이터
├── notebooks/               # Jupyter 노트북 파일들
│   ├── eda.ipynb            # EDA 코드
│   ├── wordcloud.ipynb      # Wordcloud 및 시각화 코드
│   ├── lda_analysis.ipynb   # LDA 주제 모델링 및 시각화 코드
└──  src/                     # 모듈화된 실행 코드
    ├── crawling.py          # 크롤링 관련 코드
    └──  tokenize.py          # 형태소 분석 및 데이터 전처리 코드

