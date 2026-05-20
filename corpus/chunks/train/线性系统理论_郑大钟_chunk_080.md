$$
\left\{ \begin{array}{l} x _ {1} (t) = x _ {1} \left(t _ {0}\right) \\ x _ {2} (t) = 0. 5 t ^ {2} x _ {1} \left(t _ {0}\right) - 0. 5 t _ {0} ^ {2} x _ {1} \left(t _ {0}\right) + x _ {2} \left(t _ {0}\right) \end{array} \right.
$$

再取 $x_{1}(t_{0}) = 0, x_{2}(t_{0}) = 1$ 和 $x_{1}(t_{0}) = 2, x_{2}(t_{0}) = 0$ ，可得到两个线性无关解：

$$\Psi_ {1} = [ 0 \quad 1 ] ^ {T}, \quad \Psi_ {2} = [ 2 \quad t ^ {2} - t _ {0} ^ {2} ] ^ {T}$$

于是，系统的一个基本解阵为：

$$
\varPsi (t) = \left[ \begin{array}{c c} 0 & 2 \\ 1 & t ^ {2} - t _ {0} ^ {2} \end{array} \right]
$$

现利用(2.105)，就可定出系统的状态转移矩阵 $\Phi(t, t_0)$ 为：

$$
\begin{array}{l} \Phi (t, t _ {0}) = \Psi (t) \Psi^ {- 1} (t _ {0}) = \left[ \begin{array}{l l} 0 & 2 \\ 1 & t ^ {2} - t _ {0} ^ {2} \end{array} \right] \left[ \begin{array}{l l} 0 & 2 \\ 1 & 0 \end{array} \right] ^ {- 1} \\ = \left[ \begin{array}{c c} 1 & 0 \\ 0. 5 t ^ {2} - 0. 5 t _ {0} ^ {2} & 1 \end{array} \right] \\ \end{array}
$$

进而确定系统的运动规律：利用上述得到的状态转移矩阵 $\Phi(t, t_{0})$ 和式 (2.107)，即可定出：

$$
\begin{array}{l} x (t) = \Phi (t, t _ {0}) x _ {0} + \int_ {t _ {0}} ^ {t} \Phi (t, \tau) B (\tau) u (\tau) d \tau \\ - \left[ \begin{array}{c c} 1 & 0 \\ 0. 5 t ^ {2} - 0. 5 & 1 \end{array} \right] \left[ \begin{array}{l} 1 \\ 2 \end{array} \right] + \int_ {1} ^ {t} \left[ \begin{array}{c c} 1 & 0 \\ 0. 5 t ^ {2} - 0. 5 \tau^ {2} & 1 \end{array} \right] \left[ \begin{array}{l} 1 \\ 1 \end{array} \right] d \tau \\ = \left[ \begin{array}{c} 1 \\ 0. 5 t ^ {2} + 1. 5 \end{array} \right] + \left[ \begin{array}{c} t - 1 \\ \frac {1}{3} t ^ {3} - 0. 5 t ^ {2} + t - \frac {5}{6} \end{array} \right] \\ = \left[ \begin{array}{c} t \\ \frac {1}{3} t ^ {3} + t + \frac {2}{3} \end{array} \right] \\ \end{array}
$$

线性时变系统的脉冲响应矩阵 令 $G(t, \tau)$ 为线性时变系统的脉冲响应矩阵, 则通过和上一节中相类同的推导, 可导出其和状态空间描述间的基本关系式为:

$$G (t, \tau) = C (t) \Phi (t, \tau) B (\tau) + D (t) \delta (t - \tau) \tag {2.116}$$

关系式 $(2.116)$ 可用来确定零初始状态时的任意输入作用下的输出响应,即有:

$$\mathcal {Y} (t) = \int_ {t _ {0}} ^ {t} G (t, \tau) u (\tau) d \tau , \quad t \in [ t _ {0}, t _ {\alpha} ] \tag {2.117}$$

具有周期变化阵 A(·) 的线性时变系统的运动分析 我们现在来讨论一类特殊的线性时变系统, 其状态空间描述

$$
\begin{array}{l} \dot {x} = A (t) x + B (t) a \\ \mathbf {y} = C (t) \mathbf {x} + D (t) \mathbf {u} \tag {2.118} \\ \end{array}
$$

中，系统矩阵 $A(t)$ 满足下述关系式：

$$A (t) = A (t + T), \quad \forall t \tag {2.119}$$

其中 $T$ 为正常数, 物理上 (2.119) 意味着 $A(\cdot)$ 的每一个元均是以 $T$ 为周期的一个周期函数。

对于这类线性时变系统,可以指出其如下的一些有意义的属性:

(1) 设 $\Psi(t)$ 是系统 $\dot{\pmb{x}} = A(t)\pmb{x}, A(t) = A(t + T)$ 的一个基本解阵，则 $\Psi(t + T)$ 也必是它的一个基本解阵。

考虑到

$$\Psi (t + T) = A (t + T) \Psi (t + T) = A (t) \Psi (t + T) \tag {2.120}$$
