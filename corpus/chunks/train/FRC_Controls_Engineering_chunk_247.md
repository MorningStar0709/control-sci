$$
\mathbf {x} = \left[ \begin{array}{c} x \\ y \\ \theta \\ v _ {l} \\ v _ {r} \end{array} \right] = \left[ \begin{array}{c} \text {x position} \\ \text {y position} \\ \text {heading} \\ \text {left velocity} \\ \text {right velocity} \end{array} \right] \quad \mathbf {u} = \left[ \begin{array}{c} V _ {l} \\ V _ {r} \end{array} \right] = \left[ \begin{array}{c} \text {left voltage} \\ \text {right voltage} \end{array} \right]

\mathbf {A} = \left. \frac {\partial f (\mathbf {x})}{\partial \mathbf {x}} \right| _ {\theta = 0} = \left[ \begin{array}{c c c c c} 0 & 0 & 0 & \frac {1}{2} & \frac {1}{2} \\ 0 & 0 & v & 0 & 0 \\ 0 & 0 & 0 & - \frac {1}{2 r _ {b}} & \frac {1}{2 r _ {b}} \\ 0 & 0 & 0 & \left(\frac {1}{m} + \frac {r _ {b} ^ {2}}{J}\right) C _ {1} & \left(\frac {1}{m} - \frac {r _ {b} ^ {2}}{J}\right) C _ {3} \\ 0 & 0 & 0 & \left(\frac {1}{m} - \frac {r _ {b} ^ {2}}{J}\right) C _ {1} & \left(\frac {1}{m} + \frac {r _ {b} ^ {2}}{J}\right) C _ {3} \end{array} \right] \tag {8.15}

\mathbf {B} = \left[ \begin{array}{c c} 0 & 0 \\ 0 & 0 \\ 0 & 0 \\ \left(\frac {1}{m} + \frac {r _ {b} ^ {2}}{J}\right) C _ {2} & \left(\frac {1}{m} - \frac {r _ {b} ^ {2}}{J}\right) C _ {4} \\ \left(\frac {1}{m} - \frac {r _ {b} ^ {2}}{J}\right) C _ {2} & \left(\frac {1}{m} + \frac {r _ {b} ^ {2}}{J}\right) C _ {4} \end{array} \right] \tag {8.16}
$$

where $\begin{array} { r } { v = \frac { v _ { l } + v _ { r } } { 2 } , C _ { 1 } = - \frac { G _ { l } ^ { 2 } K _ { t } } { K _ { v } R r ^ { 2 } } , C _ { 2 } = \frac { G _ { l } K _ { t } } { R r } , C _ { 3 } = - \frac { G _ { r } ^ { 2 } K _ { t } } { K _ { v } R r ^ { 2 } } } \end{array}$ = GlKt , C = − G2rKt2 , and C4 = GrKt . $\begin{array} { r } { C _ { 4 } = \frac { G _ { r } K _ { t } } { R r } } \end{array}$ The constants $C _ { 1 }$ through $C _ { 4 }$ are from the derivation in section 12.6.

The linear time-varying differential drive controller is

$$
\mathbf {u} = \mathbf {K} \left[ \begin{array}{c c c} \cos \theta & \sin \theta & \\ - \sin \theta & \cos \theta & \mathbf {0} _ {2 \times 3} \\ \hline \mathbf {0} _ {3 \times 2} & & \mathbf {I} _ {3 \times 3} \end{array} \right] (\mathbf {r} - \mathbf {x}) \tag {8.17}
$$

At each timestep, the LQR controller gain K is computed for the (A, B) pair evaluated at the current state.
