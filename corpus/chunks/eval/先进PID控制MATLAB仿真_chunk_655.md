# 17.5.3 仿真实例

假设不考虑小车的控制问题，被控对象取单级倒立摆，则动态方程如下：

$$\dot {x} _ {1} = x _ {2}\dot {x} _ {2} = f (\boldsymbol {x}) + g (\boldsymbol {x}) u$$

式中， $f(x)=\frac{g\sin x_{1}-mlx_{2}^{2}\cos x_{1}\sin x_{1}/(m_{c}+m)}{l(4/3-m\cos^{2}x_{1}/(m_{c}+m))}$ ； $g(x)=\frac{\cos x_{1}/(m_{c}+m)}{l(4/3-m\cos^{2}x_{1}/(m_{c}+m))}$ ； $x_{1}$ 和 $x_{2}$ 分别为摆角和摆速； $g=9.8m/s^{2}$ ； $m_{c}$ 为小车质量， $m_{c}=1kg$ ；m为摆杆质量，m=0.1kg；l为摆长的一半，l=0.5m；u为控制输入。

位置指令为 $y_{\mathrm{d}}(t)=0.1\sin(\pi t)$ ，采用控制律式（17.26），倒立摆初始状态为 $[-π/60,0]$ ，仿真结果如图 17-13 和图 17-14 所示。

![](image/e4aacccc1de901eeba10acf5ce7226a3407c27b282aaf8ba95d1f58d521f9080.jpg)

<details>
<summary>line</summary>

| time(s) | ideal position signal | position tracking |
| --- | --- | --- |
| 0.0 | 0.0 | 0.0 |
| 0.5 | 0.1 | 0.05 |
| 1.0 | 0.0 | -0.05 |
| 1.5 | -0.1 | -0.1 |
| 2.0 | 0.0 | -0.05 |
| 2.5 | 0.1 | 0.05 |
| 3.0 | 0.0 | 0.0 |
</details>

![](image/f3541167ad2a858ac822847e9a75c5d524e5c600f42668122511cc0e8eab8e2f.jpg)

<details>
<summary>line</summary>

| time(s) | ideal speed signal | speed tracking |
| --- | --- | --- |
| 0.0 | 0.3 | -0.1 |
| 0.5 | 0.1 | 0.2 |
| 1.0 | -0.3 | -0.3 |
| 1.5 | 0.1 | 0.1 |
| 2.0 | 0.3 | 0.2 |
| 2.5 | 0.1 | 0.1 |
| 3.0 | -0.3 | -0.3 |
</details>

图 17-13 位置和速度跟踪

![](image/f19544e0b0880c4fa0ae79d3a490d51677804e5891c5aa303597f660addee842.jpg)

<details>
<summary>line</summary>

| time(s) | Control input |
| --- | --- |
| 0.0 | 2.0 |
| 0.5 | -2.0 |
| 1.0 | 0.0 |
| 1.5 | 2.0 |
| 2.0 | 0.0 |
| 2.5 | -2.0 |
| 3.0 | 0.0 |
</details>

图 17-14 控制输入
