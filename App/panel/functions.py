from bs4 import BeautifulSoup
import requests
import time
import requests
import json
from bs4 import BeautifulSoup
import re
import itertools
import json
import xlsxwriter

startTime = time.time()
WAIT_TIME = 1
MAX_WORKERS = 20
lang = "fa"
# Functions For Related Search--------------------------------

def get_related_keyword(keyword):
    time.sleep(WAIT_TIME)
    url = "https://www.google.com/search"
    params = {"q": keyword}  
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0"
    }
    soup = BeautifulSoup(
        requests.get(url, params=params, headers=headers).content, "html.parser"
    )
    result = soup.find_all("div", {"class": "s75CSd OhScic AB4Wff"})
    keywords=[]
    for keyword in result:
        keyword=re.sub(r'<.*?>', '', str(keyword))
        keywords.append(keyword)
    return keywords

def Layout_related(keyword,layer):
    layout1=get_related_keyword(keyword)
    if layer == 1:
        return layout1
    else:
        layout2=[]
        for keyword in layout1:
            result=get_related_keyword(keyword)
            [layout2.append(item) for item in result]
        if layer == 2:
            return list(dict.fromkeys(layout1+layout2))
        else:
            layout3=[]
            for keyword in layout2:
                result=get_related_keyword(keyword)
                [layout3.append(item) for item in result]
            if layer == 3:               
                return list(dict.fromkeys(layout1+layout2+layout3))
            else:
                layout4=[]
                for keyword in layout3:
                    result=get_related_keyword(keyword)
                    [layout4.append(item) for item in result]               
                    return list(dict.fromkeys(layout1+layout2+layout3+layout4))

# Functions For Sugessted Search--------------------------------

def makeGoogleRequest(query):
    # If you make requests too quickly, you may be blocked by google 
    time.sleep(WAIT_TIME)
    URL="http://suggestqueries.google.com/complete/search"
    PARAMS = {"client":"firefox",
            "hl":lang,
            "q":query}
    headers = {'User-agent':'Mozilla/5.0'}
    response = requests.get(URL, params=PARAMS, headers=headers)
    if response.status_code == 200:
        suggestedSearches = json.loads(response.content.decode('utf-8'))[1]
        return suggestedSearches
    else:
        return "ERR"

def getGoogleSuggests(keyword):
    # err_count1 = 0
    charList = ['آ','ا','ب','پ','ت','ث','ج','چ','ح','خ','د','ذ','ر','ز','ژ','س','ش','ص','ض','ط','ظ','ع','غ','ف','ق','ک','گ','ل','م','ن','ه','و','ی']
    queryList1 = [keyword + " " + char for char in charList]
    queryList2 = [char + " "+keyword for char in charList]
    queryList=queryList1+queryList2
    suggestions = []
    for query in queryList:
        suggestion = makeGoogleRequest(query)
        if suggestion != 'ERR':
            suggestions.append(suggestion)

    # Remove empty suggestions
    suggestions = set(itertools.chain(*suggestions))
    if "" in suggestions:
        suggestions.remove("")
    return list(dict.fromkeys(suggestions))
            
# Functions For Create exell Files--------------------------------

def create_exel(filename,data1,column1,data2=None,column2=None):
    workbook = xlsxwriter.Workbook(f'{filename}.xlsx')
    worksheet = workbook.add_worksheet()
    worksheet.write(0, 0, column1)
    row = 1
    column = 0
    for item in data1 :
        worksheet.write(row, column, item)
        row += 1
    if data2:
        worksheet.write(0, 1, column2)
        row = 1
        column = 1
        for item in data2 :
            worksheet.write(row, column, item)
            row += 1

     
    workbook.close()
