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
