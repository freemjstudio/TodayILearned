import requests
import pandas as pd 

MobileOS_list = ["IOS", "AND", "WIN"]
showflag = 0 # 컨텐츠표출여부(1=표출, 0=비표출)

contentType_list = [12, 14, 15, 25, 28, 32, 38, 39] # 관광타입(12:관광지, 14:문화시설, 15:축제공연행사, 25:여행코스, 28:레포츠, 32:숙박, 38:쇼핑, 39:음식점) ID

contentType_dict = {12:"관광지", 14:"문화시설", 15:"축제공연행사", 25:"여행코스", 28:"레포츠", 32:"숙박", 38:"쇼핑", 39:"음식점"}

areaCode = 1 # Seoul 지역 코드 
sigungu_list = [i for i in range(1, 11)] # 1 ~ 10 시군구 코드 

# {"response": {"header":{"resultCode":"0000","resultMsg":"OK"},"body": {"items": "","numOfRows":0,"pageNo":10,"totalCount":33}}} 

entire_data = [] 


for mobile in MobileOS_list:
    print("mobile Type:", mobile)
    for content in contentType_list:
        print("content Type : " , contentType_dict[content])
        for sgg in sigungu_list:
            print("시군구: ", sgg)
            for page in range(5):
                url = f"https://apis.data.go.kr/B551011/KorWithService1/areaBasedSyncList1?serviceKey=xz7iOMQiFnZbsS4NZx5uCNKfQ0A%2Bwilakf8cCYkqPSIpaECLDbV5G0%2BnNYxTyzYpbLcRVtbonCU22Uqd5F2bDA%3D%3D&numOfRows=100&pageNo={page}&MobileOS={mobile}&MobileApp=AppTest&_type=json&showflag=1&listYN=Y&arrange=C&contentTypeId={content}&areaCode=1&sigunguCode={sgg}"

                
                # data_list = json_data['response']['body']['items']['item']
                result = requests.get(url)
                json_data = result.json()
                
                if not json_data['response']['body']['items']:
                    break 
                data_list = json_data['response']['body']['items']['item']
                entire_data.append(data_list)