# #부산 사하구 낙동대로 반경 2km 편의점 데이터

# import json
# import requests
# import pandas as pd

# addr = '부산시 사하구 낙동대로'
# url = 'https://dapi.kakao.com/v2/local/search/address.json?query=' + addr
# headers = {'Authorization': 'KakaoAK efc1b26d609b687398664b4f30490c20'}

# response = requests.get(url, headers=headers)
# result = response.json()

# if result.get('documents'):
#     x = result['documents'][0]['x']
#     y = result['documents'][0]['y']
#     print(f"x: {x}, y: {y}")
# else:
#     print("No results found.")
#     print(result)  # 에러 메시지 출력

# # 집 주소 반경 30km 이내 편의점 리스트 추출
# convs = {}
# places_name_list=[]
# for i in range(1, 46):
#     headers = {
#         "Authorization": "KakaoAK efc1b26d609b687398664b4f30490c20"
#     }
    
#     params = {
#         'x': float(x),
#         'y': float(y),
#         'radius': 2000,
#         'page': i,
#         'size': 15,
#         'sort': 'distance'
#     }

#     keywords = '편의점'
    
#     url_keyword_search='https://dapi.kakao.com/v2/local/search/keyword.json?query={}'.format(keywords)
    
#     places_res=requests.get(url_keyword_search, headers=headers,params=params)
   
#     places_json=places_res.json()
#     if places_json.get('documents'):
#         places=places_json['documents']
#         for place in places:
#             place_name=place['place_name'] #장소 이름 가져오기 
#             places_name_list.append(place_name) #리스트에 추가 
        
#     else:
#         print(f"No results found on page {i}")
#         print(places_json) 

# #리스트를 데이터프레임으로 변환 
# df=pd.DataFrame(places_name_list,columns=['Convenience Store'])

# # 중복 제거
# df.drop_duplicates(inplace=True)
# df.to_csv('convenienceStore.csv',index=False)

# print("편의점 csv파일 생성")