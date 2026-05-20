# 15.2.1 四旋翼飞行器动力学模型

四旋翼飞行器的动力学模型的特点为具有多入多出，带有强耦合的欠驱动系统。根据拉格朗日方程，其动力学模型表示为 $^{[5]}$

$$\ddot {x} = u _ {1} \left(\cos \phi \sin \theta \cos \psi + \sin \phi \sin \psi\right) - K _ {1} \dot {x} / m\ddot {y} = u _ {1} (\sin \phi \sin \theta \cos \psi - \cos \phi \sin \psi) - K _ {2} \dot {y} / m\ddot {z} = u _ {1} \cos \phi \cos \psi - g - K _ {3} \dot {z} / m\ddot {\theta} = u _ {2} - \frac {l K _ {4}}{I _ {1}} \dot {\theta} \tag {15.11}\ddot {\psi} = u _ {3} - \frac {l K _ {5}}{I _ {2}} \dot {\psi}\ddot {\phi} = u _ {4} - \frac {l K _ {6}}{I _ {3}} \dot {\phi}$$

式中， $[\phi,\theta,\psi]$ 为飞行器三个姿态的欧拉角度，分别代表滚转角、俯仰角和偏航角； $[x,y,z]$ 为飞行器质心在惯性坐标系中的位置坐标；l 为飞行器半径长度表示每个旋翼末端到飞行器重心的距离；m 为四旋翼无人机的负载总质量； $I_{i}$ 为围绕每个轴的转动惯量； $K_{i}$ 为阻力系数。

控制目标： $x \rightarrow 0$ ， $y \rightarrow 0$ ， $z \rightarrow z_{d}$ ， $\phi \rightarrow \phi_{d}$ 。

需要说明的是，由于欠驱动特性的存在，不可能对所有的6个自由度都进行跟踪。一个合理的控制目标方案为：跟踪航迹 $[x,y,z]$ 和滚转角 $\phi$ ，同时保证另外两个角度。

下面的设计过程中，采用了Hurwitz判据，即针对二阶系统 $a_2s^2 + a_1s + a_0 = 0$ 的稳定性条件为

$$
\left\{ \begin{array}{l l} a _ {0}, & a _ {1}, a _ {2} > 0 \\ a _ {1} a _ {0} > 0 \end{array} \right.
$$

![](image/a1a658cbe746cf56868bf569505618b886d4a61f1007175deab0d85734f5b987.jpg)
