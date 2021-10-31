import requests
import json
import base64
import re

def main(targetsrting):
    email=""    #email
    key=""  #key
    #targetsrting='ip="202.107.117.5/24"' #搜索关键字
    target=base64.b64encode(targetsrting.encode('utf-8')).decode("utf-8")
    url="https://fofa.so/api/v1/search/all?email={}&key={}&qbase64={}&fields=host,server,title&size=1000".format(email,key,target)
    resp = requests.get(url)
    try:
        resp = requests.get(url)
        data_model = json.loads(resp.text) #字符串转换为字典
        #print(data_model)
        num = 0
        for i in data_model["results"]:
            num = num +1
            if (len(i[2]) > 0) and ('Not Found' not in i[2])&('ERROR' not in i[2])&('Unavailable' not in i[2]):
                print('{:<30}{:<30}{:<20}'.format(i[0],i[1],i[2]))
        a = input('是否要进行边缘资产的title筛查(建议用body搜索 --确定的话请摁1):')
        if(a == '1'):
            body(targetsrting,data_model)
        print("fofa查询总共",num,"条数据,以上数据均通过title筛查不输出空值。")
    except:
        print("'\n',出现问题了,账号密码、网络、其他原因，无法fofa查询")

def body(targetsrting,data_model):
    print('/n','body筛查的结果')
    num = 0
    inputString = '{}'.format(targetsrting)
    f2 = re.findall(r'"([^"]*)"', inputString)
    for i in data_model["results"]:
        num = num +1
        if (f2[0] in i[2]):
            print('{:<30}{:<30}{:<20}'.format(i[0],i[1],i[2]))

if __name__ == '__main__':
    print('''
    fofa语法
    host=".gov.cn"
    port="6379"
    ip="1.1.1.1"
    ip="220.181.111.1/24"
    
    该脚本主要用于快速C段寻找目标边缘资产。 --by aufeng
    ''')
    a = input("请输入需要查询的fofa语法：")
    main(a)
