$$
\begin{array}{l} \phi (t; 0, 0, u) = \int_ {0} ^ {t} e ^ {A (t - \tau)} B u (\tau) d \tau^ {1} \\ - \int_ {0} ^ {1} \left[ \begin{array}{l l} 2 e ^ {- (s - \tau)} - e ^ {- 2 (s - \tau)} & e ^ {- (s - \tau)} - e ^ {- 2 (s - \tau)} \\ - 2 e ^ {- (s - \tau)} + 2 e ^ {- 2 (s - \tau)} & - e ^ {- (s - \tau)} + 2 e ^ {- 2 (s - \tau)} \end{array} \right] \\ \left[ \begin{array}{c} 0 \\ 1 \end{array} \right] \cdot 1 d \tau \\ = \int_ {0} ^ {t} \left[ \begin{array}{l} e ^ {- (s - \tau)} - e ^ {- 2 (s - \tau)} \\ - e ^ {- (s - \tau)} + 2 e ^ {- 2 (s - \tau)} \end{array} \right] d \tau \\ = \left[ \begin{array}{c} \frac {1}{2} - e ^ {- t} + \frac {1}{2} e ^ {- 2 t} \\ e ^ {- t} - e ^ {- 2 t} \end{array} \right], \quad t \geqslant 0 \\ \end{array}
$$

线性定常系统的状态运动规律 同时考虑初始状态 $x_0$ 和外输入作用 $\pmb{\alpha}$ 的线性定常系统的状态运动规律，即状态方程的一般形式

$$\dot {x} = A x + B u, x (0) = x _ {0}, t \geqslant 0 \tag {2.51}$$

的解的表达式,可由(2.12)和(2.46)的叠加而导出。因此,下面我们直接给出线性定常系统状态运动的一般性结论。

结论 3 线性定常系统在初始状态和外输入同时作用下的状态运动的表达式为:

$$\phi (t; 0, x _ {0}, u) = e ^ {A t} x _ {0} + \int_ {0} ^ {t} e ^ {A (t - \tau)} B u (\tau) d \tau , \quad t \geqslant 0 \tag {2.52}$$

或者表为更为一般的形式为：

$$\phi (t; t _ {0}, x _ {0}, u) = e ^ {A (s - t _ {0})} x _ {0} + \int_ {t _ {0}} ^ {s} e ^ {A (s - \tau)} B u (\tau) d \tau , \quad t \geqslant t _ {0} \tag {2.53}$$

式（2.52）或（2.53）在物理上的含义是，系统的运动由两部分组成，其中第一项是初始状态的转移项,而第二项为控制输入作用下的受控项。正是由于受控项的存在,提供了通过选取合适的 u 使 $x(t)$ 的轨线满足期望的要求的可能性。这一思想,是我们分析系统的结构特性和对系统进行综合的基本依据。
