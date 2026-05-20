$$
\operatorname{rank} \mathbf {V} _ {1} = \operatorname{rank} \left[ \begin{array}{l l l l} \mathbf {C} ^ {\mathrm{T}} & \mathbf {G} ^ {\mathrm{T}} \mathbf {C} ^ {\mathrm{T}} & \dots & (\mathbf {G} ^ {\mathrm{T}}) ^ {n - 1} \mathbf {C} ^ {\mathrm{T}} \end{array} \right] = n \tag {9-162}
$$

例9-18 已知线性定常离散系统的动态方程为

$$\boldsymbol {x} (k + 1) = \boldsymbol {G x} (k) + \boldsymbol {h u} (k); \quad \boldsymbol {y} (k) = \boldsymbol {C} _ {i} \boldsymbol {x} (k); \quad i = 1, 2$$

其中

$$
\mathbf {G} = \left[ \begin{array}{c c c} 1 & 0 & - 1 \\ 0 & - 2 & 1 \\ 3 & 0 & 2 \end{array} \right], \quad \mathbf {h} = \left[ \begin{array}{l} 2 \\ - 1 \\ 1 \end{array} \right], \quad \mathbf {c} _ {1} = \left[ \begin{array}{l l l} 0 & 1 & 0 \end{array} \right], \quad \mathbf {C} _ {2} = \left[ \begin{array}{l l l} 0 & 0 & 1 \\ 1 & 0 & 0 \end{array} \right]
$$

试判断系统的可观测性，并讨论可观测性的物理解释。

解 当观测矩阵为 $c_{1}$ 时，

$$
\boldsymbol {c} _ {1} ^ {\mathrm{T}} = \left[ \begin{array}{l} 0 \\ 1 \\ 0 \end{array} \right], \quad \boldsymbol {G} ^ {\mathrm{T}} \boldsymbol {c} _ {1} ^ {\mathrm{T}} = \left[ \begin{array}{l} 0 \\ - 2 \\ 1 \end{array} \right], \quad (\boldsymbol {G} ^ {\mathrm{T}}) ^ {2} \boldsymbol {c} _ {1} ^ {\mathrm{T}} = \left[ \begin{array}{l} 3 \\ 4 \\ 0 \end{array} \right]

\operatorname{rank} \mathbf {V} _ {1} = \operatorname{rank} \left[ \begin{array}{c c c} 0 & 0 & 3 \\ 1 & - 2 & 4 \\ 0 & 1 & 0 \end{array} \right] = 3 = n
$$

故系统可观测。由输出方程 $y(k) = c_1x(k) = x_2(k)$ 可见，在第 $k$ 步便可由输出确定状态变量 $x_2(k)$ 。由于

$$y (k + 1) = x _ {2} (k + 1) = - 2 x _ {2} (k) + x _ {3} (k)$$

故在第 $k + 1$ 步便可确定 $x_{3}(k)$ 。由于

$$y (k + 2) = x _ {2} (k + 2) = - 2 x _ {2} (k + 1) + x _ {3} (k + 1)= - 2 \left[ - 2 x _ {2} (k) + x _ {3} (k) \right] + 3 x _ {1} (k) + 2 x _ {3} (k)= 4 x _ {2} (k) + 3 x _ {1} (k)$$

故在第 $k + 2$ 步便可确定 $x_{1}(k)$ 。

该系统为三阶系统,可观测意味着至多三步便可由输出 $y(k),y(k+1),y(k+2)$ 的测量值来确定三个状态变量。

当观测矩阵为 $C_2$ 时，

$$
\boldsymbol {C} _ {2} ^ {\mathrm{T}} = \left[ \begin{array}{l l} 0 & 1 \\ 0 & 0 \\ 1 & 0 \end{array} \right], \quad \boldsymbol {G} ^ {\mathrm{T}} \boldsymbol {C} _ {2} ^ {\mathrm{T}} = \left[ \begin{array}{c c} 3 & 1 \\ 0 & 0 \\ 2 & - 1 \end{array} \right], \quad (\boldsymbol {G} ^ {\mathrm{T}}) ^ {2} \boldsymbol {C} _ {2} ^ {\mathrm{T}} = \left[ \begin{array}{c c} 9 & - 2 \\ 0 & 0 \\ 1 & - 3 \end{array} \right]

\operatorname{rank} \mathbf {V} _ {1} = \operatorname{rank} \left[ \begin{array}{c c c c c c} 0 & 1 & 3 & 1 & 9 & - 2 \\ 0 & 0 & 0 & 0 & 0 & 0 \\ 1 & 0 & 2 & - 1 & 1 & - 3 \end{array} \right] = 2 \neq n = 3
$$

故系统不可观测。

根据系统动态方程可导出
