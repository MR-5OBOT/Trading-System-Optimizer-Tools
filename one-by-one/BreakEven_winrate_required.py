# 2. Minimum Required Win Rate (WR)
# Formula to calculate the minimum win rate needed for a given risk-reward ratio (RR):
# Minimum Win % = Risk ÷ (Risk + Reward) x 100
# Formula: WR = 1 / (1 + RR)
# Example: If RR = 1.5, then WR = 1 / (1 + 1.5) = 0.40 (40% win rate required to break even).
import sys

def main():
    risk_reward = input("Enter you RR : (E.x 2, 3, 1.5)  ")
    # errors cheking
    try:
        # Try converting input string to int
        risk_reward = float(risk_reward)
    except ValueError:
        print("Invalid Entry Please type a valid RR Value!")
        sys.exit()
    # formula
    formula = 1 / (1 + risk_reward) * 100 # convert float to int
    # RR required
    print(f"BreakEven Winrate Required from 1:{int(risk_reward)}RR is: {formula:.0f}%")

main()
    
# always remomber input() return a string by default

