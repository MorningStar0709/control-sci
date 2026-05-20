# 习题

10.1 判断下列各 PMD 是否为不可简约:

(i) $\left[ \begin{array}{cc} s^2 - 1 & 0 \\ 0 & s + 1 \end{array} \right]\hat{\zeta}(s) = \left[ \begin{array}{c}s + 1\\ s - 1 \end{array} \right]\hat{\boldsymbol{u}} (s)$

$$
\hat {y} (s) = \left[ \begin{array}{l l} s (s + 1) & 2 \\ s & 1 \end{array} \right] \hat {\zeta} (s) + \left[ \begin{array}{l} s + 1 \\ 2 \end{array} \right] \hat {u} (s)
$$

(ii) $\left[ \begin{array}{ccc}s^2 -1 & 1\\ 0 & s + 1 \end{array} \right]\hat{\zeta} (s) = \left[ \begin{array}{ccc}s + 2 & 2\\ s & 0 \end{array} \right]\hat{\boldsymbol{u}} (s)$

$$\hat {y} (s) = [ 2 \quad s - 1 ] \hat {\zeta} (s) + [ s + 1 \quad 4 ] \hat {u} (s)$$

10.2 对于上题中给出的 PMD，当为可简约时导出一个不可简约 PMD，当为不可简约时导出另一形式的一个不可简约 PMD。

10.3 确定下列各 MFD 的一个不可简约的 PMD:

(i) $[s + 2, s + 1] \cdot \begin{bmatrix} s + 1 & 0 \\ (s + 1)(s + 2) & s^2 - 1 \end{bmatrix}^{-1}$

(ii) $\left[ \begin{array}{ccc}s^2 -1 & 0\\ 0 & s - 1 \end{array} \right]^{-1}\left[ \begin{array}{ccc}0 & s^{-1}\\ 2 & s^2 \end{array} \right]$

10.4 确定下列各传递函数矩阵 $G(s)$ 的一个不可简约的 PMD:

(i) $G(s) = \begin{bmatrix} \frac{2s + 1}{s^{2} + s + 1} \\ \frac{1}{s + 3} \end{bmatrix}$

(ii) $G(s) = \begin{bmatrix} \frac{s^{2} + s}{s^{2} + 1} & \frac{s + 1}{s + 2} \\ 0 & \frac{(s + 2)(s + 1)}{s^{2} + 2s + 2} \end{bmatrix}$

10.5 已知状态空间描述为

$$\dot {\boldsymbol {x}} = A \boldsymbol {x} + B \boldsymbol {u}, \boldsymbol {y} = C \boldsymbol {x} + E \boldsymbol {u}$$

且设其为完全能控和完全能观测，试证明：当取

$$P (s) = (s I - A), Q (s) = B, R (s) = C, W (s) = E$$

时,所导出的 PMD 必是不可简约的。

10.6 给定系统的 PMD 为:

$$
\left[ \begin{array}{c c} s ^ {2} + 2 s + 1 & 2 \\ 0 & s + 1 \end{array} \right] \hat {\zeta} (s) = \left[ \begin{array}{l l} s + 2 \\ s + 1 \end{array} \right] \hat {u} (s)
\hat {y} (s) = [ s + 1 \quad 2 ] \hat {\zeta} (s) + 2 \hat {u} (s)
$$

(i) 计算系统的传递函数 $g(s)$ ;

(ii) 求系统的一个最小实现。

10.7 给定系统的 PMD 为:

$$
\left[ \begin{array}{c c} s ^ {2} + 2 s + 1 & 3 \\ 0 & s + 1 \end{array} \right] \hat {\zeta} (s) = \left[ \begin{array}{c c} s + 2 & s \\ 0 & s + 1 \end{array} \right] \hat {u} (s)

\hat {\mathbf {y}} (s) = \left[ \begin{array}{c c} s + 1 & 2 \\ 0 & s \end{array} \right] \hat {\boldsymbol {\zeta}} (s)
$$

(i) 计算系统的传递函数矩阵 $G(s)$ ;

(ii) 求此 PMD 的一个最小实现。

10.8 设 $\{P, Q, R, W\}$ 为一个不可简约的 PMD，试证明：

矩阵 $\begin{bmatrix} P^2 & PQ \\ -RP & -RQ \end{bmatrix}$ 的史密斯形为 $\begin{bmatrix} I & 0 \\ 0 & 0 \end{bmatrix}$

10.9 设有 $G(s) = R(s)P^{-1}(s)Q(s) + W(s)$ 为 $q \times q$ 的有理分式矩阵, 其中

$$\det W (s) \not \equiv 0 _ {\circ}$$

试证明： $G(s)$ 是可逆的，当且仅当有

$$\det \left[ P (s) + Q (s) W ^ {- 1} (s) R (s) \right] \neq 0$$
