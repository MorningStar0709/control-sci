$$
\begin{array}{l} \det (s I - A + B K) = \det (s I - \bar {A} + \bar {B} K P ^ {- 1}) \\ = \det \left[ \begin{array}{c c} (s I - \bar {A} _ {e} + \bar {B} _ {c} \bar {K} _ {1}) & - \bar {A} _ {1 2} + \bar {B} _ {c} \bar {K} _ {2} \\ 0 & (s I - \bar {A} _ {t}) \end{array} \right] \\ = \det (s I - \bar {A} _ {c} + \bar {B} _ {c} \bar {K} _ {1}) \det (s I - \bar {A} _ {c}) \tag {5.39} \\ \end{array}
$$

其中 $\overline{K} = KP^{-1} = [\overline{K}_1, \overline{K}_2]$ 。这表明，状态反馈不能改变系统不能控部分的特征值，也即此种情况下不可能任意配置全部极点。这显然是和已知前提相矛盾的，故反设不成立，也就是 $\{A, B\}$ 为能控。必要性得证。

充分性：已知 $\{A, B\}$ 为能控，欲证可配置极点。现分成三步来证明。第一步，使系统矩阵 A 具有循环性。如果 A 已为循环，则可由此出发直接去证明。如果 A 不是循环的，则可予置一个状态反馈 $u = -K_{1}x + w$ ，使得

$$\dot {\boldsymbol {x}} = (A - B K _ {1}) \boldsymbol {x} + B \boldsymbol {w} \tag {5.40}$$

中 $(A - BK_{1}) = \hat{A}$ 为循环，且由(5.40)出发去进一步推证。第二步，化多输入系统的极点配置问题为等价的单输入系统的极点配置问题。不失一般性，设 $A$ 为循环，则当引入状态反馈 $\pmb {u} = -K\pmb {x} + \pmb{v}$ ，并取 $K = \rho k$ ，其中 $\pmb{\rho}$ 为 $p\times 1$ 阵且选取为使 $\{A,B\rho \}$ 保持能控，那么就有

$$
\begin{array}{l} \dot {x} = (A - B K) x + B v = (A - B \rho k) x + B v \\ = (A - b k) x + B v \tag {5.41} \\ \end{array}
$$

其中 $b = B\rho$ 为 $n\times 1$ 阵。并且，成立

$$\det (s I - A + B K) = \det (s I - A + b k) \tag {5.42}$$

这表明，多输入极点配置问题 $\{A, B, K\}$ 化成了单输入极点配置问题 $\{A, b, k\}$ ，其中 $k$ 为 $1 \times n$ 反馈增益阵。第三步，对单输入问题来证明，若 $\{A, b\}$ 能控，则必可任意配置闭环极点。为此，令

$$\alpha (s) = \det (s I - A) = s ^ {n} + \alpha_ {s - 1} s ^ {n - 1} + \dots + \alpha_ {1} s + \alpha_ {0} \tag {5.43}$$

且由 $\{A, b\}$ 为能控，故可导出如下的能控规范形：

$$
\bar {A} = P ^ {- 1} A P = \left[ \begin{array}{c c} 0 & I _ {n - 1} \\ \vdots & \\ 0 & \\ - \alpha_ {0} & - \alpha_ {1} \dots - \alpha_ {n - 1} \end{array} \right], \quad \bar {b} = P ^ {- 1} b = \left[ \begin{array}{l} 0 \\ \vdots \\ 0 \\ 1 \end{array} \right] \tag {5.44}
$$

再由任意指定的期望闭环极点 $\{\lambda_{1}^{*}, \lambda_{2}^{*}, \cdots, \lambda_{n}^{*}\}$ ，导出

$$\alpha^ {*} (s) = \prod_ {i = 1} ^ {n} \left(s - \lambda_ {i} ^ {*}\right) = s ^ {n} + \alpha_ {n - 1} ^ {*} s ^ {n - 1} + \dots + \alpha_ {1} ^ {*} s + \alpha_ {0} ^ {*} \tag {5.45}$$

并且，取

$$
\begin{array}{l} \vec {k} - k P = \left[ \vec {k} _ {0}, \dots , \vec {k} _ {n - 1} \right] \\ = \left[ \alpha_ {0} ^ {*} - \alpha_ {0}, \dots , \alpha_ {n - 1} ^ {*} - \alpha_ {n - 1} \right] \tag {5.46} \\ \end{array}
$$

于是，利用（5.44）和（5.46），就得到
