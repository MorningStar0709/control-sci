# 10.3 多项式矩阵描述的互质性和状态空间描述的能控性和能观测性

本节中,我们来指出线性系统的两种描述的结构特性间的等价关系,也即多项式矩阵描述中的左和右互质与状态空间描述中的能控性和能观测性间的等价关系。

互质性与能控性和能观测性的等价性 给定多项式矩阵描述为

$$
\left\{ \begin{array}{c} P (s) \hat {\zeta} (s) = Q (s) \hat {\boldsymbol {u}} (s) \\ \hat {\boldsymbol {y}} (s) = R (s) \hat {\zeta} (s) + W (s) \hat {\boldsymbol {u}} (s) \end{array} \right. \tag {10.45}
$$

它的一个状态空间实现是

$$
\left\{ \begin{array}{l} \dot {\boldsymbol {x}} = A \boldsymbol {x} + B \boldsymbol {u} \\ \boldsymbol {y} = C \boldsymbol {x} + E (p) \boldsymbol {u}, p = d / d t \end{array} \right. \tag {10.46}
$$

且其维数为

$$\dim (A) = \deg \det P (s) = n \tag {10.47}$$

则两种描述的结构特性之间有着如下的结论。

结论 对系统的两种描述(10.45)和(10.46)， $\{P(s), Q(s)\}$ 的左互质等价于 $\{A, B\}$ 的完全能控，而 $\{P(s) R(s)\}$ 的右互质则等价于 $\{A, C\}$ 的完全能观测。

证 只需就左互质和能控性的等价性进行证明。为此，分成三步来进行。

① 根据(10.32)，得 $P^{-1}(s)Q(s) = P_{r}^{-1}(s)Q_{r}(s)$ ，其中 $P_{r}(s)$ 为行既约。再表 $P_{r}^{-1}(s)\overline{Q}_{r}(s)$ 为 $P_{r}^{-1}(s)Q_{r}(s)$ 的严格真部分，而 $(A, B, \overline{C}_{o})$ 为它的维数等于

$$n = \deg \det P _ {r} (s) = \deg \det P (s) \tag {10.48}$$

的一个实现，且不妨设其为观测器形实现。于是，可通过表 $\overline{Q}_r(s)$ 为：

$$\overline {{{Q}}} _ {r} (s) = \Psi_ {L} (s) \overline {{{Q}}} _ {r l} \tag {10.49}$$

其中

$$
\Psi_ {L} (s) = \left[ \begin{array}{c c c c} s ^ {l _ {1} - 1} & \dots & s & 1 \\ \hdashline & & & \\ & \ddots & & \\ & & \vdots & \\ & & s ^ {l _ {m} - 1} & \dots & s & 1 \end{array} \right] \tag {10.50}
l _ {i} = \delta_ {r i} P _ {r} (s), \sum_ {i = 1} ^ {m} l _ {i} = n \tag {10.51}
$$

并考虑到观测器形实现的特点,而有

$$\bar {C} _ {\bullet} (s I - A) ^ {- 1} B = \bar {C} _ {\bullet} (s I - A) ^ {- 1} \bar {Q} _ {n l} = P _ {r} ^ {- 1} (s) \Psi_ {L} (s) \bar {Q} _ {n l} \tag {10.52}$$

又因为 $\overline{Q}_n$ 的任意性，所以由上式又可得到：

$$P _ {r} (s) \bar {C} _ {\bullet} = \Psi_ {L} (s) (s I - A) \tag {10.53}$$

再由(10.35)、(10.39)和(10.42)，进一步有

$$\bar {Q} _ {r} (s) = Q _ {r} (s) - P _ {r} (s) Y (s) = \Psi_ {L} (s) B \tag {10.54}R (s) \bar {C} _ {\bullet} = X (s) (s I - A) + C \tag {10.55}E (s) = X (s) B + R (s) Y (s) + W (s) \tag {10.56}$$

这样，把等式(10.53)—(10.56)组合在一起，就可导出如下的关系式：

$$
\left[ \begin{array}{l l} \Psi_ {L} (s) & 0 \\ - X (s) & I _ {q} \end{array} \right] \left[ \begin{array}{c c} s I - A & B \\ - C & E (s) \end{array} \right] = \left[ \begin{array}{l l} P _ {r} (s) & Q _ {r} (s) \\ - R (s) & W (s) \end{array} \right] \left[ \begin{array}{c c} \bar {C} _ {\bullet} & - Y (s) \\ 0 & I _ {p} \end{array} \right] \tag {10.57}
$$

此外，由 $\Psi_L(s)$ 的形式可知

$$\{P _ {r} (s), \Psi_ {L} (s) \} \text {为左互质} \tag {10.58}$$
