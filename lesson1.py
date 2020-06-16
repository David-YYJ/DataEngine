# -*- coding: utf-8 -*-

# Action1：求2+4+6+8+...+100的求和
sum = 0
number = 2
while number <= 100:
       sum = sum + number
       number = number + 2
print("..............action1................")        
print(sum) 


from pandas import Series, DataFrame
import pandas as pd
data = {'语文': [68, 95, 98, 90,80], '数学': [65, 76, 86, 88, 90], '英语': [30, 98, 88, 77, 90]}
df = DataFrame(data, index=['张飞', '关羽', '刘备', '典韦', '许褚'], columns=['语文', '数学', '英语'])
print("............action2............") 
print('平均成绩：', df.mean())
print('最小成绩：', df.min())
print('最大成绩：', df.max())
print('成绩的方差：', df.var())
print('成绩的标准差：', df.std())
df['总分']=df.sum(axis=1)
print(df.sort_values(by='总分', ascending=False))

# 对汽车投诉信息进行分析
import pandas as pd

result = pd.read_csv('car_complain.csv',encoding="gbk")
result = result.drop('problem', 1).join(result.problem.str.get_dummies(','))
print("............action3............") 
df= result.groupby(['brand'])['id'].agg(['count'])
print('品牌投诉总数：',df.sort_values('count',ascending=False))

df1= result.groupby(['car_model'])['id'].agg(['count'])
print('车型投诉总数：',df1.sort_values('count',ascending=False))

df2= result.groupby(['brand','car_model'])['id'].agg(['count']).groupby(['brand']).mean()
print('平均车型投诉总数：',df2.sort_values('count',ascending=False))