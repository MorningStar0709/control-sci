$$J _ {1} ^ {*} = E \left\{\boldsymbol {X} ^ {\mathrm{T}} \boldsymbol {\Phi} ^ {\mathrm{T}} \overline {{\boldsymbol {Q}}} \boldsymbol {\Phi} \boldsymbol {X} + \boldsymbol {W} ^ {\mathrm{T}} \overline {{\boldsymbol {Q}}} \boldsymbol {W} + \widetilde {\boldsymbol {X}} ^ {\mathrm{T}} \boldsymbol {S} \widetilde {\boldsymbol {X}} - \boldsymbol {X} ^ {\mathrm{T}} \boldsymbol {S} \boldsymbol {X} \right\}$$

利用式 $(8-35)$ 合并同类项,并恢复下标,可得

$$J _ {1} ^ {*} = E \left\{\boldsymbol {X} _ {N - 1} ^ {\mathrm{T}} \boldsymbol {\Phi} _ {N, N - 1} ^ {\mathrm{T}} \widetilde {\boldsymbol {Q}} _ {N} \boldsymbol {\Phi} _ {N, N - 1} \boldsymbol {X} _ {N - 1} \right\} + \alpha_ {N - 1} \tag {8-38}$$

式中

$$\widetilde {\boldsymbol {Q}} _ {N} = \boldsymbol {Q} _ {N} ^ {0} - \boldsymbol {Q} _ {N} ^ {0} \boldsymbol {\Gamma} _ {N - 1} \boldsymbol {\Lambda} _ {N}, \quad \boldsymbol {Q} _ {N} ^ {0} = \overline {{{{\boldsymbol {Q}}}}} _ {N} \tag {8-39}\alpha_ {N - 1} = E \left\{\boldsymbol {W} _ {N - 1} ^ {\mathrm{T}} \boldsymbol {Q} _ {N} ^ {0} \boldsymbol {W} _ {N - 1} + \widetilde {\boldsymbol {X}} _ {N - 1} ^ {\mathrm{T}} \boldsymbol {\Phi} _ {N, N - 1} ^ {\mathrm{T}} \boldsymbol {Q} _ {N} ^ {0} \boldsymbol {\Gamma} _ {N - 1} \boldsymbol {\Lambda} _ {N} \boldsymbol {\Phi} _ {N, N - 1} \widetilde {\boldsymbol {X}} _ {N - 1} \right\} \tag {8-40}$$

$\alpha_{N - 1}$ 反映了由动态噪声 $\pmb{W}_{N - 1}$ 和滤波误差 $\widetilde{\pmb{X}}_{N - 1}$ 造成的指标函数的增加。在确定性最优控制中因 $Q_N^0$ 为0，这项将为0。
