$$
\mathbf {A} = \left[ \begin{array}{l l l l} 0 & 1; & - 5 & - 3 \end{array} \right];
\mathbf {B} = [ 0; 1 ];\mathrm{Q} = [ 5 0 0 2 0 0; 2 0 0 1 0 0 ];\mathrm{R} = 1. 6 6 6 7;[ \mathrm{P}, \mathrm{E}, \mathrm{K}, \mathrm{RR} ] = \operatorname{care} (\mathrm{A}, \mathrm{B}, \mathrm{Q}, \mathrm{R}, [ 0. 2; 0. 2 ], \text {eye} (\text {size} (\mathrm{A}))
$$

运行结果：

$$
\mathrm{P} = 6 7. 7 2 3 3 \quad 2 1. 5 6 8 5
\begin{array}{l l} 2 1. 5 6 8 5 & 1 1. 0 9 6 1 \end{array}
\mathrm{E} = - 7. 3 0 5 2- 2. 4 7 2 3\mathrm{K} = 1 3. 0 6 0 8 \quad 6. 7 7 7 5\mathrm{RR} = 1. 2 8 4 7 \mathrm{e} - 0 1 4
$$

最优控制变量与状态变量之间的关系：

$$u ^ {*} (t) = - 1 3. 0 6 0 8 x _ {1} (t) - 6. 7 7 7 5 x _ {2} (t)$$

例12-2 无人飞行器的最优高度控制，飞行器的控制方程如下

$$
\left[ \begin{array}{l} \dot {h} (t) \\ \ddot {h} (t) \\ \dddot {h} (t) \end{array} \right] = \left[ \begin{array}{l l l} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & - \frac {1}{2} \end{array} \right] \left[ \begin{array}{l} h (t) \\ \dot {h} (t) \\ \ddot {h} (t) \end{array} \right] + \left[ \begin{array}{l} 0 \\ 0 \\ \frac {1}{2} \end{array} \right] u (t)
$$

$h(t)$ 是飞行器的高度； $u(t)$ 是油门输入；设计控制律使得如下指标最小

$$
J [ \boldsymbol {x} (t), \boldsymbol {u} (t) ] = \frac {1}{2} \int_ {0} ^ {\infty} \left\{\left[ h (t), \dot {h} (t), \ddot {h} (t) \right] \left[ \begin{array}{l l l} 1 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{array} \right] \left[ \begin{array}{l} h (t) \\ \dot {h} (t) \\ \ddot {h} (t) \end{array} \right] + 2 \boldsymbol {u} ^ {2} (t) \right\} \mathrm{d} t
$$

初始状态 $[h(t),\dot{h}(t),\ddot{h}(t)] = [10,0,0]^{\mathrm{T}}$ 。绘制系统状态与控制输入，对如下给定的 $QR$ 矩阵进行仿真分析.

a) $\pmb{Q} = \begin{bmatrix} 1 & 0 & 0\\ 0 & 0 & 0\\ 0 & 0 & 0 \end{bmatrix},\pmb {R} = 2000$   
b) $\pmb{Q} = \begin{bmatrix} 10 & 0 & 0\\ 0 & 0 & 0\\ 0 & 0 & 0 \end{bmatrix},\pmb {R} = 2$   
c) $\pmb{Q} = \begin{bmatrix} 1 & 0 & 0\\ 0 & 100 & 0\\ 0 & 0 & 0 \end{bmatrix},\pmb {R} = 2$

解 线性二次型最优控制指标如下：

$$J (\boldsymbol {x} (t), \boldsymbol {u} (t)) = \frac {1}{2} \int_ {0} ^ {\infty} [ \boldsymbol {x} ^ {\mathrm{T}} (t) \boldsymbol {Q} \boldsymbol {x} (t) + \boldsymbol {u} ^ {\mathrm{T}} (t) \boldsymbol {R} \boldsymbol {u} (t) ] \mathrm{d} t$$

其中 Q 和 R 分别是对状态变量和控制量的加权矩阵, 线性二次型最优控制器设计如下:

1） $Q = \text{diag}(1, 0, 0)$ ，R = 2 时，由 MATLAB 求得最优状态反馈矩阵为 $k1=\left[0.707\quad1\quad2.077\quad2\quad2.051\quad0\right]$ ，所以 $u(t)=-k1*x(t)$ 。

所画状态响应曲线及控制输入响应曲线如下图 12-2 所示：

2） $Q = \text{diag}(1,0,0)$ ，R = 2000 时，由 MATLAB 求得最优状态反馈矩阵为
