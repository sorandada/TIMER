#カウントダウンタイマー
from time import sleep
from playsound import playsound

def down_timer_s(s):#秒単位の関数
    for i in range(0, s):
        if i < 60:
            if i in range(0, 10):
                print("0"+str(i))
            else:
                print(i)
        sleep(1)
    print("TIME!!!!!!!!")

def down_timer_m(m):#分単位の関数
    for i in range(target_time_m):
        for j in range(0, 60):

            if i < 10:
                print("0" + str(i)+":", end="")

            if j < 10:
                print("0"+str(j))
            else:
                print(j)

            sleep(1)
    print("TIME!!!!!!!!")


"""def down_timer_h(h):#分単位の関数
    for h in range(target_time_h):
        for m in range(0, 60):
            for s in range(0, 60):
                if h < 10:
                    print("0" + str(h) + ":", end="")
                else:
                    print(str(h) + ":", end="")

                if m < 10:
                    print("0" + str(m) + ":", end="")
                else:
                    print(str(m) + ":", end="")

                if s < 10:
                    print("0" + str(s))
                else:
                    print(s)


                sleep(1)
    print("TIME!!!!!!!!")"""


#target_time_s = 20
#target_time_m = 3
#target_time_h = 1


#down_timer_h(target_time_h)
#down_timer_m(target_time_m)
#down_timer_s(target_time_s)

t=input("入力：")
target_time_m=int(t)
down_timer_m(target_time_m)

playsound("bacs.MP3")


