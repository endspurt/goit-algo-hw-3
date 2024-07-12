def hanoi(n, source, target, auxiliary, moves):
    """
    Функція для переміщення дисків у задачі Ханойських башт.
    
    n: Кількість дисків
    source: Початкова стрижень (A)
    target: Цільова стрижень (C)
    auxiliary: Допоміжна стрижень (B)
    moves: Список для збереження кроків
    """
    if n > 0:
        # Переміщуємо n-1 дисків з source до auxiliary, використовуючи target як допоміжну
        hanoi(n-1, source, auxiliary, target, moves)
        # Переміщуємо n-й диск з source до target
        moves.append((source, target))
        # Переміщуємо n-1 дисків з auxiliary до target, використовуючи source як допоміжну
        hanoi(n-1, auxiliary, target, source, moves)

def print_hanoi_moves(n):
    """
    Функція для друку кроків переміщення дисків.
    
    n: Кількість дисків
    """
    moves = []
    hanoi(n, 'A', 'C', 'B', moves)
    for move in moves:
        print(f"Перемістити диск з {move[0]} на {move[1]}")

if __name__ == "__main__":
    n = int(input("Введіть кількість дисків: "))
    print_hanoi_moves(n)
