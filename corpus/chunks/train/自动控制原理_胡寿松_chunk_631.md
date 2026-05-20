# (3) 定常离散动态方程的解

求解离散动态方程的方法有递推法和 z 变换法, 这里只介绍常用的递推法, 令式(9-70)中的 k = 0, 1, …, k - 1, 可得到 T, 2T, …, kT 时刻的状态, 即

$$
\begin{array}{l} k = 0; \quad x (1) = \Phi (T) x (0) + G (T) u (0) \\ k = 1: \quad x (2) = \Phi (T) x (1) + G (T) u (1) \\ = \boldsymbol {\Phi} ^ {2} (T) \boldsymbol {x} (0) + \boldsymbol {\Phi} (T) \boldsymbol {G} (T) \boldsymbol {u} (0) + \boldsymbol {G} (T) \boldsymbol {u} (1) \\ k = 2: \quad x (3) = \Phi (T) x (2) + G (T) u (2) \\ = \boldsymbol {\Phi} ^ {3} (T) \boldsymbol {x} (0) + \boldsymbol {\Phi} ^ {2} (T) \boldsymbol {G} (T) \boldsymbol {u} (0) + \boldsymbol {\Phi} (T) \boldsymbol {G} (T) \boldsymbol {u} (1) + \boldsymbol {G} (T) \boldsymbol {u} (2) \\ \vdots \quad k = k - 1: \quad x (k) = \Phi (T) x (k - 1) + G (T) u (k - 1) \\ = \boldsymbol {\Phi} ^ {k} (T) \boldsymbol {x} (0) + \boldsymbol {\Phi} ^ {k - 1} (T) \boldsymbol {G} (T) \boldsymbol {u} (0) + \boldsymbol {\Phi} ^ {k - 2} (T) \boldsymbol {G} (T) \boldsymbol {u} (1) \\ + \dots + \boldsymbol {\Phi} (T) \mathbf {G} (T) \mathbf {u} (k - 2) + \mathbf {G} (T) \mathbf {u} (k - 1) \\ = \boldsymbol {\Phi} ^ {k} (T) \boldsymbol {x} (0) + \sum_ {i = 0} ^ {k - 1} \boldsymbol {\Phi} ^ {k - 1 - i} (T) \boldsymbol {G} (T) \boldsymbol {u} (i) \tag {9-72} \\ \end{array}
$$

式(9-72)为离散化状态方程的解,又称离散化状态转移方程。当 $u(i)=0(i=0,1,\cdots,k-1)$ 时,有

$$
\begin{array}{l} \boldsymbol {x} (k) = \boldsymbol {\Phi} ^ {k} (T) \boldsymbol {x} (0) \\ = \Phi (k T) x (0) = \Phi (k) x (0) \\ \end{array}
$$

$\Phi(k)$ 称为离散化系统动态转移矩阵。

输出方程为

$$\mathbf {y} (k) = \mathbf {C x} (k) + \mathbf {D u} (k)= C \Phi^ {k} (T) x (0) + C \sum_ {i = 0} ^ {k - 1} \Phi^ {k - 1 - i} (T) G (T) u (i) + D u (k) \tag {9-73}$$

对于离散动态方程式(9-68)，采用递推法可得其解为

$$\pmb {x} (k) = \pmb {G} ^ {k} \pmb {x} (0) + \sum_ {i = 0} ^ {k - 1} \pmb {G} ^ {k - 1 - i} \pmb {H u} (i) \tag {9-74}\mathbf {y} (k) = \mathbf {C G} ^ {k} \mathbf {x} (0) + \mathbf {C} \sum_ {i = 0} ^ {k - 1} \mathbf {G} ^ {k - 1 - i} \mathbf {H u} (i) + \mathbf {D u} (k) \tag {9-75}$$

式中， $G^{k}$ 表示 k 个 G 自乘。

例 9-8 已知连续时间系统的状态方程为

$$
\dot {\boldsymbol {x}} = \left[ \begin{array}{c c} 0 & 1 \\ - 2 & - 3 \end{array} \right] \boldsymbol {x} + \left[ \begin{array}{l} 0 \\ 1 \end{array} \right] \boldsymbol {u}
$$

设 T = 1，试求相应的离散时间状态方程。

解 由例9-4已知该连续系统的状态转移矩阵为

$$
\boldsymbol {\Phi} (t) = \left[ \begin{array}{c c} 2 \mathrm{e} ^ {- t} - \mathrm{e} ^ {- 2 t} & \mathrm{e} ^ {- t} - \mathrm{e} ^ {- 2 t} \\ - 2 \mathrm{e} ^ {- t} + 2 \mathrm{e} ^ {- 2 t} & - \mathrm{e} ^ {- t} + 2 \mathrm{e} ^ {- 2 t} \end{array} \right]

\boldsymbol {\Phi} (T) = \boldsymbol {\Phi} (t) \left| _ {t = T = 1} \right. = \left[ \begin{array}{c c} 0. 6 0 0 4 & 0. 2 3 2 5 \\ - 0. 4 6 5 1 & - 0. 0 9 7 2 \end{array} \right]

\boldsymbol {G} (t) = \int_ {0} ^ {T} \boldsymbol {\Phi} (\tau) \boldsymbol {B} d \tau = \int_ {0} ^ {T} \left[ \begin{array}{l} e ^ {- \tau} - e ^ {- 2 \tau} \\ - e ^ {- \tau} + 2 e ^ {- 2 \tau} \end{array} \right] d \tau = \left[ \begin{array}{c} \frac {1}{2} - e ^ {- T} + \frac {1}{2} e ^ {- 2 T} \\ e ^ {- T} - e ^ {- 2 T} \end{array} \right]

\mathbf {G} (T) \big | _ {T = 1} = \left[ \begin{array}{c} 0. 1 9 9 8 \\ 0. 2 3 2 5 \end{array} \right]
$$
