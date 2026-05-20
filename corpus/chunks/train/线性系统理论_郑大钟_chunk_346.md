$$
\left[ \begin{array}{c c} \Psi_ {L} (s) & \mathbf {0} \\ \mathbf {0} & I \end{array} \right] \left[ \begin{array}{l l} s I - A _ {o} & B _ {o} \\ - C _ {o} & \mathbf {0} \end{array} \right] = \left[ \begin{array}{c c} D _ {L} (s) & N _ {L} (s) \\ - I & \mathbf {0} \end{array} \right] \left[ \begin{array}{l l} C _ {o} & \mathbf {0} \\ \mathbf {0} & I \end{array} \right] \tag {9.158}
$$

其中

$$\left\{\Psi_ {L} (s), D _ {L} (s) \right\} \text {为左互质} \tag {9.159}\{s I - A _ {o}, C _ {o} \} \text {为右互质} \tag {9.160}$$

性质 3 观测器形实现 $(A_{o}, B_{o}, C_{o})$ 和左 MFD $D_{L}^{-1}(s)N_{L}(s)$ 之间, 成立如下的关系式:

$$\det (s I - A _ {o}) = \left(\det D _ {h r}\right) ^ {- 1} \det D _ {L} (s) \tag {9.161}\dim (A _ {o}) = \deg \det D _ {L} (s) \tag {9.162}$$

性质 4 左 MFD 和其观测器形实现之间有着如下的关系式:

$$
\left[ \begin{array}{c c} s I - A _ {o} & B _ {o} \\ - C _ {o} & 0 \end{array} \right] \sim \left[ \begin{array}{c c} I _ {s} & \mathbf {0} \\ \mathbf {0} & N _ {L} (s) \end{array} \right] \tag {9.163}
$$

并且， $(A_{o}, B_{o}, C_{o})$ 为联合能控和能观测的一个充分条件是对所有 $s \in \mathcal{C} N_{L}(s)$ 为行满秩。

性质5 设 $\lambda$ 为 $A_{0}$ 的一个特征值， $\bar{q}^{T}$ 为使 $\bar{q}^{T}D_{L}(\lambda)=0$ 的任一非零常行向量，则 $A_{0}$ 的属于 $\lambda$ 的一个特征行向量 $\bar{p}^{T}$ 可按下式来确定：

$$\bar {\boldsymbol {p}} ^ {T} = \bar {\boldsymbol {q}} ^ {T} \Psi_ {L} (\lambda) \tag {9.164}$$

其中 $\Psi_{L}(s)$ 如(9.154)所示。
