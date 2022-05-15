from urllib.request import HTTPDefaultErrorHandler


Hurdle=0
for i in range(0,5):
    Hurdle=i
    print("허들을 넘었습니다.")
    if Hurdle ==4:
        print("레이스를 완주했습니다.")
