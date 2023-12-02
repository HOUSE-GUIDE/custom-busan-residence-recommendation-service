# import pandas as pd
# import os
# from sklearn.metrics.pairwise import cosine_similarity
# import numpy as np

# facility_list = ['지하철역','대형마트','유치원','경찰서','종합병원','소방서','도시근린공원','해수욕장','대학교']

# base_dir = 'data/행정구별_data'

# directory_list = [os.path.join(base_dir, '금정구'), os.path.join(base_dir, '남구'), os.path.join(base_dir, '동구'), os.path.join(base_dir, '동래구'), os.path.join(base_dir, '부산진구'), os.path.join(base_dir, '북구'), os.path.join(base_dir, '사상구'), os.path.join(base_dir, '사하구'), os.path.join(base_dir, '서구'), os.path.join(base_dir, '수영구'), os.path.join(base_dir, '연제구'), os.path.join(base_dir, '영도구'), os.path.join(base_dir, '중구'), os.path.join(base_dir, '해운대구'),]

# dong_list = []
# for directory in directory_list:
#     for file_name in os.listdir(directory):
#         dong = file_name.split('_')[0]
#         if dong not in dong_list:
#             dong_list.append(dong)

# df_matrix = pd.DataFrame(index=dong_list, columns=facility_list)

# for directory in directory_list:
#     for file_name in os.listdir(directory):
#         dong, facility = file_name.split('_')[0], file_name.split('_')[1].replace('.csv', '')
#         df=pd.read_csv(os.path.join(directory, file_name))
#         df_matrix.loc[dong, facility] = len(df)

# def calculate_similarity(user_weights):
#     category_weights = {
#         'traffic': np.mean([user_weights.get(f'traffic{i}', 0) for i in range(1, 6)]),
#         'education': np.mean([user_weights.get(f'education{i}', 0) for i in range(1, 6)]),
#         'nature': np.mean([user_weights.get(f'nature{i}', 0) for i in range(1, 6)]),
#         'shopping': np.mean([user_weights.get(f'shopping{i}', 0) for i in range(1, 6)]),
#         'society': np.mean([user_weights.get(f'society{i}', 0) for i in range(1, 6)])
#     }

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

#     user_weights_expanded = np.array([facility_weights.get(facility, 0) for facility in df_matrix.columns])
#     user_weights_expanded = user_weights_expanded / np.sum(user_weights_expanded)

#     print(user_weights_expanded)

#     df_matrix_weighted = df_matrix.mul(user_weights_expanded, axis=1)
#     print(df_matrix_weighted)

#     similarity_matrix = cosine_similarity(df_matrix_weighted)
#     print(similarity_matrix)

#     # 사용자 가중치와 각 동과의 유사도 계산
#     user_weights_expanded_2d = user_weights_expanded[np.newaxis, :]  # 2차원 배열로 변환
#     user_dong_similarity = cosine_similarity(user_weights_expanded_2d, df_matrix_weighted)[0]  # 코사인 유사도

#     # 유사도가 가장 높은 동 3개 추출
#     top3_dong_index = user_dong_similarity.argsort()[-3:][::-1]
#     top3_dong = df_matrix.index[top3_dong_index]

#     return top3_dong

# # test 데이터, 프론트에서 입력받을 가중치들을 임의로 배정한 것임당😀
# user_weights = { 
#     'traffic1': 1,
#     'traffic2': 1,
#     'traffic3': 2,
#     'traffic4': 3,
#     'traffic5': 3,
#     'education1': 1,
#     'education2': 1,
#     'education3': 1,
#     'education4': 3,
#     'education5': 4,
#     'nature1': 1,
#     'nature2': 1,
#     'nature3': 1,
#     'nature4': 1,
#     'nature5': 1,
#     'shopping1': 1,
#     'shopping2': 1,
#     'shopping3': 1,
#     'shopping4': 1,
#     'shopping5': 1,
#     'society1': 4,
#     'society2': 5,
#     'society3': 1,
#     'society4': 1,
#     'society5': 1
# }

# top3_dong = calculate_similarity(user_weights)
# print(top3_dong)


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
        'traffic': np.mean([user_weights.get(f'traffic{i}', 0) for i in range(1, 6)]),
        'education': np.mean([user_weights.get(f'education{i}', 0) for i in range(1, 6)]),
        'nature': np.mean([user_weights.get(f'nature{i}', 0) for i in range(1, 6)]),
        'shopping': np.mean([user_weights.get(f'shopping{i}', 0) for i in range(1, 6)]),
        'society': np.mean([user_weights.get(f'society{i}', 0) for i in range(1, 6)])
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

    df_matrix_weighted = df_matrix.mul(user_weights_expanded, axis=1)

    similarity_matrix = cosine_similarity(df_matrix_weighted)

    # 사용자 가중치와 각 동과의 유사도 계산
    user_weights_expanded_2d = user_weights_expanded[np.newaxis, :]  # 2차원 배열로 변환
    user_dong_similarity = cosine_similarity(user_weights_expanded_2d, df_matrix_weighted)[0]  # 코사인 유사도

    # 유사도가 가장 높은 동 3개 추출
    top3_dong_index = user_dong_similarity.argsort()[-3:][::-1]
    top3_dong = df_matrix.index[top3_dong_index]

    return top3_dong
