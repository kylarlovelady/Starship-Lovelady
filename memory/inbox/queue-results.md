 | -0.01 | +0.15 | +0.24 | +0.31 | +0.42 | +0.42 |
| funding rate | -0.02 | -0.01 | -0.03 | -0.02 | -0.01 | +0.11 |

## C. Simple edge rule: model chance Phi(z) vs the Kalshi ask, buy the side with the bigger gap if gap > threshold (after fee), hold to the result

| left | min gap | bets | win rate | profit per $ staked | avg cost |
|---|---|---|---|---|---|
| 600s | 0.05 | 69 | 41% | +1.5% | 0.40 |
| 600s | 0.10 | 31 | 42% | +25.6% | 0.33 |
| 600s | 0.20 | 4 | 50% | +27.0% | 0.39 |
| 420s | 0.05 | 89 | 29% | +5.1% | 0.28 |
| 420s | 0.10 | 44 | 23% | +26.3% | 0.18 |
| 420s | 0.20 | 3 | 0% | -100.0% | 0.09 |
| 300s | 0.05 | 77 | 25% | -4.3% | 0.26 |
| 300s | 0.10 | 36 | 19% | -4.6% | 0.20 |
| 300s | 0.20 | 2 | 50% | +411.5% | 0.10 |
| 180s | 0.05 | 63 | 29% | +1.9% | 0.28 |
| 180s | 0.10 | 32 | 31% | +30.1% | 0.24 |
| 180s | 0.20 | 1 | 100% | +490.3% | 0.17 |
| 90s | 0.05 | 66 | 17% | -11.6% | 0.19 |
| 90s | 0.10 | 35 | 11% | -23.3% | 0.15 |
| 90s | 0.20 | 6 | 0% | -100.0% | 0.09 |
| 45s | 0.05 | 35 | 23% | +42.0% | 0.16 |
| 45s | 0.10 | 33 | 24% | +52.9% | 0.16 |
| 45s | 0.20 | 21 | 14% | +4.1% | 0.14 |

## How much to trust this

- 307 rounds, many signals x checkpoints: a few will look good by luck. Only a signal that stays on the same side in both halves, at several checkpoints, deserves a real test.
- Hindsight always finds a great trade. The test that matters is walk-forward: pick the rule on older rounds, test it on newer ones, after fees.
- Practice only. Nothing here changes any setting.
(exit 0)
```

## 2026-11-06 03:17:44 tasks/queue/072-oracle-check.sh
```
-rw-rw-r-- 1 kylarlovelady kylarlovelady 5459 Nov  6 03:16 /home/kylarlovelady/starship/memory/inbox/oracle-study.md
-rw-rw-r-- 1 kylarlovelady kylarlovelady 5459 Nov  6 03:16 /tmp/oracle-study.out
366M	/home/kylarlovelady/market-data
agent_trades.json
alerts.log
archive
calendar.json
calls.jsonl
coach_rules.json
config.json
entry_stats.json
env
exit_rules.json
exits.jsonl
hindsight.jsonl
history
innovations.jsonl
island.json
kalshi_key.pem
kalshi_raw.json
kalshi_sync.log
lab.log
lab_log.jsonl
# Hindsight / oracle study (last 7 days)

Rounds with a full recording, a strike and a real Kalshi result: **307** (149 UP, 158 DOWN).

## A. The perfect-hindsight buy (cheapest ask of the side that won, with 3+ s left)

| statistic | value |
|---|---|
| rounds with a usable book | 307 |
| median cheapest winning ask | 39c |
| average perfect-hindsight profit per contract | 61.1c (157% on cost) |
| share of rounds where the perfect buy was 30c or less | 33% |
| share where it was 50c or less | 78% |
| WHEN in the round the cheapest winning ask was (seconds left) | 0-60 s: 2%, 60-180 s: 5%, 180-420 s: 15%, >420 s: 76% |

Reading: the perfect buy is nearly always a *cheap* winner early in the round that you could not have known about. The rest of this report asks which signals could have pointed to it in advance.

## B. Which signals predict UP/DOWN? (AUC: 0.50 = coin flip, 1.00 = perfect, below 0.50 = points the other way)

Each cell: AUC all rounds (older half / newer half). **Bold** = 0.60 or more (or 0.40 or less) AND the same side of 0.50 in both halves. 'vs market' = rank correlation of the signal with (result minus Kalshi mid), i.e. does it know something the price does not. Roughly +-0.13 is noise at this sample size.

