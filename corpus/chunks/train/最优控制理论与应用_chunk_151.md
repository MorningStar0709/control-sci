# 3）一般结果

类似于从一步问题至两步问题的推演过程,由后向前算第 N-K 步(即由前向后算第 K 步)的最优指标为

$$J _ {N - k} = \min _ {\boldsymbol {U} _ {k}} \left\{E \left\{\boldsymbol {X} _ {k + 1} ^ {\mathrm{T}} \overline {{\boldsymbol {Q}}} _ {k + 1} \boldsymbol {X} _ {k + 1} + \boldsymbol {U} _ {k} ^ {\mathrm{T}} \overline {{\boldsymbol {R}}} _ {k} \boldsymbol {U} _ {k} \right\} + J _ {N - k - 1} ^ {*} \right\} \tag {8-50}$$

采用数学归纳法即可得出如下的一般结果

$$\boldsymbol {U} _ {k} = - \boldsymbol {\Lambda} _ {k + 1} \boldsymbol {\Phi} _ {k + 1, k} \hat {\boldsymbol {X}} _ {k} \tag {8-51}\boldsymbol {\Lambda} _ {k + 1} = \left(\boldsymbol {\Gamma} _ {k} ^ {\mathrm{T}} \boldsymbol {Q} _ {k + 1} ^ {0} \boldsymbol {\Gamma} _ {k} + \overline {{\boldsymbol {R}}} _ {k}\right) ^ {- 1} \boldsymbol {\Gamma} _ {k} ^ {\mathrm{T}} \boldsymbol {Q} _ {k + 1} ^ {0} \tag {8-52}\boldsymbol {Q} _ {k + 1} ^ {0} = \overline {{\boldsymbol {Q}}} _ {k + 1} + \boldsymbol {\Phi} _ {k + 2, k + 1} ^ {\mathrm{T}} \widetilde {\boldsymbol {Q}} _ {k + 2} \boldsymbol {\Phi} _ {k + 2, k + 1} \tag {8-53}\widetilde {\boldsymbol {Q}} _ {k + 1} = \boldsymbol {Q} _ {k + 1} ^ {0} - \boldsymbol {Q} _ {k + 1} ^ {0} \boldsymbol {\Gamma} _ {k} \boldsymbol {\Lambda} _ {k + 1} \tag {8-54}J _ {N - k} ^ {*} = E \left\{X _ {k} ^ {\mathrm{T}} \Phi_ {k + 1, k} \widetilde {Q} _ {k + 1} \Phi_ {k + 1, k} X _ {k} \right\} + \alpha_ {k}\alpha_ {k} = E \left\{\sum_ {j = 1} ^ {N - k} \left(\boldsymbol {W} _ {N - j} ^ {\mathrm{T}} \boldsymbol {Q} _ {N - j + 1} ^ {0} \boldsymbol {W} _ {N - j} + \right. \right.\left. \widetilde {\boldsymbol {X}} _ {N - j} ^ {\mathrm{T}} \boldsymbol {\Phi} _ {N - j + 1, N - j} ^ {\mathrm{T}} \boldsymbol {Q} _ {N - j + 1} ^ {0} \boldsymbol {\Gamma} _ {N - j} \boldsymbol {\Lambda} _ {N - j + 1} \boldsymbol {\Phi} _ {N - j + 1, N - j} \widetilde {\boldsymbol {X}} _ {N - j}) \right\} \tag {8-55}$$

将式(8-54)代入式(8-53)，并将下标 $k+1$ 改为k，可得

$$\boldsymbol {Q} _ {k} ^ {0} = \overline {{\boldsymbol {Q}}} _ {k} + \boldsymbol {\Phi} _ {k + 1, k} ^ {\mathrm{T}} \boldsymbol {Q} _ {k + 1} ^ {0} \boldsymbol {\Phi} _ {k + 1, k} -\boldsymbol {\Phi} _ {k - 1, k} ^ {\mathrm{T}} \boldsymbol {Q} _ {k + 1} ^ {0} \boldsymbol {\Gamma} _ {k} \left(\boldsymbol {\Gamma} _ {k} ^ {\mathrm{T}} \boldsymbol {Q} _ {k + 1} ^ {0} \boldsymbol {\Gamma} _ {k} + \overline {{\boldsymbol {R}}} _ {k}\right) ^ {- 1} \boldsymbol {\Gamma} _ {k} ^ {\mathrm{T}} \boldsymbol {Q} _ {k + 1} ^ {0} \boldsymbol {\Phi} _ {k + 1, k} \tag {8-56}$$

此即 $Q_{K}^{0}$ 所满足的矩阵黎卡提方程。终端条件为
