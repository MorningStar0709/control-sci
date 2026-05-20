# 例 2.9 含电流源的电路方程

确定图 2.26 所示电路的微分方程。选择电容电压和电感电流作为未知量。

解答。选取节点4作为参考点，且节点1、2处的电压 $v_{1}$ 、 $v_{2}$ 以及流过电感的电流 $i_{L}$ 作为未知量。我们来确定KCL关系。

节点1的KCL方程为

$$i (t) = i _ {3} + i _ {1} + i _ {\mathrm{L}} \tag {2.36}$$

节点 2 的 KCL 方程为

$$i _ {\mathrm{L}} = i _ {2} + i _ {4} \tag {2.37}$$

另外，由图2.24，我们可以看出：

$$i _ {3} = \frac {v _ {1}}{R _ {1}} \tag {2.38}i _ {1} = C _ {1} \frac {\mathrm{d} v _ {1}}{\mathrm{d} t} \tag {2.39}i _ {2} = C _ {2} \frac {\mathrm{d} v _ {2}}{\mathrm{d} t} \tag {2.40}i _ {4} = \frac {v _ {2}}{R _ {2}} \tag {2.41}v _ {1} - v _ {2} = L \frac {\mathrm{d} i _ {\mathrm{L}}}{\mathrm{d} t} \tag {2.42}$$

化简为含有三个未知量的三个微分方程分别为

$$i (t) = \frac {v _ {1}}{R _ {1}} + C _ {1} \frac {\mathrm{d} v _ {1}}{\mathrm{d} t} + i _ {\mathrm{L}} \tag {2.43}$$

![](image/9fc756cb16e7aa20f2c0f1b165640de5fe2f687a773b047318a6be7d5ba1a849.jpg)

<details>
<summary>text_image</summary>

C₂
+
-
①
R₁
②
R₂
③
+
vᵢ
~
-
v₁
C₁
+
-
v₂
v₃
vₒ
④
</details>

图 2.25 桥式 T 形电路

![](image/80c981a444f908773bc3cb3fd6ce0a20ceec74c032ec5bd823c881a3a5d318a3.jpg)

<details>
<summary>text_image</summary>

i(t)
↑
i3
R1
C1
① v1 L ② v2
i1 iL i2 i4
C2 R2
④ v=0
</details>

图2.26 例2.9的电路

$$i _ {\mathrm{L}} = C _ {2} \frac {\mathrm{d} v _ {2}}{\mathrm{d} t} + \frac {v _ {2}}{R _ {2}} \tag {2.44}v _ {1} = L \frac {\mathrm{d} i _ {\mathrm{L}}}{\mathrm{d} t} + v _ {2} \tag {2.45}$$

基尔霍夫定律也可以应用在含有运算放大器的电路中。运算放大器的简化电路如图2.27a所示，元件符号如图2.27b所示。如果图中正端未画出，则假定它是连到接地端，即 $v_{+}=0$ ，简化符号如图2.27c所示。在控制电路中，通常认为运算放大器是理想的，也就是 $R_{1}=\infty$ ， $R_{0}=0$ 且 $A=\infty$ 。理想运算放大器的方程相当简单，为

$$i _ {+} = i _ {-} = 0 \tag {2.46}v _ {+} - v _ {-} = 0 \tag {2.47}$$

![](image/35ddeab3071d33f0eda891a82f9569deadf8c9beadea0742002a835ec9955eda.jpg)

<details>
<summary>text_image</summary>

i₋
v₋ ○─┐
          │
          │
          │
          │
          │
          │
          │
          │
          │
          │
          │
          │
          │
          │
          │
          │
          │
          │
          │
          │
          │
          │
          │
          │
          │
          │
          │
          │
          │
          │
          │
          │
          │
          │

R₁
v₊ ○─┘

R₀     i₀ →○
      │
      │
      │
      │
      │
      │
      │
      │
      │
      │
      │
      │
      │
      │
      │
      │
      │
      │
      │
      │
      │
      │
      │
      │
      │
      │
      │
      │
      │
      │
      │
      │
      │
      │

+
-
v₀ = A(v₊ - v₋)
</details>

a）运算放大器简化电路图

![](image/ae153c7ccf24b9f498a64ddbca88c34254d110395e1374b856bb3284be7db4e8.jpg)

<details>
<summary>text_image</summary>

i₋
v₋ ○→
      i₊
v₊ ○→
      +
      vₒ
</details>

b）运算放大器示意符号  
![](image/16d230a4dac96fb2aaa55cefdbb3124f3e26aa0b72d3f6d2f42c0aa3e89ad7fd.jpg)

<details>
<summary>text_image</summary>

v₋ ○———○ v₀
</details>

c) $v_{+}=0$ 时的简化符号  
图 2.27

假定放大器的增益足够大，使得输出电压 $v_{0}$ 取任意值都满足这两个方程。当然，实际放大器只近似地满足这两个方程，除非特殊声明，一般我们都假定所有运算放大器是理想的。本章后面列出的几个习题为实际的模型。
