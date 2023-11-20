import pandas as pd
import os
from sklearn.metrics.pairwise import cosine_similarity

facility_list = ['지하철역','대형마트','유치원','경찰서','종합병원','소방서','도시근린공원','해수욕장']

# csv 파일이 있는 디렉토리 리스트 (각 구별로 분류된 폴더)
# directory_list = ['금정구','남구','동구','동래구','부산진구','북구','사상구','사하구','서구','수영구','연제구','영도구','중구','해운대구']  # 구 폴더 이름~~ 기장 강서 제외

base_dir = 'data/행정구별_data'

directory_list = [os.path.join(base_dir, '금정구'), os.path.join(base_dir, '남구'), os.path.join(base_dir, '동구'), os.path.join(base_dir, '동래구'), os.path.join(base_dir, '부산진구'), os.path.join(base_dir, '북구'), os.path.join(base_dir, '사상구'), os.path.join(base_dir, '사하구'), os.path.join(base_dir, '서구'), os.path.join(base_dir, '수영구'), os.path.join(base_dir, '연제구'), os.path.join(base_dir, '영도구'), os.path.join(base_dir, '중구'), os.path.join(base_dir, '해운대구'),]


# 각 폴더에서 동 리스트 생성
print("시스템 시작")
dong_list = []
for directory in directory_list:
    for file_name in os.listdir(directory):
        dong = file_name.split('_')[0]
        if dong not in dong_list:
            dong_list.append(dong)

# 각 동별 시설의 개수를 담을 데이터프레임
df_matrix = pd.DataFrame(index=dong_list, columns=facility_list)

for directory in directory_list:
    for file_name in os.listdir(directory):
        dong, facility = file_name.split('_')[0], file_name.split('_')[1].replace('.csv', '')
        df=pd.read_csv(os.path.join(directory, file_name))
        df_matrix.loc[dong, facility] = len(df)

print("가중치 계산 시작")
def calculate_similarity(user_weights):
    # 사용자의 가중치에 따라 동별 시설 점수 계산
    print(len(user_weights.values()))  # 사용자 가중치의 길이 출력
    print(df_matrix.shape[1])  # df_matrix의 열의 수 출력
    
    df_matrix_weighted = df_matrix * list(user_weights.values())

    # 동 간 유사도 계산
    similarity_matrix = cosine_similarity(df_matrix_weighted)

    # 사용자 가중치와 각 동과의 유사도 계산
    user_dong_similarity = similarity_matrix @ list(user_weights.values())

    # 유사도가 가장 높은 동 3개 추출
    top3_dong_index = user_dong_similarity.argsort()[-3:][::-1]
    top3_dong = df_matrix.index[top3_dong_index]

    return top3_dong

print("코드 끝")