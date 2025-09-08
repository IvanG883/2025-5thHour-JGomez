import pygame
import random
import sys

# Initialize Pygame
pygame.init()
WIDTH, HEIGHT = 600, 400
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Slot Machine")
FONT = pygame.font.SysFont('arial', 32)
BIG_FONT = pygame.font.SysFont('arial', 48)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GOLD = (255, 215, 0)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
GRAY = (200, 200, 200)

# Game Variables
symbols = ['🍒', '🍋', '🔔', '⭐', '💎']
reels = ["", "", ""]
balance = 100
bet = 10
message = "Press SPIN!"
spinning = False

# Button class
class Button:
    def __init__(self, x, y, w, h, text, callback):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.callback = callback

    def draw(self):
        pygame.draw.rect(SCREEN, GOLD, self.rect)
        pygame.draw.rect(SCREEN, BLACK, self.rect, 2)
        label = FONT.render(self.text, True, BLACK)
        SCREEN.blit(label, (self.rect.x + 15, self.rect.y + 10))

    def click(self, pos):
        if self.rect.collidepoint(pos):
            self.callback()

# Functions
def spin():
    global reels, balance, bet, message

    if balance < bet:
        message = "Not enough balance!"
        return

    # Deduct bet
    balance -= bet

    # Spin reels
    reels[:] = [random.choice(symbols) for _ in range(3)]

    # Evaluate result
    if reels[0] == reels[1] == reels[2]:
        winnings = bet * 10
        message = f"JACKPOT! You win ${winnings}!"
    elif reels[0] == reels[1] or reels[1] == reels[2] or reels[0] == reels[2]:
        winnings = bet * 3
        message = f"You matched 2! Win ${winnings}"
    else:
        winnings = 0
        message = "Try again!"

    balance += winnings

def increase_bet():
    global bet
    if bet < 50:
        bet += 5

def decrease_bet():
    global bet
    if bet > 5:
        bet -= 5

# Buttons
buttons = [
    Button(250, 300, 100, 50, "SPIN", spin),
    Button(100, 300, 50, 50, "-", decrease_bet),
    Button(160, 300, 50, 50, "+", increase_bet),
]

# Symbol colors for colored rectangles
symbol_colors = {
    '🍒': (220, 20, 60),   # Cherry red
    '🍋': (255, 255, 102), # Lemon yellow
    '🔔': (255, 215, 0),   # Bell gold
    '⭐': (255, 255, 255), # Star white
    '💎': (135, 206, 235), # Diamond blue
}

# Game loop
clock = pygame.time.Clock()
running = True
while running:
    SCREEN.fill(GREEN)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for b in buttons:
                b.click(event.pos)

    # Display reels with colored rectangles and symbols
    for i, symbol in enumerate(reels):
        x = 100 + i * 130
        y = 140
        color = symbol_colors.get(symbol, (255, 255, 255))
        pygame.draw.rect(SCREEN, color, (x, y, 100, 100))
        pygame.draw.rect(SCREEN, BLACK, (x, y, 100, 100), 3)

        label = BIG_FONT.render(symbol or "❔", True, BLACK)
        label_rect = label.get_rect(center=(x + 50, y + 50))
        SCREEN.blit(label, label_rect)

    # Labels
    balance_text = FONT.render(f"Balance: ${balance}", True, WHITE)
    bet_text = FONT.render(f"Bet: ${bet}", True, WHITE)
    msg_text = FONT.render(message, True, WHITE)
    SCREEN.blit(balance_text, (20, 20))
    SCREEN.blit(bet_text, (20, 60))
    SCREEN.blit(msg_text, (20, 100))

    # Draw buttons
    for b in buttons:
        b.draw()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
