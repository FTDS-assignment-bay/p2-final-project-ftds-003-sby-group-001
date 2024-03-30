import requests
import pandas as pd


API_KEY = open('API_KEY').read()
SEARCH_ENGINE_ID = open('SEARCH_ENGINE_ID').read()
indexs = 436
df =pd.read_csv('tourism_image_url.csv')

# place = df['Place_Name'][indexs]
# search_query = place

url = 'https://www.googleapis.com/customsearch/v1'

params ={
    'q': search_query,          # Kata Kunci yang dicari
    'key': API_KEY,             # Code API user
    'cx': SEARCH_ENGINE_ID,     # code project
    'searchType': 'image',      # bentuk apa yang dicari
    # 'dateRestrict': '2016-01-01:2016-12-31' # Tanggal dalam perncarian
    # 'fileType': 'pdf',                      # file apa yang dicari
    'lr': 'lang_id',                        # bahasa apa yang dicari
    'gl': 'ID'                              # negara mana 
}   


# print(response.text)
# result1 = pd.DataFrame(response)
# result1.to_csv('test.csv',index=False)

# print(results)


# if 'items' in results:
#     print(results['items'][0]['link'])
# result =
# test=[1]
# i=int(0)
# for item in results:
#     test[1][i] = item[1]['link']
#     i+= 1

# response =requests.get(url, params=params)
# results = response.json()['items']
# print(results)
# for item in results:
#     print (item['link'])

for i in df:
    params ={
        'q': df['Place_Name'][i],          # Kata Kunci yang dicari
        'key': API_KEY,             # Code API user
        'cx': SEARCH_ENGINE_ID,     # code project
        'searchType': 'image',      # bentuk apa yang dicari
        'lr': 'lang_id',                        # bahasa apa yang dicari
        'gl': 'ID'                              # negara mana 
        }
    response =requests.get(url, params=params)
    results = response.json()['items']
    links = results[indexs]['link']
        

    
df.to_csv('test.csv')