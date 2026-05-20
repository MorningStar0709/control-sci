# 8.1.3 仿真实例

被控对象取单级倒立摆，其动态方程如下：

$$
\begin{array}{l} \dot {x} _ {1} = x _ {2} \\ \dot {x} _ {2} = f (\boldsymbol {x}) + g (\boldsymbol {x}) u \\ \end{array}
$$

式中， $f(x)=\frac{g\sin x_{1}-mlx_{2}^{2}\cos x_{1}\sin x_{1}/(m_{c}+m)}{l(4/3-m\cos^{2}x_{1}/(m_{c}+m))}$ ； $g(x)=\frac{\cos x_{1}/(m_{c}+m)}{l(4/3-m\cos^{2}x_{1}/(m_{c}+m))}$ ； $x_{1}$ 和 $x_{2}$ 分别为摆角和摆速； $g=9.8m/s^{2}$ ； $m_{c}$ 为小车质量， $m_{c}=1kg$ ； m 为摆杆质量， $m=0.1kg$ ； l 为摆长的一半， $l=0.5m$ ； u 为控制输入。

位置指令为 $x_{\mathrm{d}}(t)=0.1\sin(t)$ 。倒立摆初始状态为 $[\pi/60,0]$ ，采用控制律式（8-2），取 $\lambda=5$ ，则有 $k_{p}=25$ ， $k_{d}=10$ 。仿真结果如图 8-1 和图 8-2 所示。

![](image/5d23e342c81e63b03a01cd31bdfb2d812cb4708daa336678134eb0e98e875477.jpg)

<details>
<summary>line</summary>

| time(s) | ideal angle signal | angle tracking |
| --- | --- | --- |
| 0 | 0.0 | 0.0 |
| 5 | -0.1 | -0.1 |
| 10 | 0.0 | 0.0 |
| 15 | -0.1 | -0.1 |
| 20 | 0.0 | 0.0 |
| 25 | -0.1 | -0.1 |
| 30 | 0.0 | 0.0 |
</details>

图 8-1 摆角跟踪

![](image/65f6ed069355166a7431db38df788712ef1420a135b607eeb524bbf456e6cecd.jpg)

<details>
<summary>line</summary>

| time(s) | Control input |
| --- | --- |
| 0 | -0.5 |
| 5 | 1.1 |
| 10 | -1.1 |
| 15 | 1.1 |
| 20 | -1.1 |
| 25 | 1.1 |
| 30 | -1.1 |
</details>

图 8-2 控制输入信号
