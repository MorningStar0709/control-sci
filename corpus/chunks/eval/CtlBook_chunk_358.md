# 10.5 Example Design

(This problem is Example 9.5 from Nice, page 483).

Problem: Design a PID controller for a system where the plant is:

$$P (s) = \frac {2 2 . 5 (s + 8)}{(s + 3) (s + 6) (s + 1 0)}$$

Step response must have

$$T _ {S} = 0. 5 5 (\mathrm{sec}) \quad \% O S = 20 \% \quad S S E = 0$$

Solution Procedure

![](image/d26fbd4492ae49d4d56399d9603fbdfd487640429e320a47eccc3665fb842fa5.jpg)

<details>
<summary>line</summary>

| Time (s) | WTS | WOS | WSSE | WU | WM | Wbal | W_BH |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| 0.2 | 0.6 | 1.1 | 0.6 | 0.2 | 0.8 | 0.3 | 0.8 |
| 0.4 | 0.9 | 0.9 | 0.8 | 0.2 | 1.0 | 0.6 | 1.0 |
| 0.6 | 1.0 | 0.9 | 0.9 | 0.2 | 1.0 | 1.0 | 1.0 |
| 0.8 | 1.0 | 0.9 | 1.0 | 0.2 | 1.0 | 1.4 | 1.4 |
| 1.0 | 1.0 | 0.9 | 1.0 | 0.2 | 1.0 | 1.5 | 1.5 |
</details>

Figure 10.3: Results of our rst PID search. There are 6 step responses. Red horizontal lines are shown for the $T _ { S }$ window which must be entered by t = 0.55 (green line)

Rename userSetup.py to setup10p6.py (for this example) to input the plant and the performance specications above. Set the initial values of $\dot { K _ { P } } = K _ { I } = K _ { D } = \dot { 1 }$ (note K1, K2, K3 are used in some parts of the code instead of $K _ { P } , K _ { I } , K _ { D } )$ .

Let's say that some initial manual PID design work for this system gave a starting point of

$$K _ {P} = 1 5, K _ {I} = 1 5, K _ {D} = 0. 2 5$$

Set Nvals = 12 (the code actually searches Nvals+1 values each to hit both ends of the search range) and start close to this value: scale\_range = 5.
