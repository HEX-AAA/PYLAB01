import time
import math

CSI = "\x1b["
ZERO = f"{CSI}0G"  # Курсор в начало строки
RESET = f"{CSI}0m"

WHITE_BG = f"{CSI}47m"
BLUE_BG = f"{CSI}44m"

def draw_horizontal_wave_flag(frame_time):
    height = 9
    base_width = 25
    
    # Делаем фиксированный красивый отступ от левого края терминала
    print(" " * 5, end="")
    
    for y in range(height):
        is_middle_line = (3 <= y <= 5)
        line = ""
        
        for x in range(base_width):
            # МАГИЯ ГОРИЗОНТАЛЬНОЙ ВОЛНЫ:
            # Синусоида зависит от горизонтальной координаты 'x' и времени 'frame_time'.
            # Это создает эффект, будто волна бежит слева направо вдоль флага.
            wave = math.sin(x * 0.4 - frame_time * 2)
            
            # Базовые границы синего креста (вертикальная полоса)
            blue_start = 7
            blue_end = 10
            
            # Под воздействием волны границы синего креста немного смещаются вбок
            if wave > 0:
                blue_start += 1
                blue_end += 1
            elif wave < -0.5:
                blue_start -= 1
                blue_end -= 1
                
            # Отрисовка пикселей флага
            if (blue_start <= x <= blue_end) or is_middle_line:
                line += f"{BLUE_BG} {RESET}"
            else:
                line += f"{WHITE_BG} {RESET}"
                
        # Выводим готовую строку флага
        print(line)
        # Для всех строк, кроме последней, добавляем отступ слева наперед
        if y < height - 1:
            print(" " * 5, end="")

def animate_flag():
    t = 0.0
    height = 9  # Высота флага в строках
    
    try:
        while True:
            # 1. Рисуем флаг с горизонтальной волной
            draw_horizontal_wave_flag(t)
            
            # 2. Возвращаем курсор на 9 строк вверх, чтобы не плодить флаги вниз
            print(f"{CSI}{height}A{ZERO}", end="", flush=True)
            
            # Скорость анимации
            t += 0.15
            time.sleep(0.08)
            
    except KeyboardInterrupt:
        # Отступаем вниз, чтобы текст остановки не затер флаг
        print("\n" * height)
        print("Анимация флага остановлена.")

# Запуск флага с горизонтальным развиванием
animate_flag()
