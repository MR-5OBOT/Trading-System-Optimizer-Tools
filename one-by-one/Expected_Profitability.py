# Expected Profitability (EP) or Expectancy:
#    Formula: EP = (WR * Average Win) - (LR * Average Loss)
#    Where:
#    - WR = Win Rate
#    - LR = Loss Rate (1 - WR)
#    Explanation: This formula calculates the expected profitability per trade.
#    Example: If the win rate is 40%, average win is $100, average loss is $50, the EP is: 
#    EP = (0.4 * 100) - (0.6 * 50) = 40 - 30 = $10.


def main():
    print()
    print("Explanation: This formula calculates the expected profitability per trade.")
    print()
    # user inputs & strip %/ $ symbols
    winrate = input("Enter your WR: (ex: 40%) ").strip("%")
    # print(winrate) # for debuging
    averege_win = input("Enter your averege win: ").strip("$")
    averege_loss = input("Enter your averege loss: ").strip("$")


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

main()



