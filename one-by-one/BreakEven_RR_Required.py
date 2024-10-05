
# Required Risk-Reward Ratio (RR)
# Formula to calculate the RR needed to break even given a win rate (WR):
# RR = (1 - WR) / WR
# Example: If WR = 0.40 (40% win rate), then RR = (1 - 0.40) / 0.40 = 1.5
# This means you'd need a 1.5:1 RR to break even with a 40% win rate.
import sys

def rr_required():
    winrate = input("your winrate is: (e.x: 40%)  ")
    clean = winrate.strip("%") # strip function to remove things from strings
    # errors cheking
    try:
        # try converting input string to int
        clean = int(clean)
    except ValueError:
        print("invalid entry please type a valid winrate value!")
        sys.exit()

    def formula():
        # convert int to percentage float
        wr = int(clean) / 100 
        # the formula to calculate min rr
        formula = (1 - wr) / wr
        print(f"breakeven r/r required from {winrate} is 1:{formula:.1f}rr")
    formula()

# always remomber input() return a string by default