| signal | 600s left | 420s left | 300s left | 180s left | 90s left | 45s left |
|---|---|---|---|---|---|---|
| z (btc vs strike, in sigmas) | **0.77 (0.73 / 0.82)** | **0.85 (0.80 / 0.89)** | **0.89 (0.85 / 0.91)** | **0.93 (0.91 / 0.94)** | **0.98 (0.99 / 0.98)** | **1.00 (1.00 / 0.99)** |
| dist $ (btc - strike) | **0.78 (0.74 / 0.82)** | **0.86 (0.81 / 0.91)** | **0.90 (0.87 / 0.91)** | **0.93 (0.92 / 0.93)** | **0.98 (0.99 / 0.97)** | **0.99 (1.00 / 0.99)** |
| mom 10s $ | 0.57 (0.55 / 0.58) | 0.51 (0.52 / 0.50) | 0.49 (0.50 / 0.48) | 0.52 (0.54 / 0.49) | 0.52 (0.49 / 0.54) | 0.53 (0.55 / 0.52) |
| mom 30s $ | **0.61 (0.62 / 0.61)** | 0.58 (0.61 / 0.56) | 0.54 (0.53 / 0.55) | 0.57 (0.66 / 0.46) | 0.58 (0.57 / 0.60) | 0.56 (0.54 / 0.58) |
| mom 60s $ | 0.58 (0.55 / 0.60) | **0.65 (0.65 / 0.65)** | 0.56 (0.58 / 0.55) | 0.56 (0.65 / 0.47) | **0.62 (0.62 / 0.60)** | **0.63 (0.61 / 0.65)** |
| kraken - coinbase $ | 0.48 (0.52 / 0.44) | 0.49 (0.48 / 0.52) | 0.52 (0.53 / 0.51) | 0.43 (0.32 / 0.55) | 0.42 (0.44 / 0.40) | 0.51 (0.48 / 0.55) |
| trade flow imbalance | 0.50 (0.49 / 0.51) | 0.48 (0.43 / 0.53) | 0.50 (0.51 / 0.51) | 0.53 (0.52 / 0.55) | 0.57 (0.58 / 0.56) | 0.55 (0.59 / 0.52) |
| coinbase book imbalance | 0.51 (0.69 / 0.41) | 0.47 (0.61 / 0.42) | 0.45 (0.55 / 0.39) | 0.50 (0.54 / 0.51) | 0.53 (0.64 / 0.48) | 0.49 (0.47 / 0.49) |
| kalshi book imbalance | 0.48 (0.48 / 0.47) | 0.59 (0.57 / 0.61) | 0.45 (0.51 / 0.41) | **0.33 (0.29 / 0.37)** | **0.33 (0.35 / 0.30)** | **0.24 (0.31 / 0.19)** |
| kalshi mid (crowd) | **0.78 (0.72 / 0.83)** | **0.86 (0.80 / 0.91)** | **0.90 (0.87 / 0.92)** | **0.93 (0.91 / 0.94)** | **0.97 (0.98 / 0.96)** | **0.97 (1.00 / 0.93)** |
| funding rate | 0.50 (0.50 / 0.50) | 0.50 (0.50 / 0.50) | 0.50 (0.50 / 0.50) | 0.50 (0.50 / 0.50) | 0.50 (0.50 / 0.50) | 0.50 (0.50 / 0.50) |

### Does it beat the market price? (rank correlation with result minus Kalshi mid)

| signal | 600s left | 420s left | 300s left | 180s left | 90s left | 45s left |
|---|---|---|---|---|---|---|
| z (btc vs strike, in sigmas) | -0.00 | +0.16 | +0.24 | +0.32 | +0.45 | +0.45 |
| dist $ (btc - strike) | +0.01 | +0.18 | +0.26 | +0.31 | +0.44 | +0.43 |
| mom 10s $ | +0.08 | -0.05 | -0.08 | -0.01 | +0.03 | +0.09 |
| mom 30s $ | +0.02 | +0.04 | +0.03 | +0.03 | +0.09 | +0.07 |
| mom 60s $ | -0.06 | +0.15 | +0.01 | -0.06 | +0.09 | +0.13 |
| kraken - coinbase $ | +0.02 | +0.05 | +0.05 | -0.09 | -0.18 | +0.10 |
| trade flow imbalance | +0.03 | -0.04 | -0.01 | +0.08 | +0.15 | +0.21 |
| coinbase book imbalance | -0.00 | -0.01 | -0.05 | -0.00 | +0.06 | -0.07 |
| kalshi book imbalance | +0.04 | +0.14 | -0.00 | -0.04 | -0.06 | -0.14 |
| kalshi mid (crowd) | -0.01 | +0.15 | +0.24 | +0.31 | +0.42 | +0.42 |
| funding rate | -0.02 | -0.01 | -0.03 | -0.02 | -0.01 | +0.11 |

## C. Simple edge rule: model chance Phi(z) vs the Kalshi ask, buy the side with the bigger gap if gap > threshold (after fee), hold to the result

| left | min gap | bets | win rate | profit per $ staked | avg cost |
|---|---|---|---|---|---|
| 600s | 0.05 | 69 | 41% | +1.5% | 0.40 |
| 600s | 0.10 | 31 | 42% | +25.6% | 0.33 |
| 600s | 0.20 | 4 | 50% | +27.0% | 0.39 |
| 420s | 0.05 | 89 | 29% | +5.1% | 0.28 |
| 420s | 0.10 | 44 | 23% | +26.3(exit 0)
```

## 2026-11-06 03:17:44 tasks/queue/073-oracle-light.sh
```
               total        used        free      shared  buff/cache   available
Mem:            8058        2589        2228          64        3391        5469
Mem:            8058        2489        2327          63        3392        5569
# Hindsight / oracle study (last 3 days)

Rounds with a full recording, a strike and a real Kalshi result: **300** (147 UP, 153 DOWN).

## A. The perfect-hindsight buy (cheapest ask of the side that won, with 3+ s left)

