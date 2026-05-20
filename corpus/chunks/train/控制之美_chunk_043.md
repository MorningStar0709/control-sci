# 2.3.1 传递函数

本节将介绍传递函数(Transfer Function)，它是经典控制理论的基础。系统的传递函数 $G(s)$ 的定义是：在零初始条件下，系统输出的拉普拉斯变换与系统输入的拉普拉斯变换之间的比值，即

$$G (s) = \frac {X (s)}{U (s)} \tag {2.3.1}$$

式(2.3.1)所示系统可以用框图表示,如图2.3.1所示,其中, $U(s)G(s)=X(s)$ 。

根据表 2.2.1, 单位冲激函数 $\delta(t)$ 的拉普拉斯变换 $\mathcal{L}[\delta(t)]=1$ , 系统对其响应为

$$X (s) = \mathcal {L} [ \delta (t) ] G (s) = G (s) \tag {2.3.2}$$

式(2.3.2)说明,当单位冲激函数作用在线性时不变系统上时,其输出(即系统的单位冲激响应)等于传递函数本身。

![](image/32871cd858c816a7151a23f621b9736c1b147f88d79770842ba72c0361e1b543.jpg)  
图2.3.1 动态系统框图

式(2.3.2)从另一个角度验证了2.1.1节中提出的重要概念: 单位冲激响应可以完全地定义线性时不变系统。同时, 根据例2.2.5, 卷积运算通过拉普拉斯变换成为乘法运算, 这也符合式(2.3.1)所表达出来的输入与输出之间的乘积关系。希望读者可以把这几部分内容结合起来理解, 从不同的角度理解线性时不变系统的特性。

经过拉普拉斯变换后,卷积关系的系统输入与输出 $x(t) = u(t) * h(t)$ 被简化为乘积关系 $X(s) = U(s)G(s)$ , 这将在很大程度上简化系统分析的复杂程度。回到图2.2.1的例子,首先对式(2.2.2)左右两边进行拉普拉斯变换,得到

$$
\begin{array}{l} \mathcal {L} [ u (t) ] = \mathcal {L} \left[ L \frac {\mathrm{d} x (t)}{\mathrm{d} t} + R x (t) \right] \\ \Rightarrow U (s) = L (s X (s) - x (0)) + R X (s) \tag {2.3.3a} \\ \end{array}
$$

其中， $L$ 是电感， $R$ 是电阻，它们都是正数。考虑零初始状态，即系统输出 $x(t)$ 的初始状态为 $x(0) = 0$ ，式(2.3.3a)可写成

$$U (s) = L s X (s) + R X (s) = (L s + R) X (s) \tag {2.3.3b}$$

其传递函数为

$$G (s) = \frac {X (s)}{U (s)} = \frac {1}{L s + R} \tag {2.3.4}$$

当一个常数输入 $u(t)=C$ 作用在系统上时, 其拉普拉斯变换为

$$U (s) = \mathcal {L} [ u (t) ] = \mathcal {L} [ C ] = \mathcal {L} [ C e ^ {- 0 t} ] = C \frac {1}{s + 0} = C \frac {1}{s} \tag {2.3.5}$$

将式(2.3.5)代入式(2.3.4)中,可以得到系统输出的拉普拉斯变换为

$$X (s) = U (s) G (s) = C \left(\frac {1}{s}\right) \left(\frac {1}{L s + R}\right) = \frac {C}{L} \frac {1}{s \left(s + \frac {R}{L}\right)} \tag {2.3.6}$$

若要分析这一系统输出的时间函数 $x(t)$ 的表现，可以采用2.2.3节中的方法求解其拉普拉斯逆变换。式(2.3.6)可以写为

$$X (s) = \frac {C}{L} \frac {1}{s \left(s + \frac {R}{L}\right)} = \frac {C}{L} \left(\frac {A}{s} + \frac {B}{s + \frac {R}{L}}\right) \tag {2.3.7}$$

利用分式分解法可得 $A=\frac{L}{R}$ , $B=-\frac{L}{R}$ ，代入式(2.3.7)中，得到

$$X (s) = \frac {C}{L} \left(\frac {\frac {L}{R}}{s} - \frac {\frac {L}{R}}{s + \frac {R}{L}}\right) = \frac {C}{R} \left(\frac {1}{s} - \frac {1}{s + \frac {R}{L}}\right) \tag {2.3.8}$$

对式(2.3.8)两边进行拉普拉斯逆变换,便可以得到系统的输出,即

$$x (t) = \mathcal {L} ^ {- 1} [ X (s) ] = \frac {C}{R} (\mathrm{e} ^ {0 t} - \mathrm{e} ^ {- \frac {R}{L} t}) = \frac {C}{R} - \frac {C}{R} \mathrm{e} ^ {- \frac {R}{L} t} \tag {2.3.9}$$

$x(t)$ 随时间的变化如图2.3.2所示。从图中可以得出，系统的输出将从0开始，随着时间的增加而无限地接近一个定值 $\frac{C}{R}$ 。
