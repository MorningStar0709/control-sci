# 10.1 多项式矩阵描述

描述的表达形式 我们从讨论一个具体电路入手来引出系统的多项式矩阵描述。所

讨论的电路如图 10.1 所示,选定两个回路电流 $\zeta_{1}$ 和 $\zeta_{2}$ 作为部分状态变量, u 为输入变量, y 为输出变量。

根据电路的有关定律，先列出两个回路的回路方程，并表为拉普拉斯变换后的形式：

![](image/f147ee3c8645b647733c1caf1def8133d19aa395f1d12d1f89d322156ef16c8e.jpg)

<details>
<summary>text_image</summary>

u(t)
+
-
3H
1F
ζ₁
3F ζ₂
2H
y
+
2Ω
1Ω
</details>

图10.1 一个电路

$$
\left\{ \begin{array}{l} \left(3 s + 2 + \frac {1}{3 s}\right) \hat {\xi} _ {1} (s) - \frac {1}{3 s} \hat {\xi} _ {2} (s) = \hat {u} (s) \\ - \frac {1}{3 s} \hat {\xi} _ {1} (s) + \left(2 s + 1 + \frac {1}{3 s} + \frac {1}{s}\right) \hat {\xi} _ {2} (s) = 0 \end{array} \right. \tag {10.1}
$$

将上式化简,可导出

$$
\left\{ \begin{array}{l} (9 s ^ {2} + 6 s + 1) \hat {\zeta} _ {1} (s) - \hat {\zeta} _ {2} (s) = 3 s \hat {u} (s) \\ - \hat {\zeta} _ {1} (s) + (6 s ^ {2} + 3 s + 4) \hat {\zeta} _ {2} (s) = ^ {\flat} 0 \end{array} \right. \tag {10.2}
$$

再将其表为向量方程的形式,则为

$$
\left[ \begin{array}{c c} 9 s ^ {2} + 6 s + 1 & - 1 \\ - 1 & 6 s ^ {2} + 3 s + 4 \end{array} \right] \left[ \begin{array}{l} \hat {\zeta} _ {1} (s) \\ \hat {\zeta} _ {2} (s) \end{array} \right] = \left[ \begin{array}{l} 3 s \\ 0 \end{array} \right] \hat {u} (s) \tag {10.3}
$$

而电路的输出方程为

$$\hat {y} (s) = 2 s \hat {\xi} _ {2} (s) \tag {10.4}$$

将其表为向量方程的形式,则是

$$
\hat {y} (s) = [ 0 2 s ] \left[ \begin{array}{l} \hat {\zeta} _ {1} (s) \\ \hat {\zeta} _ {2} (s) \end{array} \right] + 0 \hat {u} (s) \tag {10.5}
$$

不难看出，描述此电路的状态和输出行为的方程(10.3)和(10.5)中，每个系数矩阵都有着

多项式矩阵的形式,因此称它们为给定电路的一个多项式矩阵描述。

现在, 我们把讨论推广到一般的情况, 来考虑任意一个多输入-多输出线性定常系统。设系统输入 u 为 p 维的, 输出 y 为 q 维的, 而描述系统内部运动状态的广义状态 $\zeta$ 为 m 维的, 那么系统的动态过程就可以用如下的一个向量方程来描述:

$$
\left\{ \begin{array}{c} P (s) \hat {\zeta} (s) = Q (s) \hat {\boldsymbol {u}} (s) \\ \hat {\boldsymbol {y}} (s) = R (s) \hat {\zeta} (s) + W (s) \hat {\boldsymbol {u}} (s) \end{array} \right. \tag {10.6}
$$

其中， $P(s)$ 为 $m \times m$ 多项式矩阵， $Q(s)$ 、 $R(s)$ 和 $W(s)$ 分别为 $m \times p$ 、 $q \times m$ 和 $q \times p$ 的多项式矩阵。并且，称(10.6)为系统的多项式矩阵描述，简称为 PMD，它是英文术语 Polynomial matrix discription 的简写。

进一步, 如果在(10.6)的各系数矩阵中, 用微分算子 $p \triangle d / dt$ 来代替复数变量 $s$ , 那么上述描述就化成了时间域的多项式矩阵描述:

$$
\left\{ \begin{array}{l} P (p) \zeta (t) = Q (p) \boldsymbol {u} (t) \\ \boldsymbol {y} (t) = R (p) \zeta (t) + W (p) \boldsymbol {u} (t) \end{array} \right. \tag {10.7}
$$

此时，(10.7)所示的描述不但适用于表征线性定常系统，而且也适用于线性时变系统。并且，也将其称为微分算子描述。