| statistic | value |
|---|---|
| rounds with a usable book | 300 |
| median cheapest winning ask | 39c |
| average perfect-hindsight profit per contract | 61.0c (157% on cost) |
| share of rounds where the perfect buy was 30c or less | 32% |
| share where it was 50c or less | 78% |
| WHEN in the round the cheapest winning ask was (seconds left) | 0-60 s: 2%, 60-180 s: 5%, 180-420 s: 15%, >420 s: 77% |

Reading: the perfect buy is nearly always a *cheap* winner early in the round that you could not have known about. The rest of this report asks which signals could have pointed to it in advance.

## B. Which signals predict UP/DOWN? (AUC: 0.50 = coin flip, 1.00 = perfect, below 0.50 = points the other way)

Each cell: AUC all rounds (older half / newer half). **Bold** = 0.60 or more (or 0.40 or less) AND the same side of 0.50 in both halves. 'vs market' = rank correlation of the signal with (result minus Kalshi mid), i.e. does it know something the price does not. Roughly +-0.13 is noise at this sample size.

| signal | 600s left | 420s left | 300s left | 180s left | 90s left | 45s left |
|---|---|---|---|---|---|---|
| z (btc vs strike, in sigmas) | **0.78 (0.74 / 0.83)** | **0.85 (0.80 / 0.89)** | **0.90 (0.87 / 0.91)** | **0.93 (0.92 / 0.93)** | **0.98 (0.99 / 0.98)** | **0.99 (1.00 / 0.99)** |
| dist $ (btc - strike) | **0.78 (0.75 / 0.82)** | **0.86 (0.81 / 0.91)** | **0.90 (0.89 / 0.91)** | **0.93 (0.93 / 0.93)** | **0.98 (0.99 / 0.97)** | **0.99 (1.00 / 0.99)** |
| mom 10s $ | 0.57 (0.55 / 0.59) | 0.50 (0.50 / 0.50) | 0.49 (0.51 / 0.48) | 0.52 (0.53 / 0.50) | 0.52 (0.49 / 0.55) | 0.52 (0.51 / 0.53) |
| mom 30s $ | **0.62 (0.63 / 0.61)** | 0.58 (0.60 / 0.57) | 0.54 (0.55 / 0.54) | 0.56 (0.64 / 0.47) | 0.59 (0.57 / 0.61) | 0.56 (0.52 / 0.59) |
| mom 60s $ | 0.58 (0.56 / 0.60) | **0.66 (0.66 / 0.66)** | 0.57 (0.59 / 0.55) | 0.55 (0.63 / 0.47) | **0.62 (0.60 / 0.62)** | **0.62 (0.59 / 0.66)** |
| kraken - coinbase $ | 0.48 (0.53 / 0.44) | 0.50 (0.50 / 0.51) | 0.53 (0.54 / 0.52) | 0.44 (0.36 / 0.53) | 0.42 (0.44 / 0.38) | 0.52 (0.52 / 0.52) |
| trade flow imbalance | 0.50 (0.48 / 0.52) | 0.48 (0.41 / 0.54) | 0.51 (0.52 / 0.51) | 0.54 (0.55 / 0.54) | 0.58 (0.60 / 0.57) | 0.54 (0.56 / 0.53) |
| coinbase book imbalance | 0.51 (0.65 / 0.43) | 0.47 (0.60 / 0.42) | 0.45 (0.51 / 0.40) | 0.50 (0.52 / 0.51) | 0.53 (0.60 / 0.49) | 0.49 (0.47 / 0.49) |
| kalshi book imbalance | 0.47 (0.46 / 0.48) | 0.59 (0.58 / 0.61) | 0.46 (0.51 / 0.42) | **0.33 (0.27 / 0.38)** | **0.32 (0.34 / 0.30)** | **0.24 (0.29 / 0.20)** |
| kalshi mid (crowd) | **0.79 (0.73 / 0.84)** | **0.86 (0.80 / 0.91)** | **0.90 (0.88 / 0.92)** | **0.93 (0.92 / 0.93)** | **0.97 (0.98 / 0.96)** | **0.97 (1.00 / 0.93)** |
| funding rate | 0.50 (0.50 / 0.50) | 0.50 (0.50 / 0.50) | 0.50 (0.50 / 0.50) | 0.50 (0.50 / 0.50) | 0.50 (0.50 / 0.50) | 0.50 (0.50 / 0.50) |

### Does it beat the market price? (rank correlation with result minus Kalshi mid)

| signal | 600s left | 420s left | 300s left | 180s left | 90s left | 45s left |
|---|---|---|---|---|---|---|
| z (btc vs strike, in sigmas) | +0.01 | +0.16 | +0.26 | +0.33 | +0.44 | +0.45 |
| dist $ (btc - strike) | +0.01 | +0.18 | +0.27 | +0.32 | +0.44 | +0.43 |
| mom 10s $ | +0.08 | -0.07 | -0.08 | +0.01 | +0.04 | +0.09 |
| mom 30s $ | +0.03 | +0.04 | +0.03 | +0.01 | +0.10 | +0.07 |
| mom 60s $ | -0.06 | +0.15 | +0.03 | -0.07 | +0.10 | +0.14 |
| kraken - coinbase $ | +0.01 | +0.06 | +0.06 | -0.08 | -0.19 | +0.09 |
| trade flow imbalance | +0.03 | -0.05 | +0.01 | +0.09 | +0.17 | +0.20 |
| coinbase book imbalance | -0.00 | -0.01 | -0.05 | -0.00 | +0.06 | -0.07 |
| kalshi book imbalance | +0.03 | +0.14 | +0.01 | -0.04 | -0.06 | -0.13 |
| kalshi mid (crowd) | +0.00 | +0.15 | +0.26 | +0.32 | +0.41 | +0.42 |
| funding rate | -0.02 | -0.01 | -0.03 | -0.02 | -0.01 | +0.11 |

