$$1 + K _ {a} K _ {3} \frac {\left(s ^ {2} + \frac {K _ {2} + K _ {3}}{K _ {3}} s + \frac {1}{K _ {3}}\right)}{s (s + 1) (s + 5)} = 0$$

以 $K_{a}K_{3}$ 为可变参数, 绘制等效系统的根轨迹图, 并适当选择待定参数, 使系统性能满足设

计指标。

根据给定的性能指标要求,应有

$$\sigma \% \cong 100 \mathrm{e} ^ {- \pi \zeta / \sqrt {1 - \zeta^ {2}}} \% < 4 \%t _ {s} \cong \frac {4 . 4}{\zeta \omega_ {n}} < 2 \quad (\Delta = 2 \%)$$

故可求得

$$\zeta > 0. 7 2, \omega_ {n} > 3. 1$$

则系统希望主导极点在复平面上的有效取值区域，如图 9-41(a) 中阴影线区域所示。

为了把根轨迹拉向图 9-41(a) 所示阴影线区域, 将等效系统的开环零点取为 $s = -4 \pm j2$ (位于阴影线区域内), 且令

![](image/feca6eb75a50304a57a36daafc08af195a68d147a53bde5e970822435bffafe6.jpg)

<details>
<summary>other</summary>

| Real Axis | Imaginary Axis | Notes |
| --- | --- | --- |
| -4.0 | 2.0 | KαK₃=12 (shaded region) |
| -4.0 | -2.0 | Φn (solid line) |
| -1.0 | 0.0 | ζωn (dotted line) |
| -1.0 | 0.0 | ωn (dashed line) |
</details>

(a) 自动检测系统的根轨迹

![](image/45dfc073364f3305d1f04a096143c43ca13d89bad2af93b6af9f75b48cf7ab05.jpg)

<details>
<summary>text_image</summary>

clc; clear;
num=[1 8 20]; den=[1 6 5 0];
rlocus (num, den); hold on
%
zeta=0.72,wn=3.1;
x=-10:0.1:-zeta*wn; y=-(sqrt (1-zeta^2)/zeta)*x;
xc=-10:0.1:-zeta*wn; c=sqrt (wn^2-xc.^2);
plot (x, y, ':', x, -y, ':', xc, c, ':', xc, -c, ':')
axis([-10 1 -10 10]);
(b) MATLAB 文本
使图形处于保护模式.
显示稳定性区域
</details>

图 9-41 自动检测系统设计(MATLAB)

$$
\begin{array}{l} s ^ {2} + \frac {K _ {2} + K _ {3}}{K _ {3}} s + \frac {1}{K _ {3}} = (s + 4 + \mathrm{j} 2) (s + 4 - \mathrm{j} 2) \\ = s ^ {2} + 8 s + 2 0 \\ \end{array}
$$

即有 $\frac{K_2 + K_3}{K_3} = 8, \quad \frac{1}{K_3} = 20$

解出

$$K _ {2} = 0. 3 5, K _ {3} = 0. 0 5$$

运行图 9-41(b) 所示 MATLAB 文本, 可以画出以 $K_{a} K_{3}$ 为可变参数的根轨迹图, 如图 9-41(a) 所示。由图可见, 当取根轨迹增益 $K_{a} K_{3} = 12$ 时, 闭环极点位于有效取值区域之内。从而满足设计指标要求。本例最终设计结果为: $K_{a} = 240.00, K_{1} = 1.00, K_{2} = 0.35, K_{3} = 0.05$ 。

最后，校验设计参数，系统的单位阶跃响应曲线如图9-42所示。由图得，设计后系统的 $\sigma \% = 2\% ,t_s = 0.88s(\Delta = 2\%)$ ，系统确实满足了设计要求。

MATLAB 文本：

$$
\begin{array}{l} \mathrm{Ka} = 2 4 0; \mathrm{K1} = 1; \mathrm{K2} = 0. 3 5; \mathrm{K3} = 0. 0 5; \\ \mathrm{A} = [ 0 1 0; 0 - 1 1; - \mathrm{Ka} - \mathrm{Ka} * \mathrm{K2} - 5 - \mathrm{Ka} * \mathrm{K3} ]; \\ \mathrm{b} = [ 0 0 \mathrm{Ka} ] ^ {\prime}; \\ c = [ 1 0 0 ]; \\ \mathrm{d} = 0; \\ \mathrm{sys} = \mathrm{ss} (\mathrm{A}, \mathrm{b}, \mathrm{c}, \mathrm{d}); \\ t = 0: 0. 0 1: 3; \\ \text { step } (\text { sys }, t); \text { grid } \\ \end{array}
$$
