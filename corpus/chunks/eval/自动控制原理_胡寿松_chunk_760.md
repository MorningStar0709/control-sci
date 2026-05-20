# (2) 连续泛函与线性泛函

如果式(10-13)满足下列线性条件：

1) $J[x_1 + x_2] = J[x_1] + J[x_2], \quad \forall x_1, x_2 \in \mathbf{R}^n$ (10-14)

2) $J[\alpha x] = \alpha J[x],\quad \forall x\in \mathbf{R}^n$

则称 $J[x]$ : $R^{n} \rightarrow R$ 为线性泛函算子, 其中 $\alpha$ 为标量。

为了讨论泛函 $J[x]$ 的性质和运算， $J[x]$ 需为连续的，其定义如下：设 $J[x]$ 是线性赋范空间$\mathbf{R}^n$ 中子集 $D(J)$ 到实数集 $\mathbf{R}$ 上的泛函算子， $D(J)$ 为泛函 $J[x]$ 的定义域。若对于收敛于点 $x_0$ 的点列 $x_n$ ，其中 $x_0, x_n \in D(J)$ ，均有

$$\lim _ {n \rightarrow \infty} J [ \boldsymbol {x} _ {n} ] = J [ \boldsymbol {x} _ {0} ] \tag {10-15}$$

则称泛函 $J$ 在 $\pmb{x}_0$ 处连续；若 $J[\pmb{x}]$ 在子集 $D(J)$ 上的每一点都连续，则称 $J[\pmb{x}]$ 在 $D(J)$ 中连续。

由于泛函 $J[x]$ 定义在线性赋范空间上，因此对于线性泛函 $J[x]$ ，若

$$\| x _ {n} - x \| \rightarrow 0 (n \rightarrow \infty), \quad \forall x _ {n}, x \in \mathbf {R} ^ {n}$$

时，必有

$$\lim _ {n \rightarrow \infty} J [ x _ {n} ] = J [ x ]$$

则线性泛函 $J[x]$ 是连续的，称 $J[x]$ 为线性连续泛函。

在用变分法求解最优控制问题时,要求指标泛函 $J[x]$ 为线性连续泛函,以使得 $J[x]$ 在任一点上的值均可用该点附近的泛函值任意逼近。应当指出,在有限维线性空间上,任何线性泛函都是连续的。
