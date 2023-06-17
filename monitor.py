import requests
import json
import time
import os
from main import *

file=open('monitor\\monitorList.txt','r',encoding='utf-8')
monitorList=file.readline()
file.close()
monitorList=list(map(int,monitorList.split(',')))
print(monitorList)
for uid in monitorList:
    data=getUser(uid)
    user=data['currentData']['user']
    if user['passedProblemCount'] != None:
        Try=int(user['submittedProblemCount'])
        AC=int(user['passedProblemCount'])
    else:
        print('用户编号为 '+str(uid)+' 的用户开启了完全隐私保护。')
        continue
    if os.path.exists(monitorListPath+'\\'+str(uid)+'.txt'):
        # print('ok')
        file=open(monitorListPath+'\\'+str(uid)+'.txt','r',encoding='utf-8')
        ACL,TryL=map(int,file.readline().split(','))
        file.close()
        print('用户编号为 '+str(uid)+' 的用户距离上次运行监视器，又通过了 '+str(AC-ACL)+' 题，又提交了 '+str(Try-TryL)+' 发代码。')
        saveData(str(AC)+','+str(Try),monitorListPath,str(uid)+'.txt')
    else:
        saveData(str(AC)+','+str(Try),monitorListPath,str(uid)+'.txt')
        print('用户编号为 '+str(uid)+' 的用户第一次进入卷王监视名单。')
# for uid in range(UidStart,UidEnd+1):
#     data=getUser(uid)
    
#     user=data['currentData']['user']
    
#     saveData(user['name'],UserSavePath,str(uid)+'.md')