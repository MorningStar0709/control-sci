| Point | Label | Value |
| --- | --- | --- |
| s₁ | β | 4.33 |
| s₂ | β | 4.33 |
| s₁ | ζ | 0.707 |
</details>

(b) $\beta$ 为可变参数  
图 4-28 自动焊接头控制系统根轨迹图

其次，考虑参数 $\beta$ 的选择。在闭环特征方程 $D(s) = 0$ 中，代入 $\alpha = 20$ ，则 $\beta$ 变化时的根轨迹方程为

$$1 + \frac {\beta s}{s ^ {2} + 2 s + 2 0} = 0$$

即 $1 + \beta \frac{s}{(s + 1 + \mathrm{j}4.36)(s + 1 - \mathrm{j}4.36)} = 0$

令 $\beta$ 从0变化到 $\infty$ ，其根轨迹图如图4-28(b)所示。分离点坐标 $d = -4.47$ 。当取模值条件 $\beta = 4.33 = 20K_{2}$ ，即 $K_{2} = 0.2165$ 时，就得到了满足阻尼比 $\zeta = 0.707$ 的闭环主导极点 $s_{1,2} = -3.16 \pm j3.16$ ，其实部绝对值 $\sigma = 3.16$ ，由其决定的调节时间

$$t _ {s} = \frac {4 . 4}{\sigma} = 1. 3 9 < 3 (\Delta = 2 \%)$$

相应的稳态误差值

$$\frac {e _ {\mathrm{ss}} (\infty)}{R} = \frac {2 + K _ {1} K _ {2}}{K _ {1}} = \frac {2 + \beta}{\alpha} = 0. 3 1 6 5 < 0. 3 5$$

因而 $K_{1}=20, K_{2}=0.2165$ 的设计值，满足全部设计指标要求。

MATLAB 产生的系统根轨迹如图 4-29 所示, 系统的单位阶跃响应和单位斜坡响应分别如图 4-30(a) 和图 4-30(b) 所示。

MATLAB 文本如下：

$$
\begin{array}{l} \mathrm{Ga} = \mathrm{zpk} ([ ], [ 0 - 2 ], 1); \\ \text { figure;   rlocus(Ga);   alpha = 20; } \\ \text { hold   on; } r l o c u s (G a, \text { alpha }) \\ \mathrm{Gb} = \mathrm{zpk} ([ 0 ], [ - 1 - 4. 3 6 \mathrm{i} - 1 + 4. 3 6 \mathrm{i} ], 1) \\ \text { figure }; \text { rlocus } (\mathrm{Gb}); \\ \% \text { alpha } \text { 为变参数时的等效开环传递函数模型 } \\ \% \text { 绘制相应系统的根轨迹 } \\ \% \text{求} \mathrm{alpha} = 20 \text{时,系统的闭环特征根} \\ \% \text { beta变参数时的等效开环传递函数模型} \\ \% \text { 绘制相应系统的要轨迹 } \\ \end{array}
$$

![](image/076c143224e4f53549a336234bf36b589137d1a3cb1095c2df1fc90a668df9b0.jpg)

<details>
<summary>scatter</summary>

| System | Gain | Pole | Damping | Overshoot(%) | Frequency(rad/sec) |
| --- | --- | --- | --- | --- | --- |
| G1 | 20 | -1+4.361 | 0.224 | 48.6 | 4.47 |
| G2 | 1 | -1 | 1 | 0 | 1 |
</details>

![](image/dd76ab8a338f1051ad659d76b47ecc5f9135dd50c7582dcdf747f3b974155999.jpg)

<details>
<summary>scatter</summary>

| Point | Real Axis | Imaginary Axis |
| --- | --- | --- |
| ▲ | -1.0 | 4.5 |
| × | -2.0 | 0.0 |
| × | 0.0 | 0.0 |
| ▲ | -1.0 | -4.5 |
</details>

(a) $\alpha$ 为可变参数

![](image/321c85c4522842b6a7f7fd08296b27bc1e9007a1de0e09a76935cae7e5f23921.jpg)

<details>
<summary>scatter</summary>

| System | Gain | Pole | Damping | Overshoot(%) | Frequency(rad/sec) |
| --- | --- | --- | --- | --- | --- |
| G2 | 6.95 | -4.47e-0081 | 1 | 0 | 4.47 |
</details>

![](image/a63eccdfb03cbef26bc1014e1eb659ca718a92d00edf6ce9cb89d6cc1e853401.jpg)

<details>
<summary>line</summary>
