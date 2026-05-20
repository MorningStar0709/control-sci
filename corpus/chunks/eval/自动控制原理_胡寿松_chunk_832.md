# (3) 最优闭环系统的渐近稳定性

定理 10-22 对于问题 10-3, 由定理 10-21 得到的最优闭环系统

$$\dot {\boldsymbol {x}} (t) = \left(\boldsymbol {A} - \boldsymbol {B} \boldsymbol {R} ^ {- 1} \boldsymbol {B} ^ {\mathrm{T}} \bar {\boldsymbol {P}}\right) \boldsymbol {x} (t), \quad \boldsymbol {x} (0) = \boldsymbol {x} _ {0} \tag {10-124}$$

必定是渐近稳定的。

证明 取二次型函数

$$V (\boldsymbol {x}) = \boldsymbol {x} ^ {\mathrm{T}} (t) \overline {{{\boldsymbol {P}}}} \boldsymbol {x} (t) \tag {10-125}$$

上式仅当 $x(t) = 0$ 时，才有 $V(x) = 0$ ；对于非零 $x(t)$ ，由于 $\bar{P}$ 为对称正定常值矩阵，必有 $V(x) > 0$ ；而且

$$\lim _ {\| x \| \rightarrow \infty} V (x) = \lim _ {\| x \| \rightarrow \infty} x ^ {T} (t) \overline {{{P}}} x (t) \rightarrow \infty$$

故式(10-125)表示的 $V(x)$ 是一个李雅普诺夫函数。

取式(10-125)对时间 t 的导数, 得

$$\dot {V} (\boldsymbol {x}) = \dot {\boldsymbol {x}} ^ {\mathrm{T}} (t) \overline {{{\boldsymbol {P}}}} \boldsymbol {x} (t) + \boldsymbol {x} ^ {\mathrm{T}} (t) \overline {{{\boldsymbol {P}}}} \dot {\boldsymbol {x}} (t)$$

将式(10-119)及式(10-123)代入上式,可得

$$
\begin{array}{l} \dot {V} (\boldsymbol {x}) = \boldsymbol {x} ^ {\mathrm{T}} (t) \left[ \left(\boldsymbol {A} - \boldsymbol {B} \boldsymbol {R} ^ {- 1} \boldsymbol {B} ^ {\mathrm{T}} \bar {\boldsymbol {P}}\right) ^ {\mathrm{T}} \bar {\boldsymbol {P}} + \bar {\boldsymbol {P}} \left(\boldsymbol {A} - \boldsymbol {B} \boldsymbol {R} ^ {- 1} \boldsymbol {B} ^ {\mathrm{T}} \bar {\boldsymbol {P}}\right) \right] \boldsymbol {x} (t) \\ = - \boldsymbol {x} ^ {\mathrm{T}} (t) (\boldsymbol {Q} + \overline {{\boldsymbol {P}}} \boldsymbol {B} \boldsymbol {R} ^ {- 1} \boldsymbol {B} ^ {\mathrm{T}} \overline {{\boldsymbol {P}}}) \boldsymbol {x} (t) \tag {10-126} \\ \end{array}
$$

因 $Q \geqslant 0, R > 0$ ，故有

$$\dot {V} (x) \leqslant 0$$

显然，仅在 $x(t) = x_0 = 0$ 的原平衡状态时，才有 $\dot{V} (x) = 0$ ，此外 $\dot{V} (x)\neq 0$ 。反设对于非零 $x_0$ 有 $\dot{V} (x)\equiv 0$ ，则由式(10-126)知，应有

$$\boldsymbol {x} ^ {\mathrm{T}} (t) \boldsymbol {Q} \boldsymbol {x} (t) = 0 \tag {10-127}\boldsymbol {x} ^ {\mathrm{T}} (t) \overline {{\boldsymbol {P}}} \boldsymbol {B} \boldsymbol {R} ^ {- 1} \boldsymbol {B} ^ {\mathrm{T}} \overline {{\boldsymbol {P}}} \boldsymbol {x} (t) = 0 \tag {10-128}$$

将 $\pmb{u}^{*}(t) = -\pmb{R}^{-1}\pmb{B}^{\mathrm{T}}\overline{\pmb{P}}\pmb{x}(t)$ 代入式(10-128)，得

$$\boldsymbol {u} ^ {* \mathrm{T}} (t) \boldsymbol {R u} ^ {*} (t) = 0$$

由于 R>0，故应有 $u^{*}(t)=0$ ，此时系统(10-119)只有零输入响应
