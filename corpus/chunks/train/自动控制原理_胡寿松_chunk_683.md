$$\dot {\boldsymbol {x}} = \boldsymbol {A} \boldsymbol {x} + \boldsymbol {B} \boldsymbol {u} = [ (\boldsymbol {A} - \boldsymbol {B} \boldsymbol {K}) + \boldsymbol {B} \boldsymbol {K} ] \boldsymbol {x} + \boldsymbol {B} \boldsymbol {u}$$

同理可得

$$\operatorname{rank} \mathbf {S} _ {c} \leqslant \operatorname{rank} \mathbf {S} _ {c K} \tag {9-218}$$

由式(9-217)和式(9-218)可得

$$\operatorname{rank} \mathbf {S} _ {c K} = \operatorname{rank} \mathbf {S} _ {c} \tag {9-219}$$

从而当且仅当 $\Sigma_{0}$ 可控时， $\Sigma_{K}$ 可控。

再来证明状态反馈系统不一定能保持可观测性，对此只需举一反例说明。例如，考察

$$
\dot {\boldsymbol {x}} = \left[ \begin{array}{l l} 1 & 2 \\ 0 & 3 \end{array} \right] \boldsymbol {x} + \left[ \begin{array}{l} 0 \\ 1 \end{array} \right] \boldsymbol {u}, \quad y = [ 1 \quad 1 ] \boldsymbol {x}
$$

其可观测性判别阵

$$
\mathbf {V} _ {o} = \left[ \begin{array}{l} c \\ c A \end{array} \right] = \left[ \begin{array}{l l} 1 & 1 \\ 1 & 5 \end{array} \right], \quad \operatorname{rank} \mathbf {V} _ {o} = n = 2
$$

故该系统可观测。现引入状态反馈，取 $k = [0, 4]$ ，则状态反馈系统 $\Sigma_{K}$ 为

$$
\dot {\boldsymbol {x}} = (\boldsymbol {A} - \boldsymbol {b k}) \boldsymbol {x} + \boldsymbol {b v} = \left[ \begin{array}{c c} 1 & 2 \\ 0 & - 1 \end{array} \right] \boldsymbol {x} + \left[ \begin{array}{l} 0 \\ 1 \end{array} \right] \boldsymbol {v}, \quad y = [ 1, 1 ] \boldsymbol {x}
$$

其可观测性判别阵

$$
\mathbf {V} _ {\alpha K} = \left[ \begin{array}{c} \mathbf {c} \\ \mathbf {c} (\mathbf {A} - \mathbf {b k}) \end{array} \right] = \left[ \begin{array}{l l} 1 & 1 \\ 1 & 1 \end{array} \right], \quad \operatorname{rank} \mathbf {V} _ {\alpha K} = 1 <   n = 2
$$

故该状态反馈系统为不可观测。而若取 $k = [0 - 5]$ ，则通过计算可知，此时它成为可观测的。这表明状态反馈可能改变系统的可观测性，其原因是状态反馈造成了所配置的极点与零点相对消。

定理 9-2 对于系统(9-208)，输出至状态微分反馈的引入不改变系统的可观测性，但可能改变系统的可控性。

证明 用对偶定理证明。设被控对象 $\Sigma_0$ 为 $(A, B, C)$ ，将输出反馈至状态微分的系统 $\Sigma_H$ 为 $((A - HC), B, C)$ ，若 $(A, B, C)$ 可观测，则对偶系统 $(A^{\mathrm{T}}, C^{\mathrm{T}}, B^{\mathrm{T}})$ 可控，由定理9-1可知，系统 $(A^{\mathrm{T}}, C^{\mathrm{T}}, B^{\mathrm{T}})$ 加入状态反馈后的系统 $((A^{\mathrm{T}} - C^{\mathrm{T}}H^{\mathrm{T}}), C^{\mathrm{T}}, B^{\mathrm{T}})$ 的可控性不变，但可能改变其可观测性。因而有
