$$
H \left(\boldsymbol {X}, \boldsymbol {U} ^ {*}, \boldsymbol {\lambda} ^ {*}, t\right) = \boldsymbol {\lambda} ^ {* T} \boldsymbol {f} \left(\boldsymbol {X}, \boldsymbol {U} ^ {*}, t\right) \tag {4-10}
\dot {\boldsymbol {\lambda}} ^ {*} = - \frac {\partial H}{\partial \boldsymbol {X}} \Bigg | _ {\substack {U = U ^ {*} \\ \boldsymbol {\lambda} = \boldsymbol {\lambda} ^ {*}}} = - \left(\frac {\partial \boldsymbol {f} ^ {\mathrm{T}}}{\partial \boldsymbol {X}}\right) \mid_ {U = U ^ {*}} \boldsymbol {\lambda} ^ {*} \tag{4 - 11}
\boldsymbol {\lambda} ^ {*} \left(t _ {\mathrm{f}}\right) = \frac {\partial \phi}{\partial \boldsymbol {X} \left(t _ {\mathrm{f}}\right)} + \frac {\partial \boldsymbol {G} ^ {\mathrm{T}}}{\partial \boldsymbol {X} \left(t _ {\mathrm{f}}\right)} \boldsymbol {v} \tag {4-12}
$$

显然,方程 $(4-9)$ 和 $(4-11)$ 为共轭方程,立即求得积分

$$\boldsymbol {\lambda} ^ {* \mathrm{T}} (t) \delta \boldsymbol {X} (t) = \text { const }$$

或 $\pmb{\lambda}^{*\mathrm{T}}(t_{\mathrm{f}})\delta \pmb {X}(t_{\mathrm{f}}) = \pmb{\lambda}^{*\mathrm{T}}(t_1)\delta \pmb {X}(t_1)$ (4-13)

即最终求得了由于 $\delta U$ 的有限改变而引起的最优轨线的变化 $\delta X(t)$ ，特别是末值状态的变化 $\delta X(t_{\mathrm{f}})$ 。

下面研究由 $\delta U$ 引起的最优性能指标的改变量 $\Delta J$ 。

由于 $J = \phi [X(t_{\mathrm{f}}),t_{\mathrm{f}}] + \pmb{v}^{\mathrm{T}}\pmb {G}[X(t_{\mathrm{f}}),t_{\mathrm{f}}]$

故有

$$\Delta J = \left(\frac {\partial \phi}{\partial \boldsymbol {X} (t _ {\mathrm{f}})} + \frac {\partial \boldsymbol {G} ^ {\mathrm{T}}}{\partial \boldsymbol {X} (t _ {\mathrm{f}})} \boldsymbol {v}\right) ^ {\mathrm{T}} \delta \boldsymbol {X} (t _ {\mathrm{f}}) + o (\varepsilon) \geqslant 0 \tag {4-14}$$

综合式 $(4-8)$ 、 $(4-12)$ 、 $(4-13)$ 和 $(4-14)$ 等式，可以建立 $\Delta J$ 与有限改变量 $\delta U$ 之间的关系

$$\Delta J = \left[ \lambda^ {* T} f (X ^ {*}, U _ {*} ^ {*} + \delta U, t) - \lambda^ {* T} f (X ^ {*}, U ^ {*}, t) \right] | _ {t = t _ {1}} \varepsilon + o (\varepsilon) \geqslant 0$$

已知 $t_1 \in [t_0, t_f]$ 中的任意时刻，并以 $\pmb{U}$ 表示 $U^* + \delta U$ ，当 $\varepsilon \to 0$ 时，上式变为

$$\boldsymbol {\lambda} ^ {* \mathrm{T}} \boldsymbol {f} (\boldsymbol {X} ^ {*}, \boldsymbol {U} ^ {*}, t) \leqslant \boldsymbol {\lambda} ^ {* \mathrm{T}} \boldsymbol {f} (\boldsymbol {X} ^ {*}, \boldsymbol {U}, t), \boldsymbol {U} \in \Omega , t \in [ t _ {0}, t _ {\mathrm{f}} ]$$

或用哈密顿函数 $H$ 的表达式(4-10)表示可得
