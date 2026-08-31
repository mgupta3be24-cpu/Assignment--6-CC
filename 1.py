import numpy as np

#i.
temperature = [25, 28, 31, 35, 38, 27, 33, 40]

add_array =[2,2,2,2,2,2,2,2]
ans=[]
for n,m in zip(temperature, add_array):
    ans.append(n+m)
print(ans)

#ii.
first=[1.8,1.8,1.8,1.8,1.8,1.8,1.8,1.8]

second = [32,32,32,32,32,32,32,32]

temp1=[]
Far_temp =[]
for n,m in zip(ans, first):
    temp1.append(n* m)

for n,m in zip(temp1, second):
    Far_temp.append(n+m)
print(Far_temp)


#iii.
temperature = np.array(temperature)
ans = temperature[temperature > 32]
print(ans)

#iv.
print(np.count_nonzero(ans))



#v.
#iteration is done one by one to each elements where as vectorization and Boolean indexing
# is done on whole dataset.
