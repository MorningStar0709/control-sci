(a) 求出在区域 $-\pi \leqslant x_{1} \leqslant \pi$ 内的所有平衡点, 并用线性化方法确定所有平衡点的稳定性质。

(b) 估算每个渐近稳定平衡点的吸引区。

8.20 （见文献[113]）考虑系统 $\dot{x}_1 = x_2$ ， $\dot{x}_2 = -x_1 - g(t)x_2$

其中 $g(t)$ 是连续可微的, 对于所有 $t \geqslant 0, 0 < k_{1} \leqslant g(t) \leqslant k_{2}$ 。

(a) 证明原点是指数稳定的。

(b) 设 $g(t)=2+\exp(t)$ ，如果 $g(t)$ 是无界的，(a) 能否成立？

8.21 考虑系统 $\dot{x}_1 = x_2, \quad \dot{x}_2 = -\sin x_1 - g(t)x_2$

其中 $g(t)$ 是连续可微的,且对于所有 $t \geqslant 0, 0 < k_{1} \leqslant g(t) \leqslant k_{2}$ 。证明原点是指数稳定的。
提示:利用上一习题。

8.22 考虑系统 $\dot{x}_{1}=-x_{1}-x_{2}-\alpha(t)x_{3},\quad\dot{x}_{2}=x_{1},\quad\dot{x}_{3}=\alpha(t)x_{1}$

其中 $\alpha(t)=\sin t+\sin 2t$ ，证明原点是指数稳定的。

8.23 考虑单输入-单输出非线性系统

$$\dot {x} _ {i} = x _ {i + 1}, \quad 1 \leqslant i \leqslant n - 1\dot {x} _ {n} = f _ {0} (x) + \left(\theta^ {*}\right) ^ {\mathrm{T}} f _ {1} (x) + g _ {0} (x) u$$

其中 $f_{0}, f_{1}$ 和 $g_{0}$ 已知，它们是定义在 $x \in R^{n}$ 上关于 $x$ 的光滑函数，而 $\theta^{*} \in R^{p}$ 是未知常参数向量。函数 $g_{0}(x)$ 有界而远离零点，即对于所有 $x \in R^{n}$ ，有 $|g_{0}(x)| \geqslant k_{0} > 0$ 。假设所有状态变量都是可测的。希望设计一个状态反馈自适应控制器，使 $x_{1}$ 渐近跟踪期望的参考信号 $r(t)$ ，其中 $r$ 及其直到 $n$ 阶导数 $r^{(n)}$ 对于所有 $t \geqslant 0$ 都是连续有界的。

(a) 取 $e_{i}=x_{i}-r^{(i-1)}$ 和 $e=\left[e_{1},\cdots,e_{n}\right]^{T}$ ，证明 e 满足方程

$$\dot {e} = A e + B \left[ f _ {0} (x) + \left(\theta^ {*}\right) ^ {\mathrm{T}} f _ {1} (x) + g _ {0} (x) u - r ^ {(n)} \right]$$

其中 $(A,B)$ 是可控矩阵对。

(b) 设计 $K$ , 使得 $A - BK$ 是赫尔维茨矩阵, 并设 $P$ 是李雅普诺夫方程 $P(A - BK) + (A - BK)^{\mathrm{T}}P = -I$ 的正定解。用备选李雅普诺夫函数 $V = e^{\mathrm{T}}Pe + \phi^{\mathrm{T}}\Gamma^{-1}\phi$ , 其中 $\phi = \theta - \theta^{*}, \Gamma$ 是一个正定对称矩阵, 证明自适应控制器

$$
\begin{array}{l} u = \frac {1}{g _ {0} (x)} \left[ - f _ {0} (x) - \theta^ {\mathrm{T}} f _ {1} (x) + r ^ {(n)} - K e \right] \\ \dot {\theta} = \Gamma f _ {1} (x) e ^ {T} P B \\ \end{array}
$$

保证所有状态变量都有界,且 $\lim_{t\to\infty}e(t)=0$ 。

(c) 设 $\bar{A}(t) = \left[ \begin{array}{cc}0_{n\times n} & -Bf_1^{\mathrm{T}}(\mathcal{R})\\ 0_{p\times n} & 0_{p\times p} \end{array} \right],\quad C = \left[ \begin{array}{ll}I_n & 0_{n\times p} \end{array} \right]$

其中 $\mathcal{R}=\left[r,\cdots,r^{(n-1)}\right]^{\mathrm{T}}$ 。证明如果 $(\bar{A}(t),C)$ 是一致可观测的，则当t趋于无穷时，参数误差 $\phi$ 收敛于零。
