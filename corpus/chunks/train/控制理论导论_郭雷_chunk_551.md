Riccati 矩阵代数方程 (7.3.51) 有正定对称解矩阵 $P$ . 根据定理 7.3.5, 知 $(A, C_1^{\mathrm{T}})$ 完全能观测. 又由于 $(A, B)$ 完全能控, $P$ 是方程 (7.3.51) 的唯一正定对称解. 由定理 7.3.5、定理 7.3.6 和式 (7.3.49) 知, $u = -B^{\mathrm{T}}Px = -K^{\mathrm{T}}x$ 是系统 (7.3.44) 和含 $Q_1 = LL^{\mathrm{T}} + KK^{\mathrm{T}}$ 的二次性能指标 $J^1[u]$ 的最优控制综合函数, 且 $A - BK^{\mathrm{T}}$ 是稳定矩阵.

定理 7.3.9 对于线性定常系统 (7.3.1) 和性能指标 (7.3.19)，当 $(A, B)$ 完全能控， $(A, C^{\mathrm{T}})$ 完全能观测 $(Q = CC^{\mathrm{T}}, R = I_{\tau})$ 时，有理分式阵 $K^{*T}(sI_{n} - A + BK^{\mathrm{T}})^{-1}B$ 是正实的，这里 $K^{*T} = B^{T}P^{*}$ ， $P^{*}$ 是 Riccati 矩阵代数方程 (7.3.29) 的唯一正定对称解.

该定理证明详见文献 [2].

“逆问题”求解依赖于正实引理中矩阵方程(7.3.46)的求解，问题的实质是有理分式矩阵的因式分解。为对此有感性认识，这里分析单输入系统（即 $B = b$ 为 $n$ 维常向量）。

(1) 通过一线性变换，将线性定常线性 (7.3.44) 化为能控标准形，即

$$
A = \left( \begin{array}{c c c c c} 0 & 1 & 0 & \dots & 0 \\ 0 & 0 & 1 & \dots & 0 \\ \vdots & \vdots & \vdots & & \vdots \\ 0 & 0 & 0 & \dots & 1 \\ a _ {1} & a _ {2} & a _ {3} & \dots & a _ {n} \end{array} \right), \quad b = \left( \begin{array}{c} 0 \\ 0 \\ \vdots \\ 0 \\ 1 \end{array} \right);
$$

(2) 取常向量 $k^{T} = [k_{1}, k_{2}, \cdots, k_{n}]$ ，使 $(A, k^{T})$ 完全能观测，且 $(A - bk^{T})$ 为稳定矩阵；

(3) 分别求出矩阵 $A$ 和 $(A - bk^{\mathrm{T}})$ 的特征多项式 $\psi(s)$ 和 $p(s)$

$$\psi (s) = s ^ {n} + a _ {n} s ^ {n - 1} + \dots + a _ {2} s + a _ {1},p (s) = s ^ {n} + \left(a _ {n} - k _ {n}\right) s ^ {n - 1} + \dots + \left(a _ {2} - k _ {2}\right) s + \left(a _ {1} - k _ {1}\right);$$

(4) 对多项式 $p(-\mathrm{j}\omega)p(\mathrm{j}\omega) - \psi (-\mathrm{j}\omega)\psi (\mathrm{j}\omega)$ 做因式分解，即

$$p (- \mathrm{j} \omega) p (\mathrm{j} \omega) - \psi (- \mathrm{j} \omega) \psi (\mathrm{j} \omega) = l (- \mathrm{j} \omega) l (\mathrm{j} \omega),$$

这里 $l(s)=d_{n}s^{n-1}+d_{n-1}s^{n-2}+\cdots+d_{2}s+d_{1};$

(5) $d^{T}=[d_{1},d_{2},\cdots,d_{n}]\neq0$ 且 $(A,d^{T})$ 完全能观测；

(6) 令 $Q \stackrel{\mathrm{def}}{=} dd^{\mathrm{T}}, u = -k^{\mathrm{T}}x$ 是单输入线性定常系统

$$\dot {x} = A x + b u \tag {7.3.52}$$

在二次性能指标

$$J [ u ] = \frac {1}{2} \int_ {0} ^ {+ \infty} \left[ x ^ {\mathrm{T}} (t) Q x (t) + u ^ {\mathrm{T}} (t) u (t) \right] d t \tag {7.3.53}$$

之下的最优反馈控制规律.

我们已看到，Riccati 矩阵代数方程 (7.3.29) 的正定对称解矩阵直接给出线性二次最优调节问题的解。方程 (7.3.29) 是一个含 $\frac{n(n + 1)}{2}$ 个未知数的二次代数方程组。通常采用基于求解 Lyapunov 方程（线性代数方程组）的迭代求解方法。限于篇幅，本章不再叙述，有兴趣的读者可参阅文献 [2]。
