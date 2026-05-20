# 2）两步问题

接下来讨论最后两步的最优控制问题。根据动态规划最优化原则，可把最后两步的最优化指标表示为

$$J _ {2} ^ {*} = \min _ {U _ {N - 2}} \left\{E \left\{\boldsymbol {X} _ {N - 1} ^ {\mathrm{T}} \overline {{{\boldsymbol {Q}}}} _ {N - 1} \boldsymbol {X} _ {N - 1} + \boldsymbol {U} _ {N - 2} ^ {\mathrm{T}} \overline {{{\boldsymbol {R}}}} _ {N - 2} \boldsymbol {U} _ {N - 2} \right\} + J _ {1} ^ {*} \right\} (8 - 4 1)$$

将一步最优化的结果式(8-38)代入上式,并注意到 $\alpha_{N-1}$ 不受 $U_{N-2}$ 的影响,可把它提到 min 号之外,即可得到

$$
\begin{array}{l} J _ {2} ^ {*} = \min _ {\boldsymbol {U} _ {N - 2}} E \left\{\boldsymbol {X} _ {N - 1} ^ {\mathrm{T}} \overline {{{\boldsymbol {Q}}}} _ {N - 1} \boldsymbol {X} _ {N - 1} + \boldsymbol {U} _ {N - 2} ^ {\mathrm{T}} \overline {{{\boldsymbol {R}}}} _ {N - 2} \boldsymbol {U} _ {N - 2} + \right. \\ \left. \boldsymbol {X} _ {N - 1} ^ {\mathrm{T}} \boldsymbol {\Phi} _ {N, N - 1} ^ {\mathrm{T}} \widetilde {\boldsymbol {Q}} _ {N} \boldsymbol {\Phi} _ {N, N - 1} \boldsymbol {X} _ {N - 1} \right\} + \alpha_ {N - 1} \\ = \min _ {\boldsymbol {U} _ {N - 2}} E \left\{\boldsymbol {X} _ {N - 1} ^ {\mathrm{T}} \boldsymbol {Q} _ {N - 1} ^ {0} \boldsymbol {X} _ {N - 1} + \boldsymbol {U} _ {N - 2} ^ {\mathrm{T}} \overline {{{\boldsymbol {R}}}} _ {N - 2} \boldsymbol {U} _ {N - 2} \right\} + \alpha_ {N - 1} (8 - 4 2) \\ \end{array}
$$

其中

$$\boldsymbol {Q} _ {N - 1} ^ {0} = \overline {{\boldsymbol {Q}}} _ {N - 1} + \boldsymbol {\Phi} _ {N, N - 1} ^ {\mathrm{T}} \widetilde {\boldsymbol {Q}} _ {N} \boldsymbol {\Phi} _ {N, N - 1} \tag {8-43}$$

将 $J_{2}^{*}$ 的表达式(8-42)与 $J_{1}^{*}$ 的表达式(8-20)相比，可见除 $J_{2}^{*}$ 中多一个常数项 $\alpha_{N - 1}$ 之外，两者形式完全相同，于是可重复一步最优化过程的步骤，得到下面的结果：
