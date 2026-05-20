$$
\begin{array}{l} \sup _ {u \in \mathcal {U}} \left\{\| P _ {+} y \| _ {2} ^ {2} - \| u \| _ {2} ^ {2} \mid x (0) = x _ {0} \right\} \\ = \sup _ {u _ {2} \in L _ {+} ^ {2}} \left\{\| P _ {+} y \| _ {2} ^ {2} - \| P _ {+} u _ {2} \| _ {2} ^ {2} \right\} - \inf _ {u \in L _ {-} ^ {2}} \left\{\| P _ {-} u \| _ {2} ^ {2} \right\} \\ = x _ {0} ^ {\mathrm{T}} X x _ {0} - x _ {0} ^ {\mathrm{T}} L _ {\mathrm{c}} ^ {- 1} x _ {0} \\ = x _ {0} ^ {\mathrm{T}} S ^ {\mathrm{T}} \left(S ^ {- T} X S ^ {- 1} - I\right) S x _ {0}. \\ \end{array}
$$

由上式可知， $\rho(XL_c) \geqslant 1$ 当且仅当 $\sup_{u \in B\mathcal{U}} \| \Gamma u \|_2 \geqslant 1$ ，这是因为，若 $\rho(XL_c) \geqslant 1$ ，则存在 $x_0 \neq 0$ 使得上式右端为正，即存在 $u \in \mathcal{U}$ ， $u \neq 0$ 使得 $\| P_+y \|_2^2 \geqslant \| u \|_2^2$ 。

现在我们应用上述引理来证明定理6.4.1的必要性．不失一般性，在以下证明中，我们假设 $(D_{\perp}^{\mathrm{T}}C_{1}, - A)$ 是能检测的，其中 $D_{\perp}$ 是 $D_{12}$ 的正交阵，且满足

$$[ D _ {1 2} D _ {\perp} ] ^ {\mathrm{T}} [ D _ {1 2} D _ {\perp} ] = I. \tag {6.5.18}$$

如果该假设不成立，总可以找到适当的坐标变换和矩阵分块方法，使问题等价于对应的 $A, C_1, D_{12}$ 满足该假设条件的情况（详细参见文献[5]).

证明 设对于广义受控对象 (6.4.1)，存在反馈控制器 $u = K(s)y$ 使得闭环系统是内部稳定的，并且 $\|T_{zw}(\cdot)\|_{\infty}<1$ 成立，即有

$$\sup _ {w \in B L _ {+} ^ {2}} \min _ {K} | | z | | _ {2} < 1. \tag {6.5.19}$$

令

$$u = K (s) y = F _ {0} x + K (s) y - F _ {0} x = F _ {0} x + \nu , \tag {6.5.20}$$

其中 $\nu = K(s)y - F_0x, F_0 = -B_2^{\mathrm{T}}X_0, X_0$ 是由如下 Riccati 方程给定的 $H_2$ 最优增益（由于 $(A, B_2)$ 是能稳，且 $(D_{\perp}^{\mathrm{T}}C_1, -A)$ 是能检测，该 Riccati 方程有正定解 $X_0$ ）

$$A ^ {\mathrm{T}} X _ {0} + X _ {0} A - X _ {0} B _ {2} B _ {2} ^ {\mathrm{T}} X _ {0} + C _ {1} ^ {\mathrm{T}} D _ {\perp} D _ {\perp} ^ {\mathrm{T}} C _ {1} = 0. \tag {6.5.21}$$

于是该闭环系统可以表示为

$$
\left\{ \begin{array}{l} \dot {x} = A _ {F} x + B _ {1} w + B _ {2} \nu , \\ z = C _ {1 F} x + D _ {1 2} \nu , \\ \nu = K (s) y - F _ {0} x. \end{array} \right. \tag {6.5.22}
$$

其中 $A_{F} = A + B_{2}F_{0}, C_{1F} = C_{1} + D_{12}F_{0}$ . 由上式可求出 $w, \nu$ 到 $z$ 的开环传递函数阵

$$
z = \left[ G _ {c} (s) U (s) \right] \left[ \begin{array}{l} w \\ \nu \end{array} \right].
$$

设有理函数阵 $U_{\perp}(s)$ 的状态空间实现为 $\{A_F, -X_0^{-1}C_1^{\mathrm{T}}D_{\perp}, C_{1F}, D_{\perp}\}$ . 利用引理6.4.2, 容易验证有理函数阵

$$\widehat {U} (s) = \left[ U (s) U _ {\perp} (s) \right]$$

是内函数阵. 因此 $\widehat{U}^{\mathrm{T}}(-s) = [\widehat{U}(-s)]^{\mathrm{T}}$ 也是内函数阵. 于是

$$\| z \| _ {2} = \left\| \widehat {U} ^ {\mathrm{T}} (- s) z \right\| _ {2}.$$

注意
