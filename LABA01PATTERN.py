import time

CSI = "\x1b["
RESET = f"{CSI}0m"

# Цвета
W = f"{CSI}47m"   # Белый фон
B = f"{CSI}44m"   # Синий фон

# 1. Готовые кусочки флага (каждый строго своей длины)
L_white = f"{W}{' ' * 5}{B}{' ' * 3}{RESET}"   # Длина: 8 символов
L_blue  = f"{B}{' ' * 8}{RESET}"               # Длина: 8 символов

R_white = f"{W}{' ' * 17}{RESET}"              # Длина: 17 символов
R_blue  = f"{B}{' ' * 17}{RESET}"               # Длина: 17 символов

# Пустые заглушки, чтобы выравнивать строки до одной длины (29 символов)
EMPTY_21 = " " * 21
EMPTY_29 = " " * 29
S = "    " # Сдвиг вправо на 4 пробела

# === КАДР 1: Ровный флаг ===
frame1 = [
    L_white + R_white + "    ",
    L_white + R_white + "    ",
    L_white + R_white + "    ",
    L_blue  + R_blue  + "    ",
    L_blue  + R_blue  + "    ",
    L_blue  + R_blue  + "    ",
    L_white + R_white + "    ",
    L_white + R_white + "    ",
    L_white + R_white + "    ",
    EMPTY_29,
    EMPTY_29,
    EMPTY_29,
    EMPTY_29
]

# === КАДР 2: Флаг со сдвигом на 4 вниз и на 4 вправо ===
frame2 = [
    L_white + EMPTY_21,
    L_white + EMPTY_21,
    L_white + EMPTY_21,
    L_blue  + EMPTY_21,
    L_blue  + S + R_white,
    L_blue  + S + R_white,
    L_white + S + R_white,
    L_white + S + R_blue,
    L_white + S + R_blue,
    L_white + S + R_blue,
    S + R_white + "    ",
    S + R_white + "    ",
    S + R_white + "    "
]

def animate():
    try:
        while True:
            # Шаг 1: Гарантированно очищаем экран прокруткой
            print("\n" * 50)
            
            # Шаг 2: Печатаем Кадр 1
            for line in frame1:
                print(line)
            time.sleep(0.5)
            
            # Шаг 3: Гарантированно очищаем экран прокруткой
            print("\n" * 50)
            
            # Шаг 4: Печатаем Кадр 2
            for line in frame2:
                print(line)
            time.sleep(0.5)
            
    except KeyboardInterrupt:
        print("\nАнимация остановлена.")

animate()
