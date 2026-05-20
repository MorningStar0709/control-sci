$$\boldsymbol {U} _ {N - 1} = - \left(\boldsymbol {\Gamma} _ {N - 1} ^ {\mathrm{T}} \overline {{\boldsymbol {Q}}} _ {N} \boldsymbol {\Gamma} _ {N - 1} + \overline {{\boldsymbol {R}}} _ {N - 1}\right) ^ {- 1} \boldsymbol {\Gamma} _ {N - 1} ^ {\mathrm{T}} \overline {{\boldsymbol {Q}}} _ {N} \boldsymbol {\Phi} _ {N, N - 1} \hat {\boldsymbol {X}} _ {N - 1} \quad (8 - 3 0)$$

把上式与确定性最优控制的解式(8-13)(令 $k = N - 1$ )对照，并注意式(8-12)即 $\overline{\pmb{Q}}_N = \pmb{P}_N = \overline{\pmb{K}}_N$ ，可见两者形式完全一样，只是将 $\hat{\pmb{X}}_{N - 1}$ 代 $\pmb{X}_{N - 1}$ 而已。式(8-30)还可简化为

$$\boldsymbol {U} _ {N - 1} = - \boldsymbol {\Lambda} _ {N} \boldsymbol {\Phi} _ {N, N - 1} \hat {\boldsymbol {X}} _ {N - 1} \tag {8-31}$$

其中

$$\boldsymbol {\Lambda} _ {N} = \left(\boldsymbol {\Gamma} _ {N - 1} ^ {\mathrm{T}} \overline {{\boldsymbol {Q}}} _ {N} \boldsymbol {\Gamma} _ {N - 1} + \overline {{\boldsymbol {R}}} _ {N - 1}\right) ^ {- 1} \boldsymbol {\Gamma} _ {N - 1} ^ {\mathrm{T}} \overline {{\boldsymbol {Q}}} _ {N} \tag {8-32}$$

这样,就证明了分离定理对最后一步来讲是正确的。

下面来计算最后一段的最优指标值 $J_{1}^{*}$ 。将式(8-31)代入式(8-25)得

$$J _ {1} ^ {*} = E \left\{\boldsymbol {X} _ {N - 1} ^ {\mathrm{T}} \boldsymbol {\Phi} _ {N, N - 1} ^ {\mathrm{T}} \overline {{{\boldsymbol {Q}}}} _ {N} \boldsymbol {\Phi} _ {N, N - 1} \boldsymbol {X} _ {N - 1} - \right.2 \boldsymbol {X} _ {N - 1} ^ {\mathrm{T}} \boldsymbol {\Phi} _ {N, N - 1} ^ {\mathrm{T}} \overline {{\boldsymbol {Q}}} _ {N} \boldsymbol {\Gamma} _ {N - 1} \boldsymbol {\Lambda} _ {N} \boldsymbol {\Phi} _ {N, N - 1} \hat {\boldsymbol {X}} _ {N - 1} +\boldsymbol {W} _ {N - 1} ^ {\mathrm{T}} \overline {{\boldsymbol {Q}}} _ {N} \boldsymbol {W} _ {N - 1} + \hat {\boldsymbol {X}} _ {N - 1} ^ {\mathrm{T}} \boldsymbol {\Phi} _ {N, N - 1} ^ {\mathrm{T}} \boldsymbol {\Lambda} _ {N} ^ {\mathrm{T}} \left(\boldsymbol {\Gamma} _ {N - 1} ^ {\mathrm{T}} \overline {{\boldsymbol {Q}}} _ {N} \boldsymbol {\Gamma} _ {N - 1} + \right.\left. \overline {{{\boldsymbol {R}}}} _ {N - 1}\right) \boldsymbol {\Lambda} _ {N} \boldsymbol {\Phi} _ {N, N - 1} \hat {\boldsymbol {X}} _ {N - 1} \rbrace \tag {8-33}$$

上式第二项可写成(略去下标)
