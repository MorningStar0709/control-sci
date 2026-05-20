$$
\begin{array}{l} \dot {x} _ {1} = v _ {1} \\ \dot {x} _ {2} = v _ {2} \\ \dot {v} _ {1} = - \frac {K _ {1}}{M} (x _ {1} - x _ {2} - x _ {1 0}) - \frac {D}{M} (v _ {1} - v _ {2}) - g + \frac {1}{M} u \\ \dot {v} _ {2} = \frac {K _ {1}}{m} (x _ {1} - x _ {2} - x _ {1 0}) + \frac {D}{m} (v _ {1} - v _ {2}) \\ - \frac {K _ {2}}{m} (x _ {2} - y _ {R} - x _ {2 0}) - g - \frac {1}{m} u. \tag {2.20} \\ \end{array}
$$

![](image/0d8f04ef15b99396454e70b99a801f6f6805c3a501dc3596ef8afa613826d665.jpg)

<details>
<summary>line</summary>

| Time(s) | x1 | x2 |
| --- | --- | --- |
| 0 | 1.5 | 0.7 |
| 0.5 | 1.2 | 0.65 |
| 1 | 1.0 | 0.65 |
| 1.5 | 1.1 | 0.65 |
| 2 | 1.2 | 0.65 |
| 2.5 | 1.2 | 0.65 |
| 3 | 1.2 | 0.65 |
| 3.5 | 1.2 | 0.65 |
| 4 | 1.2 | 0.65 |
| 4.5 | 1.2 | 0.65 |
| 5 | 1.2 | 0.65 |
</details>

Figure 2.5 Time responses for the active suspension system: Zero-input case

The output equation is

$$
x _ {1} = \left[ \begin{array}{l l l l} 1 & 0 & 0 & 0 \end{array} \right] \left[ \begin{array}{l} x _ {1} \\ x _ {2} \\ v _ {1} \\ v _ {2} \end{array} \right]. \tag {2.21}
$$

For the specific values $M = 300 \, kg, m = 50 \, kg, K_{1} = 3000 \, N/m, K_{2} = 3 \times 10^{4} \, N/m, D = 600 \, N/ms^{-1}, x_{10} = 1.5 \, m, x_{20} = .75 \, m,$ and $g = 9.8 \, m/s^{2}$ , the state equations are

$$
\begin{array}{l} \frac {d}{d t} \left[ \begin{array}{l} x _ {1} \\ x _ {2} \\ v _ {1} \\ v _ {2} \end{array} \right] = \left[ \begin{array}{c c c c} 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \\ - 1 0 & 1 0 & - 2 & 2 \\ 6 0 & - 6 6 0 & 1 2 & - 1 2 \end{array} \right] \left[ \begin{array}{l} x _ {1} \\ x _ {2} \\ v _ {1} \\ v _ {2} \end{array} \right] \\ + \left[ \begin{array}{c} 0 \\ 0 \\ . 0 0 3 3 4 \\ -. 0 2 \end{array} \right] u + \left[ \begin{array}{c} 0 \\ 0 \\ 0 \\ 6 0 0 \end{array} \right] y _ {R} + \left[ \begin{array}{c} 0 \\ 0 \\ 5. 2 \\ 3 5 0. 2 \end{array} \right]. \tag {2.22} \\ \end{array}
$$

The simulation conditions are as follows:
