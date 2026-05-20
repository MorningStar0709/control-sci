# 5.4.3 自适应律的设计

由式(5.46)得

$$f (\boldsymbol {x}) = - \boldsymbol {b u} ^ {*} + y _ {m} ^ {(n)} + \boldsymbol {K} ^ {\mathrm{T}} \boldsymbol {e}$$

将上式代入式(5.42)，并引入式(5.48)得

$$x ^ {(n)} = - \boldsymbol {b u} ^ {*} + y _ {m} ^ {(n)} + \boldsymbol {K} ^ {\mathrm{T}} \boldsymbol {e} + \boldsymbol {b u}$$

整理得

$$e ^ {(n)} = - \boldsymbol {K} ^ {\mathrm{T}} \boldsymbol {e} + \boldsymbol {b} \left[ u ^ {*} - u _ {\mathrm{D}} (\boldsymbol {x} \mid \boldsymbol {\theta}) \right] \tag {5.53}$$

令

$$
\boldsymbol {\Lambda} = \left[ \begin{array}{c c c c c c c} 0 & 1 & 0 & 0 & \dots & 0 & 0 \\ 0 & 0 & 1 & 0 & \dots & 0 & 0 \\ \dots & \dots & \dots & \dots & \dots & \dots & \dots \\ 0 & 0 & 0 & 0 & \dots & 0 & 1 \\ - k _ {n} & - k _ {n - 1} & \dots & \dots & \dots & \dots & - k _ {1} \end{array} \right], \boldsymbol {b} = \left[ \begin{array}{l} 0 \\ 0 \\ \dots \\ 0 \\ b \end{array} \right] \tag {5.54}
$$

则闭环系统动态方程式(5.53)可写成向量形式

$$\dot {\boldsymbol {e}} = \boldsymbol {\Lambda} \boldsymbol {e} + \boldsymbol {b} \left[ u ^ {*} - u _ {\mathrm{D}} (\boldsymbol {x} \mid \boldsymbol {\theta}) \right] \tag {5.55}$$

定义最优参数为

$$\boldsymbol {\theta} ^ {*} = \arg \min _ {\prod_ {i = 1} ^ {n} m _ {i}} \left[ \sup _ {x \in R ^ {n}} | u _ {\mathrm{D}} (\boldsymbol {x} | \boldsymbol {\theta}) - u ^ {*} | \right] \tag {5.56}$$

定义最小逼近误差为

$$\omega = u _ {\mathrm{D}} (\boldsymbol {x} \mid \boldsymbol {\theta} ^ {*}) - u ^ {*} \tag {5.57}$$

由式(5.55)可得

$$\dot {\boldsymbol {e}} = \boldsymbol {\Lambda} \boldsymbol {e} + \boldsymbol {b} \left(u _ {\mathrm{D}} (\boldsymbol {x} \mid \boldsymbol {\theta} ^ {*}) - u _ {\mathrm{D}} (\boldsymbol {x} \mid \boldsymbol {\theta})\right) - \boldsymbol {b} \left(u _ {\mathrm{D}} (\boldsymbol {x} \mid \boldsymbol {\theta} ^ {*}) - u ^ {*}\right) \tag {5.58}$$

由式(5.57)，可将误差方程式(5.58)改写为

$$\dot {\boldsymbol {e}} = \boldsymbol {\Lambda} \boldsymbol {e} + \boldsymbol {b} \left(\boldsymbol {\theta} ^ {*} - \boldsymbol {\theta}\right) ^ {\mathrm{T}} \boldsymbol {\xi} (\boldsymbol {x}) - \boldsymbol {b} _ {\omega} \tag {5.59}$$

参考文献[12],本控制算法的稳定性分析如下:

定义 Lyapunov 函数为

$$V = \frac {1}{2} e ^ {\mathrm{T}} P e + \frac {b}{2 \gamma} (\boldsymbol {\theta} ^ {*} - \boldsymbol {\theta}) ^ {\mathrm{T}} (\boldsymbol {\theta} ^ {*} - \boldsymbol {\theta}) \tag {5.60}$$

式中, 参数 $\gamma$ 是正的常数。

$\pmb{P}$ 为一个正定矩阵且满足Lyapunov方程

$$\boldsymbol {\Lambda} ^ {\mathrm{T}} \boldsymbol {P} + \boldsymbol {P} \boldsymbol {\Lambda} = - \boldsymbol {Q} \tag {5.61}$$
