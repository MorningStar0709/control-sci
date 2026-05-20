# 2. 幅值裕度 h

设 $\omega_{x}$ 为系统的穿越频率, 则系统在 $\omega_{x}$ 处的相角

$$\varphi (\omega_ {x}) = \underline {{{G (j \omega_ {x}) H (j \omega_ {x})}}} = (2 k + 1) \pi ; \quad k = 0, \pm 1, \dots \tag {5-82}$$

定义幅值裕度为

$$h = \frac {1}{\mid G (\mathrm{j} \omega_ {x}) H (\mathrm{j} \omega_ {x}) \mid} \tag {5-83}$$

幅值裕度 h 的含义是, 对于闭环稳定系统, 如果系统开环幅频特性再增大 h 倍, 则系统将处于临界稳定状态, 复平面中 $\gamma$ 和 h 的表示如图 5-39(b) 所示; 对于闭环不稳定的系统, 幅值裕度指出了为使系统临界稳定, 开环幅频特性应当减小到原来的 1/h。

对数坐标下，幅值裕度按下式定义：

$$h (\mathrm{dB}) = - 2 0 \lg | G (\mathrm{j} \omega_ {x}) H (\mathrm{j} \omega_ {x}) | \quad (\mathrm{dB}) \tag {5-84}$$

半对数坐标图中的 $\gamma$ 和 h 的表示如图 5-39(a) 所示。

![](image/1ea3a8438e1f886a28e0cebe10d9c058f6d6f707f6e102966893acf949053ddd.jpg)  
图 5-39 稳定和不稳定系统的相角裕度和幅值裕度

![](image/8fc3089e099d2c505a768f725bc71e60556e25027c665378eaf5bc0af9046d3f.jpg)

<details>
<summary>text_image</summary>

正幅值裕度
1/h
G平面
-1
γ
φ
正相角裕度
G(jω)
稳定系统
</details>

![](image/d0edbcf8e69b684e4f2019c27e9a2c8674b34b9a850fa4dad1d1f7ccb5da0a42.jpg)

<details>
<summary>text_image</summary>

j
G平面
负相角裕度
γ
1
-1
φ
1/h
G(jω)
负幅值裕度
不稳定系统
</details>

(b) 幅值裕度  
图 5-39 稳定和不稳定系统的相角裕度和幅值裕度(续)

当幅值裕度以分贝表示时,如果 h 大于 1,则幅值裕度为正值;如果 h 小于 1,则幅值裕度为负值。因此,正幅值裕度(以 dB 表示)表示系统是稳定的,负幅值裕度(以 dB 表示)表示系统是不稳定的。

一阶或二阶系统的幅值裕度为无穷大, 因为这类系统的极坐标图与负实轴不相交。因此, 理论上, 一阶或二阶系统不可能是不稳定的 (当然, 一阶或二阶系统在一定意义上说只能是近似的,因为在推导系统方程时, 忽略了一些小的时间滞后, 因此它们不是真正的一阶或二阶系统。如果考虑这些小的滞后, 则所谓的一阶或二阶系统也可能是不稳定的)。

注意,对于具有不稳定开环系统的非最小相位系统,除非 $G(+j\omega)$ 图包围 $(-1+j0)$ 点,否则不能满足稳定条件。因此,这种稳定的非最小相位系统将具有负的相角裕度和幅值裕度。

条件稳定系统将具有两个或多个穿越频率，并且某些具有复杂动态特性的高阶系统还可能具有两个或多个截止频率，如图 5-40 所示。对于具有两个或多个截止频率的稳定系统，相角裕度应在最高的截止频率上测量。

![](image/bf1b990564fc0c3eeab399b742b7bb736ed10efdba69fe99e6412b646d8ba74a.jpg)

<details>
<summary>text_image</summary>

穿越频率
(ω₁,ω₂,ω₃)
ω₃
ω₂
ω₁
ω=∞
ω
0
</details>

![](image/3af7a0a6296f0213f393f79b6c9a48883746f9f989dead4a9ca5425a55570ada.jpg)

<details>
<summary>text_image</summary>

j
-1
ω=∞
ω₁
ω₂
ω₃
截止频率
(ω₁,ω₂,ω₃)
ω
0
</details>

图 5-40 具有多于两个以上的穿越频率或截止频率系统的极坐标图

例 5-13 已知单位反馈系统

$$G (s) = \frac {K}{(s + 1) ^ {3}}$$

设 K 分别为 4 和 10 时，试确定系统的稳定裕度。

解 系统开环频率特性

$$
\begin{array}{l} G (\mathrm{j} \omega) = \frac {K}{(1 + \omega^ {2}) ^ {\frac {3}{2}}} \angle - 3 \arctan \omega \\ = \frac {K [ (1 - 3 \omega^ {2}) - \mathrm{j} \omega (3 - \omega^ {2}) ]}{(1 + \omega^ {2}) ^ {3}} \\ \end{array}
$$

按 $\omega_{x},\omega_{c}$ 定义可得
