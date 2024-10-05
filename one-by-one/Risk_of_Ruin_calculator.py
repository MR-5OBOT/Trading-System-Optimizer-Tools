# Risk of Ruin (RoR):
#    Approximate Formula (simplified for fixed bet sizes): 
#    RoR = [(1 - WR) / (1 + WR)] ^ Number of Trades
#    Explanation: This formula estimates the probability of losing the entire capital after a certain number of trades.
#    Example: If WR is 60% and you make 100 trades, RoR ≈ [(1 - 0.6) / (1 + 0.6)] ^ 100.
import sys

def risk_of_ruin():
    use_input = input("Enter you Winrate: ").strip("%")
    nTrades = input("Enter you Total N of trades: ")

    winrate = use_input
    wr = float(winrate) / 100
    nt = int(nTrades)

    try:
        # Try converting input string to int
        wr = int(wr)
        nt = int(wr)
    except ValueError:
        print("Invalid Entry Please type a valid Value!")
        sys.exit()

    def formula():
        f = (1 - wr) / (1 + wr) * nt
        print(f"The RoR results is: {f:.0f} Trades")
    formula()

risk_of_ruin()
