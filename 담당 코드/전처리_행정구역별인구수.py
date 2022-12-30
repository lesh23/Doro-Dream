# 전국 시도별 18,19,20,21년 인구수 코드

# 사용 패키지
import pandas as pd

# 전국 시도별 인구수 데이터 불러오기
pop = pd.read_csv('/doro-dream/행정안전부_주민등록인구통계/201712_202112_주민등록인구및세대현황_연간_전체.csv', thousands = ',')

# 필요한 행, 열 값 가져오기 및 행정구역 순으로 정렬
pop = pop.iloc[1:19,[0,7,13,19,25]]
pop = pop.sort_values('행정구역')

# 칼럼명 수정
pop.columns = ['지역명','2018','2019','2020','2021']

# 시도별 4개년 인구수 csv파일 저장
pop.to_csv('전처리_행정구역별인구수.csv', index=False, encoding = 'utf-8')


