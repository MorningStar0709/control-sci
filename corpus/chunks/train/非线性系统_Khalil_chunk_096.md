# 3.5 习题

3.1 对下面给出的每个函数 $f(x)$ ，求 (a) f 是否连续可微；(b) f 是否为局部利普希茨的；(c) 是 f 否连续；(d) f 是否为全局利普希茨的。

(1) $f(x)=x^{2}+|x|$

(2) $f(x) = x + \operatorname{sgn}(x)$

(3) $f(x)=\sin(x)\operatorname{sgn}(x)$

(4) $f(x) = -x + a\sin (x)$

(5) $f(x) = -x + 2|x|$

(6) $f(x) = \tan(x)$

(7) $f(x) = \left[ \begin{array}{l} ax_{1} + \tanh (bx_{1}) - \tanh (bx_{2}) \\ ax_{2} + \tanh (bx_{1}) + \tanh (bx_{2}) \end{array} \right]$

(8) $f(x) = \left[ \begin{array}{c} -x_{1} + a|x_{2}|\\ -(a + b)x_{1} + bx_{1}^{2} - x_{1}x_{2} \end{array} \right]$

3.2 设 $D_{r} = \{x\in R^{n}\mid \| x\| < r\}$ 。下列各系统由 $\dot{x} = f(t,x)$ 表示，求

(a) 对于足够小的 r，在 $D_{r}$ 上，f 对 x 是否为局部利普希茨的；(b) 对于任意有限的 r > 0，在 $D_{r}$ 上，f 对 x 是否为局部利普希茨的；(c) f 对 x 是为否全局利普希茨的。

(1) 具有摩擦力和常数输入力矩的单摆方程(见 1.2.1 节)。

(2) 隧道二极管电路(见例 2.1)。  
(3) 具有线性弹簧、线性黏滞阻力、库仑摩擦力且外力为零时的质量-弹簧方程（见1.2.3节）。  
(4) 范德波尔振荡器(见例 2.6)。  
(5) 三阶自适应控制系统的闭环方程(见1.2.6节)。  
(6) 系统 $\dot{x}=Ax-B\psi(Cx)$ ，其中 A, B 和 C 分别是 $n \times n, n \times 1$ 和 $1 \times n$ 阶矩阵， $\psi(\cdot)$ 为图 1.10(c) 所示的死区非线性特性。

3.3 证明: 如果 $f_{1}: R \rightarrow R$ 和 $f_{2}: R \rightarrow R$ 是局部利普希茨的, 那么 $f_{1} + f_{2}, f_{1}f_{2}$ 和 $f_{2} \circ f_{1}$ 都是局部利普希茨的。

3.4 设 $f: R^n \to R^n$ 定义为

$$
f (x) = \left\{ \begin{array}{l l} \frac {1}{\| K x \|} K x, & g (x) \| K x \| \geqslant \mu > 0 \\ \frac {g (x)}{\mu} K x, & g (x) \| K x \| <   \mu \end{array} \right.
$$

其中， $g:R^{n}\rightarrow R$ 是局部利普希茨的，且非负，K 是常数矩阵。证明 $f(x)$ 在 $R^{n}$ 的任何紧子集上都是利普希茨的。

3.5 设 $\|\cdot\|_{\alpha}$ 和 $\|\cdot\|_{\beta}$ 在 $R^{n}$ 上有两个不同的 p 范数。证明: $f: R^{n} \to R^{m}$ 对 $\|\cdot\|_{\alpha}$ 是利普希茨的, 当且仅当它对 $\|\cdot\|_{\beta}$ 是利普希茨的时。

3.6 设 $f(t,x)$ 对于 t 分段连续, 对于 x 是局部利普希茨的, 且

$$\| f (t, x) \| \leqslant k _ {1} + k _ {2} \| x \|, \quad \forall (t, x) \in [ t _ {0}, \infty) \times R ^ {n}$$

(a) 证明式(3.1)的解对存在解的所有 $t \geqslant t_0$ 满足

$$\| x (t) \| \leqslant \| x _ {0} \| \exp [ k _ {2} (t - t _ {0}) ] + \frac {k _ {1}}{k _ {2}} \{\exp [ k _ {2} (t - t _ {0}) ] - 1 \}$$

(b) 该解存在有限逃逸时间吗?

3.7 设 $g: R^{n} \rightarrow R^{n}$ 对于所有 $x \in R^{n}$ 连续可微, $f(x)$ 由下式定义:

$$f (x) = \frac {1}{1 + g ^ {T} (x) g (x)} g (x)$$

证明 $\dot{x}=f(x)$ , $x(0)=x_{0}$ 对于所有 $t\geqslant0$ 有唯一解。

3.8 证明状态方程

$$\dot {x} _ {1} = - x _ {1} + \frac {2 x _ {2}}{1 + x _ {2} ^ {2}}, \quad x _ {1} (0) = a\dot {x} _ {2} = - x _ {2} + \frac {2 x _ {1}}{1 + x _ {1} ^ {2}}, \quad x _ {2} (0) = b$$

对于所有 $t \geqslant 0$ 有唯一解。

3.9 假二阶系统 $\dot{x}=f(x)$ 有一个极限环， $f(x)$ 是局部利普希茨的。证明任何始于极限环包围的区域内的解都不可能存在有限逃逸时间。

3.10 当 L 和 C 与其标称值不同时, 推导例 2.1 中隧道二极管电路的灵敏度方程。
