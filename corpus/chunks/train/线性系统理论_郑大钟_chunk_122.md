$$
Q = \left[ \begin{array}{c} \bar {\boldsymbol {e}} _ {1} \\ \vdots \\ \bar {\boldsymbol {e}} _ {n} \end{array} \right] = \left[ \begin{array}{c c c c c} 1 & \alpha_ {n - 1} & \dots & \alpha_ {1} \\ & \ddots & \ddots & & \vdots \\ & & \ddots & \ddots & \alpha_ {n - 1} \\ & & & & 1 \end{array} \right] \left[ \begin{array}{c} \mathbf {c A} ^ {n - 1} \\ \vdots \\ \mathbf {c A} \\ \mathbf {c} \end{array} \right] \tag {3.172}
$$

显然，当且仅当系统为完全能观测时，上式定义的变换阵 $Q$ 才是非奇异的。从而；在此基础上，可导出关于系统能观测规范形的基本结论。

结论 对完全能观测的单输入-单输出线性定常系统（3.170），引入线性非奇异变换 $\hat{x} = 2x$ ，即可导出其能观测规范形为：

$$\Sigma_ {o}: \quad \dot {\hat {x}} = A _ {o} \hat {x} + b _ {o} u \tag {3.173}$$

其中

$$
\begin{array}{l} A _ {0} = Q A Q ^ {- 1} = \left[ \begin{array}{c c c c c} 0 & \dots & 0 & - \alpha_ {0} \\ \hline 1 & & & & - \alpha_ {1} \\ & \ddots & & & \vdots \\ & & \ddots & & - \alpha_ {n - 1} \end{array} \right], b _ {0} = Q b = \left[ \begin{array}{c} \beta_ {0} \\ \beta_ {1} \\ \vdots \\ \beta_ {n - 1} \end{array} \right] \\ c _ {o} = c Q ^ {- 1} = [ 0 \dots 0 1 ] \end{array} \tag {3.174}
$$

证 推证过程和能控规范形的推导过程相类似,故略去。

例 给定能观测的单输入-单输出线性定常系统为：

$$
\dot {\boldsymbol {x}} = \left[ \begin{array}{c c c} 1 & 0 & 2 \\ 2 & 1 & 1 \\ 1 & 0 & - 2 \end{array} \right] \boldsymbol {x} + \left[ \begin{array}{l} 1 \\ 2 \\ 1 \end{array} \right] \boldsymbol {u}, n = 3
y = [ 0 \quad 1 \quad 1 ] x
$$

先定出其特征多项式

$$\alpha (s) \triangleq \det (s I - A) = s ^ {3} - 5 s + 4$$

和常数

$$\beta_ {2} = c b = 3\beta_ {1} = \mathbf {c} A \mathbf {b} + \alpha_ {2} \mathbf {c b} = 4\beta_ {0} = \mathbf {c} A ^ {2} \mathbf {b} + \alpha_ {2} \mathbf {c} A \mathbf {b} + \alpha_ {1} \mathbf {c b} = 0$$

则利用 $(3.173)$ 和 $(3.174)$ ，即可导出系统的能观测规范形为：

$$
\begin{array}{l} \dot {\hat {x}} = \left[ \begin{array}{c c c} 0 & 0 & - 4 \\ 1 & 0 & 5 \\ 0 & 1 & 0 \end{array} \right] \hat {x} + \left[ \begin{array}{c} 0 \\ 4 \\ 3 \end{array} \right] u \\ y = [ 0 & 0 & 1 ] \hat {x} \end{array}
$$

再利用(3.172)可求出变换阵

$$
Q = \left[ \begin{array}{l l l} 1 & \alpha_ {2} & \alpha_ {1} \\ 0 & 1 & \alpha_ {2} \\ 0 & 0 & 1 \end{array} \right] \left[ \begin{array}{l} c A ^ {2} \\ c A \\ c \end{array} \right] = \left[ \begin{array}{r r r} 4 & - 4 & 4 \\ 3 & 1 & - 1 \\ 0 & 1 & 1 \end{array} \right]
$$

于是，又可来定出能观测规范形中的状态向量为：

$$
\hat {\boldsymbol {x}} = Q \boldsymbol {x} = \left[ \begin{array}{c c c} 4 & - 4 & 4 \\ 3 & 1 & - 1 \\ 0 & 1 & 1 \end{array} \right] \left[ \begin{array}{l} x _ {1} \\ x _ {2} \\ x _ {3} \end{array} \right] = \left[ \begin{array}{c} 4 x _ {1} - 4 x _ {2} + 4 x _ {3} \\ 3 x _ {1} + x _ {2} - x _ {3} \\ x _ {2} + x _ {3} \end{array} \right]
$$
