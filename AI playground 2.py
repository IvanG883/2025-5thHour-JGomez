import random
import time

# Config
STARTING_BALANCE = 100
MIN_BET = 20
MAX_BET = 100_000

# Slot Symbols and their multipliers
symbols = {
    '🍒': 2,
    '🍋': 3,
    '🔔': 5,
    '💎': 10,
    '7️⃣': 25,
}

symbol_list = list(symbols.keys())

def spin_reels():
    return [random.choice(symbol_list) for _ in range(3)]

def calculate_payout(reels, bet):
    if reels.count(reels[0]) == 3:
        # 3 matching symbols
        symbol = reels[0]
        multiplier = symbols[symbol] * 10
        return bet * multiplier, f"🎉 JACKPOT! 3x {symbol} | Multiplier: {multiplier}x"
    elif reels[0] == reels[1] or reels[1] == reels[2] or reels[0] == reels[2]:
        # 2 matching symbols
        match = reels[0] if reels[0] == reels[1] or reels[0] == reels[2] else reels[1]
        multiplier = symbols[match]
        return bet * multiplier, f"✅ Nice! 2x {match} | Multiplier: {multiplier}x"
    else:
        return 0, "❌ No match. You lost."

def get_bet(balance):
    while True:
        try:
            bet = int(input(f"💰 Enter your bet (${MIN_BET}–${MAX_BET}): "))
            if bet < MIN_BET:
                print(f"❌ Minimum bet is ${MIN_BET}.")
            elif bet > MAX_BET:
                print(f"❌ Maximum bet is ${MAX_BET}.")
            elif bet > balance:
                print("❌ You don't have enough balance.")
            else:
                return bet
        except ValueError:
            print("❌ Please enter a valid number.")

def print_reels(reels):
    print("\n🎰 Spinning reels...")
    time.sleep(1)
    print(" | ".join(reels))
    print()

def slot_machine():
    balance = STARTING_BALANCE
    print("🎰 Welcome to Python Slot Machine!")
    print(f"💵 Starting balance: ${balance}\n")

    while balance >= MIN_BET:
        print(f"Current balance: ${balance}")
        bet = get_bet(balance)

        reels = spin_reels()
        print_reels(reels)

        winnings, result_msg = calculate_payout(reels, bet)
        print(result_msg)

        if winnings > 0:
            print(f"🎊 You won ${winnings}!")
            balance += winnings
        else:
            balance -= bet
            print(f"💸 You lost ${bet}.")

        if balance < MIN_BET:
            print("\n🛑 Not enough balance to continue. Game over!")
            break

        again = input("🎲 Spin again? (y/n): ").strip().lower()
        if again != 'y':
            break

    print(f"\n🏁 Final balance: ${balance}")
    print("Thanks for playing!")

if __name__ == "__main__":
    slot_machine()
