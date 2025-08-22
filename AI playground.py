import pygame
import random
import sys

# Initialize Pygame
pygame.init()
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Blackjack")
FONT = pygame.font.SysFont('arial', 24)
BIG_FONT = pygame.font.SysFont('arial', 36)

# Colors
GREEN = (34, 139, 34)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GOLD = (218, 165, 32)
RED = (220, 20, 60)

# Game Variables
suits = ['♠', '♥', '♦', '♣']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
balance = 100
MAX_BET = 100_000
MIN_BET = 20

# Button class
class Button:
    def __init__(self, x, y, w, h, text, callback):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.callback = callback

    def draw(self):
        pygame.draw.rect(SCREEN, GOLD, self.rect)
        label = FONT.render(self.text, True, BLACK)
        SCREEN.blit(label, (self.rect.x + 10, self.rect.y + 10))

    def click(self, pos):
        if self.rect.collidepoint(pos):
            self.callback()

# Game Classes
def create_deck():
    deck = [(rank, suit) for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck

def card_value(card):
    rank, _ = card
    if rank in ['J', 'Q', 'K']:
        return 10
    elif rank == 'A':
        return 11
    return int(rank)

def hand_value(hand):
    value = sum(card_value(c) for c in hand)
    aces = sum(1 for c in hand if c[0] == 'A')
    while value > 21 and aces:
        value -= 10
        aces -= 1
    return value

def draw_hand(hand, x, y, hide_first=False):
    for i, card in enumerate(hand):
        if hide_first and i == 0:
            draw_card("?", "?", x + i * 70, y)
        else:
            draw_card(card[0], card[1], x + i * 70, y)

def draw_card(rank, suit, x, y):
    pygame.draw.rect(SCREEN, WHITE, (x, y, 60, 90))
    pygame.draw.rect(SCREEN, BLACK, (x, y, 60, 90), 2)
    label = FONT.render(f'{rank}{suit}', True, BLACK)
    SCREEN.blit(label, (x + 5, y + 5))

# Game Logic Variables
deck = []
player_hand = []
dealer_hand = []
message = ""
bet = 0
game_over = False
player_turn = False

# Functions
def reset_game():
    global deck, player_hand, dealer_hand, message, bet, player_turn, game_over
    deck = create_deck()
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]
    message = "Your move"
    player_turn = True
    game_over = False

def place_bet():
    global bet, balance, message
    if balance >= MIN_BET:
        bet = MIN_BET
        balance -= bet
        reset_game()
    else:
        message = "Not enough balance to bet!"

def hit():
    global player_hand, message, player_turn, game_over
    if player_turn:
        player_hand.append(deck.pop())
        if hand_value(player_hand) > 21:
            message = "Bust! You lose."
            player_turn = False
            end_round()

def stand():
    global player_turn
    if player_turn:
        player_turn = False
        dealer_play()

def dealer_play():
    global dealer_hand, message
    while hand_value(dealer_hand) < 17:
        dealer_hand.append(deck.pop())
    end_round()

def end_round():
    global balance, message, game_over
    player_total = hand_value(player_hand)
    dealer_total = hand_value(dealer_hand)

    if player_total > 21:
        message = "You busted! Dealer wins."
    elif dealer_total > 21 or player_total > dealer_total:
        message = "You win!"
        balance += bet * 2
    elif player_total < dealer_total:
        message = "Dealer wins!"
    else:
        message = "Push. Bet returned."
        balance += bet
    game_over = True

# Buttons
buttons = [
    Button(50, 500, 100, 40, "Hit", hit),
    Button(160, 500, 100, 40, "Stand", stand),
    Button(270, 500, 150, 40, "Place Bet", place_bet),
]

# Main Loop
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

    # Draw cards
    draw_hand(dealer_hand, 50, 50, hide_first=player_turn)
    draw_hand(player_hand, 50, 200)

    # Labels
    SCREEN.blit(BIG_FONT.render("Dealer", True, WHITE), (50, 20))
    SCREEN.blit(BIG_FONT.render("Player", True, WHITE), (50, 170))
    SCREEN.blit(FONT.render(f"Balance: ${balance:,}", True, WHITE), (600, 20))
    SCREEN.blit(FONT.render(f"Bet: ${bet:,}", True, WHITE), (600, 50))
    SCREEN.blit(FONT.render(message, True, WHITE), (50, 400))

    # Draw buttons
    for b in buttons:
        b.draw()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
