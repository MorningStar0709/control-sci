$$
\begin{array}{l} \operatorname{rank} \left[ \begin{array}{c c c c} \mathbf {C} ^ {\mathrm{T}} & \mathbf {A} ^ {\mathrm{T}} \mathbf {C} ^ {\mathrm{T}} & \dots & (\mathbf {A} ^ {\mathrm{T}}) ^ {n - 1} \mathbf {C} ^ {\mathrm{T}} \end{array} \right] \\ = \operatorname{rank} \left[ \begin{array}{l l l l} \boldsymbol {C} ^ {\mathrm{T}} & \left(\boldsymbol {A} ^ {\mathrm{T}} - \boldsymbol {C} ^ {\mathrm{T}} \boldsymbol {H} ^ {\mathrm{T}}\right) \boldsymbol {C} ^ {\mathrm{T}} & \dots & \left(\boldsymbol {A} ^ {\mathrm{T}} - \boldsymbol {C} ^ {\mathrm{T}} \boldsymbol {H} ^ {\mathrm{T}}\right) ^ {n - 1} \boldsymbol {C} ^ {\mathrm{T}} \end{array} \right] \\ = \operatorname{rank} \left[ \begin{array}{l l l l} \mathbf {C} ^ {\mathrm{T}} & (\mathbf {A} - \mathbf {H C}) ^ {\mathrm{T}} \mathbf {C} ^ {\mathrm{T}} & \dots & ((\mathbf {A} - \mathbf {H C}) ^ {\mathrm{T}}) ^ {n - 1} \mathbf {C} ^ {\mathrm{T}} \end{array} \right] \tag {9-220} \\ \end{array}
$$

上式表明，系统 $\Sigma_0$ 与系统 $\Sigma_H$ 可观测性判别阵的秩相等，这意味着若 $\Sigma_0$ 可观测，则 $\Sigma_H$ 也是可观测的，输出至状态微分反馈的引入不改变系统的可观测性。

由于系统 $(\boldsymbol{A}^{\mathrm{T}},\boldsymbol{C}^{\mathrm{T}},\boldsymbol{B}^{\mathrm{T}})$ 的可观测性判别阵为

$$
\begin{array}{l} \bar {\boldsymbol {S}} _ {0} = \left[ \begin{array}{l l l l} (\boldsymbol {B} ^ {\mathrm{T}}) ^ {\mathrm{T}} & (\boldsymbol {A} ^ {\mathrm{T}}) ^ {\mathrm{T}} (\boldsymbol {B} ^ {\mathrm{T}}) ^ {\mathrm{T}} & \dots & ((\boldsymbol {A} ^ {\mathrm{T}}) ^ {\mathrm{T}}) ^ {n - 1} (\boldsymbol {B} ^ {\mathrm{T}}) ^ {\mathrm{T}} \end{array} \right] \\ = \left[ \begin{array}{l l l l} \boldsymbol {B} & \boldsymbol {A B} & \dots & \boldsymbol {A} ^ {n - 1} \boldsymbol {B} \end{array} \right] \\ \end{array}
$$

系统 $((A^{\mathrm{T}}-C^{\mathrm{T}}H^{\mathrm{T}}),C^{\mathrm{T}},B^{\mathrm{T}})$ 的可观测性判别阵为

$$
\begin{array}{l} \bar {\boldsymbol {V}} _ {o H} = \left[ \begin{array}{l l l l} (\boldsymbol {B} ^ {T}) ^ {T} & (\boldsymbol {A} ^ {T} - \boldsymbol {C} ^ {T} \boldsymbol {H} ^ {T}) ^ {T} (\boldsymbol {B} ^ {T}) ^ {T} & \dots & ((\boldsymbol {A} ^ {T} - \boldsymbol {C} ^ {T} \boldsymbol {H} ^ {T}) ^ {T}) ^ {n - 1} (\boldsymbol {B} ^ {T}) ^ {T} \end{array} \right] \\ = \left[ \begin{array}{l l l l} \boldsymbol {B} & (\boldsymbol {A} - \boldsymbol {H C}) \boldsymbol {B} & \dots & (\boldsymbol {A} - \boldsymbol {H C}) ^ {n - 1} \boldsymbol {B} \end{array} \right] \\ \end{array}
$$
