# Selenium 라이브러리를 이용해 관광지 위치 정보 수집

# 사용 패키지
import pandas as pd
from selenium import webdriver 
from selenium.webdriver.common.by import By 
import time

# driver 객체 생성
path = r"..\tensorflow\tools" 
driver = webdriver.Chrome(path + '/chromedriver.exe')

# 한국관광데이터랩 관광지 url
driver.get('https://datalab.visitkorea.or.kr/datalab/portal/loc/getTourDataForm.do')

# 관광지 -> 목록
driver.find_element(By.XPATH, '//*[@id="listView"]').click()

# 지역 선택
driver.find_element(By.XPATH, '//*[@id="tgtTypeCd"]/option[2]').click()
time.sleep(1)

# 전라남도 관광지 목록
driver.find_element(By.XPATH, '//*[@id="searchKey2"]/option[15]').click()
time.sleep(1)

driver.find_element(By.XPATH, '//*[@id="searchBox"]/div/div/input[2]').click()
time.sleep(1)

tr_name = []
reg_name = []

# 1~10 페이지
for n in range(3,13):
       
    driver.find_element(By.XPATH, f'/html/body/div[2]/div[2]/form/div/div/div[3]/div[2]/a[{n}]').click()
    time.sleep(2)
    
    names = driver.find_elements(By.XPATH, '//*[@id="tabCon2"]/ul/li/div[1]/a/span')
    regs = driver.find_elements(By.XPATH, '//*[@id="tabCon2"]/ul/li/div[1]/p')

    
    for name in names : 
        tr_name.append(name.text) # a tag 내용
        
    for reg in regs:
        reg_name.append(reg.text)
        
        
# 다음 페이지로 이동
driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/form/div/div/div[3]/div[2]/a[13]').click()
time.sleep(2)
        
# 11 ~ 20 페이지
for n in range(3,13):
       
    driver.find_element(By.XPATH, f'/html/body/div[2]/div[2]/form/div/div/div[3]/div[2]/a[{n}]').click()
    time.sleep(2)
    
    names = driver.find_elements(By.XPATH, '//*[@id="tabCon2"]/ul/li/div[1]/a/span')
    regs = driver.find_elements(By.XPATH, '//*[@id="tabCon2"]/ul/li/div[1]/p')

    
    for name in names : 
        tr_name.append(name.text) # a tag 내용
        
    for reg in regs:
        reg_name.append(reg.text)

# 다음 페이지로 이동
driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/form/div/div/div[3]/div[2]/a[13]').click()
time.sleep(2)

# 21 ~ 24 페이지
for n in range(3,7):
       
    driver.find_element(By.XPATH, f'/html/body/div[2]/div[2]/form/div/div/div[3]/div[2]/a[{n}]').click()
    time.sleep(2)
    
    names = driver.find_elements(By.XPATH, '//*[@id="tabCon2"]/ul/li/div[1]/a/span')
    regs = driver.find_elements(By.XPATH, '//*[@id="tabCon2"]/ul/li/div[1]/p')

    
    for name in names : 
        tr_name.append(name.text) # a tag 내용
        
    for reg in regs:
        reg_name.append(reg.text)

# 결과 확인
len(reg_name)
tr_jn = pd.DataFrame()
tr_jn['관광지주소'] = reg_name
tr_jn['관광지명'] = tr_name
tr_jn

# 결과 저장
tr_jn.to_excel('tr_jnam.xlsx', index=False, encoding = 'utf-8')
