import time

def countdown(t):
    while t > 0:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        t -= 1
    print("倒计时结束")

t = int(input("请输入倒计时的秒数："))
countdown(t)
