# Maximum Drawdown (MDD):
# Formula: MDD = (Peak Value - Trough Value) / Peak Value
# Explanation: This formula calculates the maximum observed loss from a peak to a trough during a specific period.
# Example: If the portfolio value dropped from $10,000 to $7,000, MDD = (10000 - 7000) / 10000 = 30%.


def maximumDD():
    peak_value = input("Enter your Peak value (peak of the profits): ").strip("$")
    trough_value = input("Enter your trough value (trough of the losses): ").strip("$")
    pv = int(peak_value)
    tv = int(trough_value)

    def formula():
        maxDD = (pv - tv) / pv
        maxDD = (maxDD * 100) # convert float to int to make it 50% 20% ...
        print(f"your Maximum Drawdown Value = {maxDD:.0f}%")
    formula()

maximumDD()
