有半正定解 $W$ ，且 $A_{F} + X_{0}^{-1}C_{1}^{\mathrm{T}}D_{\perp}D_{\perp}^{\mathrm{T}}C_{1}X_{0}^{-1}W$ 是稳定阵，同时满足 $\rho(WL_c) < 1$ ，其中 $L_{c}$ 满足方程

$$L _ {c} A _ {F} ^ {\mathrm{T}} + A _ {F} L _ {c} = - \widehat {B} \widehat {B} ^ {\mathrm{T}}, \widehat {B} = [ B _ {2} - X _ {0} ^ {- 1} C _ {1} ^ {\mathrm{T}} D _ {\perp} ]. \tag {6.5.28}$$

注意 Riccati 方程 (6.5.21) 可以表示为

$$X _ {0} ^ {- 1} A _ {F} + A _ {F} ^ {\mathrm{T}} X _ {0} ^ {- 1} = - \widehat {B} \widehat {B} ^ {\mathrm{T}},$$

所以 $L_{c} = X_{0}^{-1}$ . 于是 $\rho (WX_0^{-1}) < 1$ . 又因为 $[D_{12} D_{\perp}][D_{12} D_{\perp}]^{\mathrm{T}} = I$ , 故根据定理的假设 (A2), 得

$$C _ {1} ^ {\mathrm{T}} \left[ D _ {1 2} D _ {\perp} \right] \left[ D _ {1 2} D _ {\perp} \right] ^ {\mathrm{T}} C _ {1} ^ {\mathrm{T}} = C _ {1} ^ {\mathrm{T}} D _ {\perp} D _ {\perp} ^ {\mathrm{T}} C _ {1} ^ {\mathrm{T}} = C _ {1} ^ {\mathrm{T}} C _ {1}.$$

再根据 Riccati 方程 (6.5.21), 有

$$X _ {0} A _ {F} = - (A ^ {\mathrm{T}} X _ {0} + C _ {1} ^ {\mathrm{T}} C _ {1}) = X _ {0} (- X _ {0} ^ {- 1} A ^ {\mathrm{T}} X _ {0} - X _ {0} ^ {- 1} C _ {1} ^ {\mathrm{T}} C _ {1}).$$

因此 $A_{F} = \tilde{A} = -X_{0}^{-1}A^{\mathrm{T}}X_{0} - X_{0}^{-1}C_{1}^{\mathrm{T}}C_{1}$ 利用Riccati方程(6.5.21）以及上述 $\tilde{A},$ Riccati方程(6.5.27）可以表示为

$$
\begin{array}{l} W \tilde {A} + \tilde {A} ^ {\mathrm{T}} W + W X _ {0} ^ {- 1} C _ {1} ^ {\mathrm{T}} C _ {1} X _ {0} ^ {- 1} W \\ + X _ {0} \left(B _ {1} B _ {1} ^ {\mathrm{T}} - B _ {2} B _ {2} ^ {\mathrm{T}}\right) X _ {0} + X _ {0} A + A ^ {\mathrm{T}} X _ {0} + C _ {1} ^ {\mathrm{T}} C _ {1} = 0. \tag {6.5.29} \\ \end{array}
$$

利用 Riccati 方程与 Hamilton 矩阵的关系，上式可以进一步表示为

$$
[ W - I ] H _ {W} \left[ \begin{array}{l} I \\ W \end{array} \right] = 0, \tag {6.5.30}
$$

其中

$$
H _ {W} = \left[ \begin{array}{c c} \widetilde {A} & X _ {0} ^ {- 1} C _ {1} ^ {\mathrm{T}} C _ {1} X _ {0} ^ {- 1} \\ - X _ {0} (B _ {1} B _ {1} ^ {\mathrm{T}} - B _ {2} B _ {2} ^ {\mathrm{T}}) X _ {0} - X _ {0} A - A ^ {\mathrm{T}} X _ {0} - C _ {1} ^ {\mathrm{T}} C _ {1} & - \widetilde {A} ^ {\mathrm{T}} \end{array} \right],
$$

而 Riccati 方程 (6.4.3) 可以表示为

$$
[ X - I ] H _ {\infty} \left[ \begin{array}{l} I \\ X \end{array} \right] = 0, \tag {6.5.31}
$$

其中

$$
H _ {\infty} = \left[ \begin{array}{c c} A & B _ {1} B _ {1} ^ {\mathrm{T}} - B _ {2} B _ {2} ^ {\mathrm{T}} \\ - C _ {1} ^ {\mathrm{T}} C _ {1} & - A ^ {\mathrm{T}} \end{array} \right].
$$

容易验证， $H_{W}$ 与 $H_{\infty}$ 满足

$$
H _ {W} = T ^ {- 1} H _ {\infty} T, \quad T = \left[ \begin{array}{c c} - I & X _ {0} ^ {- 1} \\ - X _ {0} & 0 \end{array} \right]. \tag {6.5.32}
$$

于是注意到 $\rho (WX_0^{-1}) < 1$ ，将上式代入式(6.5.30)，得
