# B.2 周期为 $2 \pi$ 的函数展开成傅里叶级数

B.1节介绍了三角函数的正交性,本节将利用这一性质推导周期为 $2\pi$ 的函数展开为傅里叶级数。式(B.2.1)描述了周期 $T=2\pi$ 的函数表达式:

$$f _ {T} (x) = f _ {T} (x + 2 \pi) \tag {B.2.1}$$

$f_{T}(x)$ 可以用三角级数表达为

$$f _ {T} (x) = \frac {a _ {0}}{2} + \sum_ {n = 1} ^ {\infty} \left(a _ {n} \cos n x + b _ {n} \sin n x\right) \tag {B.2.2}$$

式(B.2.2)是在大部分教科书中出现的傅里叶级数展开表达式,但是它很不容易理解,尤其是 $\frac{a_{0}}{2}$ 项在式子中显得很不和谐。这也是影响很多读者理解傅里叶级数的主要障碍。

从直观上看, 观察图 B.2.1。当从三角函数系中选择几个元素, 让它们分别乘以一个系数后再叠加在一起, 就会形成一个以 $2 \pi$ 为周期的函数。

![](image/55701c821046ae465b1e15bb1676a1fc7ae363bdb9af5cf259b286da87ba9153.jpg)

<details>
<summary>text_image</summary>

f_T(x)
sinx
0.5cos2x
0.3cos4x
O
0.2cos3x
x
f_T(x)
sinx+0.5cos2x+0.2sin3x+0.3cos4x
O
x
</details>

图 B.2.1 不同周期与振幅的三角函数叠加形成新的周期函数

这一现象可以拓展为：将式(B.1.7)三角函数系中的所有元素乘以特定的系数后叠加，就可以构成任意周期为 $2\pi$ 的函数 $f_{T}(x)$ 。用数学语言表达为

$$f _ {T} (x) = \sum_ {n = 0} ^ {\infty} a _ {n} ^ {*} \cos n x + \sum_ {n = 0} ^ {\infty} b _ {n} \sin n x \tag {B.2.3}$$

其中， $a_{n}^{*}$ 和 $b_{n}$ 是常数，代表不同频率（周期）的振幅。下面来求解 $a_{n}^{*}$ 和 $b_{n}$ 的表达式。

将式(B.2.3)中 n=0 的项单独列出来, 得到

$$
\begin{array}{l} f _ {T} (x) = a _ {0} ^ {*} \cos 0 + b _ {0} \sin 0 + \sum_ {n = 1} ^ {\infty} \left(a _ {0} ^ {*} \cos n x + b _ {n} \sin n x\right) \\ = a _ {0} ^ {*} + \sum_ {n = 1} ^ {\infty} (a _ {n} ^ {*} \cos n x + b _ {n} \sin n x) \tag {B.2.4} \\ \end{array}
$$

此时比较式(B.2.4)和式(B.2.2)，会发现只有第一项 $a_0^*$ 不太一样。这将在后面的推导中解释。

首先求 $a_0^*$ ，对式(B.2.4)等号两边从 $-\pi$ 到 $\pi$ 做定积分，得到

$$
\begin{array}{l} \int_ {- \pi} ^ {\pi} f _ {T} (x) \mathrm{d} x = \int_ {- \pi} ^ {\pi} a _ {0} ^ {*} \mathrm{d} x + \int_ {- \pi} ^ {\pi} \sum_ {n = 1} ^ {\infty} \left(a _ {n} ^ {*} \cos n x + b _ {n} \sin n x\right) \mathrm{d} x \\ = \int_ {- \pi} ^ {\pi} a _ {0} ^ {*} \mathrm{d} x + \sum_ {n = 1} ^ {\infty} a _ {n} ^ {*} \int_ {- \pi} ^ {\pi} \cos n x \mathrm{d} x + \sum_ {n = 1} ^ {\infty} b _ {n} \int_ {- \pi} ^ {\pi} \sin n x \mathrm{d} x \tag {B.2.5} \\ \end{array}
$$

根据三角函数的正交性，等号右边的 $\sum_{n=1}^{\infty} a_n^* \int_{-\pi}^{\pi} \cos nx \, \mathrm{d}x + \sum_{n=1}^{\infty} b_n \int_{-\pi}^{\pi} \sin nx \, \mathrm{d}x = 0$ 。可得

$$
\begin{array}{l} \int_ {- \pi} ^ {\pi} f _ {T} (x) \mathrm{d} x = \int_ {- \pi} ^ {\pi} a _ {0} ^ {*} \mathrm{d} x \Rightarrow \int_ {- \pi} ^ {\pi} f _ {T} (x) \mathrm{d} x = 2 \pi a _ {0} ^ {*} \\ \Rightarrow a _ {0} ^ {*} = \frac {1}{2 \pi} \int_ {- \pi} ^ {\pi} f _ {T} (x) \mathrm{d} x \tag {B.2.6} \\ \end{array}
$$

下面求 $a_{n}^{*}$ ，令式(B.2.4)等号两边乘以 $\cos mx$ 后再从一π到π做定积分，得到
