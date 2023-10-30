import json
import requests
import pandas as pd

# 행정동 리스트
dong_list = {'대연1동', '대연3동', '대연4동', '대연5동', '대연6동',
             '용호1동', '용호2동', '용호3동','용호4 동','용당 동',
             '감만1 동','감만2 동','우암 동',
             '문현1 동','문현2 동','문현3 동','문현4 동'}

# 시설 리스트 (카테고리)
facility_list = ['지하철역','대형마트','백화점',
                 {'category':'유치원', "code":'PS3'},
                 {'category':'초등학교',"code":'PS3'},
                 '경찰서',
                 '종합병원',
                 '소방서',
                 {'category':'공원',"code":'PK6'}]

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
                    "page": page_num,
                    "radius": 1500,
                    "size": 15,
                    "sort":"distance",
                    "x": x,
                    "y": y
                }

                # 유치원, 초등학교, 공원은 카테고리 검색으로 처리
                if isinstance(facility, dict):
                  params["category_group_code"] = facility["code"]
                  url_search=f'https://dapi.kakao.com/v2/local/search/category.json'
                  category_or_keyword=facility["category"]
                else:
                  params["query"] = facility
                  url_search=f'https://dapi.kakao.com/v2/local/search/keyword.json'
                  category_or_keyword=facility
                
                places_res=requests.get(url_search, headers=headers,params=params)

                places_json=places_res.json()
                
                if places_json.get('documents'):
                    places=places_json['documents']
                    
                    for place in places:
                        place_name=place['place_name'] 
                        places_name_list.append(place_name) 

                else:
                    break
                
                page_num+=1
            
            df=pd.DataFrame(places_name_list,columns=[f'{category_or_keyword}'])
            df.drop_duplicates(inplace=True)
            
            filename=f'{dong}_{category_or_keyword}.csv' 
            df.to_csv(filename,index=False)

print("csv파일 생성 완료! 다음 수집할 데이터를 리스트에 넣고 생성해!")