## C. Simple edge rule: model chance Phi(z) vs the Kalshi ask, buy the side with the bigger gap if gap > threshold (after fee), hold to the result

| left | min gap | bets | win rate | profit per $ staked | avg cost |
|---|---|---|---|---|---|
| 600s | 0.05 | 68 | 40% | +0.8% | 0.39 |
| 600s | 0.10 | 31 | 42% | +25.6% | 0.33 |
| 600s | 0.20 | 4 | 50% | +27.0% | 0.39 |
| 420s | 0.05 | 89 | 29% | +5.1% | 0.28 |
| 420s | 0.10 | 44 | 23% | +26.3% | 0.18 |
| 420s | 0.20 | 3 | 0% | -100.0% | 0.09 |
| 300s | 0.05 | 75 | 24% | -1.4% | 0.24 |
| 300s | 0.10 | 35 | 17% | -9.7% | 0.19 |
| 300s | 0.20 | 2 | 50% | +411.5% | 0.10 |
| 180s | 0.05 | 61 | 28% | +2.4% | 0.27 |
| 180s | 0.10 | 31 | 32% | +32.3% | 0.24 |
| 180s | 0.20 | 1 | 100% | +490.3% (exit 0)
```

## 2026-11-06 13:01:02 tasks/queue/074-send-cover-a.sh
```
(exit 0)
```

## 2026-11-06 13:52:02 tasks/queue/075-pihole-check.sh
```
== container
pihole Up 11 hours (healthy) 
== pi address
192.168.1.107 100.105.140.126 172.17.0.1 fd7a:115c:a1e0::2f4c:8c7f 
== normal lookup via pihole
tasks/queue/075-pihole-check.sh: line 6: dig: command not found
== ad domain via pihole (blocked answers 0.0.0.0 or ::)
tasks/queue/075-pihole-check.sh: line 7: dig: command not found
== same ad domain via 1.1.1.1 (real address)
tasks/queue/075-pihole-check.sh: line 8: dig: command not found
== pihole version
Core version is v6.5 (Latest: v6.5)
Web version is v6.6.1 (Latest: v6.6.1)
FTL version is v6.8 (Latest: v6.8)
== pihole status
  [✓] FTL is listening on port 53
     [✓] UDP (IPv4)
     [✓] TCP (IPv4)
     [✓] UDP (IPv6)
     [✓] TCP (IPv6)
== what the Pi itself uses for DNS

nameserver 100.100.100.100
nameserver fd7a:115c:a1e0::53
(exit 0)
```

## 2026-11-06 14:04:02 tasks/queue/076-kalshi-series-probe.sh
```
crypto series: 294
  KXCRYPTOLEAD15M | Coin Race 15 minutes | fifteen_min
  KXDOGE15M | DOGE 15 min | fifteen_min
  KXBTC15M | BTC 15 min | fifteen_min
  KXBNB15M | BNB 15 min | fifteen_min
  KXZEC15M | Zcash 15min | fifteen_min
  KXETH15M | ETH 15 min | fifteen_min
  KXADA15M | Cardano 15 Minute | fifteen_min
  KXBCH15M | Bitcoin Cash 15 Minute | fifteen_min
  KXTON15M | TON 15m | fifteen_min
  KXCRYPTOCOMP15M | Crypto Comparison 15 minute | fifteen_min
  KXXRP15M | XRP 15 min | fifteen_min
  KXHYPE15M | HYPE 15 min | fifteen_min
  KXSOL15M | SOL 15 min | fifteen_min
  KXNEAR15M | NEAR 15m | fifteen_min
