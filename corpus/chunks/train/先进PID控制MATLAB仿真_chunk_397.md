# 8.2.4 仿真实例

被控对象取单级倒立摆，其动态方程如下：

$$\dot {x} _ {1} = x _ {2}\dot {x} _ {2} = f (\boldsymbol {x}) + g (\boldsymbol {x}) u$$

式中， $f(x)=\frac{g\sin x_{1}-mlx_{2}^{2}\cos x_{1}\sin x_{1}/(m_{c}+m)}{l(4/3-m\cos^{2}x_{1}/(m_{c}+m))}$ ； $g(x)=\frac{\cos x_{1}/(m_{c}+m)}{l(4/3-m\cos^{2}x_{1}/(m_{c}+m))}$ ； $x_{1}$ 和 $x_{2}$ 分别为摆角和摆速； $g=9.8m/s^{2}$ ； $m_{c}$ 为小车质量， $m_{c}=1kg$ ；m为摆杆质量，m=0.1kg；l为摆长的一半，l=0.5m；u为控制输入。

位置指令为 $x_{\mathrm{d}}(t)=0.1\sin(\pi t)$ 。针对变量 $x_{1}$ 和 $x_{2}$ ，分别定义 5 个模糊集合，即取 $p_{1}=p_{2}=5$ ，则 $\prod_{i=1}^{2}p_{i}=p_{1}p_{2}=25$ 。

取以下 5 种隶属函数：

$$\mu_ {\mathrm{NM}} \left(x _ {i}\right) = \exp \left[ - \left(\left(x _ {i} + \pi / 6\right) / (\pi / 2 4)\right) ^ {2} \right]\mu_ {\mathrm{NS}} \left(x _ {i}\right) = \exp \left[ - \left(\left(x _ {i} + \pi / 1 2\right) / (\pi / 2 4)\right) ^ {2} \right]\mu_ {Z} \left(x _ {i}\right) = \exp \left[ - \left(x _ {i} / (\pi / 2 4)\right) ^ {2} \right]\mu_ {\mathrm{PS}} \left(x _ {i}\right) = \exp \left[ - \left(\left(x _ {i} - \pi / 1 2\right) / (\pi / 2 4)\right) ^ {2} \right]\mu_ {\mathrm{PM}} \left(x _ {i}\right) = \exp \left[ - \left(\left(x _ {i} - \pi / 6\right) / (\pi / 2 4)\right) ^ {2} \right]$$

则用于逼近 f 的模糊规则有 25 条。

根据隶属函数设计程序，可得到隶属函数图，如图 8-3 所示。

![](image/63c554ba5b236b23d83fb2bf3081bcf79395642f95c167e495405e8fc914e8a7.jpg)

<details>
<summary>line</summary>

| x | Membership function degree |
| --- | --- |
| -0.8 | 0.0 |
| -0.6 | 0.0 |
| -0.4 | 0.4 |
| -0.2 | 0.9 |
| 0.0 | 0.0 |
| 0.2 | 0.4 |
| 0.4 | 0.9 |
| 0.6 | 0.0 |
</details>

图8-3 $x_{i}$ 的隶属函数

倒立摆初始状态为 $[\pi / 60, 0]$ ， $\theta_f$ 的初始值取 0.10，采用控制律式（8.12），自适应律取式（8.14），取 $Q = \begin{bmatrix} 500 & 0 \\ 0 & 500 \end{bmatrix}$ ， $k_d = 20$ ， $k_p = 10$ ，自适应参数取 $\gamma = 100$ 。

在程序中，分别用 $FS_{2}$ 、 $FS_{1}$ 和 FS 表示模糊系统 $\xi(x)$ 的分子、分母和 $\xi(x)$ ，仿真结果如图 8-4～图 8-6 所示。

![](image/1e666a2ee625fc232f92eec01cc117eb39e2398a0a7dcff81148645d66cf39e9.jpg)

<details>
<summary>line</summary>

| time(s) | Ideal position | Position tracking |
| --- | --- | --- |
| 0 | 0.0 | 0.0 |
| 5 | -0.1 | -0.1 |
| 10 | 0.1 | 0.1 |
| 15 | -0.1 | -0.1 |
| 20 | 0.1 | 0.1 |
| 25 | -0.1 | -0.1 |
| 30 | 0.0 | 0.0 |
</details>

![](image/dd4a52c8c5cb28bb817f7a0a24a2483a45769d1ef628288ca040ca3ae441ad2a.jpg)

<details>
<summary>line</summary>

| time(s) | Ideal speed | Speed tracking |
| --- | --- | --- |
| 0 | 0.1 | 0.0 |
| 5 | -0.1 | -0.1 |
| 10 | 0.1 | 0.0 |
| 15 | -0.1 | -0.1 |
| 20 | 0.1 | 0.0 |
| 25 | -0.1 | -0.1 |
| 30 | 0.0 | 0.0 |
</details>

图 8-4 角度和角速度跟踪

![](image/d052f9abaa7523a9b3c7e5e0c80483a28019f739e4c98080603c9cf16a378d3b.jpg)

<details>
<summary>line</summary>

| time(s) | Control input |
| --- | --- |
| 0 | -0.5 |
| 5 | 1.2 |
| 10 | -1.2 |
| 15 | 1.2 |
| 20 | -1.2 |
| 25 | 1.2 |
| 30 | -1.2 |
</details>

图 8-5 控制输入信号

![](image/26175633c108d6d80610b18bdb660a30d00052e30e9ed07b8a4c039744bdb5ea.jpg)

<details>
<summary>line</summary>

| time(s) | practical fx | fx estimation |
| --- | --- | --- |
| 0 | 1.5 | 1.6 |
| 5 | -1.8 | -1.7 |
| 10 | 1.6 | 1.5 |
| 15 | -1.8 | -1.7 |
| 20 | 1.6 | 1.5 |
| 25 | -1.8 | -1.7 |
| 30 | 1.6 | 1.5 |
</details>

图8-6 $f(x)$ 及 $\hat{f} (x)$ 的变化
