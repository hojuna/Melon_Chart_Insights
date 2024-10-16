# selenium의 webdriver를 사용하기 위한 import
from selenium import webdriver

# selenium으로 키를 조작하기 위한 import
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

# 페이지 로딩을 기다리는데에 사용할 time 모듈 import
import time
import pandas as pd
import os

#크롤링 할 년도 리스트
year_list= [i for i in range(2000,2024)]

#페이지 조회를 위한 변수
page=(1,51)
page_id=('lst50','lst100')



for year in year_list:
    for i in [0,1]:
        get_url=f'https://www.melon.com/chart/age/index.htm?chartType=YE&chartGenre=KPOP&chartDate={year}#params%5Bidx%5D={page[i]}'
        # singer_xpath=f'//*[@id="{page_id[i]}"]/td[4]/div/div/div[2]/div[1]/a'
        # song_name_xpath=f'//*[@id="{page_id[i]}"]/td[4]/div/div/div[1]/span/strong/a'
        # song_name_xpath=f'//*[@id={page_id[i]}]/td[4]/div/div/div[1]/span'
        lyric_xpath='//*[@id="d_video_summary"]'
        btn_lyric_xpath=f'//*[@id="{page_id[i]}"]/td[4]/div/a'
        Genre_xpath='//*[@id="downloadfrm"]/div/div/div[2]/div[2]/dl/dd[3]'

        df = pd.DataFrame()


        # # 크롬드라이버 실행
        driver = webdriver.Chrome() 

        driver.implicitly_wait(3) # 묵시적 대기, 활성화를 최대 15초가지 기다린다.

        # 페이지 가져오기(이동)
        driver.get(get_url)

        # 음악 제목 가져오기
        search = driver.find_elements( By.CLASS_NAME,'rank01')
        time.sleep(0.1)
        df['title']=[i.text for i in search if i.text!=""] 

        # 가수명 가져오기
        search = driver.find_elements( By.CLASS_NAME,'rank02')
        time.sleep(0.1)
        df['singer']=[i.text for i in search if i.text!=""]

        #가사 링크 가져오기
        search = driver.find_elements(By.XPATH,btn_lyric_xpath )

        arr_lyric = []
        arr_Genre = []

        #페이지 탐색 후 가사와 장르 가져오기
        #가사가 없는 경우가 있어서 예외처리
        for index in range(50):
            search = driver.find_elements(By.XPATH, btn_lyric_xpath)  # 요소 재검색
            time.sleep(0.1)
            search[index].click()
            try:
                arr_lyric.append(driver.find_element(By.XPATH, lyric_xpath).text) 
                
            except NoSuchElementException:
                arr_lyric.append("가사 없음")
            
            arr_Genre.append(driver.find_element(By.XPATH, Genre_xpath).text)
            driver.back()
            time.sleep(0.1)

        df['lyric']= arr_lyric
        df['Genre']= arr_Genre

        if i==0:
            df_1=df.copy()
        else:
            df_51=df.copy()

    df_1_100 = pd.concat([df_1, df_51], ignore_index=True)
    df_1_100['song_year']=year
    df_1_100['song_rank'] = range(1, len(df_1_100) + 1)
    df_1_100 = df_1_100[['song_year','song_rank', 'singer', 'title','Genre', 'lyric']]

    df_1_100['title'] = df_1_100['title'].str.strip() 

    df_1_100['lyric'] = df_1_100['lyric'].str.strip() 

    df_1_100['singer'] = df_1_100['singer'].str.strip() 

    df_1_100['Genre'] = df_1_100['Genre'].str.strip() 

    df_1_100.to_csv(rf'C:\Users\hojun\2024_10_10_project\data\raw\kr_song_chart_{year}_data.csv',index=False)


#csv파일들 결합 후 저장
dfs=[]
for year in year_list:
    path=rf"C:\Users\hojun\2024_10_10_project\data\raw\kr_song_chart_{year}_data.csv"
    df=pd.read_csv(path) 
    dfs.append(df)

resutl_df= pd.concat(dfs, ignore_index=True)
resutl_df.to_csv(f'TOTAL_kr_song_chart_data.csv',index=False)