KXBTC15M KXBTC15M-26NOV061515-15 close 2026-11-06T20:15:00Z strike 75760.07 yes 0.7500 0.7600 vol 967396.49 oi None
KXETH15M KXETH15M-26NOV061515-15 close 2026-11-06T20:15:00Z strike 2232 yes 0.4900 0.5000 vol 16503.71 oi None
KXSOL15M KXSOL15M-26NOV061515-15 close 2026-11-06T20:15:00Z strike 90.0337 yes 0.7200 0.7400 vol 25736.54 oi None
KXXRP15M KXXRP15M-26NOV061515-15 close 2026-11-06T20:15:00Z strike 1.1845 yes 0.3800 0.3900 vol 15625.78 oi None
KXDOGE15M KXDOGE15M-26NOV061515-15 close 2026-11-06T20:15:00Z strike 0.072809 yes 0.6600 0.6700 vol 5688.57 oi None
KXBTCD KXBTCD-26NOV0616-T89299.99 close 2026-11-06T21:00:00Z strike 89299.99 yes 0.0000 0.0100 vol 0.00 oi None
KXBTCD KXBTCD-26NOV0616-T89199.99 close 2026-11-06T21:00:00Z strike 89199.99 yes 0.0000 0.0100 vol 0.00 oi None
KXETHD KXETHD-26NOV0616-T3144.99 close 2026-11-06T21:00:00Z strike 3144.99 yes 0.0000 0.0100 vol 0.00 oi None
KXETHD KXETHD-26NOV0616-T3139.99 close 2026-11-06T21:00:00Z strike 3139.99 yes 0.0000 0.0100 vol 0.00 oi None
KXBTC KXBTC-26NOV0616-T89299.99 close 2026-11-06T21:00:00Z strike 89299.99 yes 0.0000 0.0100 vol 0.00 oi None
KXBTC KXBTC-26NOV0616-T70700 close 2026-11-06T21:00:00Z strike 70700 yes 0.0000 0.0100 vol 0.00 oi None
KXETH KXETH-26NOV0616-T3144.99 close 2026-11-06T21:00:00Z strike 3144.99 yes 0.0000 0.0100 vol 0.00 oi None
KXETH KXETH-26NOV0616-T1655 close 2026-11-06T21:00:00Z strike 1655 yes 0.0000 0.0100 vol 0.00 oi None
(exit 0)
```

## 2026-11-06 14:07:01 tasks/queue/077-experiment-state.sh
```
== run.json
{'active': True, 'live': None, 'strategy': 'v_snipe', 'start': 1000.0, 'id': 1793935799, 'halted': None}
== sniper switch file
ls: cannot access '/home/kylarlovelady/market-data/sniper.on': No such file or directory
== review 12h
TRADE REVIEW, last 12 hours: 2136 (strategy, round) results from 42 rounds with full recordings.

EVERY STRATEGY (pretend money): rounds | profit | win%% | profit per $ staked
  v_x64216771     39    +167.36   38%   +9.5%
  v_x44219232     39    +167.36   38%   +9.5%
  v_x4227191      39    +167.36   38%   +9.5%
  v_x28219981     39    +154.33   36%   +8.7%
  v_x32221882     39    +154.33   36%   +8.7%
  v_flow_flip     41    +135.52   37%   +6.5%
  v_x68220541     39     +75.72   36%   +4.2%
  v_mood_flip     40     +74.56   40%   +4.3%
  trend           39     +51.31   28%   +5.3%
  hold            41     +50.79   59%  +11.7%
  v_x96220872     38     +30.03   37%   +3.3%
  v_x16217721     41     +29.69   29%   +1.7%
  v_x40223632     40     +10.40   45%   +2.8%
  v_x64216772     35      +5.15   46%   +1.9%
  v_x60222032     35      +5.15   46%   +1.9%
  v_x40223631     35      +5.15   46%   +1.9%
  v_x219212       39      +3.98   33%   +0.2%
  v_x96220861     36      -4.44   42%   -0.4%
  v_snipe         24     -11.03   79%   -7.4%
  run             24     -11.03   79%   -7.4%
  v_x12229262     35     -19.25   46%   -2.3%
  v_x36215122     25     -21.55   36%   -3.5%
  v_one_shot      33     -26.54   39%  -13.4%
  v_x60222031     34     -31.36   38%   -3.0%
  v_no_cut        34     -48.98   44%   -4.3%
  v_late          25     -54.40   32%   -8.1%
  v_x88221261     25     -54.40   32%   -8.1%
  flow            35     -59.72   31%  -10.5%
  v_x80218932     38     -60.76   39%  -16.8%
  v_x24220781     38     -60.76   39%  -16.8%
  v_x76218991     38     -60.76   39%  -16.8%
  v_x76218992     38     -60.76   39%  -16.8%
  v_x24220782     39     -79.50   31%   -5.0%
  v_x72222452     39     -86.56   31%   -5.5%
  v_x44219231     39     -86.56   31%   -5.5%
  v_x88221262     39     -86.56   31%   -5.5%
  v_x52220781     27     -98.53   30%  -14.0%
  v_x8220761      39    -109.77   31%   -6.5%
  v_x4227192      39    -118.76   28%   -7.3%
  v_x52220782     26    -120.69   27%  -18.5%
  v_hold          34    -123.94   41%  -16.7%
  v_x16217722     39    -138.46   23%  -16.5%
  v_x32221881     39    -154.10   31%   -7.3%
  v_x219211       36    -154.25   33%  -14.6%
  v_x72222451     36    -154.25   33%  -14.6%
  v_x80218931     36    -154.25   33%  -14.6%
  v_cut_loose     34    -162.93   29%  -16.7%
  v_cut_tight     32    -165.15    9%  -43.3%
  v_adds          34    -179.19   15%  -28.3%
  swing           41    -179.70   41%   -9.4%
  signals         34    -183.58   21%  -27.9%
  mood            34    -187.66   21%  -19.9%
(exit 0)
```

## 2026-11-06 14:10:01 tasks/queue/078-implied-vol-study.sh
```
# Kalshi pricing study (implied volatility, calibration, spreads), last 4 days

Rounds with a full recording and a strike: **479** (414 with a real result).

Settlement = average of the last 60 index prices vs the strike (CF Benchmarks), so inside the last minute part of the answer is already locked in. Sigma below is in dollars per square-root-second.

## A. Implied vs realized volatility (only seconds where the price is between 5c and 95c and BTC is at least $1 from the strike)

