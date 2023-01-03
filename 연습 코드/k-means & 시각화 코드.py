# K-Means 군집 분석 후 각 클러스터 중심 지도에 나타내기

# 사용 패키지
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans 

# 데이터 불러오기
totalgps = pd.read_csv('totalgps.csv')
df = totalgps.iloc[:,[5,6]]


# K-MEANS 군집분석
obj = KMeans(n_clusters=3, max_iter=300, algorithm='auto')
model = obj.fit(df)
pred = model.predict(df)
df['predict'] = pred

# 군집 중앙값 
centers = model.cluster_centers_
cent = pd.DataFrame(centers, columns=['lat', 'long'])
# cent.to_csv('centers_park.csv')

# 최대, 최소 값 확인
ran = ((df.long.min(), df.long.max(), df.lat.min(), df.lat.max()))

# 지도 불러오기
map_img = plt.imread('map.png')

# 산점도 그리기
plt.rc('font', family = "Malgun Gothic")
fig, ax = plt.subplots(figsize = (8,7))
ax.scatter(df.long, df.lat, zorder=1, c='b', s=10)
ax.set_title('대구광역시')
ax.set_xlim(ran[0], ran[1])
ax.set_ylim(ran[2], ran[3])
ax.imshow(map_img, zorder=0, extent = ran, aspect = 'equal')

# 군집분석 중심 좌표 그리기
fig, ax = plt.subplots(figsize = (8,7))
ax.scatter(df.long, df.lat, zorder=1, c='b', s=10)
ax.scatter(cent.long, cent.lat, c='r', marker='D')
ax.set_title('대구광역시')
ax.set_xlim(ran[0], ran[1])
ax.set_ylim(ran[2], ran[3])
ax.imshow(map_img, zorder=0, extent = ran, aspect = 'equal')











