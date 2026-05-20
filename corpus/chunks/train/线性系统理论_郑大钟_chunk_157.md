有唯一正定对称解 $P$ 。考虑到 $\tilde{A} = A + \sigma I$ ，将其代入(4.62)即可导出(4.59)；而由(4.61)知， $\operatorname{Re} \lambda_i(\tilde{A}) < 0$ 即等价于 $\operatorname{Re} \lambda_i(A) < -\sigma, \sigma \geqslant 0, i = 1, 2, \dots, n$ 。从而，就证明了结论3。

线性时变系统的自由运动的稳定性判据 现在，推广来讨论没有外输入作用存在时的线性时变自治系统

$$\dot {\boldsymbol {x}} = A (t) \boldsymbol {x}, \quad \boldsymbol {x} \left(t _ {0}\right) = \boldsymbol {x} _ {0}, t \geqslant t _ {0} \tag {4.63}$$

且其平衡状态 $x_{e}$ 满足 $\dot{x}_c(t) \equiv 0$ 。一般地说，除了零平衡状态 $x_e = 0$ 外，还可以有非零的平衡状态 $x_e$ 。通常，也可采用两种方法来判断线性时变系统的平衡状态的稳定性，即根据系统的状态转移矩阵的判断方法和根据李亚普诺夫第二方法的判断方法。下面，我们来给出这两种判据的结果，且大部分的证明过程非常类似于定常系统的情况，故将其略去。

结论1[状态转移矩阵判据] 对于线性时变系统(4.63)，有

(i) 系统的每个平衡状态在 $t_0$ 时刻是李亚普诺夫意义下稳定的充分必要条件是存在一个依赖于 $t_0$ 的常数 $k(t_0)$ ，使成立

$$\| \Phi (t, t _ {0}) \| \leqslant k (t _ {0}) < \infty , \quad \forall t \geqslant t _ {0} \tag {4.64}$$

其中 $\Phi(t, t_{0})$ 为系统的状态转移矩阵。进一步，若对一切 $t_{0}$ ，存在不依赖于 $t_{0}$ 的常数 k，使上式成立，则系统的每个平衡状态是李亚普诺夫意义下一致稳定的。

(ii) 系统的唯一平衡状态 $x_{e} = 0$ 在 $t_0$ 时刻是渐近稳定的充分必要条件，是成立

$$
\left\{\begin{array}{l}\| \Phi (t, t _ {0}) \| \leqslant k (t _ {0}) <   \infty , \quad \forall t \geqslant t _ {0}\\\lim _ {t \rightarrow \infty} \| \Phi (t, t _ {0}) \| = 0\end{array}\right. \tag {4.65}
$$

$x_{e} = 0$ 在区间 $[0, \infty)$ 上为一致渐近稳定的充分必要条件，是存在不依赖于 $t_{0}$ 的正数 $k_{1}$ 和 $k_{2}$ ，使对任意 $t_{0} \geqslant 0$ 和所有 $t \geqslant t_{0}$ 成立

$$\left\| \Phi (t, t _ {0}) \right\| \leqslant k _ {1} e ^ {- k _ {2} (t - t _ {0})} \tag {4.66}$$

证 只限于证明 (4.66)。先证充分性：已知 (4.66) 成立，故可导出

$$
\begin{array}{l} \left\| \phi (t; x _ {0}, t _ {0}) \right\| = \left\| \Phi (t, t _ {0}) x _ {0} \right\| \leqslant \left\| \Phi (t, t _ {0}) \right\| \| x _ {0} \| \\ \leqslant k _ {1} \left\| x _ {0} \right\| e ^ {- k _ {2} (t - t _ {0})} \tag {4.67} \\ \end{array}
$$

这表明，受扰运动对所有 $t \geqslant t_0$ 为有界，且当 $t \to \infty$ 时 $\| \phi(t; x_0, t_0) \| \to 0$ ，并对所有 $t_0 \geqslant 0$ 是一致的。从而， $x_e = 0$ 为一致渐近稳定。再证必要性：已知 $x_e = 0$ 为一致渐近稳定，则据定义可知， $x_e = 0$ 为李亚普诺夫意义下一致稳定，即成立

$$\| \Phi (t, t _ {0}) \| \leqslant k _ {3}, \quad \forall t _ {0} \geqslant 0, \forall t \geqslant t _ {0} \tag {4.68}$$

同时对某个 $\delta > 0$ 和每个 $\mu > 0$ ，都对应存在一个正实数 $T > 0$ ，使得对满足 $\| x_0 \| \leqslant \delta$ 的所有初态 $x_0$ 和任意的 $\iota_0 \geqslant 0$ ，有

$$\left\| \phi \left(t _ {0} + T; x _ {0}, t _ {0}\right) \right\| = \left\| \Phi \left(t _ {0} + T, t _ {0}\right) x _ {0} \right\| \leqslant \mu \tag {4.69}$$
