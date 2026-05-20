$$
\boldsymbol {A} _ {K} (t) = \left(\frac {\partial g}{\partial \boldsymbol {Y}}\right) _ {K} = \left[ \begin{array}{l l} \frac {\partial g _ {1}}{\partial x} & \frac {\partial g _ {1}}{\partial \lambda} \\ \frac {\partial g _ {2}}{\partial x} & \frac {\partial g _ {2}}{\partial \lambda} \end{array} \right] _ {K} = \left[ \begin{array}{c c} - 2 x ^ {K} & - 1 \\ 2 \lambda^ {K} - 1 & 2 x ^ {K} \end{array} \right] (7 - 9 6)

\begin{array}{l} \boldsymbol {v} _ {K} (t) = [ \boldsymbol {g} (\boldsymbol {Y} ^ {K}, t) ] - \left[ \left(\frac {\partial \boldsymbol {g}}{\partial \boldsymbol {Y}}\right) _ {K} \boldsymbol {Y} ^ {K} \right] \\ = \left[ \begin{array}{c} - (x ^ {K}) ^ {2} - \lambda^ {K} \\ - x ^ {K} + 2 \lambda^ {K} x ^ {K} \end{array} \right] - \left[ \begin{array}{c c} - 2 x ^ {K} & - 1 \\ 2 \lambda^ {K} - 1 & 2 x ^ {K} \end{array} \right] \left[ \begin{array}{l} x ^ {K} \\ \lambda^ {K} \end{array} \right] \\ = \left[ \begin{array}{c} \left(x ^ {K}\right) ^ {2} \\ - 2 \lambda^ {K} x ^ {K} \end{array} \right] \tag {7-97} \\ \end{array}
$$

于是线性化后的正则方程(7-84)中的系数阵 $A_{K}(t)$ 和驱动项 $\pmb{v}_{K}(t)$ 都已确定，解这个非齐次时变微分方程，并用边界条件 $x^{K + 1}(0) = 10$ 和 $\lambda^{K + 1}(1) = 0$ 以决定通解中的未定常数，就完全确定了 $Y^{K + 1}(t)$ ，这就完成了一次迭代。当满足式(7-87)时，停止计算，求解结束。
