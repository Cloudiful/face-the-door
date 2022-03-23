import pygame.mouse
import data
import ui

buttons = []
pressed = -1


def draw_numpad():
    ui.clear_screen()
    numbers = []
    strs = []
    bS = 100  # button size
    lS = 10  # line thickness
    for i in range(-2, 2):
        for j in range(0, 3):

            num = (i + 2) * 3 + j + 1

            if num == 10:
                strs.append("确认")
            elif num == 11:
                strs.append("0")
            elif num == 12:
                strs.append("退格")
            else:
                strs.append(str(num))

            buttons.append(
                ui.Button(data.WIDTH // 2 + (bS + lS) * j + bS // 2 + 20, data.HEIGHT // 2 + bS * i + bS // 2))
            buttons[num - 1].draw()

            numbers.append(ui.Text(strs[num - 1],
                                   data.WIDTH // 2 + (bS + lS) * j + bS // 2 + 20,
                                   data.HEIGHT // 2 + bS * i + bS // 2,
                                   32))
            numbers[num - 1].draw()

            ui.draw_screen()

        ui.draw_screen()


def input_passwd():
    draw_numpad()
    password = ''
    while True:

        for event in pygame.event.get():
            # when mouse moved
            if event.type == pygame.MOUSEMOTION:
                pos = pygame.mouse.get_pos()
                for button in buttons:
                    # touch the button
                    if button.detected(pos):
                        inputNum = buttons.index(button) + 1
                        if inputNum == 10:
                            return password
                        elif inputNum == 11 and len(password) < 6:
                            password += "0"
                        elif inputNum == 12:

                            password = password[:-1]
                        else:
                            if len(password) < 6:
                                password += str(inputNum)

                        print(password)

        ui.Title("          ", 20, data.HEIGHT // 2, 80, 'midleft')
        ui.Title(password, 40, data.HEIGHT // 2, 64, 'midleft')
        ui.draw_screen()

        if len(password) == 6:
            ui.draw_screen()
            return password
