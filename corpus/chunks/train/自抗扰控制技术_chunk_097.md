$$
\left\{ \begin{array}{l} \dot {x} _ {1} = x _ {2} \\ \dot {x} _ {2} = f (x _ {1}, x _ {2}, g (u, \dot {u})) \end{array} \right. \tag {3.1.11}
$$

只要对任意 v, U 从代数方程

$$
\left\{ \begin{array}{l} f (x _ {1}, x _ {2}, U) = v \\ g (u, \dot {u}) = U \end{array} \right. \tag {3.1.12}
$$

能解出

$$
\left\{ \begin{array}{l} U = h _ {0} (x _ {1}, x _ {2}, v) \\ \dot {u} = h _ {1} (u, U, v) \end{array} \right. \tag {3.1.13}
$$

那么原系统变成如下两个系统

$$
\sum_ {1}: \left\{ \begin{array}{l} \dot {x} _ {1} = x _ {2} \\ \dot {x} _ {2} = v \end{array} \right.
$$

和

$$\sum_ {2}: \dot {u} = h _ {1} (u, U (x _ {1}, x _ {2}, v)) \tag {3.1.14}$$

其中系统 $\sum_{i}$ 是线性控制系统，其控制量为 v。如果确定了 $v(t)$ ，那么可以确定出对应的轨线 $x_{1}(t)$ ， $x_{2}(t)$ ，从而函数 $U(x_{1}(t)$ ， $x_{2}(t)$ ， $v(t)=U(t)$ 也被确定，因此只要有了 u 的初值 $u(0)$ ，就能从方程 (3.1.14) 确定出实际需要的控制量 $u(t)$ 。在这里，为了能够确定出控制量 $u(t)$ ，需要微分方程 (3.1.14) 对任意 $U(t)$ 应该稳定才行。但是微分方程 (3.1.14) 相当于原系统的零点系统，而其稳定性相当于原系统的最小相位系统。

在这里,我们把量 $U(t)$ 作为“虚拟控制量”. 先根据控制系统

$$
\left\{ \begin{array}{l} \dot {x} _ {1} = x _ {2} \\ \dot {x} _ {2} = f (x _ {1}, x _ {2}, U) \end{array} \right.
$$

来确定出虚拟控制量 $U(t)$ ，然后根据关系式

$$g (\dot {u}, u) = U$$

确定出实际的控制量 $u(t)$ .

例如，线性最小相位系统的传递函数

$$W (s) = \frac {s + c _ {1}}{s ^ {2} + a _ {1} s + a _ {2}}, c _ {1} > 0 \tag {3.1.15}$$

的多项式表示为

$$
\left\{ \begin{array}{l} (s ^ {2} + a _ {1} s + a _ {2}) x = (s + c _ {1}) u \\ y = x \end{array} \right. \tag {3.1.16}
$$

于是其状态变量实现为

$$
\left\{ \begin{array}{l} x _ {1} = x _ {2} \\ \dot {x} _ {2} = - a _ {2} x _ {1} - a _ {1} x _ {2} + c _ {1} u + \dot {u} \\ y = x _ {1} \end{array} \right. \tag {3.1.17}
$$

对这个系统相应于(3.1.12)的代数方程为

$$
\left\{ \begin{array}{l} f (x _ {1}, x _ {2}, g (u, \dot {u})) = - a _ {2} x _ {1} - a _ {1} x _ {2} + U = v \\ g (u, \dot {u}) = c _ {1} u + \dot {u} = U \end{array} \right. \tag {3.1.18}
$$

而相当于式 $(3.1.13)$ 的解为

$$
\left\{ \begin{array}{l} U = v + a _ {2} x _ {1} + a _ {1} x _ {2} \\ \dot {u} = - c _ {1} u + U \end{array} \right. \tag {3.1.19}
$$

现在假定 $a_{1} = a_{2} = c_{1} = 1$ ，那么原系统(3.1.17)变为

$$
\left\{ \begin{array}{l} \dot {x} _ {1} = x _ {2} \\ \dot {x} _ {2} = - x _ {1} - x _ {2} + u + \dot {u} \\ y = x _ {1} \end{array} \right. \tag {3.1.20}
$$

对应于式 $(3.1.18)$ 的方程为

$$
\left\{ \begin{array}{l} - x _ {1} - x _ {2} + U = v \\ u + \dot {u} = U \end{array} \right. \tag {3.1.21}
$$

现在取

$$v = - 4 x _ {1} - 3. 5 x _ {2} + 4 \tag {3.1.22}$$

那么

$$U = - 3 x _ {1} - 2. 5 x _ {2} + 4$$

而闭环系统变成

$$
\left\{ \begin{array}{l} \dot {x} _ {1} = x _ {2} \\ \dot {x} _ {2} = - 4 x _ {1} - 3. 5 x _ {2} + 4 \\ y = x _ {1} \end{array} \right. \tag {3.1.23}
$$

式(3.1.21)的第二个方程变成

$$\dot {u} = - u - 3 x _ {1} - 2. 5 x _ {2} + 4 \tag {3.1.24}$$
