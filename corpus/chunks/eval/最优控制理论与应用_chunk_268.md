# 12.5 习题

1. 系统模型为

$$
\dot {\boldsymbol {x}} = \left[ \begin{array}{c c c} - 0. 2 & 0. 5 & 0 \\ 0 & - 0. 5 & 1. 6 \\ 0 & 0 & - 1 4. 3 \end{array} \right] \boldsymbol {x} + \left[ \begin{array}{l} 0 \\ 0 \\ 3 0 \end{array} \right] \boldsymbol {u}
$$

取 $Q = \text{diag}([100])$ , R = 1; 计算二次型调节器的状态反馈矩阵 K 和绘制最优控制的轨迹曲线。

2. 系统的模型为

$$
\dot {\boldsymbol {x}} = \left[ \begin{array}{c c c c c} - 0. 2 & 0. 5 & 0 & 0 & 0 \\ 0 & - 0. 5 & 1. 6 & 0 & 0 \\ 0 & 0 & - 1 4. 3 & 8 5. 8 & 0 \\ 0 & 0 & 0 & - 3 3. 3 & 1 0 0 \\ 0 & 0 & 0 & 0 & - 1 0 \end{array} \right] \boldsymbol {x} + \left[ \begin{array}{l} 0 \\ 0 \\ 0 \\ 0 \\ 3 0 \end{array} \right] \boldsymbol {u}

y = \left[ \begin{array}{l l l l l} 1 & 0 & 0 & 0 & 0 \end{array} \right] x
$$

取 $Q = \text{eye}(5)$ ; R = 1; 设计最优二次型调节器, 确定状态反馈矩阵 K 和黎卡提方程的解, 绘制闭环的阶跃响应曲线和状态响应曲线。

3. 系统的模型为

$$
\dot {\boldsymbol {x}} = \left[ \begin{array}{c c c} - 0. 4 & 0 & - 0. 0 1 \\ 1 & 0 & 0 \\ - 1. 4 & 9. 8 & - 0. 0 2 \end{array} \right] \boldsymbol {x} + \left[ \begin{array}{c} 6. 3 \\ 0 \\ 9. 8 \end{array} \right] \boldsymbol {u}

\boldsymbol {y} = \left[ \begin{array}{l l l} 0 & 0 & 1 \end{array} \right] \boldsymbol {x}
$$

比较加权矩阵 Q、R 在不同数值下对系统闭环特性的影响。

4. 系统的模型为

$$
\dot {\boldsymbol {x}} = \left[ \begin{array}{c c c c c} - 0. 2 & 0. 5 & 0 & 0 & 0 \\ 0 & - 0. 5 & 1. 6 & 0 & 0 \\ 0 & 0 & - 1 4. 3 & 8 5. 8 & 0 \\ 0 & 0 & 0 & - 3 3. 3 & 1 0 0 \\ 0 & 0 & 0 & 0 & 1 0 \end{array} \right] \boldsymbol {x} + \left[ \begin{array}{l} 0 \\ 0 \\ 0 \\ 0 \\ 3 0 \end{array} \right] \boldsymbol {u}
$$

5. 取 $Q = \text{diag}([ \rho, 0, 0, 0])$ ; R = 1; 求解不同的 $\rho$ 值下的黎卡提代数方程, 设计出状态反馈控制器并比较不同的状态反馈控制器下系统的闭环响应的动态性能。
