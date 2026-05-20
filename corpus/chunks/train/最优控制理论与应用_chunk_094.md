$$J = \frac {1}{2} c x ^ {2} (2) + \frac {1}{2} \sum_ {k = 0} ^ {1} u ^ {2} (k) \tag {5-67}$$

要求寻找最优序列 $u(0)$ 、 $u(1)$ ，使 J 最小。

解 从给定的系统方程可见, 系统矩阵 $A(k) = 1$ , 输入矩阵 $B(k) = 1$ 。从给定的性能指标可知加权阵 $P(N) = c, Q(k) = 0, R(k) = 1$ 。黎卡提方程(5-60)可写成

$$\boldsymbol {K} (k) = \boldsymbol {Q} (k) + \boldsymbol {A} ^ {\mathrm{T}} (k) \left[ \boldsymbol {K} ^ {- 1} (k + 1) + \boldsymbol {B} (k) \boldsymbol {R} ^ {- 1} (k) \boldsymbol {B} ^ {\mathrm{T}} (k) \right] ^ {- 1} \boldsymbol {A} (k)= \left[ \boldsymbol {K} ^ {- 1} (k + 1) + 1 \right] ^ {- 1} = \frac {\boldsymbol {K} (k + 1)}{\boldsymbol {K} (k + 1) + 1} \tag {5-68}$$

终端值 $\boldsymbol{K}(2)=\boldsymbol{P}(2)=c$ 。由 k=2 反向计算，求出 $\boldsymbol{K}(1)$ 、 $\boldsymbol{K}(0)$ 。

$$\boldsymbol {K} (1) = \frac {\boldsymbol {K} (2)}{\boldsymbol {K} (2) + 1} = \frac {c}{c + 1} \tag {5-69}\boldsymbol {K} (0) = \frac {\boldsymbol {K} (1)}{\boldsymbol {K} (1) + 1} = \frac {c}{2 c + 1} \tag {5-70}$$

再利用式(5-63)计算 $u(k), k = 0, 1$ 。

$$u (k) = - \boldsymbol {R} ^ {- 1} (k) \boldsymbol {B} ^ {\mathrm{T}} (k) \boldsymbol {A} ^ {- \mathrm{T}} (k) [ \boldsymbol {K} (k) - \boldsymbol {Q} (k) ] \boldsymbol {X} (k) = - \boldsymbol {K} (k) \boldsymbol {X} (k)u (0) = - K (0) x (0) = - \frac {c}{2 c + 1} x (0) \tag {5-71}x (1) = x (0) + u (0) = \frac {c + 1}{2 c + 1} x (0) \tag {5-72}$$

再计算 $u(1)$ ，有

$$u (1) = - K (1) x (1) = - \frac {c}{c + 1} x (1) = - \frac {c}{2 c + 1} x (0) \quad (5 - 7 3)$$
