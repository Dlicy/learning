a = 10
pi = 3.14159
#字符串编码
print(ord('A'))
print(chr(342))
print(str("434jhd"))

print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
print(b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore'))

#格式化输入
print("fjdks%s" %a)

print("hfsa,{0},fdjk,{1}fdsa{2}".format('小明','小红',pi))#format方法
print(f"dss{a}fdsjl{pi:.3f}")#f-string
