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
| Fri 17:56:42 | 51061957613883-wake.wav | 2.0 | 3293 | 521 | 292 | 12 | 0.8 |
| Fri 17:56:51 | 51061957613883-stt.wav | 9.3 | 8681 | 706 | 328 | 17 | 0.8 |
| Fri 17:57:51 | 52957987082214-wake.wav | 2.0 | 3146 | 461 | 310 | 1 | 0.7 |
| Fri 17:58:02 | 52957987082214-stt.wav | 11.5 | 6301 | 716 | 320 | 22 | 1.2 |
| Fri 17:58:08 | 53029210591923-wake.wav | 2.0 | 13939 | 1845 | 417 | 54 | 0.2 |
| Fri 17:58:15 | 53029210591923-stt.wav | 6.7 | 11225 | 670 | 300 | 11 | 2.2 |
| Sat 11:20:21 | 53042121034015-wake.wav | 2.0 | 4718 | 799 | 387 | 15 | 0.1 |
| Sat 11:26:12 | 53042121034015-stt.wav | 350.6 | 16400 | 422 | 251 | 6 | 0.0 |
| Sat 11:26:12 | 115581106260969-wake.wav | 2.0 | 2281 | 364 | 249 | 3 | 0.0 |
| Sat 11:26:37 | 115581106260969-stt.wav | 25.3 | 4097 | 435 | 286 | 2 | 0.3 |
| Sat 12:19:44 | 115944154382670-wake.wav | 2.0 | 3177 | 557 | 256 | 24 | 0.7 |
| Sat 12:20:16 | 115944154382670-stt.wav | 32.0 | 12049 | 591 | 267 | 14 | 0.8 |
| Sat 12:20:24 | 119162982453665-wake.wav | 2.0 | 16405 | 3151 | 726 | 60 | 0.2 |
| Sat 12:20:45 | 119162982453665-stt.wav | 21.8 | 15008 | 722 | 281 | 23 | 0.0 |
| Sat 13:06:11 | 119192456350792-wake.wav | 2.0 | 6530 | 707 | 306 | 19 | 0.6 |
| Sat 13:06:26 | 119192456350792-stt.wav | 14.6 | 12166 | 547 | 258 | 16 | 0.0 |
| Sat 13:06:37 | 121933009126321-wake.wav | 2.0 | 16402 | 1896 | 311 | 56 | 0.1 |
| Sat 13:07:39 | 121933009126321-stt.wav | 38.1 | 16403 | 767 | 286 | 18 | 2.1 |

Median background noise floor: 288. Clips with less than 0.8 s of tail quiet: 17 of 24.

## Satellite restarts by the watchdog (last 24 h)
Nov 07 13:07:39 LoveladyMainAiHub python3[2953]: stuck in listening for 47s, restarting satellite
