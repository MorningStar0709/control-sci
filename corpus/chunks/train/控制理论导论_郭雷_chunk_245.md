$$
\begin{array}{l} \left(\phi_ {t} ^ {X}\right) ^ {*} \omega \left(\phi_ {t} ^ {X} (x)\right) = (\omega (x) + t \left(J _ {\omega} X\right) ^ {\mathrm{T}} + O \left(t ^ {2}\right)) \left(I + t J _ {X} + O \left(t ^ {2}\right)\right) \\ = \omega (x) + t \left(J _ {\omega} X\right) ^ {T} + t \omega (x) J _ {X} + O \left(t ^ {2}\right), \\ \end{array}
$$

这里转置是由于通常作为约定将余向量场表示为行向量。将上式代入式 (3.7.10)，即为式 (3.7.11).

Lie 导数 $\operatorname{ad}_X Y$ 的几何意义是向量场 $Y$ 沿 $X$ 的积分曲线的变化量。图3.7.1给出一个描述。对于函数 $h$ 或余向量场 $\omega$ ，相应的Lie导数 $L_X(f)$ 及 $L_X(\omega)$ 具有类似的几何意义。

![](image/034843e9acf032eb170c84f5674b08eb28810e5319fe628164a8c505f18c291b.jpg)

<details>
<summary>text_image</summary>

x
y(x)
ΔY
(e_i^X)_Y(z)
y(z)
x(t)
z = e_i^X(x)
o
t
</details>

图3.7.1 Lie导数 $\mathrm{ad}_X\mathbf{Y}$

下面是一些有用的公式：

命题3.7.4 设 $p, q, h \in C^r(M), X, Y \in V(M), \omega \in V^*(M)$ . 那么：

(1) (Leibniz 等式)

$$L _ {X} \langle \omega , Y \rangle = \langle L _ {X} \omega , Y \rangle + \langle \omega , L _ {X} Y \rangle ; \tag {3.7.12}$$

(2)

$$\dot {L} _ {p X} (q \omega) = p q L _ {X} (\omega) + p L _ {X} (q) \omega + q \langle \omega , X \rangle \mathrm{d} h; \tag {3.7.13}$$

(3) 如果 $\omega = \mathrm{d}h$ ，则

$$L _ {X} (\omega) = \mathrm{d} \langle \omega , X \rangle . \tag {3.7.14}$$

证明 (1) 首先我们证明一个公式，它本身也是有用的

$$
\begin{array}{l} \mathrm{d} \langle \omega , X \rangle = \mathrm{d} \sum_ {i = 1} ^ {n} \omega_ {i} X _ {i} = \sum_ {i = 1} ^ {n} \left(\sum_ {j = 1} ^ {n} \frac {\partial \omega_ {i}}{\partial x _ {j}}\right) x _ {i} + \sum_ {i = 1} ^ {n} \left(\sum_ {j = 1} ^ {n} \frac {\partial X _ {i}}{\partial x _ {j}}\right) \omega_ {i} \\ = X ^ {\mathrm{T}} \frac {\partial \omega}{\partial x} + \omega \frac {\partial X}{\partial x}. \tag {3.7.15} \\ \end{array}
$$

将它用于式 (3.7.12) 得到

$$\mathrm{LHS} = \langle \mathrm{d} \langle \omega , Y \rangle , X \rangle = \left(Y ^ {\mathrm{T}} \frac {\partial \omega}{\partial x} + \omega \frac {\partial Y}{\partial x}\right) X = Y ^ {\mathrm{T}} \frac {\partial \omega}{\partial x} X + \omega \frac {\partial Y}{\partial x} X.\mathrm{RHS} = \left(X ^ {\mathrm{T}} \left(\frac {\partial \omega}{\partial x}\right) ^ {\mathrm{T}} + \omega \frac {\partial X}{\partial x}\right) Y + \omega \frac {\partial Y}{\partial x} X ^ {\prime} - \omega \frac {\partial X}{\partial x} Y.$$

因此 LHS=RHS.

(2)
