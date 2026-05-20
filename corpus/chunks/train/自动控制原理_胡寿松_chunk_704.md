# (2) 李雅普诺夫意义下的稳定性

设系统初始状态位于以平衡状态 $x_{e}$ 为球心、 $\delta$ 为半径的闭球域 $S(\delta)$ 内，即

$$\left\| \mathbf {x} _ {0} - \mathbf {x} _ {e} \right\| \leqslant \delta , \quad t = t _ {0} \tag {9-252}$$

若能使系统方程的解 $x(t; x_0, t_0)$ 在 $t \to \infty$ 的过程中，都位于以 $x_e$ 为球心、任意规定的半径为 $\varepsilon$ 的闭球域 $S(\varepsilon)$ 内，即

$$\left\| \boldsymbol {x} \left(t; \boldsymbol {x} _ {0}, t _ {0}\right) - \boldsymbol {x} _ {0} \right\| \leqslant \varepsilon , \quad t \geqslant t _ {0} \tag {9-253}$$

则称系统的平衡状态 $x_{e}$ 在李雅普诺夫意义下是稳定的。该定义的平面几何表示如图9-28(a)所示。式中 $\| \cdot \|$ 为欧几里得范数，其几何意义是空间距离的尺度。例如 $\| x_0 - x_e\|$ 表示状态空间中 $x_0$ 点至 $x_{e}$ 点之间距离的尺度，其数学表达式为

$$\left\| \boldsymbol {x} _ {0} - \boldsymbol {x} _ {e} \right\| = \left[ \left(x _ {1 0} - x _ {1 e}\right) ^ {2} + \dots + \left(x _ {n 0} - x _ {n e}\right) ^ {2} \right] ^ {\frac {1}{2}} \tag {9-254}$$

实数 $\delta$ 与 $\varepsilon$ 有关，通常也与 $t_{0}$ 有关。如果 $\delta$ 与 $t_{0}$ 无关，则称平衡状态是一致稳定的。

应当注意,按李雅普诺夫意义下的稳定性定义,当系统作不衰减的振荡运动时,将在平面描绘出一条封闭曲线,但只要不超出 $S(\varepsilon)$ ,则认为是稳定的,这与经典控制理论中线性定常系统稳定性的定义是有差异的。经典控制理论中的稳定性,指的是渐近稳定性。
