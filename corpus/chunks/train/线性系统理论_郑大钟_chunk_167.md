其中 $n$ 为系统的维数。考虑到， $(A - BK)B$ 的列可表为 $[B, AB]$ 的列的线性组合， $(A - BK)^2B$ 的列可表为 $[B, AB, A^2B]$ 的列的线性组合，如此等等。表明， $Q_{cK}$ 的列均可表为 $Q_c$ 的列的线性组合。由此，成立

$$\operatorname{rank} Q _ {c K} \leqslant \operatorname{rank} Q _ {e} \tag {5.17}$$

另一方面， $\Sigma_0$ 又可看成为是 $\Sigma_K$ 的一个状态反馈系统，即

$$\dot {x} = A x + B u = [ (A - B K) + B K ] x + B u \tag {5.18}$$

所以，同理也成立

$$\operatorname{rank} Q _ {c} \leqslant \operatorname{rank} Q _ {c K} \tag {5.19}$$

利用(5.17)和(5.19)，即可导出

$$\operatorname{rank} Q _ {c K} = \operatorname{rank} Q _ {e} \tag {5.20}$$

从而， $\Sigma_{cK}$ 能控当且仅当 $\Sigma_{c}$ 能控。

(ii) 再证：状态反馈系统不一定能保持能观测性。

对此，只须举例说明， $\Sigma_{\circ}$ 为能观测，但 $\Sigma_{K}$ 不一定为能观测。考察系统

$$
\dot {\boldsymbol {x}} = \left[ \begin{array}{l l} 1 & 2 \\ 0 & 3 \end{array} \right] \boldsymbol {x} + \left[ \begin{array}{l} 0 \\ 1 \end{array} \right] \boldsymbol {u}
y = [ 1 \quad 1 ] x
$$

易知,其能观测性判别阵

$$
Q _ {\bullet} = \left[ \begin{array}{l} C \\ C A \end{array} \right] = \left[ \begin{array}{l l} 1 & 1 \\ 1 & 5 \end{array} \right]
$$

满足 $\operatorname{rank} Q_{\bullet} = n = 2$ ，故 $\Sigma_{\bullet}$ 为能观测。现引入状态反馈，且取 $K = [0, 4]$ ，则状态反馈系统为：

$$
\dot {\boldsymbol {x}} = (A - B K) \boldsymbol {x} + B \nu = \left[ \begin{array}{c c} 1 & 2 \\ 0 & - 1 \end{array} \right] \boldsymbol {x} + \left[ \begin{array}{l} 0 \\ 1 \end{array} \right] \boldsymbol {v}

y = \left[ \begin{array}{l l} 1 & 1 \end{array} \right] x
$$

考虑到,其能观测性判别阵

$$
Q _ {\bullet K} = \left[ \begin{array}{c} C \\ C (A - B K) \end{array} \right] = \left[ \begin{array}{l l} 1 & 1 \\ 1 & 1 \end{array} \right]
$$

且显然有 $\operatorname{rank} Q_{\bullet K} = 1 < n = 2$ ，故 $\Sigma_K$ 为不完全能观测。而若取 $K = [0, 5]$ ，则通过计算可知，此时 $\Sigma_K$ 为能观测。从而，表明状态反馈可能改变系统的能观测性。至此，证明完成。

结论 2 输出反馈的引入能同时不改变系统的能控性和能观测性，即输出反馈系统 $\Sigma_{F}$ 为能控(能观测)的充分必要条件是受控系统 $\Sigma_{o}$ 为能控(能观测)。

证（i）由于对任一输出反馈系统都可找到一个等价的状态反馈系统，而已知状态反馈可保持能控性，从而证得输入反馈的引入不改变系统的能控性。（ii）表 $\Sigma_{\bullet}$ 和 $\Sigma_{F}$ 的能观测性判别阵分别为：

$$
Q _ {\bullet} = \left[ \begin{array}{c} C \\ C A \\ \vdots \\ C A ^ {s - 1} \end{array} \right] \tag {5.21}
$$

和

$$
Q _ {o F} = \left[ \begin{array}{c} C \\ C (A - B F C) \\ \vdots \\ C (A - B F C) ^ {n - 1} \end{array} \right] \tag {5.22}
$$

考虑到 $C(A - BFC)$ 的行可表为 $[C^T, A^T C^T]^T$ 的行线性组合， $C(A - BFC)^2$ 的行可表为 $[C^T, A^T C^T, (A^T)^2 C^T]^T$ 的行的线性组合，如此等等。于是，由此可导出

$$\operatorname{rank} Q _ {o F} \leqslant \operatorname{rank} Q _ {o} \tag {5.23}$$

进而，可把 $\Sigma_{\bullet}$ 看成为 $\Sigma_{F}$ 的输出反馈系统，又有
