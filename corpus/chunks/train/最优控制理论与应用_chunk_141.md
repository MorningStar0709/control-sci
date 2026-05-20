# 1）一步问题

首先考虑最后一段的最优控制问题, 即确定从采样时刻 k=N-1 到终止时刻 k=N 这一步上的最优控制 $U_{N-1}$ , 使这一步的指标函数为最小, 即

$$J _ {1} ^ {*} = \min _ {U _ {N - 1}} E \left\{\boldsymbol {X} _ {N} ^ {\mathrm{T}} \overline {{\boldsymbol {Q}}} _ {N} \boldsymbol {X} _ {N} + \boldsymbol {U} _ {N - 1} ^ {\mathrm{T}} \overline {{\boldsymbol {R}}} _ {N - 1} \boldsymbol {U} _ {N - 1} \right\} \tag {8-20}$$

将 $k = N - 1$ 时的状态转移方程(8-14)代入上式，消去 $\pmb{X}_N$ 后得到

$$J _ {1} ^ {*} = \min _ {\boldsymbol {U} _ {N - 1}} E \left\{\left(\boldsymbol {\Phi} _ {N, N - 1} \boldsymbol {X} _ {N - 1} + \boldsymbol {\Gamma} _ {N - 1} \boldsymbol {U} _ {N - 1} + \boldsymbol {W} _ {N - 1}\right) ^ {\mathrm{T}} \cdot \right. \tag {8-21}\overline {{{Q}}} _ {N} \left(\boldsymbol {\Phi} _ {N, N - 1} \boldsymbol {X} _ {N - 1} + \boldsymbol {\Gamma} _ {N - 1} \boldsymbol {U} _ {N - 1} + \boldsymbol {W} _ {N - 1}\right) + \boldsymbol {U} _ {N - 1} ^ {\mathrm{T}} \overline {{{R}}} _ {N - 1} \boldsymbol {U} _ {N - 1} \rbrace$$

将上式展开(为简明起见,暂时不写下标)得

$$J _ {1} ^ {*} = \min _ {U _ {N - 1}} E \left\{X ^ {\mathrm{T}} \Phi^ {\mathrm{T}} \overline {{{Q}}} \Phi X + X ^ {\mathrm{T}} \Phi^ {\mathrm{T}} \overline {{{Q}}} \Gamma U + X ^ {\mathrm{T}} \Phi^ {\mathrm{T}} \overline {{{Q}}} W + \right.\boldsymbol {W} ^ {\mathrm{T}} \overline {{\boldsymbol {Q}}} \boldsymbol {\Phi} \boldsymbol {X} + \boldsymbol {W} ^ {\mathrm{T}} \overline {{\boldsymbol {Q}}} \boldsymbol {\Gamma} \boldsymbol {U} + \boldsymbol {W} ^ {\mathrm{T}} \overline {{\boldsymbol {Q}}} \boldsymbol {W} + \boldsymbol {U} ^ {\mathrm{T}} \boldsymbol {\Gamma} ^ {\mathrm{T}} \overline {{\boldsymbol {Q}}} \boldsymbol {\Phi} \boldsymbol {X} +\boldsymbol {U} ^ {\mathrm{T}} \boldsymbol {\Gamma} ^ {\mathrm{T}} \overline {{\boldsymbol {Q}}} \boldsymbol {W} + \boldsymbol {U} ^ {\mathrm{T}} \left(\boldsymbol {\Gamma} ^ {\mathrm{T}} \overline {{\boldsymbol {Q}}} \boldsymbol {\Gamma} + \overline {{\boldsymbol {R}}}\right) \boldsymbol {U} \} \tag {8-22}$$

由于其中每一项均为标量,并且 $\overline{Q}$ 是对称阵,所以上式右端第二项等于第七项,第三项等于第四项,第五项等于第八项。于是
