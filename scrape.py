import requests
from bs4  import BeautifulSoup
def scrap_pm25():
    url ="https://data.moenv.gov.tw/api/v2/aqx_p_02?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=datacreationdate%20desc&format=JSON"
    datas = request.get(url).json()["records"]
    columns = list(datas[0].keys())
    values=[list(data.valuse()) for data in datas]
    return columns,values
def scrap_stocks():
    url = "https://histock.tw/index"
    try :
        resp = requests.get(url)
        soup = BeautifulSoup(resp.text,'lxml')
        trs = sop.find(string='加權指數').find_parent('div').find
        datas = []
        for tr in trs :
            data = []
            for th in tr.find_all('th'):
                data.append(th.text.strip())
            for td in tr.find_all('td'):
                data.append(td.text.strip())
            datas.append(date)
        return datas
    except Exception as e:
        print(e)
    return None

if __name__=="_main_":
        print(scrap_stocks())
        print(scrap_pm25)