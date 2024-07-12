import turtle

def draw_koch_segment(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        size /= 3.0
        draw_koch_segment(t, order-1, size)
        t.left(60)
        draw_koch_segment(t, order-1, size)
        t.right(120)
        draw_koch_segment(t, order-1, size)
        t.left(60)
        draw_koch_segment(t, order-1, size)

def draw_koch_snowflake(t, order, size):
    for _ in range(3):
        draw_koch_segment(t, order, size)
        t.right(120)

def main(order):
    screen = turtle.Screen()
    screen.bgcolor("white")
    t = turtle.Turtle()
    t.speed(0)
    
    size = 300  # Розмір сніжинки
    t.penup()
    t.goto(-size/2, size/3)
    t.pendown()
    
    draw_koch_snowflake(t, order, size)
    
    screen.mainloop()

if __name__ == '__main__':
    order = int(input("Введіть рівень рекурсії для сніжинки Коха: "))
    main(order)
