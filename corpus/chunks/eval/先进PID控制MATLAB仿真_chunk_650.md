# 17.4.3 仿真实例

理想指令为 $y_{d} = \sin t$ ，取 $k_{1} = k_{2} = 10$ ，取 M = 1，控制律为式（17.18），仿真结果如图 17-9 和图 17-10 所示。取 M = 2，取 PD 控制，取 $k_{p} = 150$ ， $k_{d} = 30$ ，仿真结果如图 17-11 和图 17-12 所示。可见，采用线性化反馈控制方法，可实现高精度的位置跟踪，并可获得较小的控制输入信号。

![](image/ad186b571f041197b160d906077b2e3cfacbf6b2e65a6dd10508658a0587b543.jpg)  
图 17-9 采用线性化反馈的位置跟踪（M=1）

![](image/6712cf3244ecf1786bf82bc18ce128870dd8bda03205f7aacb9d65829c6e46b0.jpg)

<details>
<summary>line</summary>

| time | control input |
| --- | --- |
| 0 | 0 |
| 5 | -2 |
| 10 | 2 |
| 15 | -2 |
| 20 | -2 |
| 25 | -2 |
| 30 | 2 |
</details>

图 17-10 采用线性化反馈的控制输入（M=1）

![](image/3a75eb50afc35d216820e0fd00d02bd70cadbbed1bff42bb62b43ec6f79f9526.jpg)

<details>
<summary>line</summary>

| time | ideal position signal | position tracking |
| --- | --- | --- |
| 0 | 0.0 | 0.0 |
| 5 | -1.0 | -1.0 |
| 10 | 0.0 | 0.0 |
| 15 | 1.0 | 1.0 |
| 20 | -1.0 | -1.0 |
| 25 | 0.0 | 0.0 |
| 30 | -1.0 | -1.0 |
</details>

![](image/9a3179443eafa85e1795c86ba8ece515445317387c9cb6ed9d20cae2af203dd4.jpg)

<details>
<summary>line</summary>

| time | position tracking error |
| --- | --- |
| 0 | -0.05 |
| 5 | 0.02 |
| 10 | -0.01 |
| 15 | 0.03 |
| 20 | -0.02 |
| 25 | 0.01 |
| 30 | 0.04 |
</details>

图 17-11 采用 PD 的位置跟踪（M=2）

![](image/3e9dc5999df44cda6c76898183ec6c409d16d18ccc8b7374985df5aa5246fa64.jpg)

<details>
<summary>line</summary>

| time | control input |
| --- | --- |
| 0 | 0 |
| 5 | -2 |
| 10 | 2 |
| 15 | -1 |
| 20 | 2 |
| 25 | -1 |
| 30 | 2 |
</details>

图 17-12 采用 PD 的控制输入 (M=2)
