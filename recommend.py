import random
import pandas as pd
import os

# data/남구 폴더 내의 CSV 파일 목록 가져오기
data_dir = 'data/행정구별_data/사하구'
csv_files = [f for f in os.listdir(data_dir) if f.endswith('.csv')]

# 무작위로 선택할 기관 수
num_criteria = random.randint(1, 5) # 예시로 1부터 5개의 기관을 선택

# CSV 파일에서 데이터를 읽어 데이터프레임에 저장
data_frames = []
for csv_file in csv_files:
    file_path = os.path.join(data_dir, csv_file)
    df = pd.read_csv(file_path, header=None, skiprows=1, names=['기관 이름'])
    df['행정동'] = csv_file[:-4]
    data_frames.append(df)

# 무작위로 기관 선택
selected_criteria = random.sample(['지하철역','대형마트','유치원','경찰서','종합병원','소방서','도시근린공원','해수욕장'], num_criteria)

# 가중치 설정 (일단 모든 기관에 동일한 가중치)
weights = [1] * num_criteria

# 점수 계산
all_data = pd.concat(data_frames)
scores = []
for index, row in all_data.iterrows():
    score = sum([weights[i] for i in range(num_criteria) if selected_criteria[i] in row['기관 이름']]) # 저 기관 이름이 있는 것만 카운트 하는 듯
    scores.append(score)
all_data['점수'] = scores

# 가장 높은 점수를 가진 행정동 추천
recommended_district = all_data.sort_values(by='점수', ascending=False).iloc[0]['행정동']

# 거주지 이름에서 기관 이름을 제거하여 행정동 이름만 남김
recommended_district = recommended_district.rsplit('_', 1)[0]

print(f"선택된 기관: {', '.join(selected_criteria)}")
print(f"거주지 추천: {recommended_district}")