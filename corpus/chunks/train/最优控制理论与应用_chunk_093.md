$$\boldsymbol {U} (k) = - \boldsymbol {R} ^ {- 1} (k) \boldsymbol {B} ^ {\mathrm{T}} (k) \boldsymbol {K} (k + 1) [ \boldsymbol {I} + \boldsymbol {B} (k) \boldsymbol {R} ^ {- 1} (k) \boldsymbol {B} ^ {\mathrm{T}} (k) \boldsymbol {K} (k + 1) ] ^ {- 1} \cdot\boldsymbol {A} (k) \boldsymbol {X} (k)= - \boldsymbol {R} ^ {- 1} (k) \boldsymbol {B} ^ {\mathrm{T}} (k) \boldsymbol {K} (k + 1) [ \boldsymbol {I} + \boldsymbol {B} (k) \boldsymbol {R} ^ {- 1} (k) \boldsymbol {B} ^ {\mathrm{T}} (k) \boldsymbol {K} (k + 1) ] ^ {- 1} \cdot\left\{\left[ \boldsymbol {I} + \boldsymbol {B} (k) \boldsymbol {R} ^ {- 1} (k) \boldsymbol {B} ^ {\mathrm{T}} (k) \boldsymbol {K} (k + 1) \right] - \right.\boldsymbol {B} (k) \boldsymbol {R} ^ {- 1} (k) \boldsymbol {B} ^ {\mathrm{T}} (k) \boldsymbol {K} (k + 1) \mid \boldsymbol {A} (k) \boldsymbol {X} (k)= - \boldsymbol {R} ^ {- 1} (k) \boldsymbol {B} ^ {\mathrm{T}} (k) \boldsymbol {K} (k + 1) \left\{\boldsymbol {I} - [ \boldsymbol {I} + \boldsymbol {B} (k) \boldsymbol {R} ^ {- 1} (k) \boldsymbol {B} ^ {\mathrm{T}} (k) \boldsymbol {K} (k + 1) ] ^ {- 1} \cdot \right.\boldsymbol {B} (k) \boldsymbol {R} ^ {- 1} (k) \boldsymbol {B} ^ {\mathrm{T}} (k) \boldsymbol {K} (k + 1) \} \boldsymbol {A} (k) \boldsymbol {X} (k)= - \left\{\boldsymbol {R} ^ {- 1} (k) - \boldsymbol {R} ^ {- 1} (k) \boldsymbol {B} ^ {\mathrm{T}} (k) \boldsymbol {K} (k + 1) [ \boldsymbol {I} + \right.\left. \boldsymbol {B} (k) \boldsymbol {R} ^ {- 1} (k) \boldsymbol {B} ^ {\mathrm{T}} (k) \boldsymbol {K} (k + 1) \right] ^ {- 1} \boldsymbol {B} (k) \boldsymbol {R} ^ {- 1} (k) \left\{\boldsymbol {B} ^ {\mathrm{T}} (k) \boldsymbol {K} (k + 1) \boldsymbol {A} (k) \boldsymbol {X} (k) \right.$$

对上式花括号内引用前面的矩阵求逆引理：

取 $\mathbf{A} = \mathbf{R}(k),\mathbf{B} = \mathbf{B}^{\mathrm{T}}(k)\mathbf{K}(k + 1),\mathbf{C} = \mathbf{B}(k)$ 可得

$$\boldsymbol {U} (k) = - \left[ \boldsymbol {R} (k) + \boldsymbol {B} ^ {\mathrm{T}} (k) \boldsymbol {K} (k + 1) \boldsymbol {B} (k) \right] ^ {- 1} \boldsymbol {B} ^ {\mathrm{T}} (k) \boldsymbol {K} (k + 1) \boldsymbol {A} (k) \boldsymbol {X} (k)= - \boldsymbol {L} (k) \boldsymbol {X} (k) \tag {5-64}L (k) = \left[ \boldsymbol {R} (k) + \boldsymbol {B} ^ {\mathrm{T}} (k) \boldsymbol {K} (k + 1) \boldsymbol {B} (k) \right] ^ {- 1} \boldsymbol {B} ^ {\mathrm{T}} (k) \boldsymbol {K} (k + 1) \boldsymbol {A} (k) \tag {5-65}$$

$L(k)$ 是最优反馈增益阵。

例5-4 设系统状态方程为

$$x (k + 1) = x (k) + u (k) \qquad x (0) \text {给定} \tag {5-66}$$

性能指标为
