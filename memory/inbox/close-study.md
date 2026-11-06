# Close study (auto)

Rounds with ticks: 271; rounds with a real settled result: 201

## 1. How fast BTC moves per second (Coinbase, USD)

- 215152 one-second changes: average size $3.12, typical (std) $6.70, 90th percentile $9.82, 99th $27.15, 99.9th $51.52, biggest $146.20.
- So in 60 s BTC typically wanders about $52 (std), and in 10 s about $21; the sqrt-of-time rule is what the z formula below uses.

## 2. Does Kalshi close rounds early?

- Recorder status rows since 20:13: 5034; rows where can_close_early was true: 5034.
- Rounds whose reported close_time CHANGED during the round: 0 of 8. Rounds seen with a non-active status more than 3 s before the 15:00 close: 7 [('KXBTC15M-26NOV052045-45', 'finalized', 866), ('KXBTC15M-26NOV052100-00', 'finalized', 855), ('KXBTC15M-26NOV052115-15', 'finalized', 862), ('KXBTC15M-26NOV052130-30', 'finalized', 857), ('KXBTC15M-26NOV052145-45', 'finalized', 861)]

## 3. When does the favourite stop being buyable below 99c?

- Last second with an ask under 99c, seconds before the close: median 90, 10th percentile 30, 90th percentile 233 (271 rounds). After that moment there is nothing to buy below 99c.

## 4. Our own z-rule: first moment the model's side is z standard deviations from the target

| z | rounds | median s before close | median ask | share with an ask under 99c | median $ buyable | win rate | profit per $ (ask under 99c only) |
|---|---|---|---|---|---|---|---|
| 2.0 | 262 | 278 | 0.940 | 82% | $8757 | 90.8% | +0.9% (216 bets) |
| 2.5 | 254 | 187 | 0.963 | 61% | $4892 | 94.1% | +1.0% (156 bets) |
| 3.0 | 252 | 135 | 0.972 | 46% | $0 | 95.2% | +1.9% (116 bets) |
| 3.5 | 246 | 122 | 0.975 | 39% | $0 | 95.5% | +1.4% (96 bets) |
| 4.0 | 242 | 89 | 0.981 | 32% | $0 | 96.7% | +2.3% (78 bets) |

Win = real settled result when known, otherwise the average of the last 60 Coinbase prices vs the target (stand-in for Kalshi's average).
