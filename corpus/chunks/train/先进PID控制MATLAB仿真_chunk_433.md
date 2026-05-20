# 3. 稳定性分析

由式（9.17）代入式（9.12），可得如下系统的闭环动态方程：

$$\ddot {e} = - \boldsymbol {K} ^ {\mathrm{T}} \boldsymbol {E} + \left[ \hat {f} (\boldsymbol {x}) - f (\boldsymbol {x}) \right] \tag {9.20}$$

令

$$
\boldsymbol {A} = \left[ \begin{array}{c c} 0 & 1 \\ - k _ {\mathrm{p}} & - k _ {\mathrm{d}} \end{array} \right], \boldsymbol {b} = \left[ \begin{array}{l} 0 \\ 1 \end{array} \right] \tag {9.21}
$$

则动态方程（9.20）可写为向量形式：

$$\dot {\boldsymbol {E}} = \boldsymbol {\Lambda} \boldsymbol {E} + \boldsymbol {b} [ \hat {f} (\boldsymbol {x}) - f (\boldsymbol {x}) ] \tag {9.22}$$

设最优参数为

$$W ^ {*} = \arg \min _ {W \in \Omega} \left[ \sup \left| \hat {f} (\boldsymbol {x}) - f (\boldsymbol {x}) \right| \right] \tag {9.23}$$

式中， $\Omega$ 为 W 的集合。

定义最小逼近误差为

$$\omega = \hat {f} (\boldsymbol {x} \mid \boldsymbol {W} ^ {*}) - f (\boldsymbol {x}) \tag {9.24}$$

式 $（9.22）$ 可写为

$$\dot {\boldsymbol {E}} = \boldsymbol {A} \boldsymbol {E} + \boldsymbol {b} \left\{\left[ \hat {f} (\boldsymbol {x}) - \hat {f} (\boldsymbol {x} | \boldsymbol {W} ^ {*}) \right] + \omega \right\} \tag {9.25}$$

将式（9.18）代入式（9.25），可得闭环动态方程：

$$\dot {\boldsymbol {E}} = \boldsymbol {\Lambda} \boldsymbol {E} + \boldsymbol {b} \left[ \left(\hat {\boldsymbol {W}} - \boldsymbol {W} ^ {*}\right) ^ {\mathrm{T}} \boldsymbol {h} (\boldsymbol {x}) + \omega \right] \tag {9.26}$$

该方程清晰地描述了跟踪误差和权值 $\hat{W}$ 之间的关系。自适应律的任务是为 $\hat{W}$ 确定一个调节机理，使得跟踪误差E和参数误差 $\hat{W}-W^{*}$ 达到最小。

定义 Lyapunov 函数:

$$V = \frac {1}{2} \boldsymbol {E} ^ {\mathrm{T}} \boldsymbol {P} \boldsymbol {E} + \frac {1}{2 \gamma} \left(\hat {\boldsymbol {W}} - \boldsymbol {W} ^ {*}\right) ^ {\mathrm{T}} \left(\hat {\boldsymbol {W}} - \boldsymbol {W} ^ {*}\right) \tag {9.27}$$

式中， $\gamma$ 为正常数；P 为一个正定矩阵且满足 Lyapunov 方程。

$$\boldsymbol {\Lambda} ^ {\mathrm{T}} \boldsymbol {P} + \boldsymbol {P} \boldsymbol {\Lambda} = - \boldsymbol {Q} \tag {9.28}$$

式中，Q 为一个任意的 $2 \times 2$ 正定矩阵；A 由式（9.21）给出。

取 $V_{1}=\frac{1}{2}E^{T}PE$ ， $V_{2}=\frac{1}{2\gamma}\left(\hat{W}-W^{*}\right)^{T}\left(\hat{W}-W^{*}\right)$ ，令 $M=b\left[\left(\hat{W}-W^{*}\right)^{T}h(x)+\omega\right]$ ，则
(9.26) 式变为

$$\dot {\boldsymbol {E}} = \boldsymbol {\Lambda} \boldsymbol {E} + \boldsymbol {M}$$

则
