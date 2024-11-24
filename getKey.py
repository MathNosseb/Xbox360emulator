import pygame
import sys
import vgamepad as vg
import time

# Create a virtual Xbox One gamepad object
gamepad = vg.VX360Gamepad()  # VX360 is compatible with newer Xbox controllers

# Initialize Pygame
pygame.init()

# Set up the joystick
pygame.joystick.init()

# Check if there are any joysticks
if pygame.joystick.get_count() < 1:
    print("No joystick detected.")
    sys.exit()

# Create a joystick object
joystick = pygame.joystick.Joystick(0)
joystick.init()

print(f"Joystick Name: {joystick.get_name()}")

left_joystick_x = 0.0
left_joystick_y = 0.0
right_joystick_x = 0.0
right_joystick_y = 0.0

try:
    while True:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.JOYBUTTONDOWN:
                print(f"Button {event.button} pressed.")
                
                #coté droit
                if event.button == 0:
                    gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
                    gamepad.update()
                if event.button == 1:
                    gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
                    gamepad.update()
                if event.button == 2:
                    gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
                    gamepad.update()
                if event.button == 3:
                    gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
                    gamepad.update()
                
                #coté gauche (fleche)
                if event.button == 11:
                    print("arow up")
                    gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)
                    gamepad.update()
                if event.button == 14:
                    print("arrow right")
                    gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)
                    gamepad.update()
                if event.button == 12:
                    print("arrow down")
                    gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
                    gamepad.update()
                if event.button == 13:
                    print("arrow left")
                    gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)
                    gamepad.update()
                    
                #boutons action
                if event.button == 9:
                    print("l")
                    gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)
                    gamepad.update()
                if event.button == 10:
                    print("r")
                    gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)
                    gamepad.update()
                if event.button == 11:
                    print("joystick L")
                    gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB)
                    gamepad.update()
                if event.button == 10:
                    print("joystick R")
                    gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB)
                    gamepad.update()
                
            if event.type == pygame.JOYBUTTONUP:
                print(f"Button {event.button} released.")
                
                #coté droit
                if event.button == 0:
                    gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
                    gamepad.update()
                if event.button == 1:
                    gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
                    gamepad.update()
                if event.button == 2:
                    gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
                    gamepad.update()
                if event.button == 3:
                    gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
                    gamepad.update()
                
                #coté gauche(flèche)
                if event.button == 11:
                    print("arow up")
                    gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)
                    gamepad.update()
                if event.button == 14:
                    print("arrow right")
                    gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)
                    gamepad.update()
                if event.button == 12:
                    print("arrow down")
                    gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
                    gamepad.update()
                if event.button == 13:
                    print("arrow left")
                    gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)
                    gamepad.update()
                    
                #boutons action
                if event.button == 9:
                    print("l")
                    gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)
                    gamepad.update()
                if event.button == 10:
                    print("r")
                    gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)
                    gamepad.update()
                if event.button == 11:
                    print("joystick L")
                    gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB)
                    gamepad.update()
                if event.button == 10:
                    print("joystick R")
                    gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB)
                    gamepad.update() 
                
            if event.type == pygame.JOYAXISMOTION:
                #print(f"Axis {event.axis} moved to {event.value}")
                
                #JOYSTICK GAUCHE
                if event.axis == 0:
                    left_joystick_x = event.value
                    
                if event.axis == 1:
                    left_joystick_y = event.value
                
                if left_joystick_x > 1:
                    left_joystick_x = 1
                if left_joystick_x < -1:
                    left_joystick_x = -1
                if left_joystick_y > 1:
                    left_joystick_y = 1
                if left_joystick_y < -1:
                    left_joystick_y = -1
                print(f"JOSTICK GAUCHE   {left_joystick_x}   {left_joystick_y}")
                gamepad.left_joystick_float(x_value_float = left_joystick_x, y_value_float = -left_joystick_y)
                gamepad.update()
                
                #JOYSTICK DROIT
                if event.axis == 2:
                    right_joystick_x = event.value
                    
                if event.axis == 3:
                    right_joystick_y = event.value
                
                if right_joystick_x > 1:
                    right_joystick_x = 1
                if right_joystick_x < -1:
                    right_joystick_x = -1
                if right_joystick_y > 1:
                    right_joystick_y = 1
                if right_joystick_y < -1:
                    right_joystick_y = -1
                print(f"JOSTICK DROIT  {right_joystick_x}   {right_joystick_y}")
                gamepad.right_joystick_float(x_value_float = right_joystick_x, y_value_float = -right_joystick_y)
                gamepad.update()
                
                #GACHETTES
                # ZL (4) - Trigger gauche
                if event.axis == 4:
                    gamepad.left_trigger_float(value_float=event.value)
                    gamepad.update()
                    if event.value > 0.2:  # Si ZL est pressé
                        print("ZL pressé")
                    elif event.value < 0.2:  # Si ZL est relâché
                        print("ZL relâché")

                # ZR (5) - Trigger droit
                if event.axis == 5:
                    gamepad.right_trigger_float(value_float=event.value)
                    gamepad.update()
                    if event.value > 0.2:  # Si ZR est pressé
                        print("ZR pressé")
                    elif event.value < 0.2:  # Si ZR est relâché
                        print("ZR relâché")
                
                
                    
                

        # Delay to limit the loop speed
        pygame.time.delay(100)

except KeyboardInterrupt:
    print("Exiting...")
    pygame.quit()
    sys.exit()