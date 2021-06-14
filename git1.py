# -*- coding: utf-8 -*-
# @Author   : knut
# @Time     : 2021/6/13 10:59

myList={1,2,3,4}
myDictionary={"key":"value","key2":"value"}

myPhones={"Iphone x":1000,"Sumsang S9":900}

print(myPhones)
# access dic keys
# str(Iphone_Price) 换算成str，两个str才能相加
Iphone_Price=myPhones["Iphone x"]
print("IPhone price:"+str(Iphone_Price))

# change key values
myPhones["Iphone x"]=500
print(myPhones)

# 清除
myPhones.clear()
print(myPhones)

#Dictionary练习1
能不能pull？
