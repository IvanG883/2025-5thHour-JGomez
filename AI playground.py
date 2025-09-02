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
GRAY = (200, 200, 200)

# Game Variables
suits = ['♠', '♥', '♦', '♣']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
balance = 10_000
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
second_hand = []       # For split hand
dealer_hand = []
message = ""
bet = 0
game_over = False
player_turn = False
split_active = False   # Track if split is active
current_hand = 0       # 0 = first hand, 1 = second hand
double_down_active = False

# For calculator bar display
payout_multiplier = 0
payout_amount = 0

# Functions
def reset_game():
    global deck, player_hand, dealer_hand, message, bet, player_turn, game_over
    global payout_multiplier, payout_amount, split_active, second_hand, current_hand, double_down_active

    deck = create_deck()
    player_hand = [deck.pop(), deck.pop()]
    second_hand.clear()
    dealer_hand = [deck.pop(), deck.pop()]
    split_active = False
    double_down_active = False
    current_hand = 0
    player_turn = True
    game_over = False
    payout_multiplier = 0
    payout_amount = 0

    if hand_value(player_hand) == 21:
        message = "Blackjack! You win!"
        payout_multiplier = 2.5
        payout_amount = int(bet * payout_multiplier)
        global balance
        balance += payout_amount
        player_turn = False
        game_over = True
    else:
        message = "Your move"

def place_bet():
    global bet, balance, message
    if balance >= MIN_BET:
        bet = MIN_BET
        balance -= bet
        reset_game()
    else:
        message = "Not enough balance to bet!"

def hit():
    global player_hand, second_hand, message, player_turn, game_over, balance, payout_multiplier, payout_amount, current_hand, double_down_active

    if not player_turn:
        return

    hand = player_hand if current_hand == 0 else second_hand
    hand.append(deck.pop())
    total = hand_value(hand)

    if total == 21:
        message = "21! You win!"
        payout_multiplier = 2
        payout_amount = bet * payout_multiplier
        balance += payout_amount
        if split_active and current_hand == 0:
            current_hand = 1
            message = "Playing second hand"
        else:
            player_turn = False
            game_over = True

    elif total > 21:
        message = "Bust! You lose."
        if split_active and current_hand == 0:
            current_hand = 1
            message = "Playing second hand"
        else:
            player_turn = False
            game_over = True

    elif double_down_active:
        # If double down, after one card, end player's turn
        double_down_active = False
        if split_active and current_hand == 0:
            current_hand = 1
            message = "Playing second hand"
        else:
            player_turn = False
            dealer_play()

def stand():
    global player_turn, current_hand, message
    if player_turn:
        if split_active and current_hand == 0:
            current_hand = 1
            message = "Playing second hand"
        else:
            player_turn = False
            dealer_play()

def double_down():
    global bet, balance, message, double_down_active, player_turn
    if player_turn and balance >= bet:
        balance -= bet
        bet *= 2
        double_down_active = True
        hit()
        # After hit() in double down, player's turn may end automatically

def split_hand():
    global player_hand, second_hand, split_active, balance, bet, message, player_turn
    if len(player_hand) == 2 and player_hand[0][0] == player_hand[1][0] and balance >= bet and not split_active:
        split_active = True
        second_hand.append(player_hand.pop())
        second_hand.append(deck.pop())
        player_hand.append(deck.pop())
        balance -= bet
        message = "Playing first hand"
        player_turn = True
    else:
        message = "Can't split"

def dealer_play():
    global dealer_hand, message
    while hand_value(dealer_hand) < 17:
        dealer_hand.append(deck.pop())
    end_round()

def end_round():
    global balance, message, game_over, payout_multiplier, payout_amount, split_active, player_hand, second_hand, bet

    dealer_total = hand_value(dealer_hand)
    hands = [player_hand]
    bets = [bet]
    messages = []

    if split_active:
        hands.append(second_hand)
        bets.append(bet)

    for i, hand in enumerate(hands):
        player_total = hand_value(hand)
        current_bet = bets[i]

        if player_total > 21:
            result = f"Hand {i + 1}: Bust! Dealer wins."
        elif dealer_total > 21 or player_total > dealer_total:
            result = f"Hand {i + 1}: You win!"
            balance += current_bet * 2
        elif player_total < dealer_total:
            result = f"Hand {i + 1}: Dealer wins!"
        else:
            result = f"Hand {i + 1}: Push."
            balance += current_bet

        messages.append(result)

    message = " | ".join(messages)
    game_over = True

def draw_calculator_bar():
    bar_height = 50
    pygame.draw.rect(SCREEN, GRAY, (0, HEIGHT - bar_height, WIDTH, bar_height))
    if split_active and current_hand == 1:
        player_total = hand_value(second_hand)
    else:
        player_total = hand_value(player_hand)

    text = f"Hand Value: {player_total}   Bet: ${bet}"

    if payout_multiplier > 0:
        text += f"   Payout: Bet ${bet} x {payout_multiplier} = ${payout_amount}"

    label = FONT.render(text, True, BLACK)
    SCREEN.blit(label, (20, HEIGHT - bar_height + 15))

# Buttons
buttons = [
    Button(50, 500, 100, 40, "Hit", hit),
    Button(160, 500, 100, 40, "Stand", stand),
    Button(270, 500, 150, 40, "Place Bet", place_bet),
    Button(430, 500, 100, 40, "Double", double_down),
    Button(540, 500, 100, 40, "Split", split_hand),
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
    draw_hand(dealer_hand, 50, 50, hide_first=(player_turn and not game_over))
    draw_hand(player_hand, 50, 200)

    if split_active:
        draw_hand(second_hand, 50, 320)
        SCREEN.blit(BIG_FONT.render("Second Hand", True, WHITE), (50, 290))

    # Labels
    SCREEN.blit(BIG_FONT.render("Dealer", True, WHITE), (50, 20))
    SCREEN.blit(BIG_FONT.render("Player", True, WHITE), (50, 170))
    SCREEN.blit(FONT.render(f"Balance: ${balance:,}", True, WHITE), (600, 20))
    SCREEN.blit(FONT.render(f"Bet: ${bet:,}", True, WHITE), (600, 50))
    SCREEN.blit(FONT.render(message, True, WHITE), (50, 400))

    # Draw buttons
    for b in buttons:
        b.draw()

    # Draw calculator bar
    draw_calculator_bar()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
