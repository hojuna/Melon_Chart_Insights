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

