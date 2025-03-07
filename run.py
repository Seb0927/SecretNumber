import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
background_image = pygame.image.load('./Numbers.png')
pygame.display.set_caption("Adivina el Número Secreto (entre 1 y 100)")

secret = random.randint(1, 100)
tries = 0

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up fonts
font = pygame.font.Font(None, 74)
small_font = pygame.font.Font(None, 36)

# Input box
input_box = pygame.Rect(300, 250, 200, 50)
color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
color = color_inactive
active = False
text = ''

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if input_box.collidepoint(event.pos):
                active = not active
            else:
                active = False
            # Change the current color of the input box.
            color = color_active if active else color_inactive
        if event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_RETURN:
                    # Check if the given value is a number
                    try:
                        int(text)
                    except ValueError:
                        label_rect = label.get_rect(center=(screen.get_width()/2, screen.get_height()/2 + 50))
                        screen.blit(label, label_rect)
                        pygame.display.flip()
                        pygame.time.wait(2000)  # Wait for 2 seconds to show the message
                        text = ''
                        continue

                    # Clues for the user
                    dif = abs(int(text) - secret)
                    if(abs(dif) > 1):
                        tries += 1
                        if(dif > 50):
                            label = small_font.render("¡Muy frío!", True, WHITE)
                        elif(dif > 35):
                            label = small_font.render("¡Frío!", True, WHITE)
                        elif(dif > 10):
                            label = small_font.render("¡Caliente!", True, WHITE)
                        elif(dif > 5):
                            label = small_font.render("¡Muy caliente!", True, WHITE)
                        else:
                            label = small_font.render("¡Hirviendo!", True, WHITE)
                        label_rect = label.get_rect(center=(screen.get_width()/2, screen.get_height()/2 + 50))
                        screen.blit(label, label_rect)
                        pygame.display.flip()
                        pygame.time.wait(2000)

                    # Check if the user guessed the secret number
                    if(int(text) == secret):
                        tries += 1
                        label = small_font.render("¡Felicidades! ¡Adivinaste el número secreto!", True, WHITE)
                        label_rect = label.get_rect(center=(screen.get_width()/2, screen.get_height()/2 + 50))
                        screen.blit(label, label_rect)
                        pygame.display.flip()
                        pygame.time.wait(2000)  # Wait for 2 seconds to show the message
                    text = ''

                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode

    screen.blit(background_image, (0, 0))

    # Render the current text.
    txt_surface = font.render(text, True, WHITE)
    # Resize the box if the text is too long.
    width = max(200, txt_surface.get_width()+10)
    input_box.w = width
    # Blit the text.
    screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
    # Blit the input_box rect.
    pygame.draw.rect(screen, color, input_box, 2)

    # Display instructions
    instructions = small_font.render("Adivina el número secreto (entre 1 y 100):", True, WHITE)
    screen.blit(instructions, (180, 200))

    tries_label = small_font.render("Intentos: " + str(tries), True, WHITE)
    screen.blit(tries_label, (330, 380))

    pygame.display.flip()

pygame.quit()
sys.exit()
