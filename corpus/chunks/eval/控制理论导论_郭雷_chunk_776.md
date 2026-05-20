# 习题 10.3

10.3.1 设 $X = \ell^2, U = \mathbb{R}^1$ . 在 $X$ 中定义线性算子 $A$

$$A (\xi_ {n}) = (n ^ {- 1} \xi_ {n}), \quad \forall (\xi_ {n}) \in X,$$

并定义控制算子 $B \in \mathcal{L}(U, X)$

$$B u = u \left(\beta_ {n}\right), \quad \forall u \in \mathbb {R} ^ {1},$$

这里 $(\beta_{n})\in \ell^{2}$ 使得 $(n\beta_{n})\in \ell^{2}$ . 试证系统 $(A,B)$ 近似能控，但不是近似能稳的.

10.3.2 设 $A, B$ 分别为 $n \times n$ 和 $n \times m$ 矩阵。考察有穷维线性控制系统

$$
\left\{ \begin{array}{l} \frac {\mathrm{d} x (t)}{\mathrm{d} t} = A x (t) + B u (t), \qquad t > 0, \\ x (0) = x + 0 \in \mathbb {R} ^ {n}. \end{array} \right.
$$

假定存在 $m \times n$ 矩阵 $K^{+}$ 和 $K^{-}$ (分别称为反馈和前馈矩阵), 使得 $A^{+} \stackrel{\mathrm{def}}{=} A + BK^{+}$ 的所有本征值具有负实部, 而 $A^{-} \stackrel{\mathrm{def}}{=} A + BK^{-}$ 的所有本征值具有正实部. 试证上述线性控制系统是精确能控的.

10.3.3 考察 Euler-Bernoulli 梁边界控制系统

$$
\left\{ \begin{array}{l l} \ddot {y} (x, t) + a ^ {4} y ^ {\prime \prime \prime \prime} (x, t) = 0, & 0 <   x <   1, t > 0, \\ y (0, t) = y ^ {\prime} (0, t) = 0, \\ y ^ {\prime \prime} (1, t) = u (t), y ^ {\prime \prime \prime} (1, t) = 0. \end{array} \right.
$$

取状态空间为 $H = V_0^2 (0,1)\times L^2 (0,1)$ ，其中 $V_{0}^{2}(0,1) = \left\{f\in H^{2}(0,1)\mid f(0) = f^{\prime}(0) = 0\right\}$ 赋以内积

$$
\left\langle \left[ \begin{array}{l} y _ {1} \\ z _ {1} \end{array} \right], \left[ \begin{array}{l} y _ {2} \\ z _ {2} \end{array} \right] \right\rangle = \int_ {0} ^ {1} [ a ^ {4} y _ {1} ^ {\prime \prime} y _ {2} ^ {\prime \prime} + z _ {1} z _ {2} ] d x,
$$

对于任意固定的 $T > 0$ , 控制 $u(\cdot) \in L^2(0, T)$ . 试证对于充分大的 $T$ , 上述控制系统是精确能控的.

10.3.4 完成推论 10.3.4 的证明.
