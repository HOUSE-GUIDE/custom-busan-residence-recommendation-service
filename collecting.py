import json
import requests
import pandas as pd


# 행정동 리스트
dong_list = {'삼락동', '모라1동', '모라3동', '덕포1동', '덕포2동', '괘법동', '감전동', '주례1동', '주례2동', '주례3동', '학장동', '엄궁동'}

# 시설 리스트 (카테고리)
# 교통 : 지하철역
# 쇼핑 : 대형마트, 백화점
# 교육 : 유치원, 초등학교
# 사회 서비스 : 파출소, 병원, 소방서
# 자연 : 공원

# 수정후
# 시설 리스트 (카테고리)
# 교통 : 지하철역
# 쇼핑 : 대형마트
# 교육 : 유치원
# 사회 서비스 : 경찰서(파출소 포함), 종합병원, 소방서
# 자연 : 도시근린공원, 해수욕장

facility_list = ['지하철역','대형마트','유치원','경찰서','종합병원','소방서','도시근린공원','해수욕장']

# 카테고리 줄이기, 초등학교와 같은 형식으로,  마트 api

# 예외 데이터 : 
# 백화점, 초등학교

# 초등학교 문제는 유치원, 어린이집 초등학교 한꺼번에 카테고리 처리하는 방법1
# 백화점은 ;



# facility_list = ['대형마트', '편의점', '어린이집', '유치원','학교','학원', '지하철역','문화시설','공공기관', '은행','관광명소','음식점', '카페','병원','약국'] 
# # 카테고리 줄이기, 초등학교와 같은 형식으로,  마트 api


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
                    "radius": 1500, # 반경
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


# MT1	대형마트
# CS2	편의점
# PS3	어린이집, 유치원
# SC4	학교
# AC5	학원
# PK6	주차장
# OL7	주유소, 충전소
# SW8	지하철역
# BK9	은행
# CT1	문화시설
# AG2	중개업소
# PO3	공공기관
# AT4	관광명소
# AD5	숙박
# FD6	음식점
# CE7	카페
# HP8	병원
# PM9	약국

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

