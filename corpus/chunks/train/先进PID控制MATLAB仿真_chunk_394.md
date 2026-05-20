# 8.2.3 稳定性分析

由式（8.12）代入式（8.4），可得如下模糊控制系统的闭环动态方程：

$$\ddot {e} = - \boldsymbol {K} ^ {\mathrm{T}} \boldsymbol {E} + \left[ \hat {f} (\boldsymbol {x} | \theta_ {f}) - f (\boldsymbol {x}) \right] \tag {8.15}$$

令

$$
\boldsymbol {A} = \left[ \begin{array}{c c} 0 & 1 \\ - k _ {\mathrm{p}} & - k _ {\mathrm{d}} \end{array} \right], \quad \boldsymbol {b} = \left[ \begin{array}{l} 0 \\ 1 \end{array} \right] \tag {8.16}
$$

则动态方程（8.15）可写为向量形式：

$$\dot {\boldsymbol {E}} = \boldsymbol {\Lambda} \boldsymbol {E} + \boldsymbol {b} \left[ \hat {f} (\boldsymbol {x} \mid \theta_ {f}) - f (\boldsymbol {x}) \right] \tag {8.17}$$

设最优参数为

$$\theta_ {f} ^ {*} = \arg \min \left[ \sup \left| \hat {f} (\boldsymbol {x} \mid \theta_ {f}) - f (\boldsymbol {x}) \right| \right] \tag {8.18}$$

式中， $\Omega_{f}$ 为 $\theta_{f}$ 的集合， $\theta_{f} \in \Omega_{f}$ 。

定义最小逼近误差为

$$\omega = \hat {f} (\boldsymbol {x} \mid \theta_ {f} ^ {*}) - f (\boldsymbol {x}) \tag {8.19}$$

式（8.17）可写为

$$\dot {\boldsymbol {E}} = \boldsymbol {A} \boldsymbol {E} + \boldsymbol {b} \left\{\left[ \hat {f} (\boldsymbol {x} | \theta_ {f}) - \hat {f} (\boldsymbol {x} | \theta_ {f} ^ {*}) \right] + \omega \right\} \tag {8.20}$$

将式（8.13）代入式（8.20），可得闭环动态方程：

$$\dot {\boldsymbol {E}} = \boldsymbol {\Lambda} \boldsymbol {E} + \boldsymbol {b} \left[ \left(\theta_ {f} - \theta_ {f} ^ {*}\right) ^ {\mathrm{T}} \xi (\boldsymbol {x}) + \omega \right] \tag {8.21}$$

该方程清晰地描述了跟踪误差和控制参数 $\theta_{f}$ 之间的关系。自适应律的任务是为 $\theta_{f}$ 确定一个调节机理，使得跟踪误差 E 和参数误差 $\theta_{f}-\theta_{f}^{*}$ 达到最小。

定义 Lyapunov 函数

$$V = \frac {1}{2} \boldsymbol {E} ^ {\mathrm{T}} \boldsymbol {P} \boldsymbol {E} + \frac {1}{2 \gamma} \left(\theta_ {f} - \theta_ {f} ^ {*}\right) ^ {\mathrm{T}} \left(\theta_ {f} - \theta_ {f} ^ {*}\right) \tag {8.22}$$

式中， $\gamma$ 为正常数；P 为一个正定矩阵且满足 Lyapunov 方程：

$$\boldsymbol {\Lambda} ^ {\mathrm{T}} \boldsymbol {P} + \boldsymbol {P} \boldsymbol {\Lambda} = - \boldsymbol {Q} \tag {8.23}$$

式中，Q 为一个任意的 $2 \times 2$ 正定矩阵；A 由式（8.16）给出。

取 $V_{1}=\frac{1}{2}\boldsymbol{E}^{\mathrm{T}}\boldsymbol{P}\boldsymbol{E}$ ， $V_{2}=\frac{1}{2\gamma}\left(\theta_{f}-\theta_{f}^{*}\right)^{\mathrm{T}}\left(\theta_{f}-\theta_{f}^{*}\right)$ 。为了描述方便，令 $M=b\left[\left(\theta_{f}-\theta_{f}^{*}\right)^{\mathrm{T}}\xi(\boldsymbol{x})+\omega\right]$ ，则（8.21）式变为
