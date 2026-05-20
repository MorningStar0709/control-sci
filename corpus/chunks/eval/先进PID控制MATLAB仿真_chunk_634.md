# 17.2.2 仿真实例

位置指令为 $x_{\mathrm{d}}(t)=0.1\sin(t)$ ，令 $e=x_{\mathrm{d}}-x_{1}$ ，将控制律设计为 $u=k_{p}e+k_{d}\dot{e}$ 。倒立摆初始状态为 $[\pi/60,0]$ ，仿真结果如图 17-2 所示。

![](image/c4f37152a4cb18dbdaa4001afa377073d0b7342e44851092f0320c325c783040.jpg)

<details>
<summary>line</summary>

| time(s) | Ideal position signal | Position signal tracking |
| --- | --- | --- |
| 0 | 0.0 | 0.0 |
| 1 | 0.1 | 0.1 |
| 2 | 0.05 | 0.05 |
| 3 | -0.05 | -0.05 |
| 4 | -0.1 | -0.1 |
| 5 | -0.05 | -0.05 |
| 6 | 0.0 | 0.0 |
| 7 | 0.1 | 0.1 |
| 8 | 0.05 | 0.05 |
| 9 | 0.0 | 0.0 |
| 10 | -0.1 | -0.1 |
</details>

![](image/1607a20a13c2f6593b5b998846cc1e1f68089e6e56fac39bb2717aa3b5e62b6f.jpg)

<details>
<summary>line</summary>

| time(s) | Ideal speed signal | Speed signal tracking |
| --- | --- | --- |
| 0 | 0.1 | -0.4 |
| 1 | 0.05 | -0.2 |
| 2 | -0.05 | -0.1 |
| 3 | -0.1 | 0.0 |
| 4 | -0.05 | 0.1 |
| 5 | 0.05 | 0.15 |
| 6 | 0.1 | 0.1 |
| 7 | 0.05 | 0.05 |
| 8 | 0.0 | 0.0 |
| 9 | -0.05 | -0.05 |
| 10 | -0.1 | -0.1 |
</details>

图 17-2 角度和角速度跟踪
