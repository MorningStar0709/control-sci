# B. 1 三角函数的正交性

首先讨论三角函数的正交性,在几何概念中正交即垂直。如图 B.1.1 所示的向量 a 和 b 互相垂直,若使用解析法来表达,它们的内积(点积)为 0 , 即

$$\boldsymbol {a} \cdot \boldsymbol {b} = | \boldsymbol {a} | | \boldsymbol {b} | \cos \varphi = 0 \tag {B.1.1}$$

图 B.1.1(a) 中的两个垂直二维列向量为 $a = [2, 1]^{\mathrm{T}}$ , $b = [-1, 2]^{\mathrm{T}}$ , 可得

$$
\boldsymbol {a} \cdot \boldsymbol {b} = [ 2 \quad 1 ] \left[ \begin{array}{c} - 1 \\ 2 \end{array} \right] = 2 \times (- 1) + 1 \times 2 = 0 \tag {B.1.2}
$$

图 B.1.1(b) 中的两个垂直三维向量为 $a = [1, 2, 3]^{T}$ , $b = [1, -2, 1]^{T}$ , 可得

$$
\boldsymbol {a} \cdot \boldsymbol {b} = \left[ \begin{array}{l l l} 1 & 2 & 3 \end{array} \right] \left[ \begin{array}{c} 1 \\ - 2 \\ 1 \end{array} \right] = 1 \times 1 + 2 \times (- 2) + 3 \times 1 = 0 \tag {B.1.3}
$$

![](image/12ce460b6d85e91a93e1ca1a46d72738239f3ffe2c8e4a4be4cfdd99e725408b.jpg)

<details>
<summary>text_image</summary>

x₂
b
2
1
a
-1
0
2
x₁
</details>

(a) 二维向量

![](image/7166e78ffbc0d2d2f0c713be8444966392d65cad1399bfc97ddbba5bb032e4d8.jpg)

<details>
<summary>text_image</summary>

x₃
3
a
1
b
-2
0
2
x₂
1
x₁
</details>

(b) 三维向量  
图 B.1.1 向量正交性举例

将上述概念推广到更高的维度,即

$$\boldsymbol {a} = \left[ a _ {1}, a _ {2}, a _ {3}, \dots , a _ {n} \right] ^ {\mathrm{T}} \tag {B.1.4a}\boldsymbol {b} = \left[ b _ {1}, b _ {2}, b _ {3}, \dots , b _ {n} \right] ^ {\mathrm{T}} \tag {B.1.4b}$$

那么， $a$ 与 $\pmb{b}$ 正交意味着

$$\boldsymbol {a} \cdot \boldsymbol {b} = \sum_ {i = 1} ^ {n} a _ {i} b _ {i} = 0 \tag {B.1.5}$$

进一步将正交的概念推广到连续函数上,在某一区间 $x \in [a, b]$ , 如果函数 $f(x)$ 和 $g(x)$ 正交, 则

$$\int_ {a} ^ {b} f (x) g (x) \mathrm{d} x = 0 \tag {B.1.6}$$

式(B.1.6)即为函数正交的定义。下面讨论三角函数系：

$$\{1, \sin x, \cos x, \sin 2 x, \cos 2 x, \sin 3 x, \cos 3 x, \dots , \sin n x, \cos n x, \dots \} \tag {B.1.7}$$

式(B.1.7)中的“1”可以理解为 $\cos 0x$ 。因为 $\sin 0x = 0$ ，所以没有写在其中。三角函数的正交性是指，在式(B.1.7)中任何两个不同函数的乘积在区间 $x \in [-\pi, \pi]$ 内正交，例如

$$\int_ {- \pi} ^ {\pi} \sin n x \cos n x \mathrm{d} x = 0 \tag {B.1.8a}\int_ {- \pi} ^ {\pi} \cos n x \cos m x d x = 0 \quad n \neq m \tag {B.1.8b}\int_ {- \pi} ^ {\pi} \sin m x \mathrm{d} x = \int_ {- \pi} ^ {\pi} 1 \times \sin m x \mathrm{d} x = 0 \tag {B.1.8c}$$

读者可以利用三角函数积化和差的方式进行验证。注意式(B.1.8b)，只有当 $n \neq m$ 时， $\cos nx$ 和 $\cos mx$ 才是三角函数系中两个不同的函数，才在区间 $x \in [-\pi, \pi]$ 内正交。否则，当 $n = m$ 时

$$
\begin{array}{l} \int_ {- \pi} ^ {\pi} \cos n x \cos n x d x = \int_ {- \pi} ^ {\pi} \frac {1}{2} (1 + \cos 2 n x) d x \\ = \frac {1}{2} \left(\int_ {- \pi} ^ {\pi} 1 \mathrm{d} x + \int_ {- \pi} ^ {\pi} \cos 2 n x \mathrm{d} x\right) = \frac {1}{2} \int_ {- \pi} ^ {\pi} 1 \mathrm{d} x \\ = \frac {1}{2} x \left| _ {- \pi} ^ {\pi} = \pi \right. \tag {B.1.9} \\ \end{array}
$$
