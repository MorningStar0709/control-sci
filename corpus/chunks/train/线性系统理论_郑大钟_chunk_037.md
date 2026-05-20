# 1.2 系统按其状态空间描述的分类

系统的状态空间描述是其动力学特性的完整表征。各类系统在结构上和特性上的质的差别,将表现为它们的状态空间描述在类型上的不同。本节中,我们来讨论系统按其状态空间描述进行分类的问题,其目的实际是要引入有关系统的一些基本术语以及它们的正确含义。

线性系统和非线性系统 在选定的一组状态变量下,称一个系统为非线性系统,当且仅当其状态空间描述

$$
\left\{ \begin{array}{l} \dot {x} = f (x, u, t) \\ y = g (x, u, t) \end{array} \right. \tag {1.19}
$$

中，向量函数 $f(x,u,t)$ 和 $g(x,u,t)$ 至少包含一个元为变量 $x_{1},\cdots,x_{n}$ 和 $u_{1},\cdots,u_{p}$ 的非线性函数。若向量方程中 $f(x,u,t)$ 和 $g(x,u,t)$ 的所有元都是变量 $x_{1},\cdots,x_{n}$ 和 $u_{1},\cdots,u_{p}$ 的线性函数，则称相应的系统为线性系统，并可将其状态空间描述表示为如下的形式：

$$
\left\{ \begin{array}{l} \dot {\boldsymbol {x}} = A (t) \boldsymbol {x} + B (t) \boldsymbol {u} \\ \boldsymbol {y} = C (t) \boldsymbol {x} + D (t) \boldsymbol {u} \end{array} \right. \tag {1.20}
$$

其中，系数矩阵 $A(t), B(t), C(t)$ 和 $D(t)$ 均为不依赖于状态 $\pmb{x}$ 和输入 $\pmb{u}$ 的时变矩阵。

严格地说，一切实际的系统都是非线性的，线性系统只是实际系统在忽略某些次要的非线性因素后的一类理想化的模型。但是，同时应当指出的是，相当多的实际系统都可按线性系统看待和处理，其分析结果将可在足够的精度下接近于系统的实际运动状态。特别是，如果只限于考虑系统在某个 $x_0(t)$ 的一个邻域内的运动时，那么任一非线性系统都可在这一邻域内用一个线性系统来代替，其状态空间描述也可容易地由非线性描述(1.19)来导出。设相应于 $x_0(t)$ 的状态空间描述为

$$
\left\{ \begin{array}{l} \dot {x} _ {0} = f (x _ {0}, u _ {0}, t) \\ y _ {0} = g (x _ {0}, u _ {0}, t) \end{array} \right. \tag {1.21}
$$

并将(1.19)中的向量函数 $f(x,u,t)$ 和 $g(x,u,t)$ 在 $(x_{0},u_{0})$ 的邻域内进行台劳展开，有

$$
\begin{array}{l} f (x, u, t) = f \left(x _ {0}, u _ {0}, t\right) + \left(\frac {\partial f}{\partial x ^ {T}}\right) _ {0} \delta x + \left(\frac {\partial f}{\partial u ^ {T}}\right) _ {0} \delta u \\ + \alpha (\delta x, \delta u, t) \\ \end{array}
\boldsymbol {g} (\boldsymbol {x}, \boldsymbol {u}, t) = \boldsymbol {g} \left(\boldsymbol {x} _ {0}, \boldsymbol {u} _ {0}, t\right) + \left(\frac {\partial \boldsymbol {g}}{\partial \boldsymbol {x} ^ {T}}\right) _ {0} \delta \boldsymbol {x} + \left(\frac {\partial \boldsymbol {g}}{\partial \boldsymbol {u} ^ {T}}\right) _ {0} \delta \boldsymbol {u}+ \beta (\delta x, \delta a, t)
$$

其中， $\delta x = x - x_0$ ， $\delta u = u - u_0$ ， $\alpha (\delta x, \delta u, t)$ 和 $\beta (\delta x, \delta u, t)$ 为台劳展开中的高次项。再据向量对向量的求导规则，表
