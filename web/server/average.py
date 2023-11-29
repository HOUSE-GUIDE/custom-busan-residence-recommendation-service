# import pandas as pd
# import os
# from sklearn.metrics.pairwise import cosine_similarity
# import numpy as np

# facility_list = ['지하철역','대형마트','유치원','경찰서','종합병원','소방서','도시근린공원','해수욕장','대학교']

# # csv 파일이 있는 디렉토리 리스트 (각 구별로 분류된 폴더)
# # directory_list = ['금정구','남구','동구','동래구','부산진구','북구','사상구','사하구','서구','수영구','연제구','영도구','중구','해운대구']  # 구 폴더 이름~~ 기장 강서 제외

# base_dir = 'data/행정구별_data'

# directory_list = [os.path.join(base_dir, '금정구'), os.path.join(base_dir, '남구'), os.path.join(base_dir, '동구'), os.path.join(base_dir, '동래구'), os.path.join(base_dir, '부산진구'), os.path.join(base_dir, '북구'), os.path.join(base_dir, '사상구'), os.path.join(base_dir, '사하구'), os.path.join(base_dir, '서구'), os.path.join(base_dir, '수영구'), os.path.join(base_dir, '연제구'), os.path.join(base_dir, '영도구'), os.path.join(base_dir, '중구'), os.path.join(base_dir, '해운대구'),]


# # 각 폴더에서 동 리스트 생성
# print("시스템 시작")
# dong_list = []
# for directory in directory_list:
#     for file_name in os.listdir(directory):
#         dong = file_name.split('_')[0]
#         if dong not in dong_list:
#             dong_list.append(dong)

# # 각 동별 시설의 개수를 담을 데이터프레임
# df_matrix = pd.DataFrame(index=dong_list, columns=facility_list)

# for directory in directory_list:
#     for file_name in os.listdir(directory):
#         dong, facility = file_name.split('_')[0], file_name.split('_')[1].replace('.csv', '')
#         df=pd.read_csv(os.path.join(directory, file_name))
#         df_matrix.loc[dong, facility] = len(df)

# print("가중치 계산 시작")


# def calculate_similarity(user_weights):
#     # 사용자가 입력한 가중치를 카테고리별로 평균내어 가중치를 계산
#     category_weights = {
#         'traffic': np.mean([user_weights.get(f'traffic{i}', 0) for i in range(1, 4)]),
#         'education': np.mean([user_weights.get(f'education{i}', 0) for i in range(1, 4)]),
#         'nature': np.mean([user_weights.get(f'nature{i}', 0) for i in range(1, 4)]),
#         'shopping': np.mean([user_weights.get(f'shopping{i}', 0) for i in range(1, 4)]),
#         'society': np.mean([user_weights.get(f'society{i}', 0) for i in range(1, 4)])
#     }

#     # 각 카테고리의 가중치를 해당 시설에 대응
#     facility_weights = {
#         '지하철역': category_weights['traffic'],
#         '대형마트': category_weights['shopping'],
#         '유치원': category_weights['education'],
#         '경찰서': category_weights['society'],
#         '종합병원': category_weights['society'],
#         '소방서': category_weights['society'],
#         '도시근린공원': category_weights['nature'],
#         '해수욕장': category_weights['nature'],
#         '대학교': category_weights['education']
#     }

#     # 사용자의 가중치에 따라 동별 시설 점수 계산
#     user_weights_expanded = np.array([facility_weights.get(facility, 0) for facility in df_matrix.columns])
#     user_weights_expanded = user_weights_expanded / np.sum(user_weights_expanded)  # 정규화

#     print(user_weights_expanded)  # 디버깅용: user_weights_expanded 출력

#     # 사용자의 가중치로 df_matrix를 조정
#     df_matrix_weighted = df_matrix.mul(user_weights_expanded, axis=1)
#     print(df_matrix_weighted)  # 디버깅용: df_matrix_weighted 출력

#     # 동 간 유사도 계산
#     similarity_matrix = cosine_similarity(df_matrix_weighted)
#     print(similarity_matrix)  # 디버깅용: similarity_matrix 출력

#     # 사용자 가중치와 각 동과의 유사도 계산
#     user_dong_similarity = similarity_matrix @ user_weights_expanded

