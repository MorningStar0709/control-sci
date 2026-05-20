其中 $\delta(x)$ 是不确定函数, 对于所有 x 以及已知函数 $|\delta(x)| \leqslant \varrho(x)$ , 满足 $\varrho$ 。设计一个连续滑模状态反馈控制器, 使得对于所有 $\|x(0)\|_{\infty} \leqslant k, x(t)$ 是有界的, $|x_{1}(t)|$ 是毕竟有界的, 且为 0.01。

14.8 例 12.5 中的水箱系统(含有积分器)表示为

$$\dot {y} = \frac {1}{A (y)} (u - c \sqrt {y}), \quad \dot {\sigma} = y - r$$

其中 $r$ 是期望的设置点。设 $\hat{c}$ 和 $\hat{A}(y)$ 分别是 $c$ 和 $A(y)$ 的标称模型，并假设已知正常数 $\varrho_{1} > 0, \varrho_{2} > 0, \varrho_{3} \geqslant 0$ 和 $0 \leqslant \varrho_{4} < 1$ ，满足

$$\varrho_ {1} \leqslant A (y) \leqslant \varrho_ {2}, \quad | \hat {c} - c | \leqslant \varrho_ {3}, \quad \left| \frac {A (y) - \hat {A} (y)}{A (y)} \right| \leqslant \varrho_ {4}$$

应用滑模控制,设计一个连续状态反馈控制器,使所有状态变量都有界,并且当t趋于无穷时, $|y(t)-r|$ 收敛到零。

14.9 考虑系统(14.1)

(a) 设 B 是秩为 p 的常数矩阵, 证明存在一个 $n \times n$ 阶非奇异矩阵 M, 满足 $MB = [0, I_{p}]^{T}$ , 其中 $I_{p}$ 是 $p \times p$ 阶单位阵, 验证 $T(x) = Mx$ 满足式 (14.2)。

(b) 设 $B(x)$ 是 x 的光滑函数，并假设在定义域 $D \subset R^{n}$ 上对于所有 x, B 的秩均为 p。设 $\Delta = \operatorname{span}\left\{b_{1}, \cdots, b_{p}\right\}$ ，其中 $b_{1}, \cdots, b_{p}$ 是 B 的列，并假设 $\Delta$ 是对合的。证明对于每个 $x_{0} \in D$ ，存在光滑函数 $\phi_{1}(x), \cdots, \phi_{n-p}(x)$ ，在 $x_{0}$ 点具有线性无关的微分 $\partial \phi_{1}/\partial x, \cdots, \partial \phi_{n-p}/\partial x$ ，使得对于 $1 \leqslant i \leqslant n - p$ ，有 $[\partial \phi_{i}/\partial x]B(x) = 0$ 。证明可以找到光滑函数 $\phi_{n-p+1}(x), \cdots, \phi_{n}(x)$ ，使得 $T(x) = [\phi_{1}(x), \cdots, \phi_{n}(x)]^{\mathrm{T}}$ 在 $x_{0}$ 的邻域内为微分同胚的，且满足式 (14.2)。

提示:运用 Frobenius 定理。

14.10 考虑非自治调节形式

$$
\begin{array}{l} \dot {\eta} = f _ {a} (t, \eta , \xi) + \delta_ {a} (t, \eta , \xi) \\ \dot {\xi} = f _ {b} (t, \eta , \xi) + G (t, x) E (t, x) u + \delta (t, x, u) \\ \end{array}
$$

其中，对于所有 $(t,x)\in [0,\infty)\times D,E$ 是已知非奇异矩阵，具有有界逆矩阵， $G$ 是正对角阵，其元素都是有界的，但不为零。假设存在一个连续可微函数 $\phi (t,\eta)$ 且 $\phi (t,0) = 0$ ，使得 $\dot{\eta} = f_{a}(t,\eta ,\phi (t,\eta)) + \delta_{\eta}(t,\eta ,\phi (t,\eta))$ 的原点是一致渐近稳定的。设

$$u = E ^ {- 1} \left[ - L \left(f _ {b} - \frac {\partial \phi}{\partial t} - \frac {\partial \phi}{\partial \eta} f _ {a}\right) + v \right]$$

其中 $L = \hat{G}^{-1}$ 或 $L = 0, \hat{G}(t,x)$ 是 $G(t,x)$ 的标称模型，设

$$\Delta = (I - G L) \left(f _ {b} - \frac {\partial \phi}{\partial t} - \frac {\partial \phi}{\partial \eta} f _ {a}\right) + \delta - \frac {\partial \phi}{\partial \eta} \delta_ {a}$$

假设 $\Delta_{i}$ 满足不等式(14.10)，且 $\varrho = \varrho(t, x)$ 。取 $s = \xi - \phi(t, \eta)$ ，设计一个滑模控制器以稳定原点，叙述并证明一个类似于定理14.1的定理。
