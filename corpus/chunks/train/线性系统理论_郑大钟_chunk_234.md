$$\boldsymbol {K} = - [ 2 \quad 5 \quad 1 6 \quad 1 0 ]$$

（2）不考虑状态反馈的存在，设计降维状态观测器。已知 $\operatorname{rank} C = 1$ ，且注意到给定的系统动态方程已处于（5.328）的形式，因此无需再引入变换。而且，显然有

$$
\bar {A} _ {1 1} = 0, \quad \bar {A} _ {1 2} = [ 1 \quad 0 \quad 0 ]
\bar {A} _ {2 1} = \left[ \begin{array}{l} 0 \\ 0 \\ 0 \end{array} \right], \quad \bar {A} _ {2 2} = \left[ \begin{array}{c c c} 0 & - 2 & 0 \\ 0 & 0 & 1 \\ 0 & 4 & 0 \end{array} \right]

\bar {B} _ {1} = 0, \quad \bar {B} _ {2} = \left[ \begin{array}{c} 1 \\ 0 \\ - 1 \end{array} \right]
$$

进而，按前面所指出的原则(5.383)，取降维观测器的特征值为：

$$\lambda_ {1} = - 3, \quad \lambda_ {2, 3} = - 3 \pm j 2$$

相应地，对应的特征多项式为：

$$\bar {\alpha} (s) = (s + 3) (s + 3 - j 2) (s + 3 + j 2)= s ^ {3} + 9 s ^ {2} + 3 1 s + 3 9$$

再表 $\overline{L}$ 为:

$$
\bar {L} = \left[ \begin{array}{l} l _ {1} \\ l _ {2} \\ l _ {3} \end{array} \right]
$$

则可得到

$$
\overline {{A}} _ {2 2} - \overline {{L}} \overline {{A}} _ {1 2} = \left[ \begin{array}{c c c} - l _ {1} & - 2 & 0 \\ - l _ {2} & 0 & 1 \\ - l _ {3} & 4 & 0 \end{array} \right]
$$

和

$$
\begin{array}{l} a _ {L} (s) = \det (s I - \bar {A} _ {2 2} + \bar {L} \bar {A} _ {1 2}) \\ = s ^ {3} + l _ {1} s ^ {2} - (2 l _ {2} + 4) s - (2 l _ {3} + 4 l _ {1}) \\ \end{array}
$$

由比较 $\bar{a}(s)$ 和 $\alpha_{L}(s)$ ，可以定出：

$$
\bar {L} = \left[ \begin{array}{c} 9 \\ - 3 5 / 2 \\ - 7 5 / 2 \end{array} \right]
$$

再可计算得到

$$
\overline {{A}} _ {2 2} - \overline {{L}} \overline {{A}} _ {1 2} = \left[ \begin{array}{c c c} - 9 & - 2 & 0 \\ 3 5 / 2 & 0 & 1 \\ 7 5 / 2 & 4 & 0 \end{array} \right]

(\bar {A} _ {2 2} - \bar {L} \bar {A} _ {1 2}) \bar {L} + (\bar {A} _ {2 1} - \bar {L} \bar {A} _ {1 1}) = (\bar {A} _ {2 2} - \bar {L} \bar {A} _ {1 2}) \bar {L} = \left[ \begin{array}{l} - 4 6 \\ 1 2 0 \\ 5 3 5 / 2 \end{array} \right]

\bar {B} _ {2} - \bar {L} \bar {B} _ {1} = \bar {B} _ {2} = \left[ \begin{array}{c} 1 \\ 0 \\ - 1 \end{array} \right]
$$

从而，降维状态观测器为：

$$
\dot {z} = \left[ \begin{array}{c c c} - 9 & - 2 & 0 \\ 3 5 / 2 & 0 & 1 \\ 7 5 / 2 & 4 & 0 \end{array} \right] z + \left[ \begin{array}{c} - 4 6 \\ 1 2 0 \\ 5 3 5 / 2 \end{array} \right] y + \left[ \begin{array}{c} 1 \\ 0 \\ - 1 \end{array} \right] u
$$

(3) 确定重构状态 $\pmb{x}$ 和由 $\pmb{x}$ 构成的状态反馈控律。其中，估计状态 $\pmb{x}$ 为：

$$
\hat {x} = \left[ \begin{array}{c c} y & \\ z + \bar {L} y \end{array} \right] = \left[ \begin{array}{l l} 1 & 0 \\ \bar {L} & I _ {3} \end{array} \right] \left[ \begin{array}{l} y \\ z \end{array} \right] = \left[ \begin{array}{c c c c} 1 & 0 & 0 & 0 \\ 9 & 1 & 0 & 0 \\ - 1 7. 5 & 0 & 1 & 0 \\ - 3 7. 5 & 0 & 0 & 1 \end{array} \right] \left[ \begin{array}{l} y \\ z _ {1} \\ z _ {2} \\ z _ {3} \end{array} \right]
$$

而由 $\pmb{\lambda}$ 构成的状态反馈为：
