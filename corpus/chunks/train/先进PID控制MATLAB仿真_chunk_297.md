# 5.5.2 输出延迟观测器的设计

引理 1 $^{[10]}$ ：针对线性延迟系统

$$\dot {x} (t) = A x (t) + B x (t - \Delta) \tag {5.52}$$

其稳定性条件为

$$s I - A - B \mathrm{e} ^ {- \Delta s} = 0 \tag {5.53}$$

的特征根的实部为负，则延迟系统式（5.52）为指数稳定。

针对本延迟系统式（5.52），取 $\hat{z} = \left[\hat{\theta} \quad \hat{\dot{\theta}}\right]^{\mathrm{T}}$ ，设计如下延迟观测器

$$\dot {\hat {z}} (t) = A \hat {z} (t) + H u (t) + K [ \overline {{{y}}} (t) - C \hat {z} (t - \Delta) ] \tag {5.54}$$

式中， $\hat{z}(t-\Delta)$ 是 $\hat{z}(t)$ 的延迟信号。

由式（5.50）～式（5.54）有

$$\dot {\delta} (t) = A \delta (t) - K C \delta (t - \Delta) \tag {5.55}$$

式中， $\delta(t)=z(t)-\hat{z}(t)$ 。

则根据引理 1，延迟观测器的稳定性条件为：选择合适的 K，使式（5.48）特征根的实部为负，则延迟系统式（5.55）为指数稳定，其稳定性条件为方程

$$s \pmb {I} - \pmb {A} + \pmb {K C} \mathrm{e} ^ {- \Delta s} = 0 \tag {5.56}$$

其特征根 s 在负半面。

仿真中首先根据经验给出 K 值，然后采用 MATLAB 函数 “fsolve” 来解方程式（5.56）中的根 s，使其在负半面，从而验证 K。

![](image/fa8c3d7d24941d46160b347ca99e8671e2055c174a4fcbb79c177f9e3ce50fcd.jpg)