| seconds left | samples | median implied sigma | median realized sigma (trailing 60 s) | median ratio implied/realized |
|---|---|---|---|---|
| 600-840 | 7601 | 4.95 | 5.70 | 0.86 |
| 420-600 | 8152 | 4.85 | 6.18 | 0.80 |
| 300-420 | 4750 | 4.65 | 5.85 | 0.79 |
| 180-300 | 3815 | 4.45 | 5.63 | 0.78 |
| 90-180 | 1993 | 3.75 | 5.58 | 0.68 |
| 45-90 | 494 | 3.04 | 6.05 | 0.51 |
| 15-45 | 55 | 2.45 | 6.16 | 0.38 |

Ratio near 1.0 = the market prices with the volatility Bitcoin is actually showing. Above 1 = the market assumes MORE movement than recent (cheaper favourite). Below 1 = it assumes less movement (dearer favourite). A ratio that changes a lot with time left shows how makers adjust near the close.

## B. Calibration: price said p (YES mid), how often did YES win? (one sample per round per checkpoint)

| left | YES mid bucket | rounds | YES won | avg mid | gap (won - mid) | profit per $ buying the CHEAPER side at its ask | profit per $ buying the DEARER side at its ask |
|---|---|---|---|---|---|---|---|
| 420s | 0-20c | 79 | 13% | 10c | +2c | +13.8% | -3.7% |
| 420s | 20-40c | 64 | 34% | 29c | +5c | +11.5% | -10.1% |
| 420s | 40-60c | 48 | 38% | 49c | -12c | -21.4% | +10.1% |
| 420s | 60-80c | 53 | 66% | 72c | -6c | +14.1% | -10.8% |
| 420s | 80-100c | 69 | 83% | 89c | -7c | +47.3% | -8.3% |
| 300s | 0-20c | 98 | 14% | 8c | +6c | +57.4% | -7.3% |
| 300s | 20-40c | 49 | 27% | 28c | -2c | -11.6% | -0.4% |
| 300s | 40-60c | 43 | 51% | 51c | +0c | +4.7% | -11.5% |
| 300s | 60-80c | 33 | 58% | 70c | -12c | +31.9% | -19.7% |
| 300s | 80-100c | 88 | 93% | 92c | +1c | -21.0% | +0.5% |
| 180s | 0-20c | 113 | 12% | 5c | +6c | +111.4% | -8.8% |
| 180s | 20-40c | 29 | 34% | 31c | +4c | +5.4% | -8.0% |
| 180s | 40-60c | 31 | 32% | 48c | -16c | +16.1% | -21.1% |
| 180s | 60-80c | 39 | 64% | 70c | -6c | +12.2% | -10.8% |
| 180s | 80-100c | 99 | 95% | 94c | +1c | -22.8% | +0.7% |
| 90s | 0-20c | 126 | 4% | 5c | -1c | -21.2% | +0.4% |
| 90s | 20-40c | 22 | 32% | 28c | +3c | +5.1% | -7.3% |
| 90s | 40-60c | 13 | 85% | 50c | +34c | -34.6% | +20.6% |
| 90s | 60-80c | 17 | 88% | 71c | +18c | -62.4% | +21.6% |
| 90s | 80-100c | 88 | 99% | 96c | +3c | -72.5% | +4.2% |
| 45s | 0-20c | 94 | 4% | 2c | +2c | +105.1% | -8.3% |
| 45s | 20-40c | 9 | 56% | 30c | +26c | +73.5% | -38.3% |
| 45s | 80-100c | 72 | 99% | 97c | +2c | -53.5% | +2.4% |

## C. What the quotes cost (ask minus bid, in cents)

| seconds left | samples | median spread | 90th percentile |
|---|---|---|---|
| 600-840 | 7995 | 1.0c | 1.0c |
| 420-600 | 8753 | 1.0c | 1.0c |
| 300-420 | 5864 | 1.0c | 1.0c |
| 180-300 | 5793 | 1.0c | 1.0c |
| 90-180 | 3909 | 0.1c | 1.0c |
| 45-90 | 1297 | 0.1c | 1.0c |
| 15-45 | 284 | 0.1c | 1.0c |

| BTC distance from strike | samples | median spread |
|---|---|---|
| $0-25 | 6804 | 1.0c |
| $25-50 | 5708 | 1.0c |
| $50-75 | 4456 | 1.0c |
| $75-100 | 2863 | 1.0c |
| $100-125 | 1773 | 1.0c |
| $125-150 | 1094 | 1.0c |
| $150-175 | 590 | 1.0c |
| $175-200 | 349 | 1.0c |
| $200-225 | 695 | 1.0c |

## Reading this

- Practice only; nothing here changes a setting. About 300 rounds: gaps under a few cents per bucket are noise.
- Look for a bias that repeats across time-left checkpoints and price buckets, and then test it forward on new rounds.
(exit 0)
```

## 2026-11-06 14:10:41 tasks/queue/079-wallet-back-to-auto.sh
```
before: {'active': True, 'live': None, 'strategy': 'v_snipe', 'start': 1000.0}
after: {'active': True, 'live': None, 'strategy': 'auto', 'start': 1000.0} backup run.json.bak-1793995841
(exit 0)
```

## 2026-11-06 14:10:41 tasks/queue/080-maker-study2.sh
```
Traceback (most recent call last):
  File "/home/kylarlovelady/starship/markets/maker_study2.py", line 43, in <module>
    for l in f:
  File "<frozen codecs>", line 325, in decode
