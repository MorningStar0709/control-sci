$$J _ {1} ^ {*} = \min _ {U _ {N - 1}} E \left\{X ^ {\mathrm{T}} \boldsymbol {\Phi} ^ {\mathrm{T}} \overline {{{Q}}} \boldsymbol {\Phi} X + 2 X ^ {\mathrm{T}} \boldsymbol {\Phi} ^ {\mathrm{T}} \overline {{{Q}}} \boldsymbol {\Gamma} U + \right.2 \boldsymbol {X} ^ {\mathrm{T}} \boldsymbol {\Phi} ^ {\mathrm{T}} \overline {{{\boldsymbol {Q}}}} \boldsymbol {W} + 2 \boldsymbol {W} ^ {\mathrm{T}} \overline {{{\boldsymbol {Q}}}} \boldsymbol {\Gamma} \boldsymbol {U} + \boldsymbol {W} ^ {\mathrm{T}} \overline {{{\boldsymbol {Q}}}} \boldsymbol {W} + \boldsymbol {U} ^ {\mathrm{T}} (\boldsymbol {\Gamma} ^ {\mathrm{T}} \overline {{{\boldsymbol {Q}}}} \boldsymbol {\Gamma} + \overline {{{\boldsymbol {R}}}}) \boldsymbol {U} \} \tag {8-23}$$

由式(8-14)可知 $X_{k}$ 只与 $W_{k-1}$ 、 $W_{k-2}$ 、 $\cdots$ 、 $W_{0}$ 有关而与 $W_{k}$ 无关，并且 $W_{k}$ 是零均值的，故上式中第三项和第四项的均值为 0。又因为所求控制量所依据的信息只有系统过去的输出量（状态变量不能直接测量）和初始状态的均值，即

$$\boldsymbol {U} _ {k} = \boldsymbol {f} _ {k} (\boldsymbol {Z} ^ {k}, m _ {0})$$

其中 $m_0 = E[X_0]$ 。

$$\mathbf {Z} ^ {k} \triangleq (\mathbf {Z} _ {1}, \mathbf {Z} _ {2}, \dots , \mathbf {Z} _ {k}) ^ {\mathrm{T}} \tag {8-24}$$

根据 $W_{k}$ 与 $Z^{k}$ 和 $X_{0}$ 的随机独立性, 可知 $U_{k}$ 与 $W_{k}$ 也是独立的, 故 (8-21) 中第四项的均值也为 0。至此 $J_{1}^{*}$ 化为(恢复下标)

$$J _ {1} ^ {*} = \min _ {\boldsymbol {U} _ {N - 1}} E \left\{\boldsymbol {X} _ {N - 1} ^ {\mathrm{T}} \boldsymbol {\Phi} _ {N, N - 1} ^ {\mathrm{T}} \overline {{\boldsymbol {Q}}} _ {N} \boldsymbol {\Phi} _ {N, N - 1} \boldsymbol {X} _ {N - 1} + \right.2 \boldsymbol {X} _ {N - 1} ^ {\mathrm{T}} \boldsymbol {\Phi} _ {N, N - 1} ^ {\mathrm{T}} \overline {{{\boldsymbol {Q}}}} _ {N} \boldsymbol {\Gamma} _ {N - 1} \boldsymbol {U} _ {N - 1} +\boldsymbol {W} _ {N - 1} ^ {\mathrm{T}} \overline {{\boldsymbol {Q}}} _ {N} \boldsymbol {W} _ {N - 1} + \boldsymbol {U} _ {N - 1} ^ {\mathrm{T}} \left(\boldsymbol {\Gamma} _ {N - 1} ^ {\mathrm{T}} \overline {{\boldsymbol {Q}}} _ {N} \boldsymbol {\Gamma} _ {N - 1} + \overline {{\boldsymbol {R}}} _ {N - 1}\right) \boldsymbol {U} _ {N - 1} \rbrace \tag {8-25}$$

由于上式右端花括号内的量是依赖于测量值 $Z^{N-1} = [Z_{1}, Z_{2}, \cdots, Z_{N-1}]^{T}$ 和 $m_{0}$ 为已知这一条件上的，而条件 $Z^{N-1}$ 又是随机的，因此要利用条件期望的性质来计算。根据本章第2节中关于条件概率的定义可推出下面的性质

$$E [ \xi ] = E _ {\eta} \left[ E _ {\xi} (\xi \mid \eta) \right] \tag {8-26}$$

上式右端方括号内的求数学期望是对随机变量 $\xi$ 而言的(假定 $\eta$ 已知)，外层的求数学期望是对条件 $\eta$ 而言的，而等式左端是无条件数学期望，上式可证明如下：
