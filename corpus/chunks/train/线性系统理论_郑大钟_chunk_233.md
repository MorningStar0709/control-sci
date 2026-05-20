很容易证明这一点。对(5.374)作线性非奇异变换,其中变换阵P如式(5.377)所示,可导出:

$$
\begin{array}{l} \widetilde {A} = P \overline {{A}} P ^ {- 1} = P \left[ \begin{array}{c c} A - B K Q _ {1} C & - B K Q _ {2} \\ G C - H K Q _ {1} C & F - H K Q _ {2} \end{array} \right] P ^ {- 1} \\ = \left[ \begin{array}{c c} A - B K & - B K Q _ {2} \\ 0 & F \end{array} \right] \\ \end{array}

\widetilde {B} = P \overline {{B}} = \left[ \begin{array}{c c} I _ {*} & 0 \\ - T & I _ {n - q} \end{array} \right] \left[ \begin{array}{l} B \\ H \end{array} \right] = \left[ \begin{array}{c} B \\ T B - H \end{array} \right] = \left[ \begin{array}{l} B \\ 0 \end{array} \right]

\widetilde {C} = \bar {C} P ^ {- 1} = [ C \quad \mathbf {0} ] \left[ \begin{array}{c c} I _ {n} & \mathbf {0} \\ T & I _ {n - q} \end{array} \right] = [ C \quad \mathbf {0} ]
$$

于是，考虑到传递函数矩阵在线性非奇异变换下保持不变，即有

$$
\begin{array}{l} G _ {K B} (s) = \widetilde {C} (s I - \bar {A}) ^ {- 1} \bar {B} = \widetilde {C} (s I - \widetilde {A}) ^ {- 1} \widetilde {B} \\ = [ C \quad 0 ] \left[ \begin{array}{c c} s I - A + B K & B K Q _ {2} \\ 0 & s I - F \end{array} \right] ^ {- 1} \left[ \begin{array}{l} B \\ 0 \end{array} \right] \\ = [ C \quad 0 ] \left[ \begin{array}{c c} (s I - A + B K) ^ {- 1} & * \\ 0 & (s I - F) ^ {- 1} \end{array} \right] \left[ \begin{array}{l} B \\ 0 \end{array} \right] \\ = C (s I - A + B K) ^ {- 1} B = G _ {K} (s) \tag {5.382} \\ \end{array}
$$

从而，证明完成。

(5) 一般地说, 包含观测器的状态反馈系统在鲁棒性上较直接状态反馈系统为差 $^{①}$ 。通常, 在考虑观测器的特征值时一条可供参考的选择原则是, 使观测器的特征值负实部是 A - BK 的特征值负实部的 2\~3 倍, 即

$$\operatorname{Re} \lambda_ {i} (F) = (2 \sim 3) \operatorname{Re} \lambda_ {i} (A - B K) \tag {5.383}$$

设计举例 现在,我们举例来说明包含观测器的状态反馈系统的设计步骤。

例 给定受控系统为

$$
\dot {x} = \left[ \begin{array}{c c c c} 0 & 1 & 0 & 0 \\ \hline 0 & 0 & - 2 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 4 & 0 \end{array} \right] x + \left[ \begin{array}{c} 0 \\ - - - \\ 1 \\ 0 \\ - 1 \end{array} \right] u
y = [ 1 \vdots 0 \quad 0 \quad 0 ] x
$$

（1）不考虑状态 x 的可量测性，设计满足性能要求的状态反馈增益阵 K。设性能指标的提法为一组期望的闭环特征值：

$$\lambda_ {1} ^ {*} = - 1, \lambda_ {2, 3} ^ {*} = - 1 \pm j, \lambda_ {4} ^ {*} = - 2$$

相应地，期望的闭环特征多项式为：

$$\alpha^ {*} (s) = (s + 1) (s + 1 - j) (s + 1 + j) (s + 2)= s ^ {4} + 5 s ^ {3} + 1 0 s ^ {2} + 1 0 s + 4$$

再表 K 为 $^{1)}$ :

$$\boldsymbol {K} = - \left[ k _ {1} \quad k _ {2} \quad k _ {3} \quad k _ {4} \right]$$

则可得

$$
A - b K = \left[ \begin{array}{c c c c} 0 & 1 & 0 & 0 \\ k _ {1} & k _ {2} & k _ {3} - 2 & k _ {4} \\ 0 & 0 & 0 & 1 \\ - k _ {1} & - k _ {2} & 4 - k _ {3} & - k _ {4} \end{array} \right]
$$

和

$$\alpha (s) = \det (s I - A + b K) = s ^ {4} + \left(k _ {4} - k _ {2}\right) s ^ {3} + \left(k _ {3} - k _ {1} - 4\right) s ^ {2} + 2 k _ {2} s + 2 k _ {1}$$

由比较 $a(s)$ 和 $a^{*}(s)$ ，即可定出：
