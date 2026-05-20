$$
\begin{array}{l} e ^ {A t} = \alpha_ {0} (t) I + \alpha_ {1} (t) A \\ = (2 e ^ {- t} - e ^ {- 2 t}) \left[ \begin{array}{l l} 1 & 0 \\ 0 & 1 \end{array} \right] + (e ^ {- t} - e ^ {- 2 t}) \left[ \begin{array}{c c} 0 & 1 \\ - 2 & - 3 \end{array} \right] \\ = \left[ \begin{array}{c c} 2 e ^ {- t} - e ^ {- 2 t} & e ^ {- t} - e ^ {- 2 t} \\ - 2 e ^ {- t} + 2 e ^ {- 2 t} & - e ^ {- t} + 2 e ^ {- 2 t} \end{array} \right] \\ \end{array}
$$

方法4：

先求出 A 的预解矩阵为:

$$
\begin{array}{l} (s I - A) ^ {- 1} = \left[ \begin{array}{c c} s & - 1 \\ 2 & s + 3 \end{array} \right] ^ {- 1} = \left[ \begin{array}{c c} \frac {(s + 3)}{(s + 1) (s + 2)} & \frac {1}{(s + 1) (s + 2)} \\ - 2 & s \\ \hline (s + 1) (s + 2) & \frac {}{(s + 1) (s + 2)} \end{array} \right] \\ = \left[ \begin{array}{l l} \frac {2}{(s + 1)} + \frac {- 1}{(s + 2)} & \frac {1}{(s + 1)} + \frac {- 1}{(s + 2)} \\ \frac {- 2}{(s + 1)} + \frac {2}{(s + 2)} & \frac {- 1}{(s + 1)} + \frac {2}{(s + 2)} \end{array} \right] \\ \end{array}
$$

于是，对上式求拉普拉斯反变换，即可定出：

$$
e ^ {A t} = \left[ \begin{array}{c c} 2 e ^ {- t} - e ^ {- 2 t} & e ^ {- t} - e ^ {- 2 t} \\ - 2 e ^ {- t} + 2 e ^ {- 2 t} & - e ^ {- t} + 2 e ^ {- 2 t} \end{array} \right]
$$

零状态响应 给定初始状态为零的线性定常系统的强迫方程:

$$\dot {x} = A x + B u, x (0) = 0, t \geqslant 0 \tag {2.45}$$

其中，x 为 n 维状态向量，u 为 p 维输入向量，A 和 B 分别为 $n \times n$ 和 $n \times p$ 常阵。那么，对其零状态响应，可导出如下的结论。

结论 2 由(2.45)所描述的线性定常系统的零状态响应的表达式为:

$$\phi (t; 0, 0, u) = \int_ {0} ^ {t} e ^ {A (t - t)} B u (\tau) d \tau , \quad t \geqslant 0 \tag {2.46}$$

证 考虑如下的显等式:

$$
\begin{array}{l} \frac {d}{d t} e ^ {- A t} x = \left(\frac {d}{d t} e ^ {- A t}\right) x + e ^ {- A t} \dot {x} \\ = e ^ {- A t} [ \dot {x} - A x ] = e ^ {- A t} B u (t) \tag {2.47} \\ \end{array}
$$

进而，对上式从0至t进行积分，得到

$$e ^ {- A t} x (t) - x (0) = \int_ {0} ^ {t} e ^ {- A \tau} B u (\tau) d \tau \tag {2.48}$$

考虑到 $x(0) = 0$ ，并将(2.48)等式两边左乘 $e^{A}$ ，就即得：

$$
\begin{array}{l} \phi (t; 0, 0, u) = \int_ {0} ^ {t} e ^ {A t} e ^ {- A \tau} B u (\tau) d \tau \\ x (t) = \int_ {0} ^ {s} e ^ {A (t - \tau)} B u (\tau) d \tau \tag {2.49} \\ \end{array}
$$

于是，就完成了证明。

进一步, 如果令 (2.45) 的时间定义区间为 $t \geqslant t_0$ , 而 $t_0 \neq 0$ , 那么系统的零状态响应的表达式应表为更一般的形式:

$$\phi (t; t _ {0}, 0, u) = \int_ {t _ {0}} ^ {t} e ^ {A (t - \tau)} B u (\tau) d \tau , \quad t \geqslant t _ {0} \tag {2.50}$$

例 给定线性定常系统为:

$$
\left[ \begin{array}{l} x _ {1} \\ x _ {2} \end{array} \right] = \left[ \begin{array}{c c} 0 & 1 \\ - 2 & - 3 \end{array} \right] \left[ \begin{array}{l} x _ {1} \\ x _ {2} \end{array} \right] + \left[ \begin{array}{l} 0 \\ 1 \end{array} \right] u, t \geqslant 0
$$

其中， $x_{1}(0)=x_{2}(0)=0,\quad u(t)$ 为单位阶跃 $1(t)$ 。

利用 $(2.46)$ ，即可导出系统的零状态响应为：
