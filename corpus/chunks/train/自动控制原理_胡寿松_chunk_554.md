# (1) 死区饱和非线性环节

将正弦输入信号 $x(t)$ 、非线性特性 $y(x)$ 和输出信号 $y(t)$ 的坐标按图8-37所示方式和位置旋转，由非线性特性的区间端点 $(\Delta, y(\Delta))$ 和 $(a, y(a))$ 可以确定 $y(t)$ 关于 $\omega t$ 的区间端点 $\psi_1$ 和 $\psi_2$ 。死区饱和特性及其正弦响应如图8-37所示。输出 $y(t)$ 的数学表达式为

![](image/5ca3cc3c9f5b5c08750129ed1dae1840a288ae4f2b935a6238f75a28580103f9.jpg)

<details>
<summary>text_image</summary>

y
K
0
Δ
a
x
y
0
φ₁
ψ₂
π
2π
ωt
A
x
0
ψ₁
ψ₂
π
2π
ωt
</details>

图 8-37 死区饱和特性和正弦响应曲线

$$
y (t) = \left\{ \begin{array}{l l} 0, & 0 \leqslant \omega t \leqslant \psi_ {1} \\ K (A \sin \omega t - \Delta), & \psi_ {1} <   \omega t \leqslant \psi_ {2} \\ K (a - \Delta), & \psi_ {2} <   \omega t \leqslant \frac {\pi}{2} \end{array} \right. \tag {8-67}
$$

如图 8-37 所示, 由非线性特性的转折点 $\Delta$ 和 a, 可确定 $y(t)$ 产生不同线性变化的区间端点为

$$\psi_ {1} = \arcsin \frac {\Delta}{A} \tag {8-68}\psi_ {2} = \arcsin \frac {a}{A} \tag {8-69}$$

由于 $y(t)$ 为奇函数，所以 $A_0 = 0, A_1 = 0$ ，而 $y(t)$ 又为半周期内对称，故
