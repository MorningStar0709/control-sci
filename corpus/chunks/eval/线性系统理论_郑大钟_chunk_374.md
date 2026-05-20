相应地，利用(10.110)，又可证得

$$
\begin{array}{l} G _ {2} (s) = R _ {2} (s) P _ {2} ^ {- 1} (s) Q _ {2} (s) + W _ {2} (s) = \left(R _ {1} (s) - X (s) P _ {1} (s)\right) V (s) \\ \cdot (U (s) P _ {1} (s) V (s)) ^ {- 1} \cdot U (s) \left(P _ {1} (s) Y (s) + Q _ {1} (s)\right) \\ + (X (s) P _ {1} (s) - R _ {1} (s)) Y (s) + (X (s) Q _ {1} (s) + W _ {1} (s)) \\ = R _ {1} (s) P _ {1} ^ {- 1} (s) Q _ {1} (s) + R _ {1} (s) Y (s) - X (s) P _ {1} (s) Y (s) - X (s) Q _ {1} (s) \\ + X (s) P _ {1} (s) Y (s) - R _ {1} (s) Y (s) + X (s) Q _ {1} (s) + W _ {1} (s) \\ = R _ {1} (s) P _ {1} ^ {- 1} (s) Q _ {1} (s) + W _ {1} (s) = G _ {1} (s), \tag {10.113} \\ \end{array}
$$

从而，就完成了证明。

结论2 给定两个多项式矩阵描述

$$
\left[ \begin{array}{l l} P _ {1} (s) & Q _ {1} (s) \\ - R _ {1} (s) & W _ {1} (s) \end{array} \right] \left[ \begin{array}{l} \hat {\zeta} _ {1} (s) \\ - \hat {\boldsymbol {u}} (s) \end{array} \right] = \left[ \begin{array}{c} \boldsymbol {0} \\ - \hat {\boldsymbol {y}} (s) \end{array} \right] \tag {10.114}
$$

和

$$
\left[ \begin{array}{l l} P _ {2} (s) & Q _ {2} (s) \\ - R _ {2} (s) & W _ {2} (s) \end{array} \right] \left[ \begin{array}{l} \hat {\zeta} _ {2} (s) \\ - \hat {\boldsymbol {u}} (s) \end{array} \right] = \left[ \begin{array}{c} \boldsymbol {0} \\ - \hat {\boldsymbol {y}} (s) \end{array} \right] \tag {10.115}
$$

则当系统矩阵 $S_{1}(s)$ 和 $S_{2}(s)$ 为严格系统等价时，两者的广义状态 $\hat{\pmb{\zeta}}_1(s)$ 和 $\hat{\pmb{\zeta}}_2(s)$ 之间成立如下的关系式：

$$
\left\{ \begin{array}{l} \hat {\xi} _ {2} (s) = V ^ {- 1} (s) \hat {\xi} _ {1} (s) + V ^ {- 1} (s) Y (s) \hat {\boldsymbol {u}} (s) \\ \hat {\xi} _ {1} (s) = V (s) \hat {\xi} _ {2} (s) - Y (s) \hat {\boldsymbol {u}} (s) \end{array} \right. \tag {10.116}
$$

证 由严格等价性定义可知， $S_{1}(s)$ 和 $S_{2}(s)$ 满足式(10.107)。再有

$$
\left[ \begin{array}{c c} V (s) & Y (s) \\ \mathbf {0} & I _ {p} \end{array} \right] ^ {- 1} = \left[ \begin{array}{c c} V ^ {- 1} (s) & - V ^ {- 1} (s) Y (s) \\ \mathbf {0} & I _ {p} \end{array} \right] \tag {10.117}
$$

故可将(10.107)改写为

$$
\left[ \begin{array}{l l} U (s) & 0 \\ X (s) & I _ {q} \end{array} \right] \left[ \begin{array}{c c} P _ {1} (s) & Q _ {1} (s) \\ - R _ {1} (s) & W _ {1} (s) \end{array} \right] = \left[ \begin{array}{c c} P _ {2} (s) & Q _ {2} (s) \\ - R _ {2} (s) & W _ {2} (s) \end{array} \right] \left[ \begin{array}{c c} V ^ {- 1} (s) & - V ^ {- 1} (s) Y (s) \\ 0 & I _ {p} \end{array} \right] \tag {10.118}
$$

从而，进一步可导出
