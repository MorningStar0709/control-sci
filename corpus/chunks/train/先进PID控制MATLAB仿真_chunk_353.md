# 7.2.4 仿真实例

取被控对象参数 J=10，C=5.0， $d=30\sin10t$ 。位置指令信号取 $\sin t$ 。采用控制律式（7.7），取 $k_{p}=100$ ， $k_{i}=50$ ， $k_{r}=50$ ，仿真结果如图 7-3 和图 7-4 所示。

![](image/1a45345b67d05e36a5a8aa945509b278a64f5751ac420579727ef86ff3f2973c.jpg)

<details>
<summary>line</summary>

| time(s) | ideal position signal | position response |
| --- | --- | --- |
| 0 | 1.0 | 0.5 |
| 1 | 1.0 | 1.1 |
| 2 | 1.0 | 1.0 |
| 3 | 1.0 | 1.0 |
| 4 | 1.0 | 1.0 |
| 5 | 1.0 | 1.0 |
| 6 | 1.0 | 1.0 |
| 7 | 1.0 | 1.0 |
| 8 | 1.0 | 1.0 |
| 9 | 1.0 | 1.0 |
| 10 | 1.0 | 1.0 |
</details>

![](image/971c3e27eaec47881a875a64e8b74bd46ede3583c9dad6b634e052bc56da54f5.jpg)

<details>
<summary>line</summary>

| time(s) | Speed response |
| --- | --- |
| 0 | 0.0 |
| 1 | 0.9 |
| 2 | -0.1 |
| 3 | 0.0 |
| 4 | 0.0 |
| 5 | 0.0 |
| 6 | 0.0 |
| 7 | 0.0 |
| 8 | 0.0 |
| 9 | 0.0 |
| 10 | 0.0 |
</details>

图 7-3 位置和速度响应

![](image/afbd9382e72d006c6405dc18640f8ea9469d0f32e7f7c7a7721445393cf2cad0.jpg)

<details>
<summary>line</summary>

| time(s) | Control input |
| --- | --- |
| 0 | 50 |
| 1 | -12 |
| 2 | 0 |
| 3 | 0 |
| 4 | 0 |
| 5 | 0 |
| 6 | 0 |
| 7 | 0 |
| 8 | 0 |
| 9 | 0 |
| 10 | 0 |
</details>

图 7-4 控制输入
