# 9-8 已知矩阵

$$
\boldsymbol {A} = \left[ \begin{array}{c c c c} 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \\ 1 & 0 & 0 & 0 \end{array} \right]
$$

试求 A 的特征方程、特征值、特征向量，并求出变换矩阵将 A 对角化。

9-9 已知矩阵

$$
\mathbf {A} = \left[ \begin{array}{c c} - 1 & 0 \\ 0 & 1 \end{array} \right]
$$

试用幂级数法及拉普拉斯变换法求出矩阵指数(即状态转移矩阵)。

9-10 试求下列状态方程的解：

$$
\dot {\boldsymbol {x}} = \left[ \begin{array}{c c c} - 1 & 0 & 0 \\ 0 & - 2 & 0 \\ 0 & 0 & - 3 \end{array} \right] \boldsymbol {x}
$$

9-11 已知系统状态方程为

$$
\dot {\boldsymbol {x}} = \left[ \begin{array}{l l} 1 & 0 \\ 1 & 1 \end{array} \right] \boldsymbol {x} + \left[ \begin{array}{l} 1 \\ 1 \end{array} \right] \boldsymbol {u}
$$

初始条件为 $x_{1}(0)=1, x_{2}(0)=0$ 。试求系统在单位阶跃输入作用下的响应。

9-12 已知线性系统状态转移矩阵

$$
\Phi (t) = \left[ \begin{array}{l l} 6 \mathrm{e} ^ {- t} - 5 \mathrm{e} ^ {- 2 t} & 4 \mathrm{e} ^ {- t} - 4 \mathrm{e} ^ {- 2 t} \\ - 3 \mathrm{e} ^ {- t} + 3 \mathrm{e} ^ {- 2 t} & - 2 \mathrm{e} ^ {- t} + 3 \mathrm{e} ^ {- 2 t} \end{array} \right]
$$

试求该系统的状态阵 A。

9-13 已知系统动态方程

$$
\begin{array}{l} \dot {\boldsymbol {x}} = \left[ \begin{array}{c c c} 0 & 1 & 0 \\ - 2 & - 3 & 0 \\ - 1 & 1 & 3 \end{array} \right] \boldsymbol {x} + \left[ \begin{array}{l} 0 \\ 1 \\ 2 \end{array} \right] \boldsymbol {u} \\ y = \left[ \begin{array}{c c c} 0 & 0 & 1 \end{array} \right] x \\ \end{array}
$$

试求传递函数 $G(s)$ 。

9-14 试求习题9-5所示系统的传递函数矩阵。

9-15 已知差分方程

$$y (k + 2) + 3 y (k + 1) + 2 y (k) = 2 u (k + 1) + 3 u (k)$$

试列写可控标准型(A为友矩阵)离散动态方程,并求出 $u(k)=1$ 时的系统响应。给定 $y(0)=0$ , $y(1)=1$ 。

9-16 已知连续系统动态方程为

$$
\boldsymbol {x} = \left[ \begin{array}{l l} 0 & 1 \\ 0 & 2 \end{array} \right] \boldsymbol {x} + \left[ \begin{array}{l} 0 \\ 1 \end{array} \right] \boldsymbol {u}, \quad y = [ 1, 0 ] \boldsymbol {x}
$$

设采样周期 T=1s，试求离散化动态方程。

9-17 试判断下列系统的状态可控性：

(1) $\dot{\pmb{x}} = \begin{bmatrix} -2 & 2 & -1\\ 0 & -2 & 0\\ 1 & -4 & 0 \end{bmatrix}\pmb {x} + \begin{bmatrix} 0\\ 0\\ 1 \end{bmatrix}\pmb {u};$

(2) $\dot{\pmb{x}} = \begin{bmatrix} 1 & 1 & 0 \\ 0 & 1 & 0 \\ 0 & 1 & 1 \end{bmatrix} \pmb{x} + \begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix} \pmb{u}$ ;

(3) $\dot{\pmb{x}} = \begin{bmatrix} 1 & 1 & 0 \\ 0 & 1 & 0 \\ 0 & 1 & 1 \end{bmatrix} \pmb{x} + \begin{bmatrix} 0 & 0 \\ 0 & 1 \\ 1 & 0 \end{bmatrix} \begin{bmatrix} u_1 \\ u_2 \end{bmatrix}$ ;

(4) $\dot{\pmb{x}} = \begin{bmatrix} -4 & & 0\\ & -4 & \\ 0 & & 1 \end{bmatrix}\pmb {x} + \begin{bmatrix} 1\\ 2\\ 1 \end{bmatrix} u_{\circ}$

9-18 已知 $ad = bc$ ，试计算 $\begin{bmatrix} a & b \\ c & d \end{bmatrix}^{100} = ?$

9-19 设系统状态方程为