object address  : 0x7fff12bcd180
object refcount : 3
object type     : 0x9f3d78
object type name: MemoryError
object repr     : MemoryError()
lost sys.stderr
(exit 0)
```

## 2026-11-06 14:19:01 tasks/queue/081-maker-study2-light.sh
```
Mem:            8058        2626        2423          74        3168        5431
# Stricter maker study (fills need a real trade on the tape), last 3 days

Rounds with a full recording, a tape and a real result: **28**. Orders are 1 contract; post 1c above the best bid; wait 120 s; hold to the result.

| entry | possible orders | skipped (spread under 2c) | filled | fill rate | win rate (filled) | win rate (all posted) | avg maker price | maker profit/$ (1.75% fee) | maker profit/$ (0 fee) | taker profit/$ same orders | taker profit/$ filled only |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 60 s in | 0 | 56 | 0 | | | | | | | | |
| 120 s in | 0 | 56 | 0 | | | | | | | | |
| 180 s in | 0 | 56 | 0 | | | | | | | | |

## How to read it

- Fill rate: the share of resting orders a real seller actually hit. The first study assumed much higher.
- If the win rate of FILLED orders is lower than for ALL posted orders, we get filled mostly when we are wrong (adverse selection) and the maker saving is partly an illusion.
- 'taker profit/$ filled only' is the fair comparison: the same orders that filled, bought at the ask instead. Maker beats taker only if maker profit/$ is higher there.
- The 1.75% maker fee is from one article (dev.to) and should be confirmed with a real fill. Practice only; sample is a few hundred orders, so small differences are noise.
(exit 0)
```

## 2026-11-06 14:20:31 tasks/queue/082-longshot-test.sh
```
# Longshot hypothesis test (cheap side 3 to 7 minutes out), last 5 days

Rounds with a full recording and a real result: **450**.

| seconds left | price ceiling | bets | wins | avg price | profit per $ | 90% range (bootstrap) | older half | newer half | days positive |
|---|---|---|---|---|---|---|---|---|---|
| 420 | 10c | 81 | 5 | 6c | -4% | -63% to +72% | +82% (42) | -100% (39) | 1 of 5 |
| 420 | 15c | 114 | 7 | 8c | -27% | -69% to +20% | +35% (55) | -80% (59) | 1 of 5 |
| 420 | 20c | 157 | 18 | 11c | +3% | -31% to +43% | +42% (72) | -28% (85) | 1 of 5 |
| 300 | 10c | 108 | 6 | 6c | -3% | -62% to +60% | +97% (49) | -72% (59) | 1 of 5 |
| 300 | 15c | 135 | 12 | 7c | +25% | -27% to +83% | +91% (66) | -39% (69) | 4 of 5 |
| 300 | 20c | 173 | 17 | 10c | +2% | -35% to +40% | +41% (83) | -32% (90) | 3 of 5 |
| 240 | 10c | 103 | 2 | 6c | -65% | -100% to -26% | -62% (51) | -68% (52) | 1 of 5 |
| 240 | 15c | 128 | 6 | 7c | -34% | -77% to +11% | +15% (64) | -79% (64) | 3 of 5 |
| 240 | 20c | 157 | 14 | 9c | -4% | -40% to +36% | +33% (80) | -44% (77) | 3 of 5 |
| 180 | 10c | 91 | 6 | 6c | +13% | -60% to +86% | -17% (43) | +37% (48) | 2 of 5 |
| 180 | 15c | 111 | 9 | 7c | +13% | -42% to +78% | +30% (54) | -3% (57) | 3 of 5 |
| 180 | 20c | 140 | 15 | 9c | +13% | -30% to +63% | +31% (66) | -2% (74) | 3 of 5 |

## Per day for the 300 s / 15c rule (Central calendar days)

| day | bets | wins | profit per $ |
|---|---|---|---|
| 11-02 | 3 | 1 | +284% |
| 11-03 | 43 | 4 | +29% |
| 11-04 | 41 | 4 | +51% |
| 11-05 | 38 | 3 | +4% |
| 11-06 | 10 | 0 | -100% |

## Reading this

