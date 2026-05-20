# 习题

5.1 判断下列系统能否用状态反馈任意地配置极点:

(i) $\dot{x}=\begin{bmatrix}1 & 2 \\ 3 & 1\end{bmatrix}x+\begin{bmatrix}1 \\ 0\end{bmatrix}u$ (ii) $\dot{x}=\begin{bmatrix}1&0&0\\ 0&-2&1\\ 0&0&-2\end{bmatrix}x+\begin{bmatrix}1&0\\ 0&1\\ 0&0\end{bmatrix}u$

(iii) $\dot{\pmb{x}} = \begin{bmatrix} 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \\ -2 & -4 & -3 & -5 \end{bmatrix} \pmb{x} + \begin{bmatrix} 0 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & 1 & 0 \\ 1 & 0 & 0 \end{bmatrix} \pmb{u}$

5.2 给定受控系统为:

$$
\dot {\boldsymbol {x}} = \left[ \begin{array}{l l} 1 & 2 \\ 3 & 1 \end{array} \right] \boldsymbol {x} + \left[ \begin{array}{l} 1 \\ 0 \end{array} \right] \boldsymbol {u}
$$

试确定一个状态反馈阵 K，使闭环极点配置为 $\lambda_{1}^{*} = -2 + j$ 和 $\lambda_{3}^{*} = -2 - j$ 。

5.3 给定受控系统的传递函数为

$$g _ {0} (s) = \frac {1}{s (s + 4) (s + 8)}$$

试确定一个状态反馈阵 K，使闭环极点配置为 $\lambda_{1}^{*} = -2, \lambda_{2}^{*} = -4$ 和 $\lambda_{3}^{*} = -7$ 。

5.4 对上题的受控系统，确定一个状态反馈阵 K，使相对于单位阶跃参考输入的输出过渡过程满足指标：超调量 $\sigma \leqslant 20\%$ ，超调点时间 $t_{\sigma} \leqslant 0.4$ 秒。

5.5 给定受控系统为:

$$
\begin{array}{l} \dot {\boldsymbol {x}} = \left[ \begin{array}{l l} 1 & 1 \\ 0 & 1 \end{array} \right] \boldsymbol {x} + \left[ \begin{array}{l} 0 \\ 1 \end{array} \right] u \\ y = \left[ \begin{array}{l l} 2 & 0 \\ 0 & 1 \end{array} \right] x \\ \end{array}
$$

试确定一个输出反馈阵 F，使闭环极点配置为 $\lambda_{1}^{*} = -2$ 和 $\lambda_{2}^{*} = -4$ 。

5.6 给定受控系统为:

$$
\dot {\boldsymbol {x}} = \left[ \begin{array}{c c c c} 2 & 1 & 0 & 0 \\ 0 & 2 & 0 & 0 \\ 0 & 0 & - 2 & 0 \\ 0 & 0 & 0 & - 2 \end{array} \right] \boldsymbol {x} + \left[ \begin{array}{l} 0 \\ 1 \\ 1 \\ 1 \end{array} \right] u
$$

试问能否找到一个状态反馈阵 K，使闭环极点配置到下列位置：

(i) $\lambda_1^* = -2, \lambda_2^* = -2, \lambda_3^* = -2, \lambda_4^* = -2$   
(ii) $\lambda_1^* = -3, \lambda_2^* = -3, \lambda_3^* = -3, \lambda_4^* = -2$   
(iii) $\lambda_{1}^{*} = -3, \lambda_{2}^{*} = -3, \lambda_{3}^{*} = -3, \lambda_{4}^{*} = -3$

5.7 给定受控系统为:

$$
\dot {\boldsymbol {x}} = \left[ \begin{array}{l l l} 1 & 1 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 2 \end{array} \right] \boldsymbol {x} + \left[ \begin{array}{l l} 0 & 0 \\ 1 & 0 \\ 0 & - 1 \end{array} \right] \boldsymbol {u}
$$

试确定两个不同的状态反馈阵 $K_{1}$ 和 $K_{2}$ ，使闭环极点配置为 $\lambda_{1}^{*} = -2, \lambda_{2}^{*} = -1 + j2$ 和 $\lambda_{3}^{*} = -1 - j2$ 。

5.8 给定受控系统为:

$$
\dot {\boldsymbol {x}} = \left[ \begin{array}{c c c c} 0 & 2 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ - 3 & 1 & 2 & 3 \\ 2 & 1 & 0 & 0 \end{array} \right] \boldsymbol {x} + \left[ \begin{array}{c c} 0 & 0 \\ 0 & 0 \\ 1 & 2 \\ 0 & 2 \end{array} \right] \boldsymbol {u}
$$
