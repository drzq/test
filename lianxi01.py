import pickle

# f = open('H:/10569.dat',"wb")
# pickle.dump("zhuqi",f,True)
# pickle.dump("zhangsan",f,True)

f2 = open('H:/10569.dat','rb')
a = pickle.load(f2)
b = pickle.load(f2)
print(a)
print(b)
