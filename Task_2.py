import turtle

# Функція для малювання однієї сторони сніжинки Коха
def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        size /= 3.0
        koch_curve(t, order-1, size)
        t.left(60)
        koch_curve(t, order-1, size)
        t.right(120)
        koch_curve(t, order-1, size)
        t.left(60)
        koch_curve(t, order-1, size)

# Основна функція програми
def main():
    # Запит рівня рекурсії у користувача
    level = int(input("Введіть рівень рекурсії: "))
    
    # Налаштування turtle
    wn = turtle.Screen()
    wn.bgcolor("white")
    wn.title("Сніжинка Коха")
    
    t = turtle.Turtle()
    t.speed(0)  # Максимальна швидкість малювання
    t.penup()
    t.goto(-150, 90)
    t.pendown()

    # Малювання трьох сторін сніжинки
    for _ in range(3):
        koch_curve(t, level, 300)
        t.right(120)
    
    # Завершення роботи turtle
    turtle.done()

# Виконання основної функції при запуску скрипта
if __name__ == "__main__":
    main()

