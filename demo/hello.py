import json

f=open("居民客户的用电缴费习惯分析2.csv","r",encoding='utf-8') #
ls=[]
for line in f:
        line = line.replace("\n", "")
        ls.append(line.split(","))

f.close()
fw=open("居民客户的用电缴费习惯分析2.json","w",encoding='utf-8')
for i in range(1,len(ls)):
    ls[i]=dict(zip(ls[0],ls[i]))
a = json.dumps(ls[1:],sort_keys=True,indent=4,ensure_ascii=False)
print(a)
fw.write(a)
fw.close()