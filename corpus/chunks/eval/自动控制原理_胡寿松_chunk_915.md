# (1) 控制系统状态空间模型描述

设有 n 个状态、m 个输入和 p 个输出的线性定常系统的状态空间模型为

$$\dot {\boldsymbol {x}} (t) = \boldsymbol {A} \boldsymbol {x} (t) + \boldsymbol {B} \boldsymbol {u} (t)\mathbf {y} (t) = \mathbf {C x} (t) + \mathbf {D u} (t)$$

在 MATLAB 中, 利用 ss 命令来建立状态空间模型。

命令格式：sys = ss(A, B, C, D, Ts)

其中，A、B、C、D表示状态空间模型的系数矩阵；Ts表示采样时间，缺省时描述的是连续系统。
