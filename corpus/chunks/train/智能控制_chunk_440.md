则 $\ddot{\pmb{e}} +\pmb{k}_{\mathrm{v}}\dot{\pmb{e}} +\pmb{k}_{\mathrm{p}}\pmb {e} + \hat{\pmb{f}} (\pmb {x},\pmb {\theta}) = \pmb{D}_{0}^{-1}(q)(\Delta \pmb {D}(\pmb {q})\ddot{\pmb{q}} +\Delta \pmb {C}(\pmb {q},\dot{\pmb{q}})\dot{\pmb{q}} +\Delta \pmb {G}(\pmb {q}) + \pmb {d})$

即 $\ddot{e}+k_{v}\dot{e}+k_{p}e+\hat{f}(x,\theta)=f(x)$

式中， $f(x) = D_0^{-1}(\Delta D\ddot{q} +\Delta C\dot{q} +\Delta G + d)$

由上式可写为

$$\dot {\boldsymbol {x}} = \boldsymbol {A} \boldsymbol {x} + \boldsymbol {B} \left\{\boldsymbol {f} (\boldsymbol {x}) - \hat {\boldsymbol {f}} (\boldsymbol {x}, \boldsymbol {\theta}) \right\}$$

式中， $A=\begin{pmatrix}0&1\\-k_{p}&-k_{v}\end{pmatrix},B=\begin{pmatrix}0\\I\end{pmatrix}$ 。

由于

$$
\begin{array}{l} f (x) - \hat {f} (x, \boldsymbol {\theta}) = f (x) - \hat {f} (x, \boldsymbol {\theta} ^ {*}) + \hat {f} (x, \boldsymbol {\theta} ^ {*}) - \hat {f} (x, \boldsymbol {\theta}) \\ = \boldsymbol {\eta} + \boldsymbol {\theta} ^ {* T} \varphi (x) - \tilde {\boldsymbol {\theta}} ^ {T} \boldsymbol {\varphi} (x) = \boldsymbol {\eta} + \tilde {\boldsymbol {\theta}} ^ {T} \boldsymbol {\varphi} (x) \\ \end{array}
$$

则

$$\dot {\boldsymbol {x}} = \boldsymbol {A} \boldsymbol {x} + \boldsymbol {B} (\boldsymbol {\eta} + \widetilde {\boldsymbol {\theta}} ^ {\mathrm{T}} \boldsymbol {\varphi} (\boldsymbol {x})) \tag {9.56}$$

式中， $\tilde{\pmb{\theta}} = \pmb{\theta}^{*} - \hat{\pmb{\theta}}$ 。

定义 Lyapunov 函数为

$$V = \frac {1}{2} \boldsymbol {x} ^ {\mathrm{T}} \boldsymbol {P} \boldsymbol {x} + \frac {1}{2 \gamma} \| \widetilde {\boldsymbol {\theta}} \| _ {\mathrm{F}} ^ {2} \tag {9.57}$$

式中， $\gamma>0$ 。

由于 A 矩阵特征根实部为负, 则存在正定阵 P 和 Q, 满足如下 Lyapunov 方程 $^{[29]}$

$$\boldsymbol {P} \boldsymbol {A} + \boldsymbol {A} ^ {\mathrm{T}} \boldsymbol {P} = - \boldsymbol {Q} \tag {9.58}$$

参考文献[18],下面给出控制系统稳定性分析。

定义

$$\| \boldsymbol {R} \| _ {\mathrm{F}} ^ {2} = \sum_ {i, j} | r _ {i j} | ^ {2} = \operatorname{tr} (\boldsymbol {R} \boldsymbol {R} ^ {\mathrm{T}}) = \operatorname{tr} (\boldsymbol {R} ^ {\mathrm{T}} \boldsymbol {R})$$

式中， $\mathrm{tr}(\cdot)$ 为矩阵 $\pmb{R}$ 的迹，则根据迹的定义，有
