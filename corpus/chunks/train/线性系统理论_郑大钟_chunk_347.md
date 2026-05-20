# 9.5 基于矩阵分式描述的典型实现：能控性形实现和能观测性形实现

右 MFD 的能控性形实现 给定 $q \times p$ 的严格真右 MFD $N(s)D^{-1}(s)$ , $D(s)$ 为行既约, 则称如下的一个状态空间描述

$$\dot {x} = A _ {c o} x + B _ {c o} u, y = C _ {c o} x, x \in \mathcal {R} ^ {*} \tag {9.165}$$

为 $N(s)D^{-1}(s)$ 的维数是 $n = \deg \det D(s)$ 的能控性形实现，如果其满足如下条件：

① $C_{co}(sI - A_{co})^{-1}B_{co} = N(s)D^{-1}(s)$ ;

② 表 $B_{co} = [b_{1}, b_{2}, \cdots, b_{p}]$ ， $l_{i} = \delta_{ri} D(s)$ 为行次数，则有

$$[ \boldsymbol {b} _ {1} A _ {c o} \boldsymbol {b} _ {1} \dots A _ {c o} ^ {l _ {1} - 1} \boldsymbol {b} _ {1} | \dots | \boldsymbol {b} _ {p} A _ {c o} \boldsymbol {b} _ {p} \dots A _ {c o} ^ {l _ {p} - 1} \boldsymbol {b} _ {p} ] = I _ {s} \tag {9.166}$$

我们首先来阐明构造能控性形实现 $(A_{co}, B_{co}, C_{co})$ 的思路。考虑到

$$\hat {\mathbf {y}} (s) = N (s) D ^ {- 1} (s) \hat {\mathbf {u}} (s) = N (s) \cdot D ^ {- 1} (s) I _ {p} \hat {\mathbf {u}} (s) \tag {9.167}$$

所以可把上式表成为

$$
\left\{ \begin{array}{l l} {\bar {y} (s) = D ^ {- 1} (s) I _ {p} \hat {u} (s), D (s) \text {为行既约}} \\ {\hat {y} (s) = N (s) \bar {y} (s)} \end{array} \right. \tag {9.168}
$$

由此可见，由 $N(s)D^{-1}(s)$ 构造 $(A_{co}, B_{co}, C_{co})$ 的问题可分成两步来进行：第一步，对左MFD $D^{-1}(s)I_p$ 构造观测器形实现 $(A_o, B_o, C_o)$ ，这可直接运用上一节中所得到的结果。第二步，根据(9.166)和 $\hat{y}(s) = N(s)\bar{y}(s)$ ，进一步由 $(A_o, B_o, C_o)$ 来导出能控性形实现 $(A_{co}, C_{co}, C_{co})$ 。

现在来指出 $D^{-1}(s)I_{p}$ 的观测器形实现 $(A_{0}, B_{0}, C_{0})$ 。表

$$
\left\{ \begin{array}{l} D (s) = S _ {L} (s) D _ {h r} + \Psi_ {L} (s) D _ {l r} \\ I _ {p} = \Psi_ {L} (s) \bar {N} _ {l r} \end{array} \right. \tag {9.169}
$$

其中， $D_{1r}$ 和 $D_{1r}$ 分别为 $D(s)$ 的行次系数矩阵和低次系数矩阵， $\overline{N}_{1r}$ 是 $I_{p}$ 的系数矩阵且具有如下形式：

$$
\bar {N} _ {l r} = \left[ \begin{array}{c c c} 0 & & \\ \vdots & & \\ 0 & & \\ 1 & & \\ - & \ddots & \\ & & \left[ \begin{array}{c} 0 \\ \vdots \\ 0 \\ 1 \end{array} \right] \end{array} \right] \Bigg \} l _ {1} \tag {9.170}
$$

那么,根据上一节中得到的结果,可知:

① $D^{-1}(s)I_{p}$ 的观测器形实现 $(A_{\bullet}, B_{\bullet}, C_{\bullet})$ 可按下述关系式来确定：

$$A _ {o} = A _ {o} ^ {o} - D _ {l r} D _ {h r} ^ {- 1} C _ {o} ^ {o}, B _ {o} = \bar {N} _ {l r}, C _ {o} = D _ {h r} ^ {- 1} C _ {o} ^ {o} \tag {9.171}$$

其中，核实现 $(A_{0}^{*}, B_{0}^{*}, C_{0}^{*})$ 如(9.155)所示。

② $(A_{\bullet}, B_{\bullet}, C_{\bullet})$ 具有如下的形式:
