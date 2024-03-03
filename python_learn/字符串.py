a = 10
pi = 3.14159
#鐎涙顑佹稉鑼椽閻拷
print(ord('A'))
print(chr(342))
print(str("434jhd"))

print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
print(b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore'))

#閺嶇厧绱￠崠鏍翻閸忥拷
print("fjdks%s" %a)

print("hfsa,{0},fdjk,{1}fdsa{2}".format('鐏忓繑妲�','鐏忓繒瀛�',pi))#format閺傝纭�
print(f"dss{a}fdsjl{pi:.3f}")#f-string
