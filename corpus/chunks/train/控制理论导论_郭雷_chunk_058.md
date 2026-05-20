$$
\begin{array}{l} \mu = \operatorname{rank} [ \overline {{{B}}}, \overline {{{A B}}}, \dots , \overline {{{A}}} ^ {n - 1} \overline {{{B}}} ] \\ = \operatorname{rank} \left[ \begin{array}{c c c c} \overline {{B}} _ {1} & \overline {{A}} _ {1 1} \overline {{B}} _ {1} & \dots & \overline {{A}} _ {1 1} ^ {n - 1} \overline {{B}} _ {1} \\ \overline {{B}} _ {2} & \overline {{A}} _ {2 1} \overline {{B}} _ {1} + \overline {{A}} _ {2 2} \overline {{B}} _ {2} & \dots & * \\ 0 & 0 & \dots & 0 \\ 0 & 0 & \dots & 0 \end{array} \right] \\ = \operatorname{rank} \left[ \left[ \begin{array}{c} \overline {{B}} _ {1} \\ \overline {{B}} _ {2} \end{array} \right], \left[ \begin{array}{c c} \overline {{A}} _ {1 1} & 0 \\ \overline {{A}} _ {2 1} & \overline {{A}} _ {2 2} \end{array} \right] \left[ \begin{array}{c} \overline {{B}} _ {1} \\ \overline {{B}} _ {2} \end{array} \right], \dots , \left[ \begin{array}{c c} \overline {{A}} _ {1 1} & 0 \\ \overline {{A}} _ {2 1} & \overline {{A}} _ {2 2} \end{array} \right] ^ {\mu - 1} \left[ \begin{array}{c} \overline {{B}} _ {1} \\ \overline {{B}} _ {2} \end{array} \right] \right]. \\ \end{array}
$$

由此可见，矩阵对

$$
\left(\left[ \begin{array}{c c} {\overline {{{A}}} _ {1 1}} & {0} \\ {\overline {{{A}}} _ {2 1}} & {\overline {{{A}}} _ {2 2}} \end{array} \right], \left[ \begin{array}{c} {\overline {{{B}}} _ {1}} \\ {\overline {{{B}}} _ {2}} \end{array} \right]\right) \quad \text {能控.}
$$

同时，还可以看出，

$$\operatorname{rank} \left[ \overline {{{B}}} _ {1}, \overline {{{A}}} _ {1 1} \overline {{{B}}} _ {1}, \dots , \overline {{{A}}} _ {1 1} ^ {n _ {1} - 1} \overline {{{B}}} _ {1} \right] = n _ {1}.$$

这说明 $(\overline{A}_{11},\overline{B}_1)$ 能控.

同理，由能观测性矩阵出发可以证明，矩阵对

$$
\left(\left[ \begin{array}{c c} {\overline {{{A}}} _ {1 1}} & {\overline {{{A}}} _ {1 3}} \\ {0} & {\overline {{{A}}} _ {3 3}} \end{array} \right], [ \overline {{{C}}} _ {1} & \overline {{{C}}} _ {3} ]\right) \quad \text {能观测},
$$

并且 $(\overline{A}_{11},\overline{C}_1)$ 能观测．这就完成了定理的证明.

定理1.3.10说明，一个定常线性系统经适当的坐标变换，可以把它分解成四个子系统，一个是既能控又能观测子系统，一个是能控但不能观测子系统，一个是不能控但能观测子系统，一个是既不能控又不能观测子系统。这就是定常线性系统的标准结构。

假设系统 (1.3.18) 的传递函数矩阵为 $\overline{\pmb{W}}(s)$ , 不难计算

$$\overline {{{\boldsymbol {W}}}} (s) = \overline {{{\boldsymbol {C}}}} _ {1} (s \boldsymbol {I} _ {n _ {1}} - \overline {{{\boldsymbol {A}}}} _ {1 1}) ^ {- 1} \overline {{{\boldsymbol {B}}}} _ {1}.$$

由于坐标变换保持系统的传递函数矩阵不变，因此有

$$\boldsymbol {W} (s) = \overline {{\boldsymbol {C}}} _ {1} (s \boldsymbol {I} _ {n _ {1}} - \overline {{\boldsymbol {A}}} _ {1 1}) ^ {- 1} \overline {{\boldsymbol {B}}} _ {1}. \tag {1.3.20}$$

这表明定常线性系统的传递函数矩阵仅仅刻画了系统的既能控又能观测的子系统的特性，而反映不出那些不能控或不能观测的子系统的特性.
