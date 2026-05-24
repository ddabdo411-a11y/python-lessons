import turtle
import time
import random

delay = 0.1
score = 0
high_score = 0

# 1. إعداد شاشة اللعبة
wn = turtle.Screen()
wn.title("لعبة الحية ببايثون")
wn.bgcolor("#2c3e50")
wn.setup(width=600, height=600)
wn.tracer(0) # إيقاف التحديث التلقائي للشاشة لجعل الحركة سلسة

# 2. رأس الحية
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("#2ecc71")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# 3. طعام الحية
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("#e74c3c")
food.penup()
food.goto(0, 100)

segments = []

# 4. لوحة النتيجة
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("النتيجة: 0  |  أعلى نتيجة: 0", align="center", font=("Arial", 16, "bold"))

# 5. دالات التحكم في الاتجاه
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# 6. ربط أزرار لوحة المفاتيح
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

# 7. حلقة اللعبة الرئيسية
while True:
    wn.update()

    # التحقق من الاصطدام بالحواف (خسارة)
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"
        
        # إخفاء أجزاء جسم الحية القديمة
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        
        # إعادة تصغير النتيجة
        score = 0
        delay = 0.1
        pen.clear()
        pen.write(f"النتيجة: {score}  |  أعلى نتيجة: {high_score}", align="center", font=("Arial", 16, "bold"))

    # التحقق من أكل الطعام
    if head.distance(food) < 20:
        # نقل الطعام لمكان عشوائي
        x = random.randint(-280, 280)
        y = random.randint(-280, 260)
        food.goto(x, y)

        # إضافة جزء جديد لجسم الحية
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("#27ae60")
        new_segment.penup()
        segments.append(new_segment)

        # تسريع اللعبة قليلاً وزيادة النقاط
        delay -= 0.003
        score += 10
        if score > high_score:
            high_score = score
            
        pen.clear()
        pen.write(f"النتيجة: {score}  |  أعلى نتيجة: {high_score}", align="center", font=("Arial", 16, "bold"))

    # تحريك جسم الحية بترتيب عكسي ليلحق بالرأس
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # تحريك أول جزء خلف الرأس مباشرة
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # التحقق من اصطدام الحية بجسمها (خسارة)
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
            
            score = 0
            delay = 0.1
            pen.clear()
            pen.write(f"النتيجة: {score}  |  أعلى نتيجة: {high_score}", align="center", font=("Arial", 16, "bold"))

    time.sleep(delay)

wn.mainloop()
