import pandas as pd
import os

# 합칠 CSV 파일들이 있는 디렉토리 경로
csv_directory = '/data/행정구별_data/'

# 결과를 저장할 CSV 파일명
output_csv_file = 'combined_data.csv'

# 빈 데이터 프레임 생성
combined_data = pd.DataFrame()

# csv_directory에 있는 모든 CSV 파일을 반복하여 데이터를 가져와서 중복을 제거하고 하나의 데이터 프레임에 추가
for root, dirs, files in os.walk(csv_directory):
    for file in files:
        if file.endswith('.csv'):
            file_path = os.path.join(root, file)
            data = pd.read_csv(file_path)
            combined_data = combined_data.append(data, ignore_index=True)

# 중복 제거
combined_data.drop_duplicates(inplace=True)

# 결과를 하나의 CSV 파일로 저장
combined_data.to_csv(output_csv_file, index=False)
