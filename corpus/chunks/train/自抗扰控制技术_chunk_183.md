# 5.1.5 函数发生器来安排过渡过程而实现的“线性 PID”

用跟踪微分器来安排过渡过程的部分改为用适当的函数发生器来直接安排过渡过程(先给出速度发生器,然后积分此速度函数得安排的过渡过程)得到如下算式

$$
\left\{ \begin{array}{l} v _ {2} = \frac {1}{4} \sin \left(\frac {\pi}{T _ {0}} t\right) \left(1 - \operatorname{sign} \left(t - T _ {0}\right)\right) \\ v _ {1} = v _ {1} + h v _ {2} \\ e = z _ {1} - y \\ \mathrm{fe} = \operatorname{fal} \left(e, \frac {1}{2}, \delta\right) \\ z _ {1} = z _ {1} + h \left(z _ {2} - \beta_ {0 1} c\right) \\ z _ {2} = z _ {2} + h \left(- \beta_ {0 2} f c\right) \\ e _ {1} = v _ {1} - z _ {1}, e _ {2} = v _ {2} - z _ {2}, e _ {0} = \int_ {0} ^ {t} e _ {1} (\tau) \mathrm{d} \tau \\ u = \beta_ {0} e _ {0} + \beta_ {1} e _ {1} + \beta_ {2} e _ {2} \end{array} \right. \tag {5.1.16}
$$

从以上仿真结果来看,对经典 PID 结构,单单引入合理“安排过渡过程”和“微分信号提取”这两种手法,已经使 PID 控制器的功能大大提高.
