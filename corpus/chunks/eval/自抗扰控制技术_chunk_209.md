来用. 只用 $B_{0}$ 来近似 $\pmb{B}(t)$ 所作的仿真结果如图6.1.6所示. 设定轨迹的跟踪是很好的. 这里 $\left[ \begin{array}{c} f_{1} \\ f_{2} \end{array} \right]$ 和 $\left[ \begin{array}{c} z_{13} \\ z_{23} \end{array} \right]$ 并不一致, 这是由于 $\left[ \begin{array}{c} z_{13} \\ z_{23} \end{array} \right]$ 估计的并不是 $\left[ \begin{array}{c} f_{1} \\ f_{2} \end{array} \right]$ , 而是 $\left[ \begin{array}{c} f_{1} \\ f_{2} \end{array} \right] + (B(t) - B_{0})\left[ \begin{array}{c} u_{1} \\ u_{2} \end{array} \right]$ . 因为我们把原问题转化成如下形式来处理的

$$
\left[ \begin{array}{l} \ddot {x} _ {1} \\ \ddot {x} _ {2} \end{array} \right] = \left[ \begin{array}{l} f _ {1} \\ f _ {2} \end{array} \right] + \boldsymbol {B} (t) \left[ \begin{array}{l} u _ {1} \\ u _ {2} \end{array} \right] = \left(\left[ \begin{array}{l} f _ {1} \\ f _ {2} \end{array} \right] + (\boldsymbol {B} (t) - \boldsymbol {B} _ {0}) \left[ \begin{array}{l} u _ {1} \\ u _ {2} \end{array} \right]\right) + \boldsymbol {B} _ {0} \left[ \begin{array}{l} u _ {1} \\ u _ {2} \end{array} \right] \tag {6.1.18}
$$

因此图6.1.6中的 $f_{i},z_{i3}$ 之间的误差就是 $(\pmb {B}(t) - \pmb{B}_0)\left[ \begin{array}{c}u_1\\ u_2 \end{array} \right]$ 部分．大量仿真研究表明 $\pmb {B}(t),\pmb{B}_0$ 之间误差不能太大，相对误差能小到 $30\%$ 以下，自抗扰控制器是能够控制好的.

![](image/33360e7b49110891d7fe63f5b509a404d1b248f17a710ab7dc3a0fa24261c8fc.jpg)

<details>
<summary>line</summary>

| x | y' (ω) | f(x) |
| --- | --- | --- |
| 0 | 1 | 4 |
| 5 | -1 | 2 |
| 10 | 0 | 6 |
| 15 | 1 | 4 |
| 20 | 0 | 2 |
</details>

![](image/a37af46922af31952bfd9803a9b59d136e035a6e8de2670dbbffb94cde7e7491.jpg)

<details>
<summary>line</summary>

| x | V'₂₃ | V₂ | I₂ | I₂'₂₃ |
| --- | --- | --- | --- | --- |
| 0 | 2.0 | 2.0 | 3.0 | 3.0 |
| 5 | -2.0 | -2.0 | 1.0 | 1.0 |
| 10 | 2.0 | 2.0 | 4.0 | 4.0 |
| 15 | -2.0 | -2.0 | 1.0 | 1.0 |
| 20 | 2.0 | 2.0 | 3.0 | 3.0 |
</details>

图6.1.6

上述对象是时变、非线性、开环不稳定的系统，在上述三个仿真中用的是同一个控制器参数.

更一般地，设有控制系统

$$\ddot {X} = F (X, \dot {X}, W, U), X \in R ^ {m}, U \in R ^ {m} \tag {6.1.19}$$

X 的每个分量都是被控量．今记 $F_{0}(X,X,W,U)=F(X,X,W,U)$ -U,那么系统变成

$$\ddot {X} = F _ {0} (X, \dot {X}, W, U) + U \tag {6.1.20}$$

如果 $B = \frac{\partial F}{\partial U}$ 比较接近单位矩阵 I，那么在 X 和 U 之间并列 m 个自抗扰控制器可以实现解耦控制，如果 $B = \frac{\partial F}{\partial U}$ 与单位矩阵 I 的差别比较大，那么可以找一个比较接近 B 的可逆矩阵 $B_{0}$ 把系统变成

$$\ddot {X} = F (X, \dot {X}, W, U) - B _ {0} U + B _ {0} UF _ {0} (X, \dot {X}, W, U) = F (X, \dot {X}, W, U) - B _ {0} U\ddot {X} = F _ {0} (X, \dot {X}, W, U) + B _ {0} U \tag {6.1.21}$$

然后按前述方法对这个系统进行解耦控制.

这样用自抗扰控制技术很容易实现很多耦合系统的解耦控制问题.
