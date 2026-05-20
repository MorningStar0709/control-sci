$$
\begin{array}{l} \mathbf {a}) \quad \boldsymbol {Q} = \left[ \begin{array}{l l l} 1 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{array} \right], \boldsymbol {R} = 2 0 0; \\ \text {b)} \boldsymbol {Q} = \left[ \begin{array}{c c c} 1 0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{array} \right], \boldsymbol {R} = 2; \\ \text {c)} \boldsymbol {Q} = \left[ \begin{array}{l l l} 1 & 0 & 0 \\ 0 & 1 0 0 & 0 \\ 0 & 0 & 0 \end{array} \right], \boldsymbol {R} = 2. \\ \end{array}
$$

系统在相同的初始条件下,控制变量和状态变量的变化曲线。

(5) 随着 Q 和 R 变化画出闭环极点的根轨迹。

b. 已知系统状态方程为

$$
\left[ \begin{array}{l} \dot {x} _ {1} (t) \\ \dot {x} _ {2} (t) \\ \dot {x} _ {3} (t) \\ \dot {x} _ {4} (t) \end{array} \right] = \left[ \begin{array}{c c c c} - 1 0 & 0 & 0 & 0 \\ 0 & - 1 0 & 0 & 0 \\ 6 & - 3 & - 5 & 0 \\ 0 & 0. 5 & 0 & - 5 \end{array} \right] \left[ \begin{array}{l} x _ {1} (t) \\ x _ {2} (t) \\ x _ {3} (t) \\ x _ {4} (t) \end{array} \right] + \left[ \begin{array}{l l} 1 0 & 0 \\ 0 & 1 0 \\ 0 & 0 \\ 0 & 0 \end{array} \right] \left[ \begin{array}{l} u _ {1} (t) \\ u _ {2} (t) \end{array} \right]
$$

设计一控制系统使得目标函数

$$J (x (t), u (t)) = \frac {1}{2} \int_ {0} ^ {\infty} \left\{x _ {3} ^ {2} (t) + x _ {4} ^ {2} (t) + \rho u ^ {\mathrm{T}} (t) u (t) \right\} \mathrm{d} t$$

最小。

(1) 当 $\rho=2$ ，求状态反馈增益阵。  
（2）当系统的初始状态为 $x(0)=[0\quad0\quad50\quad20]^{T}$ 时，进行闭环仿真。画出控制变量和状态变量的变化曲线。  
（3）当 a. $\rho=0.02$ ; b. $\rho=200$ 时, 系统在相同的初始条件下, 控制变量和状态变量的变化曲线。  
(4) 随着 $\rho$ 的变化画出闭环极点的根轨迹。
