import os
import sys
from main import *

def lineCount(file_name):
    with open(file_name) as f:
        for count, _ in enumerate(f, 1):
            pass
    return count

file=open('monitor\\monitorList.txt','r',encoding='utf-8')
lenn=lineCount('monitor\\monitorList.txt')
if lenn&1:
    print('文本行数不是偶数')
    sys.exit()
lenn>>=1
monitorList={}
for i in range(lenn):
    name=file.readline()
    name=name[0:len(name)-1]
    monitorList[name]=list(map(int,file.readline().split(',')))
file.close()

for name in monitorList:
    print('现在开始检查昵称为 '+name+' 的用户的做题情况。')
    for uid in monitorList[name]:
        time.sleep(0.1)
        data=getUser(uid)
        user=data['currentData']['user']
        if user['passedProblemCount'] != None:
            Try=int(user['submittedProblemCount'])
            AC=int(user['passedProblemCount'])
        else:
            print('用户编号为 '+str(uid)+' 的用户开启了完全隐私保护。')
            continue
        if os.path.exists(monitorListPath+'\\'+str(uid)+'.txt'):
            file=open(monitorListPath+'\\'+str(uid)+'.txt','r',encoding='utf-8')
            ACL,TryL=map(int,file.readline().split(','))
            file.close()
            print('用户编号为 '+str(uid)+' 的用户距离上次运行监视器，又通过了 '+str(AC-ACL)+' 题，又提交了 '+str(Try-TryL)+' 发代码。')
            saveData(str(AC)+','+str(Try),monitorListPath,str(uid)+'.txt')
        else:
            saveData(str(AC)+','+str(Try),monitorListPath,str(uid)+'.txt')
            print('用户编号为 '+str(uid)+' 的用户第一次进入卷王监视名单。')
    print('\n')
# for uid in range(UidStart,UidEnd+1):
#     data=getUser(uid)
    
#     user=data['currentData']['user']
    
#     saveData(user['name'],UserSavePath,str(uid)+'.md')