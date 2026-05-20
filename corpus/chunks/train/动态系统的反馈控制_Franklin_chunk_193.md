(a) 图 3.57 所示阴影区域对应的 $\omega_{n}$ 和 $\zeta$ 值是多少（通过图进行简单估计就足够了）。  
(b) 令 $K_{\alpha} = \alpha = 2$ ，求 $K$ 和 $K_{1}$ 值，以使闭环系统的极点位于阴影区域之内。  
(c) 证明无论 $K_{\alpha}$ 和 $\alpha$ 为何值，控制器都能很灵活地将极点置于复平面（左半）内的任何地方。

![](image/d89eb69a96a36b44b14351c472ec9317a0272586b283b440adffc5b29151abb7.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    R -->|+| Sum1["Σ"]
    Sum1 --> e_t["e(t)"]
    e_t -->|+| Sum2["Σ"]
    Sum2 --> K["K"]
    K --> Kα[Kα/(s+α)]
    Kα --> Y
    Y -->|-| Sum1
    Sum1 -->|+| Kf["kf/(s)"]
    Kf --> Sum2
```
</details>

图 3.56 习题 3.31 的单位反馈系统

![](image/2da6ff4db98410961aa09fdb7d8190229fad3c753a593fc2ad0e3c349e859fba.jpg)

<details>
<summary>text_image</summary>

Im(s)
4
θ₁
2
θ₂
-4
-2
Re(s)
-2
</details>

图 3.57 习题 3.31 中所期望的极点位置

3.32 单位反馈系统的开环传递函数为

$$G (s) = \frac {K}{s (s + 2)}$$

当输入为阶跃信号时，所期望的系统响应指定为峰值时间 $t_{p}=1s$ 和超调 $M_{p}=5\%$ .

(a) 通过选择合适的 K 值，确定能否同时满足这两个指标。  
(b) 在 s 平面中画出两个指标都满足的相关区域，并说明对于一些可能的 K 值，

可能的根位置是什么。

(c) 放宽(a) 问部分的指标，选择合适的 K 值，运用 Matlab 来验证这些新指标得到了满足。

3.33 如图 3.58a 所示的为一个简单的机械系统。其中参数 k 为弹簧劲度系数，b 为黏滞摩擦常数，m 为质量。其中 2N 的力以 $F=2 \times 1(t)$ 的形式施加给物体，所得的阶跃响应如图 3.58b 所示。系统参数 k，b 和 m 的值是多少？

![](image/729776ca67d75c7b351c24d3f20d9a87ee22d2c5b508e831919cbda77f6089bf.jpg)

<details>
<summary>text_image</summary>

b
k
x
F
无摩擦
</details>

a）习题3.33的机械系统  
![](image/b3dd66108fbf82a09b87e9edb8bf156082dc94d7961056ec044f2ddecfaa3a18.jpg)

<details>
<summary>line</summary>

| 时间/s | x(t) |
| --- | --- |
| 0 | 0.000 |
| 1 | 0.080 |
| 2 | 0.115 |
| 3 | 0.100 |
| 4 | 0.100 |
| 5 | 0.100 |
| 6 | 0.100 |
| 7 | 0.100 |
</details>

b）习题3.33的阶跃响应

图 3.58  
![](image/aab623c83181c9c6bf50ed5837cb13d4df28074a1f151069f8c7e0d25c81e7a0.jpg)

<details>
<summary>text_image</summary>

k
b
M
y
u
</details>

图 3.59 习题 3.34 的简易机械系统

3.34 如图 3.59 所示为一个机械系统。质量 m=20kg，并且控制力 u 与参考输入成比例：u=Ar。

(a) 求出从 R 到 Y 的传递函数。

(b) 确定参数 k, b, A 的值，使系统的上升时间 $t_{r}=1s$ ，超调 $M_{p}=16\%$ ，零点稳态误差为阶跃 r。

3.35 图 2.32 所示直流电动机的运动方程为式(2.62)～式(2.63)，即

$$J _ {\mathrm{m}} \ddot {\theta} _ {\mathrm{m}} + \left(b + \frac {K _ {\mathrm{t}} K _ {\mathrm{e}}}{R _ {\mathrm{a}}}\right) \dot {\theta} _ {\mathrm{m}} = \frac {K _ {\mathrm{t}}}{R _ {\mathrm{a}}} v _ {\mathrm{a}}$$

假设 $J_{m}=0.01kg\cdot m^{2}$ ; $b=0.001N\cdot m\cdot s$ ; $K_{e}=0.02V\cdot s;\quad K_{t}=0.02N\cdot m/A;$ $R_{a}=10\Omega$

(a) 求外加电压 $v_{n}$ 和电动机角速度 $\dot{\theta}_{m}$ 之间的传递函数。

(b) 外加 $v_{a}=10V$ 的电压后，电动机的稳态速度是多少？