#     # 유사도가 가장 높은 동 3개 추출
#     top3_dong_index = user_dong_similarity.argsort()[-3:][::-1]
#     top3_dong = df_matrix.index[top3_dong_index]

#     return top3_dong

# print("코드 끝")




import pandas as pd
import os
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

facility_list = ['지하철역','대형마트','유치원','경찰서','종합병원','소방서','도시근린공원','해수욕장','대학교']

base_dir = 'data/행정구별_data'

directory_list = [os.path.join(base_dir, '금정구'), os.path.join(base_dir, '남구'), os.path.join(base_dir, '동구'), os.path.join(base_dir, '동래구'), os.path.join(base_dir, '부산진구'), os.path.join(base_dir, '북구'), os.path.join(base_dir, '사상구'), os.path.join(base_dir, '사하구'), os.path.join(base_dir, '서구'), os.path.join(base_dir, '수영구'), os.path.join(base_dir, '연제구'), os.path.join(base_dir, '영도구'), os.path.join(base_dir, '중구'), os.path.join(base_dir, '해운대구'),]

dong_list = []
for directory in directory_list:
    for file_name in os.listdir(directory):
        dong = file_name.split('_')[0]
        if dong not in dong_list:
            dong_list.append(dong)

df_matrix = pd.DataFrame(index=dong_list, columns=facility_list)

for directory in directory_list:
    for file_name in os.listdir(directory):
        dong, facility = file_name.split('_')[0], file_name.split('_')[1].replace('.csv', '')
        df=pd.read_csv(os.path.join(directory, file_name))
        df_matrix.loc[dong, facility] = len(df)

def calculate_similarity(user_weights):
    category_weights = {
        'traffic': np.mean([user_weights.get(f'traffic{i}', 0) for i in range(1, 5)]),
        'education': np.mean([user_weights.get(f'education{i}', 0) for i in range(1, 4)]),
        'nature': np.mean([user_weights.get(f'nature{i}', 0) for i in range(1, 6)]),
        'shopping': np.mean([user_weights.get(f'shopping{i}', 0) for i in range(1, 4)]),
        'society': np.mean([user_weights.get(f'society{i}', 0) for i in range(1, 4)])
    }

    facility_weights = {
        '지하철역': category_weights['traffic'],
        '대형마트': category_weights['shopping'],
        '유치원': category_weights['education'],
        '경찰서': category_weights['society'],
        '종합병원': category_weights['society'],
        '소방서': category_weights['society'],
        '도시근린공원': category_weights['nature'],
        '해수욕장': category_weights['nature'],
        '대학교': category_weights['education']
    }

    user_weights_expanded = np.array([facility_weights.get(facility, 0) for facility in df_matrix.columns])
    user_weights_expanded = user_weights_expanded / np.sum(user_weights_expanded)

    print(user_weights_expanded)

    df_matrix_weighted = df_matrix.mul(user_weights_expanded, axis=1)
    print(df_matrix_weighted)

    similarity_matrix = cosine_similarity(df_matrix_weighted)
    print(similarity_matrix)

    # 사용자 가중치와 각 동과의 유사도 계산
    user_weights_expanded_2d = user_weights_expanded[np.newaxis, :]  # 2차원 배열로 변환
    user_dong_similarity = cosine_similarity(user_weights_expanded_2d, df_matrix_weighted)[0]  # 수정된 부분

    # 유사도가 가장 높은 동 3개 추출
    top3_dong_index = user_dong_similarity.argsort()[-3:][::-1]
    top3_dong = df_matrix.index[top3_dong_index]

    return top3_dong

user_weights = {
    'traffic1': 1,
    'traffic2': 2,
    'traffic3': 3,
    'traffic4': 4,
    'education1': 1,
    'education2': 2,
    'education3': 3,
    'nature1': 1,
    'nature2': 2,
    'nature3': 3,
    'nature4': 4,
    'nature5': 5,
    'shopping1': 1,
    'shopping2': 2,
    'shopping3': 3,
    'society1': 1,
    'society2': 2,
    'society3': 3
}

top3_dong = calculate_similarity(user_weights)
print(top3_dong)
