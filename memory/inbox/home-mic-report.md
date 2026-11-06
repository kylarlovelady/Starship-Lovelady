# Home speaker mic report (auto, stats only; audio stays on the Pi)

floor = background noise level (16-bit scale, 0 to 32767); speech% = share of the clip louder than 3x the floor; tail quiet = seconds of quiet at the end (end-of-speech needs about 1 s).

| time | clip | secs | peak | avg | floor | speech% | tail quiet |
|---|---|---|---|---|---|---|---|
| Fri 11:24:06 | 34941013996-wake.wav | 2.0 | 3139 | 655 | 288 | 27 | 0.0 |
| Fri 11:25:08 | 34941013996-stt.wav | 61.9 | 4427 | 480 | 264 | 9 | 0.5 |
| Fri 13:55:09 | 29455106377011-wake.wav | 2.0 | 1623 | 341 | 242 | 0 | 2.0 |
| Fri 17:24:50 | 29455106377011-stt.wav | 12580.0 | 16409 | 598 | 237 | 21 | 0.2 |
| Fri 17:24:50 | 38462987905312-wake.wav | 2.0 | 5235 | 744 | 342 | 21 | 0.2 |
| Fri 17:25:15 | 38462987905312-stt.wav | 25.3 | 11700 | 868 | 281 | 31 | 0.0 |

Median background noise floor: 281. Clips with less than 0.8 s of tail quiet: 5 of 6.

## Satellite restarts by the watchdog (last 24 h)
none
