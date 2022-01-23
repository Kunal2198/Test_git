low=100
high=300
digits='123456789'
seq = []
nl = len(str(low)) #4
hl = len(str(high)) #5

for i in range(nl,hl+1): #4
    for j in range(0,10-i): #(0,6)->0to5 j=0
        num = int(digits[j:j+i])  #digits[0:0+4]
        if num>low and num<high:
            seq.append(num)


print(seq)