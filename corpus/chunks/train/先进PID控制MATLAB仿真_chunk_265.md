# 5.2.3 指数收敛干扰观测器的设计

取 $\dot{\hat{d}} = K(d - \hat{d})$ ，定义辅助参数向量 $^{[2]}$

$$z = \hat {d} - K J \dot {\theta} \tag {5.12}$$

则 $\dot{z} = \dot{\hat{d}} - KJ\ddot{\theta}$ ，由于 $\dot{\hat{d}} = K(d - \hat{d}) = K(J\ddot{\theta} + b\dot{\theta} - u) - K\hat{d}$ ，则

$$\dot {z} = K (J \ddot {\theta} + b \dot {\theta} - u) - K \hat {d} - K J \ddot {\theta} = K (b \dot {\theta} - u) - K \hat {d}$$

干扰观测器设计为

$$
\left\{ \begin{array}{l} \dot {z} = K (b \dot {\theta} - u) - \dot {K} \hat {d} \\ \hat {d} = z + K J \dot {\theta} \end{array} \right. \tag {5.13}
$$

则

$$\dot {z} = K (b \dot {\theta} - T) - K (z + K J \dot {\theta}) = K (b \dot {\theta} - T - K J \dot {\theta}) - K z$$

针对常值干扰或慢干扰，可假设 $\dot{d} = 0^{[2]}$ ，则

$$\dot {\tilde {d}} = \dot {d} - \dot {\hat {d}} = - \dot {\hat {d}} = - \dot {z} - K J \ddot {\theta}$$

将 $\dot{z}$ 代入上式，得

$$
\begin{array}{l} \dot {\tilde {d}} = - \left(K (b \dot {\theta} - T - K J \dot {\theta}) - K z\right) - K J \ddot {\theta} \\ = - K (b \dot {\theta} - T - K J \dot {\theta}) + K z - K J \ddot {\theta} = K (z + K J \dot {\theta}) - K (J \ddot {\theta} + b \dot {\theta} - T) \\ = K \hat {d} - K (\boldsymbol {J} \ddot {\theta} + b \dot {\theta} - T) = K (\hat {d} - d) = - K \tilde {d} \\ \end{array}
$$

因而得到观测误差方程为

$$\dot {\tilde {d}} + K \tilde {d} = 0$$

解为

$$\tilde {d} (t) = \tilde {d} (t _ {0}) \exp (- K t)$$

由于 $\tilde{d}(t_{0})$ 的值是确定的，可见，观测器的收敛精度取决于参数 K 值。通过设计参数 K，使估计值 $\hat{d}$ 按指数逼近干扰 d 。由观测器式（5.13）可知，该观测器不需要 $\ddot{\theta}$ 信息。

![](image/a9f4888c4a8bc003a4fc71f89e5c4e37d73507212bcdae69650bdbc34a329451.jpg)
