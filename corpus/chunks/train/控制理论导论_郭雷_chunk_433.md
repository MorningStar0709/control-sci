然后，取 $\gamma_0\in [\gamma_m,\gamma_M]$ ，并验证对应的 $H_{\gamma_0}$ 的特征值以确定用 $\gamma_0$ 来代替 $\gamma_{m}$ 或者 $\gamma_{M}$ ，以缩短区间 $[\gamma_m,\gamma_M]$ 的长度．反复应用上述手法直至 $\gamma_{M} - \gamma_{m} = \varepsilon$ 充分小，这时 $\| G(\cdot)\|_{\infty}$ 近似等于 $(\gamma_{M} + \gamma_{m}) / 2,$ 且近似误差为 $\varepsilon$

定理6.2.2 设 $G(s) = \{A, B, C, 0\}$ , 则下述命题等价:

(1) $A$ 是稳定阵，且 $\| G(\cdot)\|_{\infty} < 1;$

(2) 存在正定阵 $X > 0$ 满足 Riccati 不等式

$$A ^ {\mathrm{T}} X + X A + X B B ^ {\mathrm{T}} X + C ^ {\mathrm{T}} C < 0; \tag {6.2.12}$$

(3) 存在正定矩阵 $Y > 0$ 满足线性矩阵不等式 (LMI)

$$
\left[ \begin{array}{c c} A Y + Y A ^ {\mathrm{T}} + B B ^ {\mathrm{T}} & Y C ^ {\mathrm{T}} \\ C Y & - I \end{array} \right] <   0; \tag {6.2.13}
$$

(4) 存在充分小的正数 $\varepsilon > 0$ 使得如下 Riccati 方程有正定解 $Z > 0$ :

$$A ^ {\mathrm{T}} Z + Z A + Z B B ^ {\mathrm{T}} Z + C ^ {\mathrm{T}} C + \varepsilon I = 0. \tag {6.2.14}$$

证明 以下按照 (2) $\Longrightarrow$ (1) $\Longrightarrow$ (4) $\Longrightarrow$ (2) $\Longleftrightarrow$ (3) 的顺序证明.

(2) $\Longrightarrow$ (1). 令 $Q = -(A^{\mathrm{T}}X + XA + XBB^{\mathrm{T}}X + C^{\mathrm{T}}C) > 0$ , 则有

$$A ^ {\mathrm{T}} X + X A = - \widehat {Q},$$

其中 $\hat{Q} = Q + XBB^{\mathrm{T}}X + C^{\mathrm{T}}C > 0$ 根据Lyapunov稳定性理论可知 $A$ 是稳定阵，并且易验证

$$
\begin{array}{l} \Gamma (s) = I - G ^ {\mathrm{T}} (- s) G (s) \\ = I + \tilde {C} (s I - \tilde {A}) ^ {- 1} \tilde {B} \\ = I + \widehat {C} (s I - \widehat {A}) ^ {- 1} \widehat {B}. \\ \end{array}
$$

其中 $\hat{A} = T\tilde{A}T^{-1},\hat{B} = T\tilde{B},\hat{C} = \tilde{C}T^{-1}$ 且

$$
\widetilde {A} = \left[ \begin{array}{c c} {- A ^ {\mathrm{T}} C ^ {\mathrm{T}} C} \\ {0} & {A} \end{array} \right], \quad \widetilde {B} = \left[ \begin{array}{l} {0} \\ {B} \end{array} \right], \quad \widetilde {C} = [ B ^ {\mathrm{T}} 0 ], \quad T = \left[ \begin{array}{l l} {I} & {X} \\ {0} & {I} \end{array} \right],

\hat {A} = \left[ \begin{array}{c c} {{- A ^ {\mathrm{T}}}} & {{A ^ {\mathrm{T}} X + X A + C ^ {\mathrm{T}} C}} \\ {{0}} & {{A}} \end{array} \right], \quad \hat {B} = \left[ \begin{array}{c} {{X B}} \\ {{B}} \end{array} \right], \quad \hat {C} = [ B ^ {\mathrm{T}} - B ^ {\mathrm{T}} X ].
$$

利用类似于定理6.2.1的证明方法可得

$$
\begin{array}{l} \Gamma (s) = N ^ {\mathrm{T}} (- s) N (s) + I - B ^ {\mathrm{T}} X M ^ {- 2} X B \\ = N ^ {T} (- s) N (s) + \left(I + B ^ {T} X Q ^ {- 1} X B\right) ^ {- 1}, \\ \end{array}
$$

其中 $M^2 = Q + XBB^{\mathrm{T}}X, N(s) = M^{-1}XB + M(sI - A)^{-1}B.$ 因此
