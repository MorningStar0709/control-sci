$$
\begin{array}{l} \dot {\hat {x}} = Q ^ {- 1} A Q \hat {x} + Q ^ {- 1} B u \\ = \left[ \begin{array}{c c c c c c} 2 & 1 & 0 & 0 & 0 & 0 \\ 0 & 2 & 1 & 0 & 0 & 0 \\ 0 & 0 & 2 & 0 & 0 & 0 \\ \hline 0 & 0 & 0 & 2 & 1 & 0 \\ 0 & 0 & 0 & 0 & 2 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 \end{array} \right] \hat {x} + \left[ \begin{array}{c c} 0 & \frac {1}{4} \\ 1 - \frac {1}{2} \\ 2 & 0 \\ - \frac {1}{4} & 0 \\ \frac {1}{2} & 1 \\ - \frac {1}{2} & 1 \end{array} \right] u \\ \end{array}
$$

其中，变换后的状态向量为：

$$
\hat {x} = Q ^ {- 1} x = \left[ \begin{array}{c} \frac {1}{4} x _ {1} + \frac {1}{4} x _ {2} \\ \frac {1}{2} x _ {1} - \frac {1}{2} x _ {2} \\ x _ {3} + x _ {4} \\ - \frac {1}{2} x _ {4} - \frac {1}{4} x _ {5} - \frac {1}{4} x _ {6}, \\ \frac {1}{2} x _ {5} + \frac {1}{2} x _ {6} \\ \frac {1}{2} x _ {5} - \frac {1}{2} x _ {6} \end{array} \right]
$$
