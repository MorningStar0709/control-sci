$$
\begin{array}{l} \hat {\mathbf {y}} (s) = R (s) \hat {\boldsymbol {\zeta}} (s) + W (s) \hat {\mathbf {u}} (s) \\ = R (s) P _ {r} ^ {- 1} (s) \bar {Q} _ {r} (s) \hat {\boldsymbol {u}} (s) + [ R (s) Y (s) + W (s) ] \hat {\boldsymbol {u}} (s) \\ = R (s) \bar {C} _ {o} (s I - A _ {o}) ^ {- 1} B _ {o} \hat {\boldsymbol {u}} (s) + [ R (s) Y (s) + W (s) ] \hat {\boldsymbol {u}} (s) \tag {10.38} \\ \end{array}
$$

并且，在一般情况下， $R(s)\overline{C}_{o}(sI-A_{o})^{-1}$ 将不是严格真的。所以，需再次采用矩阵除法，使有

$$R (s) \bar {C} _ {o} = X (s) \left(s I - A _ {o}\right) + C _ {o} \tag {10.39}$$

其中， $X(s)$ 为多项式矩阵， $C_o(sI - A_o)^{-1}$ 为严格真的，而

$$C _ {o} = [ R (s) \bar {C} _ {o} ] _ {t \rightarrow A _ {o}} \tag {10.40}$$

这样，将(10.39)代入(10.38)，就进而得到

$$\hat {\mathbf {y}} (s) = C _ {o} \left(s I - A _ {o}\right) ^ {- 1} B _ {0} \hat {\mathbf {u}} (s) + [ X (s) B _ {o} + R (s) Y (s) + W (s) ] \hat {\mathbf {u}} (s) \tag {10.41}$$

再表

$$E (s) \triangleq [ X (s) B _ {o} + R (s) Y (s) + W (s) ] \tag {10.42}$$

则(10.41)还可表示为

$$\hat {y} (s) = \left[ C _ {o} \left(s I - A _ {o}\right) ^ {- 1} B _ {o} + E (s) \right] \hat {u} (s) \tag {10.43}$$

于是，即可导出，所寻求的观测器形实现为：

$$
\left\{ \begin{array}{l} \dot {\boldsymbol {x}} = A _ {o} \boldsymbol {x} + B _ {o} \boldsymbol {u} \\ \boldsymbol {y} = C _ {o} \boldsymbol {x} + E (p) \boldsymbol {u} \end{array} \right. \tag {10.44}
$$

其中 $p = d / dt$ 为微分算子。

PMD 的最小实现 我们现在来讨论 PMD 的最小实现问题，对此有如下的一个基本结论。

结论 给定多项式矩阵描述 $(P(s), Q(s), R(s), W(s))$ ，且表 $\deg \det P(s) = n$ ，则当且仅当给定的 PMD 为不可简约时，其维数为 $n$ 的任意状态空间实现（ $A, B, C, E(p)$ ）必为最小实现，即联合能控和能观测的实现。

证 在下一节中，将要证明，对于 $\operatorname{PMD}(P(s), Q(s), R(s), W(s))$ 和其维数为 $n = \deg \det P(s)$ 的状态空间实现（ $A, B, C, E(p)$ ， $\{P(s), Q(s)\}$ 左互质等价于 $\{A, B\}$ 能控， $\{P(s), R(s)\}$ 右互质等价于 $(A, C)$ 能观测。利用这一结论和最小实现的基本属性，即可证得此结论。

从上述结论可以看出, 只要将给定的多项式矩阵描述化为不可简约 PMD, 那么由它所导出的各种形式的典型实现, 如控制器形实现、观测器形实现、能控性形实现和能观测性形实现等, 将都是最小实现。这样, 就为由 PMD 寻找最小实现提供了一种比较简便的途径, 而且最小实现的形式是可由人们任意选择的。
