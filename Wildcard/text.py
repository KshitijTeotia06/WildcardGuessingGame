import pygame
import time
pygame.init()
start_ticks = pygame.time.get_ticks()
turn = 0
#Textbox stuff
validChars = "`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./"
shiftChars = '~!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:"ZXCVBNM<>?'
shiftDown = False
class TextBox(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.text = ""
    self.font = pygame.font.Font(None, 50)
    self.image = self.font.render("Enter your text here", False, [216, 216, 205])
    self.rect = self.image.get_rect()

  def add_chr(self, char):
    global shiftDown
    if char in validChars and not shiftDown:
        self.text += char
    elif char in validChars and shiftDown:
        self.text += shiftChars[validChars.index(char)]
    self.update()

  def update(self):
    old_rect_pos = self.rect.center
    self.image = self.font.render(self.text, False, [0, 0, 0])
    self.rect = self.image.get_rect()
    self.rect.center = old_rect_pos


white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
black = (0, 0, 0)
X = 800
Y = 600
display_surface = pygame.display.set_mode((X, Y))
pygame.display.set_caption('Wildcard')
font = pygame.font.Font('freesansbold.ttf', 32)

hintLabel = font.render('Hint', True, black, white)
hintLabelRect = hintLabel.get_rect()
hintLabelRect.center = (40, 40)

cardLabel = font.render('card name: ', True, black, white)
cardLabelRect = cardLabel.get_rect()
cardLabelRect.center = (100, 500)

textBox = TextBox()
textBox.rect.center = [500, 500]

hintImage = pygame.image.load('lightbulb.png')
car = pygame.image.load('car.jpg')
showHint = False

carHint = font.render('Vroom Vroom', True, black, white)
carHintRect = carHint.get_rect()
carHintRect.center = (350, 70)

cat = pygame.image.load('cat.jpg')

catHint = font.render('Meow Meow', True, black, white)
catHintRect = catHint.get_rect()
catHintRect.center = (350, 70)

fern = pygame.image.load('fern.jpg')

fernHint = font.render('Starts with f', True, black, white)
fernHintRect = fernHint.get_rect()
fernHintRect.center = (350, 70)

tree = pygame.image.load('tree.jpg')

treeHint = font.render('Starts with t', True, black, white)
treeHintRect = treeHint.get_rect()
treeHintRect.center = (350, 70)

peach = pygame.image.load('peach.jpg')

peachHint = font.render('juciy', True, black, white)
peachHintRect = peachHint.get_rect()
peachHintRect.center = (350, 70)

playstation = pygame.image.load('playstation.jpg')

playstationHint = font.render('sony', True, black, white)
playstationHintRect = playstationHint.get_rect()
playstationHintRect.center = (350, 70)

minecraft = pygame.image.load('minecraft.jpg')

minecraftHint = font.render('made by notch', True, black, white)
minecraftHintRect = minecraftHint.get_rect()
minecraftHintRect.center = (350, 70)

pi = pygame.image.load('pi.jpg')

piHint = font.render('circles', True, black, white)
piHintRect = piHint.get_rect()
piHintRect.center = (350, 70)

rolex = pygame.image.load('rolex.jpg')

rolexHint = font.render('expensive + watch', True, black, white)
rolexHintRect = rolexHint.get_rect()
rolexHintRect.center = (350, 70)

answers = ["car", "cat", "fern", "tree", "peach", "playstation", "minecraft", "pi", "rolex"]
hintsText = [carHint, catHint, fernHint, treeHint, peachHint, playstationHint, minecraftHint, piHint, rolexHint]
hintsRect = [carHintRect, catHintRect, fernHintRect, treeHintRect, peachHintRect, playstationHintRect,
             minecraftHintRect, piHintRect, rolexHintRect]
images = [car, cat, fern, tree, peach, playstation, minecraft, pi, rolex]


while turn < answers.__len__():
    if showHint:
        display_surface.blit(hintsText[turn], hintsRect[turn])
        pygame.display.update()
        display_surface.blit(hintsText[turn], hintsRect[turn])
    display_surface.fill(white)
    display_surface.blit(hintLabel, hintLabelRect)
    display_surface.blit(cardLabel, cardLabelRect)
    display_surface.blit(hintImage, (80, 0))
    display_surface.blit(images[turn], (400, 300))
    display_surface.blit(textBox.image, textBox.rect)
    time = ((pygame.time.get_ticks()-start_ticks) / 1000) % 1000
    if time >= 15:
        turn = turn + 1
        start_ticks = pygame.time.get_ticks()
    timeLabel = font.render(str(15-time), True, black, white)
    timeRect = timeLabel.get_rect()
    timeRect.center = (700, 40)
    display_surface.blit(timeLabel, timeRect)
    pygame.display.update()
    for e in pygame.event.get():
        time = ((pygame.time.get_ticks() - start_ticks) / 1000) % 1000
        if time >= 15:
            turn = turn + 1
            start_ticks = pygame.time.get_ticks()
        timeLabel = font.render(str(15-time), True, black, white)
        timeRect = timeLabel.get_rect()
        timeRect.center = (700, 40)
        display_surface.blit(timeLabel, timeRect)
        if e.type == pygame.QUIT:
            pygame.quit()
            quit()
        if e.type == pygame.KEYDOWN:
            textBox.add_chr(pygame.key.name(e.key))
            if e.key == pygame.K_SPACE:
                textBox.text += " "
                textBox.update()
            if e.key in [pygame.K_RSHIFT, pygame.K_LSHIFT]:
                shiftDown = True
            if e.key == pygame.K_BACKSPACE:
                textBox.text = textBox.text[:-1]
                textBox.update()
            if e.key == pygame.K_RETURN:
                if len(textBox.text) > 0:
                    print(textBox.text)
                    if textBox.text == answers[turn]:
                        turn = turn + 1
                        showHint = False
                        start_ticks = pygame.time.get_ticks()
        if e.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = e.pos  # gets mouse position

            # checks if mouse position is over the button

            if hintLabelRect.collidepoint(mouse_pos):
                # prints current location of mouse
                print('button was pressed at {0}'.format(mouse_pos))
                showHint = True
        pygame.display.update()
