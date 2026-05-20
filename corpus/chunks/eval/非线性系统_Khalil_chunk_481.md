是连续的。如果 $S_{1}, S_{2}$ 和 $S_{3}$ 是任意集合且 $f_{1}: S_{1} \to S_{2}, f_{2}: S_{2} \to S_{3}$ 是函数，则称函数 $f_{2} \circ f_{1}: S_{1} \to S_{3}$ 为 $f_{1}$ 和 $f_{2}$ 的复合函数，其定义为

$$(f _ {2} \circ f _ {1}) (\cdot) = f _ {2} (f _ {1} (\cdot))$$

两个连续函数的复合仍是连续的。如果 $S \subset R^n$ 且 $f: S \to R^m$ ，则使得 $x \in S$ 的 $f(x)$ 的集合称为 $S$ 在映射 $f$ 下的象，记为 $f(S)$ 。如果 $f$ 是定义在紧集 $S$ 上的连续函数，那么 $f(S)$ 也是紧集，因此紧集上的连续函数是有界的。而且，如果 $f$ 是实值函数，即 $f: S \to R$ ，那么在紧集 $S$ 上存在点 $p$ 和 $q$ ，使得 $f(x) \leqslant f(p)$ ， $f(x) \geqslant f(q)$ ，其中 $x \in S$ 。如果 $f$ 是定义在紧集 $S$ 上的连续函数，那么 $f(S)$ 是连通的。如果对于每一对 $x, y \in S, x \neq y$ ，有 $f(x) \neq f(y)$ ，则定义在 $S$ 上的函数 $f$ 是一一对应的。如果 $f: S \to R^m$ 是紧集 $S \subset R^n$ 上的连续一一对应函数，那么 $f$ 在 $f(S)$ 上有连续反函数 $f^{-1}$ ， $f$ 与 $f^{-1}$ 的复合是恒等映射，即 $f^{-1}(f(x)) = x$ 。如果对于每个有界子区间 $J_0 \subset J$ ， $f$ 对于所有 $x \in J_0$ ，除了有限个点不连续外，其余的点都是连续的，则函数 $f: R \to R_n$ 在区间 $J \subset R$ 上是分段连续的。对于每个不连续点 $x_0$ ，若右极限 $\lim_{h \to 0} f(x_0 + h)$ 和左极限 $\lim_{h \to 0} f(x_0 - h)$ 存在，则函数在 $x_0$ 点具有有限跃变。

可微函数:如果极限

$$f ^ {\prime} (x) = \lim _ {h \rightarrow 0} \frac {f (x + h) - f (x)}{h}$$

存在,则函数 $f: R \to R$ 在 $x$ 点可微。极限 $f'(x)$ 称为 $f$ 在 $x$ 点的导数。如果在 $x_0$ 点偏导数 $\partial f_i / \partial x_j$ 存在且连续,其中 $1 \leqslant i \leqslant m, 1 \leqslant j \leqslant n$ , 则函数 $f: R^n \to R^m$ 在 $x_0$ 点连续可微。如果函数 $f$ 在 $S$ 中每一点都连续可微,则它在集合 $S$ 上连续可微。对于连续可微函数 $f: R^n \to R$ , 行向量 $\frac{\partial f}{\partial x}$ 定义为

$$\frac {\partial f}{\partial x} = \left[ \frac {\partial f}{\partial x _ {1}}, \dots , \frac {\partial f}{\partial x _ {n}} \right]$$

梯度向量,记为 $\Delta f(x)$ , 定义为 $\nabla f(x)=\left[\frac{\partial f}{\partial x}\right]^{\mathrm{T}}$

对于连续可微函数 $f: R^n \to R^m$ ，定义雅可比矩阵 $[\partial f / \partial x]$ 是一个 $m \times n$ 矩阵，其中第 $i$ 行，第 $j$ 列元素为 $\partial f_i / \partial x_j$ 。设 $S \subset R^n$ 是开集， $f: S \to R^m$ ， $f$ 在 $x_0 \in S$ 上连续可微， $g$ 映射包含 $f(S)$ 的开集到 $R^k$ 的映射， $g$ 在 $f(x_0)$ 上连续可微，那么映射 $h: S \to R^k$ ，即 $h(x) = g(f(x))$ 在 $x_0$ 上是连续可微的，其雅可比矩阵由链式法则

$$\left. \frac {\partial h}{\partial x} \right| _ {x = x _ {0}} = \left. \frac {\partial g}{\partial f} \right| _ {f = f (x _ {0})} \left. \frac {\partial f}{\partial x} \right| _ {x = x _ {0}}$$

给出。
