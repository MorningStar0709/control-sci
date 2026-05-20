$$
\left\{ \begin{array}{l} \dot {x} _ {1} (t) = A _ {1} x _ {1} (t) + B _ {1} u _ {1} (t), \\ y _ {1} (t) = C _ {1} x _ {1} (t) + D _ {1} u _ {1} (t), \end{array} \right. \tag {1.2.14}
$$

和

$$
\left\{ \begin{array}{l} \dot {x} _ {2} (t) = A _ {2} x _ {2} (t) + B _ {2} y _ {1} (t), \\ u _ {1} (t) = C _ {2} x _ {2} (t) + D _ {2} y _ {1} (t) + u (t). \end{array} \right. \tag {1.2.15}
$$

这里把 $u(t)$ 看成参考输入信号或复合系统的控制输入，其余各符号意义同前.

将系统(1.2.15)代到系统(1.2.14)中去,复合系统的状态变量记为 $x(t)=[x_{1}^{\mathrm{T}}(t),x_{2}^{\mathrm{T}}(t)]^{\mathrm{T}}$ ，则反馈系统的状态方程和量测方程为

$$
\left\{ \begin{array}{l} \dot {x} (t) = A x (t) + \left[ \begin{array}{c} B _ {1} - B _ {1} D _ {2} D ^ {- 1} D _ {1} \\ B _ {2} D ^ {- 1} D _ {1} \end{array} \right] u (t), \\ y (t) = \left[ \begin{array}{c c} D ^ {- 1} C _ {1} & D ^ {- 1} D _ {1} C _ {2} \end{array} \right] x (t) + D ^ {- 1} D _ {1} u (t). \end{array} \right.
$$

其中 $D = I - D_{1}D_{2}$ ,

$$
\boldsymbol {A} = \left[ \begin{array}{c c} \boldsymbol {A} _ {1} + \boldsymbol {B} _ {1} \boldsymbol {D} _ {2} \boldsymbol {D} ^ {- 1} \boldsymbol {C} _ {1} & \boldsymbol {B} _ {1} \boldsymbol {C} _ {2} + \boldsymbol {B} _ {1} \boldsymbol {D} _ {2} \boldsymbol {D} ^ {- 1} \boldsymbol {D} _ {1} \boldsymbol {C} _ {2} \\ \boldsymbol {B} _ {2} \boldsymbol {D} ^ {- 1} \boldsymbol {C} _ {1} & \boldsymbol {A} _ {2} + \boldsymbol {B} _ {1} \boldsymbol {D} _ {2} \boldsymbol {D} ^ {- 1} \boldsymbol {C} _ {2} \end{array} \right]
$$

为了使反馈系统是物理能实现的，必须假定 $I - D_{1}D_{2}$ 的逆存在．记

$$\boldsymbol {W} _ {i} (s) = \boldsymbol {C} _ {i} \left(s \boldsymbol {I} _ {n _ {i}} - \boldsymbol {A} _ {i}\right) ^ {- 1} \boldsymbol {B} _ {i} + \boldsymbol {D} _ {i}, i = 1, 2,$$

可得

$$y _ {1} (s) = \boldsymbol {W} _ {1} (s) u _ {1} (s), \quad u _ {1} (s) = \boldsymbol {W} _ {2} (s) y _ {1} (s) + u (s).$$

由此得出

$$(I - W _ {1} (s) W _ {2} (s)) y _ {1} (s) = W _ {1} (s) u (s).$$

如果 $I - W_{1}(s)W_{2}(s)$ 非奇异，即 $\operatorname{det}[I - W_1(s)W_2(s)] \neq 0$ ，那么

$$y _ {1} (s) = \left(I - W _ {1} (s) W _ {2} (s)\right) ^ {- 1} W _ {1} (s) u (s).$$

因此，反馈系统的传递函数矩阵为

$$\boldsymbol {W} (s) = \left(\boldsymbol {I} - \boldsymbol {W} _ {1} (s) \boldsymbol {W} _ {2} (s)\right) ^ {- 1} \boldsymbol {W} _ {1} (s).$$

因为当 $\operatorname{det}[I - W_1(s)W_2(s)] \neq 0$ 时，有

$$\left(\boldsymbol {I} - \boldsymbol {W} _ {1} (s) \boldsymbol {W} _ {2} (s)\right) ^ {- 1} \boldsymbol {W} _ {1} (s) = \boldsymbol {W} _ {1} (s) \left(\boldsymbol {I} - \boldsymbol {W} _ {2} (s) \boldsymbol {W} _ {1} (s)\right) ^ {- 1},$$

所以反馈系统的传递函数矩阵又可写成

$$\boldsymbol {W} (s) = \boldsymbol {W} _ {1} (s) (\boldsymbol {I} - \boldsymbol {W} _ {2} (s) \boldsymbol {W} _ {1} (s)) ^ {- 1}.$$

$\operatorname{det}[I - W_1(s)W_2(s)] \neq 0$ 是使反馈系统为物理能实现的条件，即是反馈系统有意义的不可缺少的条件。因此，在研究反馈系统时必须十分谨慎。
