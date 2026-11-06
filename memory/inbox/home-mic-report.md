# Home speaker mic report (auto, stats only; audio stays on the Pi)

floor = background noise level (16-bit scale, 0 to 32767); speech% = share of the clip louder than 3x the floor; tail quiet = seconds of quiet at the end (end-of-speech needs about 1 s).

| time | clip | secs | peak | avg | floor | speech% | tail quiet |
|---|---|---|---|---|---|---|---|
| Fri 11:24:06 | 34941013996-wake.wav | 2.0 | 3139 | 655 | 288 | 27 | 0.0 |
| Fri 11:25:08 | 34941013996-stt.wav | 61.9 | 4427 | 480 | 264 | 9 | 0.5 |
| Fri 13:55:09 | 29455106377011-wake.wav | 2.0 | 1623 | 341 | 242 | 0 | 2.0 |
| Fri 14:05:04 | 29455106377011-stt.wav | 593.0 | 16405 | 513 | 268 | 10 | 1.2 |

Median background noise floor: 268. Clips with less than 0.8 s of tail quiet: 2 of 4.

## Satellite restarts by the watchdog (last 24 h)
none
