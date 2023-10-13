# 원하는 행정동과 시설들을 리스트에 넣으면, csv가 출력으로 나오는 데이터 수집 코드

import json
import requests
import pandas as pd

# 행정동 리스트

# 행정동을 리스트에 추가해주세영
dong_list = ['중앙동', '동광동', '대청동', '보수동', '부평동' , '광복동' , '남포동', '영주1동', '영주2동']  

# 시설 리스트 (카테고리)
facility_list = ['편의점', '학교', '병원'] 
headers = {
    "Authorization": "KakaoAK efc1b26d609b687398664b4f30490c20"
}

for dong in dong_list:
    addr = f'부산시 {dong}'

    url = f'https://dapi.kakao.com/v2/local/search/address.json?query={addr}'
    
    response = requests.get(url, headers=headers)
    result = response.json()

    if result.get('documents'):
        x = result['documents'][0]['x']
        y = result['documents'][0]['y']
        print(f"x: {x}, y: {y}")
        
        for facility in facility_list:
            places_name_list=[]
            for i in range(1, 46):
                params = {
                    'x': float(x),
                    'y': float(y),
                    'radius': 2000,
                    'page': i,
                    'size': 15,
                    'sort': 'distance'
                }

                url_keyword_search=f'https://dapi.kakao.com/v2/local/search/keyword.json?query={facility}'
                
                places_res=requests.get(url_keyword_search, headers=headers,params=params)

                places_json=places_res.json()
                
                if places_json.get('documents'):
                    places=places_json['documents']
                    
                    for place in places:
                        place_name=place['place_name'] 
                        places_name_list.append(place_name) 

                else:
                    print(f"No results found on page {i}")
            
            df=pd.DataFrame(places_name_list,columns=[f'{facility}'])
            df.drop_duplicates(inplace=True)
            
            filename=f'{dong}_{facility}.csv'
            df.to_csv(filename,index=False)

print("csv파일 생성 완료! \n 다음 수집할 데이터를 리스트에 넣고 생성해!")
