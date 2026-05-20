# 8.2.3 仿真实例

采用CMAC网络逼近非线性对象

$$y (k) = u (k - 1) ^ {3} + y (k - 1) / (1 + y (k - 1) ^ {2}) \tag {8.15}$$

在仿真中，网络输入取方波信号，Matlab 表示为 $u(t) = \text{sign}(\sin t)$ ，采样时间取 0.05s，网络参数取 M = 200, N = 100, c = 3, $\eta = 0.20, \alpha = 0.05$ ，可保证 $c \ll M$ 及 $c \leqslant N \leqslant M$ 。

CMAC 网络逼近程序为 chap8\_2.m, 仿真结果如图 8-6 所示。

![](image/ea5c62cbd0b6b3e879babdfe1c9137cb4f86c1e855d8dab58bce89ea8f35cdc4.jpg)

<details>
<summary>line</summary>

| time(s) | y_y_n | error |
| --- | --- | --- |
| 0 | 0 | 1 |
| 2 | -2 | -2 |
| 4 | -2 | 2 |
| 6 | -2 | -2 |
| 8 | -2 | 2 |
| 10 | 2 | 0 |
</details>

图 8-6 CMAC 的逼近
