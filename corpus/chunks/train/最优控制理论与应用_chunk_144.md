和 $E\left[\boldsymbol{U}_{N - 1}^{\mathrm{T}}\left(\boldsymbol{\Gamma}_{N - 1}^{\mathrm{T}}\overline{\boldsymbol{Q}}_{N}\boldsymbol{\Gamma}_{N - 1} + \overline{\boldsymbol{R}}_{N}\right)\boldsymbol{U}_{N - 1}\mid \boldsymbol{Z}^{N - 1},m_0\right] = \boldsymbol{U}_{N - 1}^{\mathrm{T}}\left(\boldsymbol{\Gamma}_{N - 1}^{\mathrm{T}}\overline{\boldsymbol{Q}}_{N}\boldsymbol{\Gamma}_{N - 1} + \right.$ $\overline{\boldsymbol{R}}_{N - 1})\boldsymbol{U}_{N - 1}$ 然后，将这些与 $\pmb{U}_{N - 1}$ 有关的项对 $\pmb{U}_{N - 1}$ 求导并令其等于零，即

$$\frac {\partial}{\partial \boldsymbol {U} _ {N - 1}} \left\{2 E \left[ \boldsymbol {X} _ {N - 1} ^ {\mathrm{T}} \mid \boldsymbol {Z} ^ {N - 1}, m _ {0} \right] \boldsymbol {\Phi} _ {N, N - 1} ^ {\mathrm{T}} \overline {{{\boldsymbol {Q}}}} _ {N} \boldsymbol {\Gamma} _ {N - 1} \boldsymbol {U} _ {N - 1} + \right.\boldsymbol {U} _ {N - 1} ^ {\mathrm{T}} \left(\boldsymbol {\Gamma} _ {N - 1} ^ {\mathrm{T}} \overline {{\boldsymbol {Q}}} _ {N} \boldsymbol {\Gamma} _ {N - 1} + \overline {{\boldsymbol {R}}} _ {N - 1}\right) \boldsymbol {U} _ {N - 1} \rbrace = \boldsymbol {0}$$

利用标量对向量的求导公式,可得

$$2 \boldsymbol {\Gamma} _ {N - 1} ^ {\mathrm{T}} \overline {{\boldsymbol {Q}}} _ {N} \boldsymbol {\Phi} _ {N, N - 1} E [ \boldsymbol {X} _ {N - 1} | \boldsymbol {Z} ^ {N - 1}, m _ {0} ] +2 \left(\boldsymbol {\Gamma} _ {N - 1} ^ {\mathrm{T}} \overline {{\boldsymbol {Q}}} _ {N} \boldsymbol {\Gamma} _ {N - 1} + \overline {{\boldsymbol {R}}} _ {N - 1}\right) \boldsymbol {U} _ {N - 1} = \boldsymbol {0}$$

由此解出最优控制 $U_{N - 1}$ 为

$$\boldsymbol {U} _ {N - 1} = - \left(\boldsymbol {\Gamma} _ {N - 1} ^ {\mathrm{T}} \overline {{{\boldsymbol {Q}}}} _ {N} \boldsymbol {\Gamma} _ {N - 1} + \overline {{{\boldsymbol {R}}}} _ {N - 1}\right) ^ {- 1} \boldsymbol {\Gamma} _ {N - 1} ^ {\mathrm{T}} \overline {{{\boldsymbol {Q}}}} _ {N} \boldsymbol {\Phi} _ {N, N - 1} E \left[ \boldsymbol {X} _ {N - 1} \mid \boldsymbol {Z} ^ {N - 1}, m _ {0} \right] \tag {8-28}$$

最小方差估计即条件均值,在高斯分布情况下,线性最小方差估计即最小方差估计,因为卡尔曼滤波值是线性最小方差估计,故滤波值 $\hat{X}_{N-1}$ 就是条件均值,即

$$E \left[ \boldsymbol {X} _ {N - 1} \mid \boldsymbol {Z} ^ {N - 1}, m _ {0} \right] = \hat {\boldsymbol {X}} _ {N - 1} \tag {8-29}$$

于是式(8-28)可成