- Pays about 10 to 1 when it hits, so results swing hard: a few wins decide everything. Trust only a 90% range that stays above zero AND the same sign in both halves and on most days.
- Practice only; nothing changes in the agent. If it holds, the next step is a small forward test as its own practice strategy, small stakes.
(exit 0)
```

## 2026-11-06 15:16:01 tasks/queue/083-series-catalog.sh
```
started; progress so far:
(exit 0)
```

## 2026-11-06 15:37:02 tasks/queue/084-series-nightly-install.sh
```
installed: runs every night at 4:40 am
40 4 * * * flock -n /tmp/series_catalog.lock bash $HOME/starship/tasks/series_catalog_daily.sh >> $HOME/market-data/series_catalog.log 2>&1 # series-catalog
== BTC lag-1 check
rounds: 2936 span days: 31.0 UP share: 48.6%
all                    P(UP|prev UP)=47.6% (n=1424)  P(UP|prev DOWN)=49.4% (n=1506)  gap=-1.8 pts  +-1.8 (1 SE)  z=-1.0
older half             P(UP|prev UP)=49.5% (n=734)  P(UP|prev DOWN)=50.5% (n=731)  gap=-1.0 pts  +-2.6 (1 SE)  z=-0.4
newer half             P(UP|prev UP)=45.7% (n=690)  P(UP|prev DOWN)=48.4% (n=775)  gap=-2.7 pts  +-2.6 (1 SE)  z=-1.0
after UP,UP            P(UP)=46.7% (n=677)
after DOWN,DOWN        P(UP)=49.9% (n=759)
CT hours 00-04         P(UP|prev UP)=50.0% (n=228)  P(UP|prev DOWN)=49.3% (n=225)  gap=+0.7 pts  +-4.7 (1 SE)  z=+0.1
CT hours 04-08         P(UP|prev UP)=44.2% (n=224)  P(UP|prev DOWN)=45.7% (n=269)  gap=-1.5 pts  +-4.5 (1 SE)  z=-0.3
CT hours 08-12         P(UP|prev UP)=45.6% (n=241)  P(UP|prev DOWN)=51.4% (n=255)  gap=-5.7 pts  +-4.5 (1 SE)  z=-1.3
CT hours 12-16         P(UP|prev UP)=45.5% (n=244)  P(UP|prev DOWN)=53.2% (n=252)  gap=-7.7 pts  +-4.5 (1 SE)  z=-1.7
CT hours 16-20         P(UP|prev UP)=51.5% (n=237)  P(UP|prev DOWN)=46.7% (n=259)  gap=+4.8 pts  +-4.5 (1 SE)  z=+1.1
CT hours 20-24         P(UP|prev UP)=48.8% (n=250)  P(UP|prev DOWN)=50.4% (n=246)  gap=-1.6 pts  +-4.5 (1 SE)  z=-0.4
(exit 0)
```

## 2026-11-06 20:10:01 tasks/queue/085-pihole-clients.sh
```
== devices seen in the last 24 h (address, lookups, last seen, blocked)
OCI runtime exec failed: exec failed: unable to start container process: exec: "sqlite3": executable file not found in $PATH
== names Pi-hole knows (address, name)
OCI runtime exec failed: exec failed: unable to start container process: exec: "sqlite3": executable file not found in $PATH
== local DNS names set (dns.hosts)
[]
(exit 0)
```

## 2026-11-06 20:13:01 tasks/queue/086-pihole-clients.sh
```
== devices seen in the last 24 h (address, lookups, last seen, blocked)
127.0.0.1|9852|2026-11-06 20:12:29|0
192.168.1.142|1435|2026-11-06 20:12:16|375
192.168.1.228|1009|2026-11-06 17:00:25|246
192.168.1.240|560|2026-11-06 20:06:51|52
192.168.1.130|127|2026-11-06 20:11:37|70
== names Pi-hole knows (address, name)
127.0.0.1|localhost|virtual interface
::1|localhost|virtual interface
fe80::e197:65e6:719b:399c||Raspberry Pi (Trading) Ltd
172.17.0.1||
0.0.0.0||virtual interface
ff02::16||virtual interface
192.168.1.107||Raspberry Pi (Trading) Ltd
fe80::469:a9ff:fed0:ac9f||
fe80::1034:1fff:fe35:38b9||
fe80::a405:93ff:fefe:aa3d||
fe80::98b3:90ff:fedc:483b||
192.168.1.142||
192.168.1.130||Cloud Network Technology Singapore Pte. Ltd.
fe80::a045:3bb6:47e1:55f3||Cloud Network Technology Singapore Pte. Ltd.
192.168.1.240||
192.168.1.228||
fe80::c6e:c5ff:fe19:b9b5||
fe80::1831:65ff:fe10:4206||
fe80::8064:fff:fe79:13c4||
fe80::44aa:1cff:fe5a:a4cb||
== local DNS names set (dns.hosts)
[]
(exit 0)
```

## 2026-11-06 20:16:01 tasks/queue/087-pihole-names.sh
```
[ 192.168.1.107 pi-hub, 192.168.1.142 kylar-iphone, 192.168.1.228 sharee-iphone, 192.168.1.240 warren-ipad, 192.168.1.130 living-room-tv ]
== dns.hosts now
[ 192.168.1.107 pi-hub, 192.168.1.142 kylar-iphone, 192.168.1.228 sharee-iphone, 192.168.1.240 warren-ipad, 192.168.1.130 living-room-tv ]
== name lookups via Pi-hole
kylar-iphone -> Traceback (most recent call last):
sharee-iphone -> Traceback (most recent call last):
warren-ipad -> Traceback (most recent call last):
living-room-tv -> Traceback (most recent call last):
pi-hub -> Traceback (most recent call last):
== reverse lookup of the iPad
Traceback (most recent call last):
(exit 0)
```

## 2026-11-06 20:22:01 tasks/queue/088-pihole-names-refresh.sh
```
ALL
  networkflush        Flush information stored in Pi-hole's network tables
                        Add '--arp' to additionally flush the ARP table 
== names now (address|name)
192.168.1.106|
192.168.1.107|pi-hub
192.168.1.142|kylar-iphone
192.168.1.228|sharee-iphone
192.168.1.130|living-room-tv
192.168.1.240|warren-ipad
== DNS still answering?
  [✓] FTL is listening on port 53
     [✓] UDP (IPv4)
     [✓] TCP (IPv4)
(exit 0)
```
