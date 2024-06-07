# Задание 1
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


num1 = 24
num2 = 36
print("Наибольший общий делитель чисел", num1, "и", num2, ":", gcd(num1, num2))
# задание 2
import random


def generate_number():
    return str(random.randint(1000, 9999))


def check_guess(secret_num, guess, attempts):
    cows = 0
    bulls = 0
    for i in range(4):
        if guess[i] == secret_num[i]:
            bulls += 1
        elif guess[i] in secret_num:
            cows += 1
    if bulls == 4:
        print("Поздравляю, вы угадали число! Количество попыток:", attempts)
    else:
        print("Быки:", bulls, "Коровы:", cows)
        new_guess = input("Введите следующее четырехзначное число: ")
        check_guess(secret_num, new_guess, attempts+1)


def main():
    secret_number = generate_number()
    print("Добро пожаловать в игру 'Быки и коровы'! Попробуйте угадать четырехзначное число.")
    user_guess = input("Введите четырехзначное число: ")
    check_guess(secret_number, user_guess, 1)


main()

# Задние 3


def is_safe(board, x, y, moves):
    # Проверяем, не превышает ли количество ходов максимальное значение
    if len(moves) > 35:
        return False

    # Проверяем, не была ли уже посещена текущая клетка
    if board[y][x] == 1:
        return False

    # Помечаем клетку как посещенную
    board[y][x] = 1

    # Возвращаем True, если клетка безопасна
    return True


def solve(board, x, y, moves):
    # Если все клетки посещены, возвращаем True
    if len(moves) == 36:
        return True

    # Перебираем все возможные ходы коня
    for i in range(2, 5):
        nx = x + i
        ny = y + i

        if 0 <= nx < 6 and 0 <= ny < 6:
            if is_safe(board, nx, ny, moves):
                if solve(board, nx, ny, moves):
                    return True

        nx = x + i
        ny = y - i

        if 0 <= nx < 6 and 0 <= ny < 6:
            if is_safe(board, nx, ny, moves):
                if solve(board, nx, ny, moves):
                    return True

        nx = x - i
        ny = y - i

        if 0 <= nx < 6 and 0 <= ny < 6:
            if is_safe(board, nx, ny, moves):
                if solve(board, nx, ny, moves):
                    return True

        nx = x - i
        ny = y + i

        if 0 <= nx < 6 and 0 <= ny < 6:
            if is_safe(board, nx, ny, moves):
                if solve(board, nx, ny, moves):
                    return True

    # Если ни один из ходов не приводит к решению, возвращаем False
    return False


# Инициализируем пустую доску
board = [[0 for _ in range(6)] for _ in range(6)]

# Начинаем поиск с первой клетки
solve(board, 0, 0, [])

# Выводим путь коня
for i in range(6):
    print(board[i])


# Задание 4
import random


def print_board(board):
    for row in board:
        print(" ".join(str(cell) for cell in row))


def find_blank(board):
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                return i, j


def is_solvable(board):
    inversions = 0
    nums = [num for row in board for num in row if num != 0]
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] > nums[j]:
                inversions += 1
    blank_row, _ = find_blank(board)
    if blank_row % 2 == 0 and inversions % 2 == 0:
        return True
    elif blank_row % 2 != 0 and inversions % 2 != 0:
        return True
    else:
        return False


def shuffle_board():
    board = [[j + 4 * i for j in range(1, 5)] for i in range(4)]
    random.shuffle(board)
    while not is_solvable(board):
        random.shuffle(board)
    return board


def move(board, direction):
    row, col = find_blank(board)
    if direction == 'up' and row > 0:
        board[row][col], board[row - 1][col] = board[row - 1][col], board[row][col]
    elif direction == 'down' and row < 3:
        board[row][col], board[row + 1][col] = board[row + 1][col], board[row][col]
    elif direction == 'left' and col > 0:
        board[row][col], board[row][col - 1] = board[row][col - 1], board[row][col]
    elif direction == 'right' and col < 3:
        board[row][col], board[row][col + 1] = board[row][col + 1], board[row][col]


def check_win(board):
    return all(board[i][j] == i * 4 + j + 1 for i in range(4) for j in range(4))


def main():
    board = shuffle_board()

    print("Welcome to the Game of Fifteen!")

    while True:
        print_board(board)

        if check_win(board):
            print("Congratulations! You've solved the puzzle.")
            break

        direction = input("Enter direction (up, down, left, right) to move the blank space: ")

        move(board, direction)


if __name__ == "__main__":
    main()

