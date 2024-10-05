# Tools fo risk management in trading

print("""
   ###############################################################
   #                                                             #
   #               MR5OBOT RISK MANAGEMENT TOOLS                 #
   #                                           Beta_version      #
   ###############################################################
""")

import sys

#_____________________________________________________________________________
# Required Risk-Reward Ratio (RR)
# Formula to calculate the RR needed to break even given a win rate (WR):
# RR = (1 - WR) / WR
# Example: If WR = 0.40 (40% win rate), then RR = (1 - 0.40) / 0.40 = 1.5
# This means you'd need a 1.5:1 RR to break even with a 40% win rate.

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
        print()
        print(f"breakeven RR required from {winrate} is 1:{formula:.1f}rr")
        print()
    formula()

# always remomber input() return a string by default


#--------------------------------------------------------------------------------

# 2. Minimum Required Win Rate (WR)
# Formula to calculate the minimum win rate needed for a given risk-reward ratio (RR):
# Minimum Win % = Risk ÷ (Risk + Reward) x 100
# Formula: WR = 1 / (1 + RR)
# Example: If RR = 1.5, then WR = 1 / (1 + 1.5) = 0.40 (40% win rate required to break even).

def winRate_required():
    risk_reward = input("Enter you RR : (E.x 2, 3, 1.5)  ")
    # errors cheking
    try:
        # Try converting input string to int
        risk_reward = float(risk_reward)
    except ValueError:
        print("Invalid Entry Please type a valid RR Value!")
        sys.exit()

    def formula():
        formula = 1 / (1 + risk_reward) * 100 # convert float to int
        #RR required
        print()
        print(f"BreakEven Winrate Required from 1:{int(risk_reward)}RR is: {formula:.0f}%")
        print()
    formula()
# always remomber input() return a string by default

#_____________________________________________________________________________

# Maximum Drawdown (MDD):
# Formula: MDD = (Peak Value - Trough Value) / Peak Value
# Explanation: This formula calculates the maximum observed loss from a peak to a trough during a specific period.
# Example: If the portfolio value dropped from $10,000 to $7,000, MDD = (10000 - 7000) / 10000 = 30%.

def maximumDD():
    peak_value = input("Enter your Peak value (peak of the profits): ").strip("$")
    trough_value = input("Enter your trough value (trough of the losses): ").strip("$")
    pv = int(peak_value)
    tv = int(trough_value)
    try:
        # Try converting input string to int
        pv = int(peak_value)
        tv = int(trough_value)
    except ValueError:
        print("Invalid Entry Please type a valid Value!")
        sys.exit()

    def formula():
        maxDD = (pv - tv) / pv
        maxDD = (maxDD * 100) # convert float to int to make it 50% 20% ...
        print(f"your Maximum Drawdown Value = {maxDD:.0f}%")
    formula()

#--------------------------------------------------------------------------------

# Risk of Ruin (RoR):
#    Approximate Formula (simplified for fixed bet sizes): 
#    RoR = [(1 - WR) / (1 + WR)] ^ Number of Trades
#    Explanation: This formula estimates the probability of losing the entire capital after a certain number of trades.
#    Example: If WR is 60% and you make 100 trades, RoR ≈ [(1 - 0.6) / (1 + 0.6)] ^ 100.

def risk_of_ruin():
    winrate = input("Enter you Winrate: ").strip("%")
    nTrades = input("Enter you Total N of trades: ")

    wr = float(winrate) / 100
    # print(winrate)
    nt = int(nTrades)

    try:
        # Try converting input string to int
        wr = float(wr)
        nt = int(nt)
    except ValueError:
        print("Invalid Entry Please type a valid Value!")
        sys.exit()

    def formula():
        f = (1 - wr) / (1 + wr) * nt
        print(f"The RoR results is: {f:.2f} Trades")
    formula()


#--------------------------------------------------------------------------------

# Expected Profitability (EP) or Expectancy:
#    Formula: EP = (WR * Average Win) - (LR * Average Loss)
#    Where:
#    - WR = Win Rate
#    - LR = Loss Rate (1 - WR)
#    Explanation: This formula calculates the expected profitability per trade.
#    Example: If the win rate is 40%, average win is $100, average loss is $50, the EP is: 
#    EP = (0.4 * 100) - (0.6 * 50) = 40 - 30 = $10.

def expercted_Profitability():
    print()
    print("Explanation: This formula calculates the expected profitability per trade.")
    print()
    # user inputs & strip %/ $ symbols
    winrate = input("Enter your WR: (ex: 40%) ").strip("%")
    # print(winrate) # for debuging
    averege_win = input("Enter your averege win: ").strip("$")
    averege_loss = input("Enter your averege loss: ").strip("$")

    try:
        # Try converting input string to int
        winrate = int(winrate)
        averege_loss = int(averege_loss)
        averege_win = int(averege_win)
    except ValueError:
        print("Invalid Entry Please type a valid Value!")
        sys.exit()

    def formula():
        # convert str to number
        wr = float(winrate) / 100  # dividing by 100 to get a percentage
        aw = float(averege_win)
        lr = (1 - wr)
        al = float(averege_loss)
        # calculation
        ep = (wr * aw) - (lr * al)
        ep = float(ep) # make sure to have correct value
        print(f"the expected profitability per trade is: {ep}$")
    formula()

#--------------------------------------------------------------------------------

def tools_list():
    print("List of a basic trading tool to help improving you Trading System:")
    print("""
    1. BreakEven_RR_Required
    2. BreakEven_WinRate_Required
    3. Max DrawDown Calculator
    4. Risk of Ruin probability ROR
    5. Expected Profitability EP
    """)
tools_list()

def choosing_items():
    
    user_input = int(input("Choose your tool by typing its number: "))
    if user_input == 1:
        rr_required()
    elif user_input == 2:
        winRate_required()
    elif user_input == 3:
        maximumDD()
    elif user_input == 4:
        risk_of_ruin()
    elif user_input == 5:
        expercted_Profitability()
    else:
        sys.exit()
    
# End .

















