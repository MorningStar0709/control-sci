# 7.5.2 控制律的设计与分析

通过 $b_{1}$ 和 $b_{2}$ 的设计，使矩阵 A 的特征值具有负实部，则存在对称正定矩阵 P 和 Q，使得下式成立

$$\boldsymbol {A} ^ {\mathrm{T}} \boldsymbol {P} + \boldsymbol {P A} = - \boldsymbol {Q} \tag {7.25}$$

取 PD 形式定义控制项为

$$\hat {e} = p _ {2 1} e + p _ {2 2} \dot {e} \tag {7.26}$$

式中， $[p_{21}$ $p_{22}] = [0\quad 1]\left[ \begin{array}{ll}p_{11} & p_{12}\\ p_{21} & p_{22} \end{array} \right] = [0\quad 1]\mathbf{P}$ 。

前馈加 PD 反馈的形式设计控制律为

$$u = k _ {0} r + k _ {1} \theta +. k _ {2} \dot {\theta} \tag {7.27}$$

将控制律（7.27）代入式（7.23）得

$$
\begin{array}{l} \ddot {e} + a _ {1} \dot {e} + a _ {2} e = b r - a \left(k _ {0} r + k _ {1} \theta + k _ {2} \dot {\theta}\right) + \left(a _ {1} - b _ {1}\right) \dot {\theta} + \left(a _ {2} - b _ {2}\right) \theta \\ = b r - a k _ {0} r - a k _ {1} \theta - a k _ {2} \dot {\theta} + (a _ {1} - b _ {1}) \dot {\theta} + (a _ {2} - b _ {2}) \theta \tag {7.28} \\ = (b - a k _ {0}) r + \left(a _ {2} - b _ {2} - a k _ {1}\right) \theta + \left(a _ {1} - b _ {1} - a k _ {2}\right) \dot {\theta} \\ \end{array}
$$

在式（7.28）中，为保证 $\varepsilon \rightarrow 0$ ，并实现未知参数 a、 $a_{1}$ 和 $a_{2}$ 的自适应控制，设计 Lyapunov 函数为 $^{[3]}$

$$V = \frac {1}{2} \boldsymbol {\varepsilon} ^ {\mathrm{T}} \boldsymbol {P} \boldsymbol {\varepsilon} + \frac {1}{2 \lambda_ {0} a} (b - a k _ {0}) ^ {2} + \frac {1}{2 \lambda_ {1} a} (a _ {2} - b _ {2} - a k _ {1}) ^ {2} + \frac {1}{2 \lambda_ {2} a} (a _ {1} - b _ {1} - a k _ {2}) ^ {2}$$

式中， $\lambda_{i}>0;\ i=0,1,2$ 。

对 V 取导数，由于

$$
\left(\frac {1}{2} \boldsymbol {\varepsilon} ^ {\mathrm{T}} \boldsymbol {P} \boldsymbol {\varepsilon}\right) ^ {\prime} = \frac {1}{2} \boldsymbol {\varepsilon} ^ {\mathrm{T}} \left(\boldsymbol {A} ^ {\mathrm{T}} \boldsymbol {P} + \boldsymbol {P A}\right) \boldsymbol {\varepsilon} + \boldsymbol {\varepsilon} ^ {\mathrm{T}} \boldsymbol {P} \left[ \begin{array}{l} 0 \\ 1 \end{array} \right] (\Delta - a u)
$$

考虑到式（7.25），且

$$
\boldsymbol {\varepsilon} ^ {\mathrm{T}} \boldsymbol {P} \left[ \begin{array}{l} 0 \\ 1 \end{array} \right] = \left[ \begin{array}{l l} 0 & 1 \end{array} \right] \boldsymbol {P} \boldsymbol {\varepsilon} = \left[ \begin{array}{l l} p _ {2 1} & p _ {2 2} \end{array} \right] \boldsymbol {\varepsilon} = \left[ \begin{array}{l l} p _ {2 1} & p _ {2 2} \end{array} \right] \left[ \begin{array}{l l} e & \dot {e} \end{array} \right] ^ {\mathrm{T}} = \hat {e}
$$

则
