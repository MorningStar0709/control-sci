以 $n$ 关节机械手动力学方程为例（如 $n = 2$ ), $\pmb{\varphi}^{\mathrm{T}}(\pmb{x})\widetilde{\pmb{\theta}}$ 为 $1 \times n$ 向量, $\pmb{B}^{\mathrm{T}}\pmb{P}\pmb{x}$ 为 $n \times 1$ 向量, 则 $\pmb{\varphi}^{\mathrm{T}}(\pmb{x})\widetilde{\pmb{\theta}}\pmb{B}^{\mathrm{T}}\pmb{P}\pmb{x}$ 为一实数, 且等于 $\pmb{B}^{\mathrm{T}}\pmb{P}\pmb{x}\pmb{\varphi}^{\mathrm{T}}(\pmb{x})\widetilde{\pmb{\theta}}$ 的主对角元素之和, 则下式成立

$$\boldsymbol {\varphi} ^ {T} (\boldsymbol {x}) \widetilde {\boldsymbol {\theta}} \boldsymbol {B} ^ {T} \boldsymbol {P x} = \operatorname{tr} \left[ \boldsymbol {B} ^ {T} \boldsymbol {P x} \boldsymbol {\varphi} ^ {T} (\boldsymbol {x}) \widetilde {\boldsymbol {\theta}} \right] \tag {9.60}$$

则

$$\dot {V} = - \frac {1}{2} x ^ {\mathrm{T}} Q x + \frac {1}{\gamma} \operatorname{tr} \left(\gamma B ^ {\mathrm{T}} P x \varphi^ {\mathrm{T}} (x) \bar {\theta} + \dot {\bar {\theta}} ^ {\mathrm{T}} \bar {\theta}\right) + \eta^ {\mathrm{T}} B ^ {\mathrm{T}} P x \tag {9.61}$$

由于 $\dot{\pmb{\theta}} = -\dot{\pmb{\theta}}$ ，取自适应律为

$$\dot {\hat {\boldsymbol {\theta}}} ^ {\mathrm{T}} = \gamma \boldsymbol {B} ^ {\mathrm{T}} \boldsymbol {P} \boldsymbol {x} \boldsymbol {\varphi} ^ {\mathrm{T}} (\boldsymbol {x})$$

即

$$\dot {\hat {\boldsymbol {\theta}}} = \boldsymbol {\gamma} \boldsymbol {\varphi} (\boldsymbol {x}) \boldsymbol {x} ^ {\mathrm{T}} \boldsymbol {P} \boldsymbol {B} \tag {9.62}$$

则

$$\dot {V} = - \frac {1}{2} x ^ {\mathrm{T}} Q x + \eta^ {\mathrm{T}} B ^ {\mathrm{T}} P x$$

由已知

$$\| \boldsymbol {\eta} ^ {\mathrm{T}} \| \leqslant \boldsymbol {\eta} _ {0}, \| \boldsymbol {B} \| = 1$$

设 $\lambda_{\min}(Q)$ 为矩阵 Q 特征值的最小值, $\lambda_{\max}(P)$ 为矩阵 P 特征值的最大值, 则

$$
\begin{array}{l} \dot {V} \leqslant - \frac {1}{2} \lambda_ {\min} (Q) \| x \| ^ {2} + \eta_ {0} \lambda_ {\max} (P) \| x \| \\ = - \frac {1}{2} \| \boldsymbol {x} \| [ \lambda_ {\min} (\boldsymbol {Q}) \| \boldsymbol {x} \| - 2 \eta_ {0} \lambda_ {\max} (\boldsymbol {P}) ] \tag {9.63} \\ \end{array}
$$

要使 $\dot{V} \leqslant 0$ ，需要 $\lambda_{\min}(Q) \geqslant \frac{2\lambda_{\max}(P)}{\|x\|}\eta_0$ 。由于当且仅当 $x = \frac{2\lambda_{\max}(P)}{\lambda_{\min}(Q)}$ 时， $\dot{V} = 0$ ，即当 $\dot{V} \equiv 0$ 时， $x \equiv \frac{2\lambda_{\max}(P)}{\lambda_{\min}(Q)}$ 。根据 LaSalle 不变性原理[35]，闭环系统为渐近稳定，即当 $t \to \infty$ 时， $x \to \frac{2\lambda_{\max}(P)}{\lambda_{\min}(Q)}$ ，系统的收敛速度取决于 $\lambda_{\min}(Q)$ 。

由于 $V\geqslant0,\dot{V}\leqslant0$ ，则当 $t\to\infty$ 时，V有界，从而 $\tilde{\theta}$ 有界。

可见, 当 Q 的特征值越大, P 的特征值越小, 神经网络建模误差 $\eta$ 的上界 $\eta_{0}$ 越小, 则 x 的收敛半径越小, 跟踪效果越好。
