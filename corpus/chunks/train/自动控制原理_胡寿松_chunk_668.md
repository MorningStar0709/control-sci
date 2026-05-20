$$
\begin{array}{l} \operatorname{rank} S ^ {\prime} = \operatorname{rank} \left[ \begin{array}{l l l l l} P ^ {- 1} B & (P ^ {- 1} A P) P ^ {- 1} B & (P ^ {- 1} A P) ^ {2} P ^ {- 1} B & \dots & (P ^ {- 1} A P) ^ {n - 1} P ^ {- 1} B \end{array} \right] \\ = \operatorname{rank} \left[ \begin{array}{l l l l l} P ^ {- 1} B & P ^ {- 1} A B & P ^ {- 1} A ^ {2} B & \dots & P ^ {- 1} A ^ {n - 1} B \end{array} \right] \\ = \operatorname{rank} P ^ {- 1} \left[ \begin{array}{l l l l l} B & A B & A ^ {2} B & \dots & A ^ {n - 1} B \end{array} \right] \\ = \operatorname{rank} [ \boldsymbol {B} \quad \boldsymbol {A B} \quad \boldsymbol {A} ^ {2} \boldsymbol {B} \quad \dots \quad \boldsymbol {A} ^ {n - 1} \boldsymbol {B} ] = \operatorname{rank} S \\ \end{array}
$$

式中， $S'$ 为变换后系统的可控性矩阵；S 为变换前系统的可控性矩阵。可见，变换后与变换前系统可控性矩阵的秩相等，根据系统可控性的秩判据可知，对于非奇异线性变换，系统的可控性不变。

4）变换后系统可观测性不变。设变换后系统的可观测性矩阵为 $V'$ ，变换前系统的可观测性矩阵为 V，则有
