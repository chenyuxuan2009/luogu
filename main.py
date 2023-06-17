import requests
import json
import time

headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4331.0 Safari/537.36", }
monitorListPath='monitor\\passedProblemCount'

def getUser(uid):
    url=f"https://www.luogu.com.cn/user/{uid}?_contentOnly=1"
    data=requests.get(url, headers=headers).text
    return json.loads(data)
def saveData(data,savePath,filename):
    cfilename=savePath+'\\'+filename
    file=open(cfilename,"w",encoding="utf-8")
    for d in data:
        file.writelines(d)
    file.close()