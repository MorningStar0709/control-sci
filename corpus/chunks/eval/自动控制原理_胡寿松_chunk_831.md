# (2) 最优解结果

定理 10-20 在问题 10-3 中, 若对于任意矩阵 D, 有 $DD^{T}=Q$ , 且 $\bar{P}$ 是里卡蒂矩阵代数方程

$$\overline {{\boldsymbol {P}}} \boldsymbol {A} + \boldsymbol {A} ^ {\mathrm{T}} \overline {{\boldsymbol {P}}} - \overline {{\boldsymbol {P}}} \boldsymbol {B} \boldsymbol {R} ^ {- 1} \boldsymbol {B} ^ {\mathrm{T}} \overline {{\boldsymbol {P}}} + \boldsymbol {Q} = \boldsymbol {0}$$

的解，则阵对 $\{\pmb {A},\pmb {D}\}$ 完全可观的充分必要条件是 $\bar{P}$ 为对称正定矩阵。

定理 10-21 对于问题 10-3, 若阵对 $\{A, B\}$ 完全可控, 阵对 $\{A, D\}$ 完全可观, 其中 $DD^{T}=Q$ , 且 D 任意, 则存在唯一的最优控制

$$\boldsymbol {u} ^ {*} (t) = - \boldsymbol {R} ^ {- 1} \boldsymbol {B} ^ {\mathrm{T}} \bar {\boldsymbol {P}} \boldsymbol {x} (x) \tag {10-121}$$

最优性能指标为

$$J ^ {*} = \frac {1}{2} \boldsymbol {x} ^ {\mathrm{T}} (0) \overline {{{\boldsymbol {P}}}} \boldsymbol {x} (0) \tag {10-122}$$

式中， $\bar{P}$ 为对称正定常阵，是里卡蒂矩阵代数方程

$$\overline {{{\boldsymbol {P}}}} \boldsymbol {A} + \boldsymbol {A} ^ {\mathrm{T}} \overline {{{\boldsymbol {P}}}} - \overline {{{\boldsymbol {P}}}} \boldsymbol {B} \boldsymbol {R} ^ {- 1} \boldsymbol {B} ^ {\mathrm{T}} \overline {{{\boldsymbol {P}}}} + \boldsymbol {Q} = \boldsymbol {0} \tag {10-123}$$

的唯一解。
