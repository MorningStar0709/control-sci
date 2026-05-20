$$\text { 令 } \pmb {X} (k) = \pmb {X} _ {k} \quad \pmb {U} (k) = \pmb {U} _ {k} \quad \pmb {A} (k) = \pmb {\Phi} _ {k + 1, k}\boldsymbol {B} (k) = \boldsymbol {\Gamma} (k) \quad \boldsymbol {P} (N) = \boldsymbol {P} _ {N} \quad \boldsymbol {Q} (k) = \overline {{{\boldsymbol {Q}}}} _ {k},\boldsymbol {R} (k) = \overline {{{\boldsymbol {R}}}} _ {k} \quad \boldsymbol {K} (k) = \overline {{{\boldsymbol {K}}}} _ {k} \tag {8-6}\boldsymbol {X} _ {k + 1} = \boldsymbol {\Phi} _ {k + 1, k} \boldsymbol {X} _ {k} + \boldsymbol {\Gamma} _ {k} \boldsymbol {U} _ {k} \tag {8-7}J = \frac {1}{2} \boldsymbol {X} _ {N} ^ {\mathrm{T}} \boldsymbol {P} _ {N} \boldsymbol {X} _ {N} + \frac {1}{2} \sum_ {k = 0} ^ {N - 1} \left[ \boldsymbol {X} _ {k} ^ {\mathrm{T}} \overline {{\boldsymbol {Q}}} _ {k} \boldsymbol {X} _ {k} + \boldsymbol {U} _ {k} ^ {\mathrm{T}} \overline {{\boldsymbol {R}}} _ {k} \boldsymbol {U} _ {k} \right] \tag {8-8}\boldsymbol {U} _ {k} = - \left[ \overline {{\boldsymbol {R}}} _ {k} + \boldsymbol {\Gamma} _ {k} \overline {{\boldsymbol {K}}} _ {k + 1} \overline {{\boldsymbol {R}}} _ {k} \right] ^ {- 1} \boldsymbol {\Gamma} _ {k} ^ {\mathrm{T}} \overline {{\boldsymbol {K}}} _ {k + 1} \boldsymbol {\Phi} _ {k + 1, k} \boldsymbol {X} _ {k} \tag {8-9}$$

令

$$\boldsymbol {\Lambda} _ {k + 1} = \left[ \overline {{\boldsymbol {R}}} _ {k} + \boldsymbol {\Gamma} _ {k} \overline {{\boldsymbol {K}}} _ {k + 1} \overline {{\boldsymbol {R}}} _ {k} \right] ^ {- 1} \boldsymbol {\Gamma} _ {k} ^ {\mathrm{T}} \overline {{\boldsymbol {K}}} _ {k + 1} \tag {8-10}$$

其中， $\overline{K}_k$ 满足下面的矩阵黎卡提差分方程

$$\overline {{{K}}} _ {k} = \overline {{{Q}}} _ {k} + \boldsymbol {\Phi} _ {k + 1, k} ^ {\mathrm{T}} \overline {{{K}}} _ {k + 1} \boldsymbol {\Phi} _ {k + 1, k} -\boldsymbol {\Phi} _ {k + 1, k} ^ {\mathrm{T}} \overline {{\boldsymbol {K}}} _ {k + 1} \boldsymbol {\Gamma} _ {k} \left[ \overline {{\boldsymbol {R}}} _ {k} + \boldsymbol {\Gamma} _ {k} ^ {\mathrm{T}} \overline {{\boldsymbol {K}}} _ {k + 1} \boldsymbol {\Gamma} _ {k} \right] ^ {- 1} \boldsymbol {\Gamma} _ {k} ^ {\mathrm{T}} \overline {{\boldsymbol {K}}} _ {k + 1} \boldsymbol {\Phi} _ {k + 1, k} \tag {8-11}\overline {{{K}}} _ {N} = P _ {N} \tag {8-12}$$

故

$$\boldsymbol {U} _ {k} = - \boldsymbol {\Lambda} _ {k + 1} \boldsymbol {\Phi} _ {k + 1, k} \boldsymbol {X} _ {k} \tag {8-13}$$

现在来考虑 LQG 问题。随机线性系统的状态方程和测量方程为
