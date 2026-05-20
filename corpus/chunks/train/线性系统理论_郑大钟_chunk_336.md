# 9.4 基于矩阵分式描述的典型实现:控制器形实现和观测器形实现

前已指出，随着传递函数矩阵采用不同的描述来表示，相应地可有不同的方法来构造其状态空间实现。本节中，我们从传递函数矩阵的矩阵分式描述出发，来构造其两种典型的实现，即控制器形实现和观测器形实现。

右 MFD 的控制器形实现 给定 $q \times p$ 的严格真传递函数矩阵 $G(s)$ ，并且具有右 MFD 的形式

$$G (s) = N (s) D ^ {- 1} (s), \quad D (s) \text {为列既约} \tag {9.94}$$

则定义如下的一个状态空间描述

$$\dot {x} = A _ {c} x + B _ {c} u, y = C _ {c} x \tag {9.95}$$

为给定右 MFD $N(s)D^{-1}(s)$ 的控制器形实现，如果 $(A_{c}, B_{c}, C_{c})$ 和 $N(s)D^{-1}(s)$ 之间

满足如下的关系：

① $C_{c}(sI - A_{c})^{-1}B_{c} = N(s)D^{-1}(s)$ ;

② $(A_{c}, B_{c})$ 为能控。

构造控制器形实现的思路 给定严格真的 $N(s)D^{-1}(s)$ ， $D(s)$ 为列既约，令列次数 $\delta_{ci}D(s)=k_{i}\quad(i=1,\cdots,p)$ ，且引入如下的列次表示

$$D (s) = D _ {b c} S (s) + D _ {l c} \Psi (s) \tag {9.96}N (s) = N _ {l c} \Psi (s) \tag {9.97}$$

其中

$$
\begin{array}{l} S (s) = \left[ \begin{array}{c c c} s ^ {k _ {1}} & & \\ & \ddots & \\ & & s ^ {k _ {p}} \end{array} \right], \sum_ {i = 1} ^ {p} k _ {i} = n, k _ {i} = \delta_ {c i} D (s); \\ \varPsi (s) = \left[ \begin{array}{c c c} s ^ {k _ {1} - 1} & & \\ \vdots & & \\ \vdots & & \\ s & & \\ 1 & & \\ - - - & \ddots & \\ & & \vdots \\ & & s ^ {k _ {p} - 1} \\ & & \vdots \\ & & s \\ & & 1 \end{array} \right]; \\ \end{array}
$$

$D_{bc}$ 为 $D(s)$ 的列次系数阵，且 $\operatorname{det} D_{bc} \neq 0$ ；

$D_{1c}$ 为 $D(s)$ 的低次系数阵；

$N_{lc}$ 为 $N(s)$ 的系数阵。

则传递函数矩阵 $N(s)D^{-1}(s)$ 可等价地表为图9.5的结构图, 其中 $\Psi(s)S^{-1}(s)$ 称为其核 MFD。

我们下面来证明这一点。令 $\hat{y}(s)$ 和 $\hat{u}(s)$ 分别为输出和输入的拉普拉斯变换，则有

$$\hat {\mathbf {y}} (s) = N (s) D ^ {- 1} (s) \hat {\mathbf {u}} (s) \tag {9.98}$$

现定义 $\hat{\pmb{\xi}}(s) = D^{-1}(s)\hat{\pmb{u}}(s)$ 为部分状态的拉普拉斯变换，故又有

$$
\left\{ \begin{array}{c} D (s) \hat {\xi} (s) = \hat {u} (s) \\ \hat {y} (s) = N (s) \hat {\xi} (s) \end{array} \right. \tag {9.99}
$$

再将(9.96)和(9.97)代入(9.99)，可得到

$$
\left\{ \begin{array}{c} \left[ D _ {l c} S (s) + D _ {l c} \Psi (s) \right] \hat {\xi} (s) = \hat {u} (s) \\ \hat {y} (s) = N _ {l c} \Psi (s) \hat {\xi} (s) \end{array} \right. \tag {9.100}
$$

或

$$
\left\{ \begin{array}{c} S (s) \hat {\xi} (s) = - D _ {h c} ^ {- 1} D _ {l c} \Psi (s) \hat {\xi} (s) + D _ {h c} ^ {- 1} \hat {u} (s) \\ \hat {y} (s) = N _ {l c} \Psi (s) \hat {\xi} (s) \end{array} \right. \tag {9.101}
$$

进一步，令

$$
\left\{ \begin{array}{l} \hat {\mathbf {y}} _ {o} (s) = \Psi (s) \hat {\boldsymbol {\xi}} (s) \\ \hat {\boldsymbol {u}} _ {o} (s) = - D _ {h c} ^ {- 1} D _ {l c} \Psi (s) \hat {\boldsymbol {\xi}} (s) + D _ {h c} ^ {- 1} \hat {\boldsymbol {u}} (s) \end{array} \right. \tag {9.102}
$$

那么,就可将(9.101)表示为两个部分:其核心部分为
