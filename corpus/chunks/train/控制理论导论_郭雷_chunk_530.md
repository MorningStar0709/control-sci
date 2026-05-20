$$H (x _ {1}, x _ {2}, u, \psi_ {1}, \psi_ {2}) = - 1 + \psi_ {1} x _ {2} + \psi_ {2} u.$$

由此知， $\forall x_0\in \mathbb{R}^2$ ，把 $x_0$ 控制到 $x(t_f) = 0$ 的快速控制函数 $u^{*}(t)$ 有下列形式：

$$u ^ {*} (t) = \operatorname{sign} \psi_ {2} (t),$$

其中 $\psi^{\mathrm{T}}(t) = [\psi_{1}(t),\psi (t)]$ 满足

$$
\frac {\mathrm{d}}{\mathrm{d} t} \left[ \begin{array}{l} \psi_ {1} \\ \psi_ {2} \end{array} \right] = \left[ \begin{array}{c c} 0 & 0 \\ - 1 & 0 \end{array} \right] \left[ \begin{array}{l} \psi_ {1} \\ \psi_ {2} \end{array} \right],
\psi_ {1} (t _ {f}) = \mu_ {1}, \quad \psi_ {2} (t _ {f}) = \mu_ {2},
$$

$\mu_{1}, \mu_{2}$ 为待定常数，由此可得

$$\psi_ {1} (t) = \mu_ {1},\psi_ {2} (t) = \mu_ {1} (t _ {f} - t) + \mu_ {2}.$$

由于 $\psi_{2}(t)$ 是 $t$ 的线性函数， $\psi_{2}(t)$ 最多只有一个零点，即 $u^{*}(t)$ 最多只开关一次（从定理7.2.5可直接得到此结论). 因此

$$
u ^ {*} (t) = \left\{ \begin{array}{l l} {1,} & {\text {当} \mu_ {1} (t _ {f} ^ {*} - t) + \mu_ {2} > 0 \text {时},} \\ {- 1,} & {\text {当} \mu_ {1} (t _ {f} ^ {*} - t) + \mu_ {2} <   0 \text {时},} \end{array} \right.
$$

且 $u^{*}(t)$ ，只能是下列四种形式之一：

$$u ^ {*} (t) \equiv 1, \quad t \in [ 0, t _ {f} ^ {*} ];u ^ {*} (t) \equiv - 1, \quad t \in [ 0, t _ {f} ^ {*} ];$$

$u^{*}(t)$ 从 1 转换到 -1;

$u^{*}(t)$ 从-1转换到1.

注意到，对于二阶线性定常系统，当求得系统的开关曲线后，就不难求得其快速控制综合函数.

(3) 用时间反推法求开关曲线.

相应于 $u^{*}(t) = 1$ 和 $u^{*}(t) = -1$ 的状态方程

$$
\left\{ \begin{array}{l l} {\dot {x} _ {1} = x _ {2},} \\ {\dot {x} _ {2} = 1,} \end{array} \right. \qquad \text {和} \qquad \left\{ \begin{array}{l l} {\dot {x} _ {1} = x _ {2},} \\ {\dot {x} _ {2} = - 1,} \end{array} \right.
$$

分别简称为正系统和负系统.

正系统和负系统在 $t = 0$ 时刻以 $(x_{10}, x_{20})$ 为初态的轨线方程分别为

$$
\left\{ \begin{array}{l} x _ {1} (t) = \frac {1}{2} t ^ {2} + x _ {2 0} t + x _ {1 0}, \\ x _ {2} (t) = t + x _ {2 0}, \end{array} \right.
$$

和

$$
\left\{ \begin{array}{l} x _ {1} (t) = - \frac {1}{2} t ^ {2} + x _ {2 0} t + x _ {1 0}, \\ x _ {2} (t) = - t + x _ {2 0}. \end{array} \right.
$$

正系统和负系统的轨线示意图如图 7.2.3 和图 7.2.4.

![](image/b3cfc9afdfa225a4168a46ccc0ee097792087f5aac15a799a5aa4f72a92e6719.jpg)

<details>
<summary>text_image</summary>

x₂
0
x₁
</details>

图7.2.3 正轨线图

![](image/1e9bd2b87d05b5ab9778e486c7506f3da4c7d73878a1c3d1d491e36c9dca92ce.jpg)

<details>
<summary>text_image</summary>

x₂
0
x₁
</details>

图7.2.4 负轨线图

记半轨线 $\Gamma^{+}: x_{1} = \frac{1}{2} x_{2}^{2}$ 和 $\Gamma^{-}: x_{1} = -\frac{1}{2} x_{2}^{2}$ . 容易看出, 对于正系统, 只有位于 $\Gamma^{+}$ 上的点才能在某个大于零的时刻达到原点, 而对于负系统, 只有位于 $\Gamma^{-}$ 上的点才能在某大于零的时刻达到原点. 如图 7.2.5 所示.
