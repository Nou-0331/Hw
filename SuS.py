# print("hello world")
a=5
b=5
c=a+b
print(c)
#print("answer:"+str(5+10))
print(5-2)
#number=input("Enter the price")
#print(float(number)*0.5)
print("i love Minecraft".replace("Minecraft","roblox"))
# list
machine=['gear1','gear2','gear3']
print(machine)
# add
machine.append ('gear4')
print (machine)
# how many in the bags?
print(len(machine))
# takeout
print(machine[0])
# takeout one by one
for i in machine:
    print(i)
# delete 
del machine[0]
print (machine)
#check something in bag
print ('gear2' in machine)
# dictionary
#記錄標題 (key)和內容(value)
myInformation={
    'name':'Noah',
    'hobby':'Roblox'
}
# how many slots
print(len(myInformation))
# add new key or value
myInformation['best friend'] = 'Mattie'
print (myInformation)
# tuple 元組
# 沒法修改的list
# 只有一個項目時，後面要加上 ex : ('XX市',)
Myfriends = ('Mattie','Rider')
for i in Myfriends:
    print(i)
    #字串和list轉換
    string = 'mattie,rider'
    li = string.split(',')
    print (li)

# 字母縮寫
sentence = 'As Soon As Possible'
sentenceList = sentence.split(' ')
print (sentenceList)
answer = ''
for i in sentenceList:
    print(i[0])
    answer = answer + i[0]
    print(answer)
    
