$$\dot {\boldsymbol {e}} = \boldsymbol {\Lambda} \boldsymbol {e} + \boldsymbol {b} \left\{\left[ \hat {f} (\boldsymbol {x} \mid \boldsymbol {\theta} _ {f}) - \hat {f} (\boldsymbol {x} \mid \boldsymbol {\theta} _ {f} ^ {*}) \right] + \left[ \hat {g} (\boldsymbol {x} \mid \boldsymbol {\theta} _ {g}) - \hat {g} (\boldsymbol {x} \mid \boldsymbol {\theta} _ {g} ^ {*}) \right] u + \omega \right\} \tag {5.36}$$

将式 $(5.27)$ 代入式 $(5.36)$ ，可得闭环动态方程为

$$\dot {\boldsymbol {e}} = \boldsymbol {\Lambda} \boldsymbol {e} + \boldsymbol {b} \left[ \left(\boldsymbol {\theta} _ {f} - \boldsymbol {\theta} _ {f} ^ {*}\right) ^ {\mathrm{T}} \boldsymbol {\xi} (\boldsymbol {x}) + \left(\boldsymbol {\theta} _ {g} - \boldsymbol {\theta} _ {g} ^ {*}\right) ^ {\mathrm{T}} \boldsymbol {\eta} (\boldsymbol {x}) u + \omega \right] \tag {5.37}$$

该方程清晰地描述了跟踪误差和控制参数 $\theta_{f}, \theta_{g}$ 之间的关系。自适应律的任务是为 $\theta_{f}, \theta_{g}$ 确定一个调节机理，使得跟踪误差 e 和参数误差 $\theta_{f} - \theta_{f}^{*}, \theta_{g} - \theta_{g}^{*}$ 达到最小。

定义 Lyapunov 函数

$$V = \frac {1}{2} e ^ {\mathrm{T}} P e + \frac {1}{2 \gamma_ {1}} \left(\boldsymbol {\theta} _ {f} - \boldsymbol {\theta} _ {f} ^ {*}\right) ^ {\mathrm{T}} \left(\boldsymbol {\theta} _ {f} - \boldsymbol {\theta} _ {f} ^ {*}\right) + \frac {1}{2 \gamma_ {2}} \left(\boldsymbol {\theta} _ {g} - \boldsymbol {\theta} _ {g} ^ {*}\right) ^ {\mathrm{T}} \left(\boldsymbol {\theta} _ {g} - \boldsymbol {\theta} _ {g} ^ {*}\right) \tag {5.38}$$

式中， $\gamma_{1}, \gamma_{2}$ 是正的常数， $P$ 为一个正定矩阵且满足 Lyapunov 方程

$$\boldsymbol {\Lambda} ^ {T} \boldsymbol {P} + \boldsymbol {P} \boldsymbol {\Lambda} = - \boldsymbol {Q} \tag {5.39}$$

式中，Q 是一个任意的 $n \times n$ 正定矩阵， $\Lambda$ 由式(5.31)给出，其特征根实部为负。

取 $V_{1} = \frac{1}{2}\pmb{e}^{\mathrm{T}}\pmb{P}\pmb{e}, V_{2} = \frac{1}{2\gamma_{1}} (\pmb{\theta}_{f} - \pmb{\theta}_{f}^{*})^{\mathrm{T}}(\pmb{\theta}_{f} - \pmb{\theta}_{f}^{*}), V_{3} = \frac{1}{2\gamma_{2}} (\pmb{\theta}_{g} - \pmb{\theta}_{g}^{*})^{\mathrm{T}}(\pmb{\theta}_{g} - \pmb{\theta}_{g}^{*})$ 。令 $\pmb{M} = \pmb{b}[(\pmb{\theta}_{f} - \pmb{\theta}_{f}^{*})^{\mathrm{T}}\pmb{\xi}(\pmb{x}) + (\pmb{\theta}_{f} - \pmb{\theta}_{f}^{*})^{\mathrm{T}}\pmb{\eta}(\pmb{x})u + \omega]$ ，则式(5.37)变为
