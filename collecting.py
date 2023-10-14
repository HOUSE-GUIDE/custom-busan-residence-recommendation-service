import json
import requests
import pandas as pd

# 행정동 리스트
dong_list = {'중앙동', '동광동', '대청동', '보수동', '부평동', '광복동', '남포동', '영주1동', '영주2동'}

# 시설 리스트 (카테고리)
facility_list = ['대형마트', '편의점', '어린이집', '유치원','학교','학원', '지하철역','문화시설','공공기관', '은행','관광명소','음식점', '카페','병원','약국'] 
# 카테고리 줄이기, 초등학교와 같은 형식으로,  마트 api

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
            page_num=1
            
            while page_num <= 45:
                params={
                    "query": facility,
                    "page": page_num,
                    "radius": 2000, # 반경
                    "size": 15, # api 페이지
                    "sort":"distance",
                    "x": x,
                    "y": y
                }
                
                url_keyword_search=f'https://dapi.kakao.com/v2/local/search/keyword.json'
                
                places_res=requests.get(url_keyword_search, headers=headers,params=params)

                places_json=places_res.json()
                
                if places_json.get('documents'):
                    places=places_json['documents']
                    
                    for place in places:
                        place_name=place['place_name'] 
                        places_name_list.append(place_name) 

                else:
                    break
                
                page_num+=1
            
            df=pd.DataFrame(places_name_list,columns=[f'{facility}'])
            df.drop_duplicates(inplace=True) # 중복 제거하는 코드
            
            # csv파일 생성 부분
            filename=f'{dong}_{facility}.csv' 
            df.to_csv(filename,index=False)

print("csv파일 생성 완료! 다음 수집할 데이터를 리스트에 넣고 생성해!")


# import json
# import requests
# import pandas as pd

# # 행정동 리스트

# # 행정동을 리스트에 추가해주세영
# dong_list = {'중앙동', '동광동', '대청동', '보수동', '부평동', '광복동', '남포동', '영주1동', '영주2동'}

# # 시설 리스트 (카테고리)
# facility_list = ['대형마트', '편의점', '어린이집', '유치원', '학교', '학원', '지하철역', '문화시설', '공공기관', '은행', '관광명소', '음식점', '카페', '병원', '약국'] 
# headers = {
#     "Authorization": "KakaoAK efc1b26d609b687398664b4f30490c20"
# }

# for dong in dong_list:
#     addr = f'부산시 {dong}'

#     url = f'https://dapi.kakao.com/v2/local/search/address.json?query={addr}'
    
#     response = requests.get(url, headers=headers)
#     result = response.json()

#     if result.get('documents'):
#         x = result['documents'][0]['x']
#         y = result['documents'][0]['y']
#         print(f"x: {x}, y: {y}")
        
#         for facility in facility_list:
#             places_name_list=[]
#             for i in range(1, 46):
#                 params = {
#                     'x': float(x),
#                     'y': float(y),
#                     'radius': 2000, #2km 반경으로 측정
#                     'page': i,
#                     'size': 15,
#                     'sort': 'distance'
#                 }

#                 url_keyword_search=f'https://dapi.kakao.com/v2/local/search/keyword.json?query={facility}'
                
#                 places_res=requests.get(url_keyword_search, headers=headers,params=params)

#                 places_json=places_res.json()
                
#                 if places_json.get('documents'):
#                     places=places_json['documents']
                    
#                     for place in places:
#                         place_name=place['place_name'] 
#                         places_name_list.append(place_name) 

#                 else:
#                     print(f"No results found on page {i}")
            
#             df=pd.DataFrame(places_name_list,columns=[f'{facility}'])
#             df.drop_duplicates(inplace=True) # 중복 제거하는 코드
            
#             # csv파일 생성 부분
#             filename=f'{dong}_{facility}.csv' 
#             df.to_csv(filename,index=False)

# print("csv파일 생성 완료! \n 다음 수집할 데이터를 리스트에 넣고 생성해!")

