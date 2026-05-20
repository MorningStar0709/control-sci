# 6.9.5 Implementation

C++ and Java implementations of this elevator controller are available online.[8][9]

![](image/0b521db6895048e291e71e9b28d5ab2f334ed7728bedc1279a035751229d24d5.jpg)

<details>
<summary>line</summary>

| Time (s) | Position (m) - Reference | Position (m) - State | Velocity (m/s) - Reference | Velocity (m/s) - State | Voltage (V) - Input |
| --- | --- | --- | --- | --- | --- |
| 0 | 1 | 1 | 0 | 1 | 0 |
| 1 | 1 | 1 | 0 | 1 | 10 |
| 2 | 1 | 1 | 0 | 0 | 0 |
| 3 | 1 | 1 | 0 | 0 | 0 |
| 4 | 1 | 1 | 0 | 0 | 0 |
| 5 | 1 | 1 | 0 | -1 | -10 |
| 6 | 0 | 0 | 0 | -1 | -10 |
| 7 | 0 | 0 | 0 | 0 | 0 |
| 8 | 0 | 0 | 0 | 0 | 0 |
| 9 | 0 | 0 | 0 | 0 | 0 |
| 10 | 0 | 0 | 0 | 0 | 0 |
</details>

Figure 6.3: Elevator response
