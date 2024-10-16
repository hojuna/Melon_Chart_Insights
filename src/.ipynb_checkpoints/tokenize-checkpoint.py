for year in year_list:

    # 데이터 불러오기
    df = pd.read_csv(rf"C:\Users\hojun\project\data\kr_song_chart_{year}_data.csv")

    lyric_df=pd.DataFrame()
    lyric_df['lyric'] = df['lyric'].copy()

    # 줄바꿈 제거
    lyric_df['lyric'] = lyric_df['lyric'].replace("\n", " ", regex=True)

    # a명사(N),형용사(A),동사 (V) 
    tag_list=['N','A','V']

    #임의적으로 불용어 리스트를 만듬
    stopworads= ['그댈','우리','그대','나', '너', '내', '것', '수', '말', '니', '거' , '떄' , '네', '날', '속', '뭐', '우','그' , '널', '듯', '두', '위', 'I’m', '데', '번' ,'마' ,'앞', '곳' ,'이', '줄' ,'길', '때']

    # 형태소 분석 함수 정의
    def extract_pos(text):

        #문자, 숫자, 공백 
        text = re.sub(r'[^,.?!\w\s가-힣]', '', text)
        tokens = Hannanum.pos(text, flatten=True)


        #지정 태그와 불용어를 추출함
        result= [s for s, t in tokens if t in tag_list and s not in stopworads]
    
        return ' '.join(set(result))  # 결과를 문자열로 반환

    df['lyric_tokens']=lyric_df['lyric'].apply(extract_pos)

    # 분석 결과를 파일로 저장
    df.to_csv(rf"C:\Users\hojun\2024_10_10_project\data\token_data\token_kr_song_chart_{year}_data.csv", index=False)

    # 결과 확인
    print(year," 완료")
print("형태소 분석 후 저장 완료")


# csv파일들 결합 후 저장
dfs=[]
for year in year_list:
    path=rf"C:\Users\hojun\2024_10_10_project\data\token_data\token_kr_song_chart_{year}_data.csv"
    df=pd.read_csv(path) 
    dfs.append(df)
    
resutl_df= pd.concat(dfs, ignore_index=True)
resutl_df.to_csv(r"C:\Users\hojun\2024_10_10_project\data\token_data\total_token_kr_song_chart_data.csv",index=False)
