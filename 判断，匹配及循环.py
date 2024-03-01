print("输入年龄")
a = int(input())
#判断
if a > 18:
    print("已成年")
elif a = 18:
    print("刚成年")
else:
    print("未成年")

#匹配
match a:
    case 18:
        print("18岁")
    case 19:
        print("19岁")
    case 20:
        print("20岁")
    case _: #匹配其他情况
