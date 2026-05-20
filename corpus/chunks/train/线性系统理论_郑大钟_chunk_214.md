证 仅对 $Q > 0$ 的情况进行证明，且只需对式(5.282)的左不等式来证明。取李亚普诺夫函数 $V(x) = x^{\mathrm{T}}Px$ ，且由 $P > 0$ 知 $V(x)$ 为正定。进而，不妨设 $k_{1} = 1 / 2 + \varepsilon$ ，其中 $\varepsilon$ 为正无穷小数，那么有

$$
\begin{array}{l} \dot {V} (\boldsymbol {x}) = \dot {\boldsymbol {x}} ^ {T} P \boldsymbol {x} + \boldsymbol {x} ^ {T} P \dot {\boldsymbol {x}} \\ = \boldsymbol {x} ^ {T} \left(A ^ {T} P + P A\right) \boldsymbol {x} - \boldsymbol {x} ^ {T} P B \Phi \left(K ^ {*} \boldsymbol {x}\right) - \Phi^ {T} \left(K ^ {*} \boldsymbol {x}\right) B ^ {T} P \boldsymbol {x} \\ \end{array}
$$

再利用黎卡提矩阵代数方程(5.245)和关系式(5.282)，并注意到 $K^{*} = R^{-1}B^{T}P$ ，故上式可进而表为：

$$
\begin{array}{l} \dot {V} (\boldsymbol {x}) = - \boldsymbol {x} ^ {T} Q \boldsymbol {x} + \boldsymbol {x} ^ {T} P B R ^ {- 1} B ^ {T} P \boldsymbol {x} - (K ^ {*} \boldsymbol {x}) ^ {T} R \Phi (K ^ {*} \boldsymbol {x}) - \Phi^ {T} (K ^ {*} \boldsymbol {x}) R (K ^ {*} \boldsymbol {x}) \\ \leqslant - x ^ {T} Q x + x ^ {T} P B R ^ {- 1} B ^ {T} P x - 2 \left(\frac {1}{2} + \varepsilon\right) (K ^ {*} x) ^ {T} R (K ^ {*} x) \\ = - x ^ {T} Q x - 2 \varepsilon x ^ {T} P B R ^ {- 1} B ^ {T} P x \\ = - \boldsymbol {x} ^ {T} (Q + 2 \varepsilon P B R ^ {- 1} B ^ {T} P) \boldsymbol {x} \tag {5.283} \\ \end{array}
$$

由 $Q > 0$ 和 $\varepsilon > 0$ ，表明 $\dot{V}(\pmb{x})$ 为负定。此外，显然有 $\| \pmb{x} \| \to \infty$ 时 $V(\pmb{x}) \to \infty$ 。从而，根据李亚普诺夫稳定性定理知，系统为大范围渐近稳定。证明完成。

为了说明不等式(5.282)的直观含义,现考虑受控系统为单输入的情况。易知,此时 $\sigma=kx$ 为标量,因此不等式(5.282)可进一步表示为如下的形式:

$$k _ {1} \sigma \leqslant \phi (\sigma) \leqslant k _ {2} \sigma \tag {5.284}$$

其中， $k_{1}>1/2$ ， $k_{2}<\infty$ ， $\phi(\sigma)$ 为标量非线性摄动。显然，不等式(5.284)在几何上表示 $\phi(\sigma)$ 的容许域为由直线 $k_{1}\sigma$ 和 $k_{2}\sigma$ 所围成的扇形区域，如图5.15中用阴影线所表征的区域。而这也就是把(5.282)称为扇形条件的根据。

最优跟踪问题 前面所作的讨论都是针对调节问题进行的，现在我们推广来讨论跟踪问题。仍然考虑线性定常的受控系统：

$$\dot {\boldsymbol {x}} = A \boldsymbol {x} + B \boldsymbol {u}, \quad \boldsymbol {x} (0) = \boldsymbol {x} _ {0}, t \geqslant 0 \tag {5.285}\boldsymbol {y} = C \boldsymbol {x}, \quad \boldsymbol {y} \in \mathscr {R} ^ {q}$$

其中，假定 $\{A, B\}$ 为能控， $\{A, C\}$ 为能观测， $C$ 为满秩阵。再设系统(5.285)的输出 $\pmb{y}$ 所要跟踪的信号 $\tilde{\pmb{y}}$ 是如下的稳定的线性定常系统的输出：

$$\dot {\boldsymbol {z}} = F \boldsymbol {z}, \quad \boldsymbol {z} (0) = \boldsymbol {z} _ {0} \tag {5.286}\tilde {\mathbf {y}} = H \mathbf {z}, \quad \tilde {\mathbf {y}} \in \mathcal {R} ^ {q}$$

且假定 $\{F, H\}$ 为能观测。那么，所谓最优跟踪问题，就是寻找一个控制 $u^{*}(\cdot)$ ，使 $y$ 跟踪 $\tilde{y}$ 的同时使如下定义的二次型性能指标
