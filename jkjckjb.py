import time
CSI = "\x1b["
ZERO = f"{CSI}0G"
ERASE = f"{CSI}2K"
RESET = f"{CSI}0m"

#def draw_progress(num_tasks, width):
#        for task in range(num_tasks):
#                 for filled in range(width):
#                        bar = f"{'#'*filled}{'-'*(width - filled)}"
#                        print(f"{ZERO}{ERASE}{task}:{bar}")                
def draw_line(offset, filled, color):
    offset_part =f"{ERASE}{' '*offset}"
    filled_part =f"{CSI}48;5;{color}m{' '*filled}{RESET}"
    line = f"{offset_part}{filled_part}"
    print(line)
    
def draw_romb(width, color):
    center = width // 2
    offset = center
    STEP = 1
    filled = STEP

    for line in range(width):
        draw_line(offset, filled, color)
        if line < center:
            offset -= 1
            filled += 2*STEP
        else:
            offset += STEP
            filled -= 2*STEP 

def animate():
    colors = range(40,200)
    while True:
        for color in colors:
            draw_romb(7, color)
            print(f"{CSI}{7}A{ZERO}", end="", flush = True)
            time.sleep(0.1)
animate()