import turtle
import time

def draw_clock():
    # 创建画布
    window = turtle.Screen()
    window.bgcolor("white")
    window.setup(width=600, height=600)

    # 创建表盘
    clock = turtle.Turtle()
    clock.hideturtle()
    clock.speed(0)
    clock.pensize(3)
    clock.penup()
    clock.goto(0, 0)
    clock.pendown()
    clock.circle(200)

    # 创建时针、分针、秒针
    hour_hand = turtle.Turtle()
    hour_hand.hideturtle()
    hour_hand.speed(0)
    hour_hand.pensize(5)
    hour_hand.penup()
    hour_hand.goto(0, 0)
    hour_hand.pendown()

    minute_hand = turtle.Turtle()
    minute_hand.hideturtle()
    minute_hand.speed(0)
    minute_hand.pensize(3)
    minute_hand.penup()
    minute_hand.goto(0, 0)
    minute_hand.pendown()

    second_hand = turtle.Turtle()
    second_hand.hideturtle()
    second_hand.speed(0)
    second_hand.pensize(1)
    second_hand.penup()
    second_hand.goto(0, 0)
    second_hand.pendown()

    while True:
        # 获取当前时间
        current_time = time.localtime()

        # 计算时针、分针、秒针的角度
        hour_angle = (current_time.tm_hour % 12) * 30 + current_time.tm_min / 2
        minute_angle = current_time.tm_min * 6
        second_angle = current_time.tm_sec * 6

        # 绘制时针、分针、秒针
        hour_hand.setheading(-hour_angle + 90)
        hour_hand.fd(80)

        minute_hand.setheading(-minute_angle + 90)
        minute_hand.fd(120)

        second_hand.setheading(-second_angle + 90)
        second_hand.fd(160)

        # 更新画布
        window.update()

        # 等待1秒钟，然后清除之前绘制的指针
        time.sleep(1)
        hour_hand.clear()
        minute_hand.clear()
        second_hand.clear()

draw_clock()
