# (3) 连续动态方程离散化后的可控性和可观测性

一个可控的或可观测的连续系统,当其离散化后并不一定能保持其可控性或可观测性,现举例来说明。

设连续系统动态方程为

$$
\left[ \begin{array}{l} \dot {x} _ {1} \\ \dot {x} _ {2} \end{array} \right] = \left[ \begin{array}{l l} 0 & 1 \\ - \omega^ {2} & 0 \end{array} \right] \left[ \begin{array}{l} x _ {1} \\ x _ {2} \end{array} \right] + \left[ \begin{array}{l} 0 \\ 1 \end{array} \right] u, \quad y = [ 0 \quad 1 ] \left[ \begin{array}{l} x _ {1} \\ x _ {2} \end{array} \right]
$$

由于系统的状态方程为可控标准型，故一定可控。根据可观测性判据，有

$$
\operatorname{rank} \mathbf {V} _ {1} = \operatorname{rank} \left[ \begin{array}{l l} 1 & 0 \\ 0 & 1 \end{array} \right] = 2 = n
$$

故系统可观测。

系统的状态转移矩阵为

$$
\begin{array}{l} \boldsymbol {\Phi} (t) = \mathscr {L} ^ {- 1} \left[ (s \boldsymbol {I} - \boldsymbol {A}) ^ {- 1} \right] = \mathscr {L} ^ {- 1} \left[ \begin{array}{c c} s & - 1 \\ \omega^ {2} & s \end{array} \right] ^ {- 1} = \mathscr {L} ^ {- 1} \left[ \begin{array}{c c} \frac {s}{s ^ {2} + \omega^ {2}} & \frac {1}{s ^ {2} + \omega^ {2}} \\ \frac {- \omega^ {2}}{s ^ {2} + \omega^ {2}} & \frac {s}{s ^ {2} + \omega^ {2}} \end{array} \right] \\ = \left[ \begin{array}{c c} \cos \omega t & \frac {\sin \omega t}{\omega} \\ - \omega \sin \omega t & \cos \omega t \end{array} \right] \\ \end{array}

\boldsymbol {G} (t) = \int_ {0} ^ {t} \boldsymbol {\Phi} (\tau) \boldsymbol {b} \mathrm{d} \tau = \int_ {0} ^ {\mathrm{T}} \left[ \begin{array}{c} \frac {\sin \omega \tau}{\omega} \\ \cos \omega \tau \end{array} \right] \mathrm{d} \tau = \left[ \begin{array}{c} \frac {1 - \cos \omega t}{\omega^ {2}} \\ \frac {\sin \omega t}{\omega} \end{array} \right]
$$

系统离散化后的状态方程为

$$
\begin{array}{l} \boldsymbol {x} (k + 1) = \boldsymbol {\Phi} (T) \boldsymbol {x} (k) + \boldsymbol {G} (T) \boldsymbol {u} (k) \\ = \left[ \begin{array}{l l} \cos \omega T & \frac {\sin \omega T}{\omega} \\ - \omega \sin \omega T & \cos \omega T \end{array} \right] \left[ \begin{array}{l} x _ {1} (k) \\ x _ {2} (k) \end{array} \right] + \left[ \begin{array}{c} \frac {1 - \cos \omega T}{\omega^ {2}} \\ \frac {\sin \omega T}{\omega} \end{array} \right] u (k) \\ \end{array}
$$

离散化后系统的可控性矩阵为
