实际上，我们可以用状态反馈将系统极点转移到任意期望的位置上，这对控制系统设计具有非常显著的效果。本节研究结果表明，如果能把 $(A, B)$ 转换成能控形 $(A_{\mathrm{c}}, B_{\mathrm{c}})$ ，那么实现上述转移是可能的，反之若系统能控就可以将 $(A, B)$ 变换成 $(A_{\mathrm{c}}, B_{\mathrm{c}})$ 。系统不可控的情况很少见，但如果系统不可控，就不能找到产生任意极点位置的控制律。不可控系统的某些模态或子系统不受控制律的影响。这通常是指，系统中的某些部分在物理意义上没有与输入连接上。例如，具有不同极点的系统，如果在它的模态标准形中矩阵 $B_{\mathrm{m}}$ 有一个零元素，那么状态矢量中就有一个模态没有连接到系统的输入上。从理想的物理角度来认识受控系统将有碍于不可控系统的控制器设计。如前所述，虽然可以用代数判据对可控性进行判别，但是，没有任何数学判据可以取代控制工程师对物理系统的理解。实际情况通常是这样的，每一个状态在一定程度上都是可控的，而用数学判据表明系统是可控时，某些状态的可控性非常弱，以至于对这些状态进行的控制设计实际上是毫无意义的。

飞机控制就是某些状态为弱可控性的一个很好的例子。俯仰角运动 $x_{\mathrm{p}}$ 主要受升降舵 $\delta_{\mathrm{e}}$ 的影响，同时也轻微地受横摇运动 $x_{\mathrm{r}}$ 的影响。而横摇运动本质上只受副翼 $\delta_{\mathrm{a}}$ 的影响。这些量之间的状态空间描述为

$$
\left[ \begin{array}{l} \dot {\boldsymbol {x}} _ {\mathrm{p}} \\ \dot {\boldsymbol {x}} _ {\mathrm{r}} \end{array} \right] = \left[ \begin{array}{c c} \boldsymbol {A} _ {\mathrm{p}} & \varepsilon \\ 0 & \boldsymbol {A} _ {\mathrm{r}} \end{array} \right] \left[ \begin{array}{l} \boldsymbol {x} _ {\mathrm{p}} \\ \boldsymbol {x} _ {\mathrm{r}} \end{array} \right] + \left[ \begin{array}{c c} \boldsymbol {B} _ {\mathrm{p}} & 0 \\ 0 & \boldsymbol {B} _ {\mathrm{r}} \end{array} \right] \left[ \begin{array}{l} \delta_ {\mathrm{e}} \\ \delta_ {\mathrm{a}} \end{array} \right] \tag {7.93}
$$

其中，由微小元素 $\varepsilon$ 构成的矩阵表示从横摇运动到俯仰运动的弱耦合。该系统的可控性数学判据表明副翼和升降舵是能控制俯仰翼运动（即高度）的。但是，试图用副翼横摇飞行器来控制飞机的高度是不现实的。

下面再举一例来说明用状态反馈进行极点配置的一些特点，以及可控性丧失对该过程的影响。
