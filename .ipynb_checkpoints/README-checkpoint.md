├── data/                    # 데이터 파일들을 저장하는 디렉터리
│   ├── raw/                 # 크롤링한 원본 데이터
│   ├── token_data           # token화 작업을 한 데이터
│   ├── labeled/             # 라벨링된 데이터
├── notebooks/               # Jupyter 노트북 파일들
│   ├── eda.ipynb            # EDA 코드
│   ├── labeling.ipynb       # 직접 감정 라벨링 코드
│   ├── wordcloud.ipynb      # Wordcloud 및 시각화 코드
│   ├── lda_analysis.ipynb   # LDA 주제 모델링 및 시각화 코드
├── src/                     # 모듈화된 실행 코드
│   ├── crawling.py          # 크롤링 관련 코드
│   ├── preprocessing.py     # 형태소 분석 및 데이터 전처리 코드
│   ├── train_fewshot.py     # Few-shot 학습 코드 (LLM 학습 및 프로프트 엔지니어링)
│   ├── predict.py           # 학습된 LLM으로 예측하는 코드
│   ├── visualization.py     # Wordcloud 및 그래프 시각화 코드
│   ├── eda.py               # EDA 관련 코드
│   ├── lda_model.py         # LDA 주제 모델링 코드
├── models/                  # 학습된 모델 파일들
│   ├── trained_llm.pt       # LLM 학습 결과 모델 저장
│   ├── lda_model.pkl        # 학습된 LDA 모델 파일 저장
├── tests/                   # 테스트 코드 모음
│   ├── test_crawling.py     # 크롤링 모듈 테스트 코드
│   ├── test_preprocessing.py # 전처리 모듈 테스트 코드
│   ├── test_train_fewshot.py # 학습 모듈 테스트 코드
│   ├── test_predict.py      # 예측 모듈 테스트 코드
│   ├── test_lda_model.py    # LDA 모듈 테스트 코드  <--- 추가
├── requirements.txt         # 필요한 패키지 리스트
├── README.md                # 프로젝트 설명 파일
└── .gitignore               # Git에 포함되지 않을 파일 목록
