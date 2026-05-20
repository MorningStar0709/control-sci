$$
\begin{array}{l} \overline {{{A}}} = S ^ {- 1} A S = \left[ \begin{array}{c c c c c c c c c} 0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 \\ - \alpha_ {1 0} & - \alpha_ {1 1} & - \alpha_ {1 2} & \beta_ {1 4} & \beta_ {1 5} & \beta_ {1 6} & \beta_ {1 7} & \beta_ {1 8} & \beta_ {1 9} \\ \hline 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 \\ \beta_ {2 1} & \beta_ {2 2} & \beta_ {2 3} & - \alpha_ {2 0} & - \alpha_ {2 1} & \beta_ {2 6} & \beta_ {2 7} & \beta_ {2 8} & \beta_ {2 9} \\ \hline 0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 \\ \beta_ {3 1} & \beta_ {3 2} & \beta_ {3 3} & \beta_ {3 4} & \beta_ {3 5} & - \alpha_ {3 0} & - \alpha_ {3 1} & - \alpha_ {3 2} & - \alpha_ {3 3} \end{array} \right] \\ \bar {B} = S ^ {- 1} B = \left[ \begin{array}{c c c} 0 & 0 & 0 \\ 0 & 0 & 0 \\ 1 & r & 0 \\ \hline 0 & 0 & 0 \\ 0 & 1 & 0 \\ \hline 0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 1 \end{array} \right] \\ \end{array}
$$

第2步：把给定的期望闭环特征值 $\{\lambda_{1}^{*},\lambda_{2}^{*},\cdots,\lambda_{9}^{*}\}$ 按龙伯格规范形 $\overline{A}$ 的对角线块阵的维数，相应地计算

$$\alpha_ {1} ^ {*} (s) = \left(s - \lambda_ {1} ^ {*}\right) \left(s - \lambda_ {2} ^ {*}\right) \left(s - \lambda_ {3} ^ {*}\right) = s ^ {3} + \alpha_ {1 2} ^ {*} s ^ {2} + \alpha_ {1 1} ^ {*} s + \alpha_ {1 0} ^ {*}\alpha_ {4} ^ {*} (s) = \left(s - \lambda_ {4} ^ {*}\right) \left(s - \lambda_ {5} ^ {*}\right) = s ^ {2} + \alpha_ {2 1} ^ {*} s + \alpha_ {2 0} ^ {*}\alpha_ {3} ^ {*} (s) = \left(s - \lambda_ {6} ^ {*}\right) \left(s - \lambda_ {7} ^ {*}\right) \left(s - \lambda_ {8} ^ {*}\right) \left(s - \lambda_ {9} ^ {*}\right) = s ^ {4} + \alpha_ {3 3} ^ {*} s ^ {3} + \alpha_ {3 2} ^ {*} s ^ {2} + \alpha_ {3 1} ^ {*} s + \alpha_ {3 0} ^ {*}$$

第3步：取

$$
\bar {K} = \left[ \begin{array}{c c c} \alpha_ {1 0} ^ {*} - \alpha_ {1 0} - \gamma \beta_ {2 1} & \alpha_ {1 1} ^ {*} - \alpha_ {1 1} - \gamma \beta_ {2 2} & \alpha_ {1 2} ^ {*} - \alpha_ {1 2} - \gamma \beta_ {2 3} \\ \beta_ {2 1} & \beta_ {2 2} & \beta_ {2 3} \\ \beta_ {3 1} & \beta_ {3 2} & \beta_ {3 3} \end{array} \right|

\begin{array}{c c c} \beta_ {1 4} - \gamma (\alpha_ {2 0} ^ {*} - \alpha_ {2 0}) & \beta_ {1 5} - \gamma (\alpha_ {2 1} ^ {*} - \alpha_ {2 1}) & \beta_ {1 6} - \gamma \beta_ {2 6} \\ \alpha_ {2 0} ^ {*} - \alpha_ {2 0} & \alpha_ {2 1} ^ {*} - \alpha_ {2 1} & \beta_ {2 6} \\ \beta_ {3 4} & \beta_ {3 5} & \alpha_ {3 0} ^ {*} - \alpha_ {3 0} \end{array}
