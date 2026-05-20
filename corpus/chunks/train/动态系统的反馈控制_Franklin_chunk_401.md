# 例 7.2 巡航控制阶跃响应

(1) 以状态变量形式重写例 2.1 中的运动方程，其中输出是汽车的位置 x。  
（2）对于从 t=0 输入 u=0 跳变到常值输入 u=500N 之后的这种情形，利用 Matlab 计算汽车速度的响应。假设汽车质量 m 为 1000kg 且 $b=50N\cdot s/m$ 。

解答。

（1）运动方程：首先，我们需要表示出描述被控对象式(2.3)的微分方程，将其作为一族同时成立的一阶方程。为此，我们定义汽车的位置和速度作为状态变量 $x$ 和 $v$ ，使得 $x = [x - v]^{\mathrm{T}}$ 。单个二阶式(2.3)可以重新写成一组两个一阶方程：

$$\dot {x} = v\dot {v} = - \frac {b}{m} v + \frac {1}{m} u$$

接下来，使用式(7.3)的标准形式 $\dot{x}=Ax+Bu$ 来表示上述方程：

$$
\left[ \begin{array}{l} \dot {x} \\ \dot {v} \end{array} \right] = \left[ \begin{array}{c c} 0 & 1 \\ 0 & - b / m \end{array} \right] \left[ \begin{array}{l} x \\ v \end{array} \right] + \left[ \begin{array}{l} 0 \\ 1 / m \end{array} \right] u \tag {7.5}
$$

系统的输出是汽车的位置，以矩阵形式表达为

$$
y = \left[ \begin{array}{l l} 1 & 0 \end{array} \right] \left[ \begin{array}{c} x \\ v \end{array} \right]
$$

或

$$y = C x$$

所以本例中，状态变量形式矩阵定义为

$$
\mathbf {A} = \left[ \begin{array}{c c} 0 & 1 \\ 0 & - b / m \end{array} \right], \quad \mathbf {B} = \left[ \begin{array}{c} 0 \\ 1 / m \end{array} \right], \quad \mathbf {C} = \left[ \begin{array}{l l} 1 & 0 \end{array} \right], \quad D = 0
$$

（2）时域响应：现在除了输出以外，运动方程在(1)问中已经给出。因此，输出矩阵为

$$
\mathbf {C} = \left[ \begin{array}{c c} 0 & 1 \end{array} \right]
$$

所需系数为 b/m=0.05 和 1/m=0.001。定义系统的数值矩阵分别为

$$
\mathbf {A} = \left[ \begin{array}{c c} 0 & 1 \\ 0 & - 0. 0 5 \end{array} \right], \quad \mathbf {B} = \left[ \begin{array}{c c} 0 \\ 0. 0 0 1 \end{array} \right], \quad \mathbf {C} = \left[ \begin{array}{c c} 0 & 1 \end{array} \right], \quad D = 0
$$

在 Matlab 中，阶跃函数可以计算线性系统对于单位阶跃信号输入下的时域响应。因为系统是线性的，所以，这种情形下的输出可以由输入阶跃信号的幅值进行放大，从而得到任意幅值的阶跃响应。同样地，矩阵 B 可乘以输入阶跃信号的值。

Matlab 语句如下。

```matlab
A = [0 1;0 -0.05];
B = [0;0.001];
C = [0 1];
D = 0;
sys = ss(A, 500*B,C,D); % step gives unit step response, so 500*B gives u=500 N.
step(sys); % plots the step response 
```

对于一个幅值为 500N 的输入阶跃信号，计算并画出时域响应曲线。阶跃响应如图 7.2 所示。
