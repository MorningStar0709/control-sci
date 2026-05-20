# 【仿真之二】基于 LMI 的 $H_{\infty}$ 控制

取 $\gamma = 100$ ，运行基于LMI的控制器增益求解程序chap16\_2LMI.m，求解LMI不等式（16.13）和（16.15），得 $K = [36.3149\quad 1.8765\quad 6.3851\quad 3.6704]$ 。倒立摆响应结果及控制器输出如图16-4～图16-6所示。

![](image/5908e111cc01aac5c80522c3a43962aa72dcb8d93beb2c74d1a30f464b1ac526.jpg)

<details>
<summary>line</summary>

| time(s) | Angle response of link |
| --- | --- |
| 0 | -0.6 |
| 5 | 0.0 |
| 10 | 0.0 |
| 15 | 0.0 |
| 20 | 0.0 |
| 25 | 0.0 |
| 30 | 0.0 |
</details>

![](image/086ea856136a8e424a172932c6642b39847bc6d0b26f973f949c8547bcc97149.jpg)

<details>
<summary>line</summary>

| time(s) | Position response of cart |
| --- | --- |
| 0 | 0.0 |
| 1 | -0.8 |
| 2 | -0.2 |
| 3 | 0.0 |
| 4 | 0.0 |
| 5 | 0.0 |
| 6 | 0.0 |
| 7 | 0.0 |
| 8 | 0.0 |
| 9 | 0.0 |
| 10 | 0.0 |
| 11 | 0.0 |
| 12 | 0.0 |
| 13 | 0.0 |
| 14 | 0.0 |
| 15 | 0.0 |
| 16 | 0.0 |
| 17 | 0.0 |
| 18 | 0.0 |
| 19 | 0.0 |
| 20 | 0.0 |
| 21 | 0.0 |
| 22 | 0.0 |
| 23 | 0.0 |
| 24 | 0.0 |
| 25 | 0.0 |
| 26 | 0.0 |
| 27 | 0.0 |
| 28 | 0.0 |
| 29 | 0.0 |
| 30 | 0.0 |
</details>

图 16-4 摆的角度和小车位置响应（LMI 方法）

![](image/5be09c7a510a3573c32e44144de6680ac49650d08831e0e6703050283df2e6bf.jpg)

<details>
<summary>line</summary>

| time(s) | Angle speed response of link |
| --- | --- |
| 0 | 2.0 |
| 1 | 0.0 |
| 2 | 0.0 |
| 3 | 0.0 |
| 4 | 0.0 |
| 5 | 0.0 |
| 6 | 0.0 |
| 7 | 0.0 |
| 8 | 0.0 |
| 9 | 0.0 |
| 10 | 0.0 |
| 11 | 0.0 |
| 12 | 0.0 |
| 13 | 0.0 |
| 14 | 0.0 |
| 15 | 0.0 |
| 16 | 0.0 |
| 17 | 0.0 |
| 18 | 0.0 |
| 19 | 0.0 |
| 20 | 0.0 |
| 21 | 0.0 |
| 22 | 0.0 |
| 23 | 0.0 |
| 24 | 0.0 |
| 25 | 0.0 |
| 26 | 0.0 |
| 27 | 0.0 |
| 28 | 0.0 |
| 29 | 0.0 |
| 30 | 0.0 |
</details>

![](image/973784fc02347413ff47f7343f7bb4b842d7179770317e0c63651091aa3a344c.jpg)

<details>
<summary>line</summary>

| time(s) | Position speed response of cart |
| --- | --- |
| 0 | -1.5 |
| 5 | 0.0 |
| 10 | 0.0 |
| 15 | 0.0 |
| 20 | 0.0 |
| 25 | 0.0 |
| 30 | 0.0 |
</details>

图 16-5 摆的角速度和小车速度响应（LMI 方法）

![](image/c2b8581d2f87ce98ace3ea1d036146d2b459753db0dd98866d84a58b8035fe91.jpg)

<details>
<summary>line</summary>

| time(s) | Angle speed response of link |
| --- | --- |
| 0 | 2.0 |
| 5 | 0.0 |
| 10 | 0.0 |
| 15 | 0.0 |
| 20 | 0.0 |
| 25 | 0.0 |
| 30 | 0.0 |
</details>

![](image/f8516a71effc718dbf96acbcd95dadbe1a8c3590221779719071bf61f25ae95a.jpg)

<details>
<summary>line</summary>

| time(s) | Position speed response of cart |
| --- | --- |
| 0 | -1.5 |
| 5 | 0.0 |
| 10 | 0.0 |
| 15 | 0.0 |
| 20 | 0.0 |
| 25 | 0.0 |
| 30 | 0.0 |
</details>

图 16-6 控制输入（LMI 方法）
