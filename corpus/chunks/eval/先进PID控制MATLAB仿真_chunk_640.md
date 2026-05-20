# 1. LQR 控制

采用最优控制中的 LQR 方法。该方法针对状态方程 $\dot{x} = Ax + Bu$ ，通过确定最佳控制量 $u(t) = -Kx(t)$ 的矩阵 K，使得控制性能指标 J 达到极小

$$J = \int_ {0} ^ {\infty} (\boldsymbol {x} ^ {T} \boldsymbol {Q} x + u ^ {\mathrm{T}} R u) \mathrm{d} t$$

式中，Q 为正定（或半正定）厄米特或实对称矩阵；R 为正定厄米特或实对称矩阵；Q 和 R 分别为各个状态跟踪误差和能量损耗的相对重要性；Q 中对角矩阵的各个元素分别代表各项指标误差的相对重要性。

基于 LQR 的增益及控制律为

$$u (k) = - K x \tag {17.10}\boldsymbol {K} = \mathrm{LQR} (\boldsymbol {A}, \boldsymbol {B}, \boldsymbol {Q}, \boldsymbol {R}) \tag {17.11}$$

式中，LQR 为 MATLAB 下的线性二次型调节器。
