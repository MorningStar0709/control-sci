# 2.2节习题

2.11 首先已知运算放大器的实际模型由下列方程给出，模型如图 2.47 所示

$$V _ {\mathrm{out}} = \frac {1 0 ^ {7}}{s + 1} [ v _ {+} - v _ {-} ]i _ {+} = i _ {-} = 0$$

应用此模型建立图示简单放大电路的传递函数。

![](image/502e05ebaba466cd98ca94b5796bf6cf22b32cd8d074f82c55a6df99ac598132.jpg)

<details>
<summary>text_image</summary>

Rin
v-
+
Vout
Vin
v+
</details>

图2.47 习题2.11的电路

2.12 图 2.48 所示为运算放大器的连接。若为理想运算放大器，则有 $V_{out} = V_{in}$ 。若此运算放大器存在习题 2.11 中的非理想传递函数时，列出此时的传递函数。

![](image/c59ebaf799385fc0dc0b233508b952e7b8eedcf5fc0e1030a53c247e5ecd7ade.jpg)

<details>
<summary>text_image</summary>

v-
+
V_in
v_+
V_out
</details>

图 2.48 习题 2.12 的电路

2.13 图 2.49 所示为电动机功率放大器的常见连接，目标是让电动机电流跟随输入电压，该连接称为电流放大器。假设感应电阻 $r_{s}$ 与反馈电阻 R 相比非常小，列写 $V_{in}$ 到 $I_{a}$ 的传递函数。同时写出当 $R_{f} = \infty$ 时的传递函数。

![](image/74551acf37434a753c89807aa42b526fcc802e8a717f8dcc28e2866b4ce379b1.jpg)

<details>
<summary>text_image</summary>

Rf
Vin
Rin
v-
+
va
Ia
DC 电动机
Rs
Vout
</details>

图 2.49 习题 2.13 的运算放大器电路

2.14 如图 2.50 所示，运算放大器的正端以及负端都与反馈连接，如果运算放大器存在习题 2.11 中给出的非理想传递函数，在电路维持稳定的情况下，根据负反馈系数 $N = R_{\mathrm{in}} / (R_{\mathrm{in}} + R_{\mathrm{f}})$ 给出正反馈系数 $P = r / (r + R)$ 的最大可能值。

![](image/206878d58a45e090e9ca39fa2779ec3d5e7da239c33d1f730b565cd7a7b1a45e.jpg)

<details>
<summary>text_image</summary>

Rf
Vin
v-
+
-
v+
R
r
Vout
</details>

图2.50 习题2.14的运算放大器电路

2.15 列写图 2.51 所示电路的动态方程，并建立其传递函数。

(a) 被动超前电路； (b) 主动超前电路；  
(c) 主动滞后电路；(d) 被动陷波电路。

2.16 图 2.52 所示的具有灵活性电路称之为双二次型电路，因为它的传递函数是两个二阶或二次多项式的比。

通过选取不同的 $R_{a}$ 、 $R_{b}$ 、 $R_{c}$ 、 $R_{d}$ 的值，此电路可实现低通、带通、高通或带阻（陷波）滤波器。

(a) 说明当 $R_{\mathrm{a}} = R$ 且 $R_{\mathrm{b}} = R_{\mathrm{c}} = R_{\mathrm{d}} = \infty$ 时，从 $V_{\mathrm{in}}$ 到 $V_{\mathrm{out}}$ 的传递函数可写为如下低通滤波器：

![](image/3472ad4f493765669b750666e67bd70a6983096e0d7cd79e761d23ba3edcc651.jpg)

![](image/b89b8ae873da64ea9115135212f16396d6f021f8ec340ec3b066cd1ca9c0fd39.jpg)

<details>
<summary>text_image</summary>

Vin
R2
R1
C
Rf
Vout
</details>

b）主动超前

![](image/193b64a139c0c6c3488ffe49d342832b721382a234166a657985dcff117af4df.jpg)

<details>
<summary>chemical</summary>

Electrical circuit diagram with resistors, capacitors, and voltage labels
</details>

d）被动陷波电路

图2.51  
![](image/70dfec4f6fd09868ae9616ba39e638f9f5b84be5784c684c4e743c6a76a97936.jpg)

<details>
<summary>text_image</summary>
