$$\dot {v} _ {1} = - 1 2. 5 x _ {2} -. 7 5 v _ {1} +. 7 5 v _ {2} + 2 5 0 +. 0 0 5 F _ {1}\dot {v} _ {i} = 6 2. 5 x _ {i} - 6 2. 5 x _ {i + 1} + 3. 7 5 v _ {i - 1} - 7. 5 v _ {i} + 3. 7 5 v _ {i + 1}, \quad i = 2, 3, \dots , N - 1\dot {v} _ {N} = 6 2. 5 x _ {N} + 3. 7 5 v _ {N - 1} - 3. 7 5 v _ {N} - 1 2 5 0 \tag {2.27}$$

if the last unit is a car, and

$$\dot {v} _ {N} = 1 2. 5 x _ {N} +. 7 5 v _ {N - 1} -. 7 5 v _ {N} - 2 5 0 +. 0 0 5 F _ {2}$$

if it is a locomotive. Note that $F_{1}$ and $F_{2}$ are in kilonewtons.

The simulation conditions are: N = 5, with only one locomotive; $x_{1}(0) = 0$ , $x_{2}(0) = x_{3}(0) = x_{4}(0) = x_{5}(0) = 20 \text{ m}; F_{1} = 750 \text{ kN}$ . The simulation interval is 10 s, and the results (MATLAB command step) are shown in Figures 2.9 and 2.10.

![](image/ff1d10ce5c2f4eb47b7034f5304869e40321d970767ab57f0910c965ea085edb.jpg)

<details>
<summary>line</summary>

| Time(s) | Distance (m) |
| --- | --- |
| 0 | 0 |
| 1 | 5 |
| 2 | 15 |
| 3 | 30 |
| 4 | 45 |
| 5 | 60 |
| 6 | 75 |
| 7 | 90 |
| 8 | 105 |
| 9 | 120 |
| 10 | 135 |
</details>

Figure 2.9 Response to a force step of the distance of the locomotive from the origin

![](image/46ad9fdafa16f7476b514ecba87af415c4be142413dab69fc8b23c52f8b0e194.jpg)

<details>
<summary>line</summary>

| Time(s) | x2 | x5 |
| --- | --- | --- |
| 0 | 20.0 | 20.0 |
| 1 | 20.2 | 20.08 |
| 2 | 20.1 | 20.02 |
| 3 | 20.18 | 20.04 |
| 4 | 20.12 | 20.03 |
| 5 | 20.15 | 20.03 |
| 6 | 20.14 | 20.03 |
| 7 | 20.13 | 20.03 |
| 8 | 20.14 | 20.03 |
| 9 | 20.13 | 20.03 |
| 10 | 20.13 | 20.03 |
</details>

Figure 2.10 Responses to a force step of the coupler extensions, first and last couplers
