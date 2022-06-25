import pandas as pd
import numpy as np
import csv
# 读出数据
df = pd.read_excel('./测试数据.xlsx')
data=df.values
# DataFrame数据结构
users=pd.DataFrame(data,columns=['userid','time','money'])
# 根据userid分组求和缴费金额
money_data=users.groupby('userid')['money'].sum()
# 计算平均缴费金额
mean_money=0
for i in money_data:
    mean_money+=(i/money_data.size)
# 分组求和缴费次数
num=users.groupby('userid')['time'].count()
# 计算平均缴费次数
mean_num=0
for i in num:
    mean_num+=(i/num.size)
# 写入csv
header=['平均缴费金额','平均缴费次数']
with open('居民客户的用电缴费习惯分析 1.csv','w',newline='',encoding='utf-8') as cf:
    writer=csv.writer(cf)
    writer.writerow(header)
    writer.writerow([mean_money,mean_num])
# # 读取数据
# with open('居民客户的用电缴费习惯分析 1.csv','r',encoding='utf-8') as cf:
#     reader=csv.reader(cf)
#     for i in reader:
#         print(i)
             


user_id=users['userid'].values
user_id=list(set(user_id))
user_id[99]


num=num.values
money_data=money_data.values


# 任务2、对每个居民客户的用电缴费情况按照上述四种居民客户类型进行归类，结果保存”居民客户的用电缴费习惯分析 2.csv”

# 归类对象：高价值型客户 大众性客户 潜力型客户 低价值型客户

header=['userid','times','money','std_money','std_times','type']
with open('居民客户的用电缴费习惯分析2.csv','w',newline='',encoding='utf-8') as cf:
    writer=csv.writer(cf)
    writer.writerow(header)
    for i in range(0,100):
        if num[i]>=mean_num and money_data[i]>=mean_money:
            writer.writerow([user_id[i],num[i],money_data[i],mean_money,mean_num,'高价值型用户'])
        elif num[i]>=mean_num and money_data[i]<mean_money:
            writer.writerow([user_id[i],num[i],money_data[i],mean_money,mean_num,'大众型用户'])
        elif num[i]<mean_num and money_data[i]>=mean_money:
            writer.writerow([user_id[i],num[i],money_data[i],mean_money,mean_num,'潜力型用户'])
        else:
            writer.writerow([user_id[i],num[i],money_data[i],mean_money,mean_num,'低价值型用户'])

data2 = pd.read_csv("居民客户的用电缴费习惯分析2.csv",encoding='utf-8')

data2['res'] = (data2['times']-data2['std_times'])*(data2['money']/data2['times'])
data2 = data2.sort_values(by=['res'],ascending=False).head(5)
data2 = data2.values

data2

header=['userid','times','money','std_money','std_times','type','res']
with open('居民客户的用电缴费习惯分析3.csv','w',newline='',encoding='utf-8') as cf:
    writer=csv.writer(cf)
    writer.writerow(header)
    writer.writerow(data2[0])
    writer.writerow(data2[1])
    writer.writerow(data2[2])
    writer.writerow(data2[3])  
    writer.writerow(data2[4])
   

data3 = pd.read_csv("居民客户的用电缴费习惯分析3.csv",encoding='utf-8')
data3