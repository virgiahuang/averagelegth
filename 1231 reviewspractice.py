
data = []
count = 0
with open ('reviews.txt','r') as f :
    for line in f:
        data.append(line.strip())
        count += 1
        if count % 1000 == 0:
            print (len(data))
print ('Message has been all loaded,total',len(data),'data')


#如何算出留言的平均長度 

sum_len = 0 #先設定留言長度總和為0
for d in data : #每一筆資料命名為d,每個d是一個字串 然後一筆一筆叫出來
    sum_len = sum_len + len(d) # 總和加上下一筆留言長度再存回sum_len ， 也可寫成sum_len += len(d)
print ('The average lenght of message is',sum_len/len(data),'letters')

