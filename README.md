# Trading-System-Optimizer-Tools
Basic Trading Tool to help improving youre Trading System.

1. BreakEven_RR_Required
> Formula to calculate the RR needed to break even given a win rate (WR):
``` 
RR = (1 - WR) / WR
```

2. BreakEven_WinRate_Required
> Formula to calculate the minimum win rate needed for a given risk-reward ratio (RR):
```
Minimum Win % = Risk ÷ (Risk + Reward) x 100
```

3. Max DrawDown Calculator
> Explanation: This formula calculates the maximum observed loss from a peak to a trough during a specific period.
```
Formula: MDD = (Peak Value - Trough Value) / Peak Value
```

4. Risk of Ruin probability ROR
> Explanation: This formula estimates the probability of losing the entire capital after a certain number of trades.
```
RoR = [(1 - WR) / (1 + WR)] ^ Number of Trades
```

5. Expected Profitability EP
> Explanation: This formula calculates the expected profitability per trade.
```
#    Formula: EP = (WR * Average Win) - (LR * Average Loss)
```

