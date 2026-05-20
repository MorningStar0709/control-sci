$$
\begin{array}{l} D ^ {2} x \ltimes D x = \left[ \begin{array}{c c} \sum_ {s = 1} ^ {n} \frac {\partial^ {2} x _ {1}}{\partial y _ {s} \partial y _ {1}} \frac {\partial x _ {s}}{\partial y _ {1}} & \dots \sum_ {s = 1} ^ {n} \frac {\partial^ {2} x _ {1}}{\partial y _ {s} \partial y _ {n}} \frac {\partial x _ {s}}{\partial y _ {1}} \\ & \vdots \\ \sum_ {s = 1} ^ {n} \frac {\partial^ {2} x _ {n}}{\partial y _ {s} \partial y _ {1}} \frac {\partial x _ {s}}{\partial y _ {1}} & \dots \sum_ {s = 1} ^ {n} \frac {\partial^ {2} x _ {n}}{\partial y _ {s} \partial y _ {n}} \frac {\partial x _ {s}}{\partial y _ {1}} \end{array} \right. \\ \left. \begin{array}{c} \dots \sum_ {s = 1} ^ {n} \frac {\partial^ {2} x _ {1}}{\partial y _ {s} \partial y _ {1}} \frac {\partial x _ {s}}{\partial y _ {n}} \dots \sum_ {s = 1} ^ {n} \frac {\partial^ {2} x _ {1}}{\partial y _ {s} \partial y _ {n}} \frac {\partial x _ {s}}{\partial y _ {n}} \\ \vdots \\ \dots \sum_ {s = 1} ^ {n} \frac {\partial^ {2} x _ {n}}{\partial y _ {s} \partial y _ {1}} \frac {\partial x _ {s}}{\partial y _ {n}} \dots \sum_ {s = 1} ^ {n} \frac {\partial^ {2} x _ {n}}{\partial y _ {s} \partial y _ {n}} \frac {\partial x _ {s}}{\partial y _ {n}} \end{array} \right] \\ \end{array}
$$

用 $(ij)$ 记它的列，那么它的 $(ij)$ 列为式(3.11.10)右边的第一项.

其次，记 $Dx$ 的第 $i-$ 行为 $J_{i}$ ，那么

$$\Gamma \ltimes D x = (\Gamma \ltimes J _ {1}, \Gamma \ltimes J _ {2}, \dots , \Gamma \ltimes J _ {n}).$$

因为 $I \otimes Dx = \text{diag}(J, \cdots, J)$ ，故

$$
\begin{array}{l} \Gamma \ltimes D x \ltimes (I \otimes D x) \\ = \left(\Gamma \ltimes J _ {1} \ltimes J _ {1}, \dots , \Gamma \ltimes J _ {1} \ltimes J _ {n}, \dots , \Gamma \ltimes J _ {n} \ltimes J _ {1}, \dots , \Gamma \ltimes J _ {n} \ltimes J _ {n}\right). \\ \end{array}
$$

显然上式的 $(ij)$ 列是式(3.11.10)右边的第二项.

设 $M$ 为一Riemann流形，其Riemann距离由 $G = (g_{ij})_{n\times n}$ 决定。Riemann几何基本定理说在 $M$ 上存在唯一的Riemann联络[1]，并且Christoffel符号由

$$\gamma_ {i j} ^ {k} = \frac {1}{2} \sum_ {s = 1} ^ {n} g ^ {k s} \left(\frac {\partial g _ {s i}}{\partial x _ {j}} - \frac {\partial g _ {i j}}{\partial x _ {s}} + \frac {\partial g _ {j s}}{\partial x _ {i}}\right), \tag {3.11.12}$$

决定，这里 $g^{ij}$ 是 $G^{-1}$ 的 $(i,j)$ 元.

我们知道 [4] 有以下命题：

命题3.11.2 在Riemann流形上存在唯一的联络 $\nabla$ ，使

(1)

$$[ f, g ] = \nabla_ {f} g - \nabla_ {g} f; \tag {3.11.13}$$

(2) 对 $X, Y, Z \in V(M)$ ,

$$L _ {X} (\omega (Y, Z)) = \omega (\nabla_ {X} Y, Z) + \omega (Y, \nabla_ {X} Z). \tag {3.11.14}$$

Christoffel 矩阵称为是对称的，如果
