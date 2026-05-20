# 8.1 分离定理和离散随机线性调节器问题

首先回顾一下第5章中关于确定性系统线性二次型最优控制的结果。将第5章中的式(5-52)、(5-53)、(5-64)、(5-61)重写于下：

线性离散系统状态方程(第5章式(5-52))

$$\boldsymbol {X} (k + 1) = \boldsymbol {A} (k) \boldsymbol {X} (k) + \boldsymbol {B} (k) \boldsymbol {U} (k) \tag {8-1}$$

二次型性能指标(第5章式(5-53))

$$J = \frac {1}{2} \boldsymbol {X} ^ {\mathrm{T}} (N) \boldsymbol {P} (N) \boldsymbol {X} (N) +\frac {1}{2} \sum_ {k = 0} ^ {N - 1} \left[ \boldsymbol {X} ^ {\mathrm{T}} (k) \boldsymbol {Q} (k) \boldsymbol {X} (k) + \boldsymbol {U} ^ {\mathrm{T}} (k) \boldsymbol {R} (k) \boldsymbol {U} (k) \right] \tag {8-2}$$

$P(N), Q(k)$ 为半正定加权阵， $R(k)$ 为正定加权阵。最优控制为(第5章式(5-64))

$$\boldsymbol {U} (k) = - \left[ \boldsymbol {R} (k) + \boldsymbol {B} ^ {\mathrm{T}} (k) \boldsymbol {K} (k + 1) \boldsymbol {R} (k) \right] ^ {- 1}.\boldsymbol {B} ^ {\mathrm{T}} (k) \boldsymbol {K} (k + 1) \boldsymbol {A} (k) \boldsymbol {X} (k) \tag {8-3}$$

其中 $K(k)$ 满足矩阵黎卡提差分方程(第5章式(5-61))

$$\boldsymbol {K} (k) = \boldsymbol {Q} (k) + \boldsymbol {A} ^ {\mathrm{T}} (k) \boldsymbol {K} (k + 1) \boldsymbol {A} (k) - \boldsymbol {A} ^ {\mathrm{T}} (k) \boldsymbol {K} (k + 1) \boldsymbol {B} (k) \cdot[ \boldsymbol {R} (k) + \boldsymbol {B} ^ {\mathrm{T}} (k) \boldsymbol {K} (k + 1) \boldsymbol {B} (k) ] ^ {- 1} \boldsymbol {B} ^ {\mathrm{T}} (k) \boldsymbol {K} (k + 1) \boldsymbol {A} (k) \tag {8-4}\boldsymbol {K} (N) = \boldsymbol {P} (N) \tag {8-5}$$

为了与本章的符号统一起来,将上面的方程改写如下:
