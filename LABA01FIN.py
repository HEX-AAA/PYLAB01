CSI = "\x1b["
RESET = f"{CSI}0m" 

# Коды цветов фона
WHITE_BG = f"{CSI}47m" #47 - white color
BLUE_BG = f"{CSI}44m"   #44 - blue color

def draw_finland_flag():
    # proportions: left white = 5; Width of a blue cross = 3, right white 20
    
    #hight if top part is 3
    top_line = f"{WHITE_BG}{' ' * 5}{BLUE_BG}{' ' * 5}{WHITE_BG}{' ' * 20}{RESET}"
    
    # middle - 2 lines of blue
    # Sum length: 5 + 5 + 20 = 30
    middle_line = f"{BLUE_BG}{' ' * 30}{RESET}"
    
   #bottom === top
    print(top_line)
    print(top_line)
    print(top_line)
    
    
    print(middle_line)
    print(middle_line)
    
   
    print(top_line)
    print(top_line)
    print(top_line)


draw_finland_flag()
