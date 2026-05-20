$$
\left\{ \begin{array}{l} s \hat {\boldsymbol {x}} (s) = A \hat {\boldsymbol {x}} (s) + B \hat {\boldsymbol {u}} (s) \\ \hat {\boldsymbol {y}} (s) = C \hat {\boldsymbol {x}} (s) + D \hat {\boldsymbol {u}} (s) \end{array} \right. \tag {1.86}
$$

进而，由（1.86）的第一个关系式又可得到

$$(s I - A) \hat {\boldsymbol {x}} (s) = B \hat {\boldsymbol {u}} (s) \tag {1.87}$$

且考虑到 $(sI - A)$ 作为多项式矩阵必是非奇异的，因此（1.87）可改写为：

$$\hat {\boldsymbol {x}} (s) = (s I - A) ^ {- 1} B \hat {\boldsymbol {u}} (s) \tag {1.88}$$

而把 $(1.88)$ 代入 $(1.86)$ 的第二个关系式,即得到

$$\hat {\mathbf {y}} (s) = [ C (s I - A) ^ {- 1} B + D ] \hat {\mathbf {u}} (s) \tag {1.89}$$

从而，由此就可导出（1.84）。再考虑到

$$(s I - A) ^ {- 1} = \operatorname{adj} (s I - A) / \det (s I - A) \tag {1.90}$$

且 $\operatorname{adj}(sI - A)$ 的每个元多项式的最高幂次均都小于 $\det (sI - A)$ ，所以必有

$$\lim _ {s \rightarrow \infty} (s I - A) ^ {- 1} = 0 \tag {1.91}$$

于是，由（1.91）和（1.84）即可导出（1.85）。进一步易知，当 $D \neq 0$ 时 $G(\infty)$ 为非零常阵，故由（1.84）给出的 $G(s)$ 为真的；而当 $D = 0$ 时 $G(\infty)$ 为零矩阵，所以相应地 $G(s)$ 为严格真的。至此，证明完成。

$G(s)$ 的实用计算关系式 由(1.84)给出的关系式建立了传递函数矩阵 $G(s)$ 和状态空间描述的系数矩阵之间的关系, 它在理论分析上是很重要的, 但从计算的角度而言常常不很方便, 特别是采用数字计算机进行计算时尤其如此。下面, 我们来给出由 $\{A, B, C, D\}$ 计算 $G(s)$ 的一个实用算式。

结论 给定状态空间描述的系数矩阵 $\{A, B, C, D\}$ , 求出

$$\alpha (s) \triangleq \det (s I - A) = s ^ {n} + \alpha_ {n - 1} s ^ {n - 1} + \dots + \alpha_ {1} s + \alpha_ {0} \tag {1.92}$$

和

$$
\left\{ \begin{array}{l} E _ {n - 1} = C B \\ E _ {n - 2} = C A B + \alpha_ {n - 1} C B \\ \dots \dots \\ E _ {1} = C A ^ {n - 2} B + \alpha_ {n - 1} C A ^ {n - 3} B + \dots + \alpha_ {2} C B \\ E _ {0} = C A ^ {n - 1} B + \alpha_ {n - 1} C A ^ {n - 2} B + \dots + \alpha_ {1} C B \end{array} \right. \tag {1.93}
$$

则相应的传递函数矩阵就可按下式来定出：

$$G (s) = \frac {1}{\alpha (s)} \left[ E _ {n - 1} s ^ {n - 1} + E _ {n - 2} s ^ {n - 2} + \dots + E _ {1} s + E _ {0} \right] + D \tag {1.94}$$

证 首先, 来推导 $(sI - A)^{-1}$ 的一个关系式:

$$
\begin{array}{l} (s I - A) ^ {- 1} = \frac {\operatorname{adj} (s I - A)}{\det (s I - A)} = \frac {R (s)}{\alpha (s)} \\ = \frac {1}{a (s)} \left[ R _ {n - 1} s ^ {n - 1} + R _ {n - 2} s ^ {n - 2} + \dots + R _ {1} s + R _ {0} \right] \tag {1.95} \\ \end{array}
$$

其中 $R_{0}, R_{1}, \cdots, R_{n-1}$ 可这样地来定出：将上式等式两边右乘 $\alpha(s)(sI - A)$ ，可得到

$$\alpha (s) I = \left[ R _ {n - 1} s ^ {n - 1} + R _ {n - 2} s ^ {n - 2} + \dots + R _ {1} s + R _ {0} \right] (s I - A) \tag {1.96}$$

利用（1.92），上式还可改写为

$$
\begin{array}{l} I s ^ {n} + \alpha_ {n - 1} I s ^ {n - 1} + \dots + \alpha_ {1} I s + \alpha_ {0} I \\ = R _ {n - 1} s ^ {n} + \left(R _ {n - 2} - R _ {n - 1} A\right) s ^ {n - 1} + \dots + \left(R _ {0} - R _ {1} A\right) s - R _ {0} A \tag {1.97} \\ \end{array}
$$
