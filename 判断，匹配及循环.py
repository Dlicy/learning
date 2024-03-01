print("鏉堟挸鍙嗛獮鎾窞")
a = int(input())
#閸掋倖鏌�
if a > 18:
    print("瀹稿弶鍨氶獮锟�")
elif a = 18:
    print("閸掓碍鍨氶獮锟�")
else:
    print("閺堫亝鍨氶獮锟�")

#閸栧綊鍘�
match a:
    case 18:
        print("18瀹€锟�")
    case 19:
        print("19瀹€锟�")
    case 20:
        print("20瀹€锟�")
    case _: #閸栧綊鍘ら崗鏈电铂閹懎鍠�
