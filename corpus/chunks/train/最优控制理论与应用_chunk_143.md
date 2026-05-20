$$
\begin{array}{l} E (\xi) = \int_ {- \infty} ^ {\infty} \xi f (\xi) d \xi = \int_ {- \infty} ^ {\infty} \xi d \xi \int_ {- \infty} ^ {\infty} f (\xi , \eta) d \eta \\ = \int_ {- \infty} ^ {\infty} \xi \mathrm{d} \xi \int_ {- \infty} ^ {\infty} f (\eta) f (\xi | \eta) \mathrm{d} \eta \\ = \int_ {- \infty} ^ {\infty} f (\eta) \left[ \int_ {- \infty} ^ {\infty} \xi f (\xi | \eta) d \xi \right] d \eta \\ = E _ {\eta} \left[ E _ {\xi} (\xi | \eta) \right] \\ \end{array}
$$

于是式(8-25)可进一步化为

$$J _ {1} ^ {*} = \min _ {\boldsymbol {U} _ {N - 1}} E \left\{E \left[ \boldsymbol {X} _ {N - 1} ^ {\mathrm{T}} \boldsymbol {\Phi} _ {N, N - 1} ^ {\mathrm{T}} \overline {{\boldsymbol {Q}}} _ {N} \boldsymbol {\Phi} _ {N, N - 1} \boldsymbol {X} _ {N - 1} + \right. \right.2 \boldsymbol {X} _ {N - 1} ^ {\mathrm{T}} \boldsymbol {\Phi} _ {N, N - 1} ^ {\mathrm{T}} \overline {{{\boldsymbol {Q}}}} _ {N} \boldsymbol {\Gamma} _ {N - 1} \boldsymbol {U} _ {N - 1} +\boldsymbol {W} _ {N - 1} ^ {\mathrm{T}} \overline {{\boldsymbol {Q}}} _ {N} \boldsymbol {W} _ {N - 1} + \boldsymbol {U} _ {N - 1} ^ {\mathrm{T}} \left(\boldsymbol {\Gamma} _ {N - 1} ^ {\mathrm{T}} \overline {{\boldsymbol {Q}}} _ {N} \boldsymbol {\Gamma} _ {N - 1} + \right.\left. \overline {{{\boldsymbol {R}}}} _ {N - 1}\right) \boldsymbol {U} _ {N - 1} \left| \boldsymbol {Z} ^ {N - 1}, m _ {0} \right] \} \tag {8-27}$$

由于 $m_0$ 非随机，所以上式外层数学期望只是对 $\pmb{Z}^{N - 1}$ 取的，为了找到 $\pmb{U}_{N - 1}$ 使 $J_{1}$ 最小，这等价于使上式内层的条件数学期望最小。这时假定条件 $\pmb{Z}^{N - 1}$ 给定，而 $\pmb{U}_{N - 1}$ 是 $\pmb{Z}^{N - 1}$ 的确定性函数，因此 $\pmb{U}_{N - 1}$ 与求内层条件数学期望无关，即有

$$E \left[ 2 X _ {N - 1} ^ {\mathrm{T}} \Phi_ {N, N - 1} ^ {\mathrm{T}} \overline {{{Q}}} _ {N} \Gamma_ {N - 1} U _ {N - 1} \mid Z ^ {N - 1}, m _ {0} \right]= 2 E \left[ \boldsymbol {X} _ {N - 1} ^ {\mathrm{T}} \mid \boldsymbol {Z} ^ {N - 1}, m _ {0} \right] \boldsymbol {\Phi} _ {N, N - 1} ^ {\mathrm{T}} \overline {{{\boldsymbol {Q}}}} _ {N} \boldsymbol {\Gamma} _ {N - 1} \boldsymbol {U} _ {N - 1}$$
