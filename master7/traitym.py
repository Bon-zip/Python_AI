import turtle
import math
t = turtle.Turtle()
# Đặt tốc độ vẽ nhanh nhất.
t.speed(0)
# Đặt màu bút là đỏ.
t.color("red")
# Đặt màu nền là đen.
turtle.bgcolor("pink")


# Tính toán tọa độ (x, y) dựa trên một công thức toán học tạo hình trái tim.
def corazon(n):
    # Xác định tọa độ x.
    x = 16 * math.sin(n) ** 3 
    # Xác định tọa độ y.
    y = 13 * math.cos(n) - 5 * \
    math.cos(2 * n) - 2 * math.cos(3 * n) - \
    math.cos(4 * n)
    return x, y


t.penup()
# Vẽ 15 hình trái tim lồng nhau với kích thước tăng dần.
for i in range(15):
    t.goto(0, 0)
    t.pendown()
    # Duyệt qua các góc để tính toán tọa độ từng điểm của trái tim.
    for n in range(0, 100, 2):
        # Gọi hàm corazon để tính tọa độ.
        x, y = corazon(n / 10)
        #  Đặt bút tới vị trí (x, y), nhân tọa độ với i để tăng kích thước.
        t.goto(x * i, y * i)
        t.penup()
# Ẩn con trỏ bút vẽ sau khi hoàn thành.
t.hideturtle()
# Kết thúc chương trình vẽ.
turtle.done()
