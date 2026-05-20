$$\frac {\mathrm{d}}{\mathrm{d} t} \left(\frac {\partial H}{\partial \boldsymbol {U}}\right) = \frac {\mathrm{d}}{\mathrm{d} t} \left(\boldsymbol {B} ^ {\mathrm{T}} \boldsymbol {\lambda}\right) = - \boldsymbol {B} ^ {\mathrm{T}} \left(\boldsymbol {Q} \boldsymbol {X} + \boldsymbol {A} ^ {\mathrm{T}} \boldsymbol {\lambda}\right) = 0 \tag {9-16}\frac {\mathrm{d} ^ {2}}{\mathrm{d} t ^ {2}} \left(\frac {\partial H}{\partial \boldsymbol {U}}\right) = \frac {\mathrm{d}}{\mathrm{d} t} \left[ - \boldsymbol {B} ^ {\mathrm{T}} \left(\boldsymbol {Q} \boldsymbol {X} + \boldsymbol {A} ^ {\mathrm{T}} \boldsymbol {\lambda}\right) \right]= - \boldsymbol {B} ^ {\mathrm{T}} \left[ \boldsymbol {Q} \boldsymbol {A} \boldsymbol {X} + \boldsymbol {Q} \boldsymbol {B} \boldsymbol {U} - \boldsymbol {A} ^ {\mathrm{T}} \boldsymbol {Q} \boldsymbol {X} - \boldsymbol {A} ^ {\mathrm{T}} \boldsymbol {A} ^ {\mathrm{T}} \boldsymbol {\lambda} \right] = \mathbf {0} \tag {9-17}$$

假设 $B^{T}QB$ 是非奇异阵, 否则, 奇异控制不存在。解得

$$\boldsymbol {U} = - \left(\boldsymbol {B} ^ {\mathrm{T}} \boldsymbol {Q} \boldsymbol {B}\right) ^ {- 1} \boldsymbol {B} ^ {\mathrm{T}} \left[ \left(\boldsymbol {Q} \boldsymbol {A} - \boldsymbol {A} ^ {\mathrm{T}} \boldsymbol {Q}\right) \boldsymbol {X} - \boldsymbol {A} ^ {\mathrm{T}} \boldsymbol {A} ^ {\mathrm{T}} \boldsymbol {\lambda} \right] \tag {9-18}$$

上式表明,若存在奇异解,则奇异解必具有式(9-18)的形式。将式(9-18)和式(9-8)、(9-13)联立求解两点边值问题,可求出最优奇异弧段及其上的奇异最优控制。

若哈密顿函数 H 不显含 t，且末端时间 T 未定，由极小值原理可知沿最优轨迹哈密顿函数值恒等于零，即

$$H \equiv 0 \tag {9-19}$$

式(9-14)、(9-16)和(9-19)共 $2r+1$ 个标量方程，它们共同决定2n维(X,λ)空间中的 $2(n-r)-1$ 维的超曲面。这是因为奇异弧上的各点(X,λ)满足上述 $2r+1$ 个方程。因此，若最优奇异弧存在，必在由上述 $2r+1$ 个方程所决定的超曲面上，此超曲面称为奇异超曲面。

例9-1 已知二阶受控系统

$$\dot {x} _ {1} = x _ {2} (t) + u (t) \tag {9-20}\dot {x} _ {2} = - u (t)$$

标量约束满足如下不等式约束

$$\left| u (t) \right| \leqslant 1 \tag {9-21}$$

试求系统(9-20)由已知初态 $x_{1}(0) = x_{10}, x_{2}(0) = x_{20}$ 转移到坐标原点。且使性能指标

$$J = \frac {1}{2} \int_ {0} ^ {T} x _ {1} ^ {2} (t) \mathrm{d} t \tag {9-22}$$

为极小的最优控制。

哈密顿函数为

$$H = \frac {1}{2} x _ {1} ^ {2} + \lambda_ {1} (x _ {2} + u) - \lambda_ {2} u \tag {9-23}$$

由极小值原理可知,正常弧段上的最优控制为 Bang-Bang 形式,即

$$u ^ {*} = - \operatorname{sgn} \left\{\lambda_ {1} - \lambda_ {2} \right\} \tag {9-24}$$

相应的最优控制轨线(Bang-Bang弧段)满足如下的规范方程：
