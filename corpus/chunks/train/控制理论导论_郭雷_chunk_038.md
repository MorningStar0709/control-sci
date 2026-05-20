但是，由于坐标变换反映了状态变量的不同选择，因此可以想像坐标变换不能保持系统的状态转移矩阵不变。事实上，在坐标变换下，代数等价系统的状态转移矩阵是相似的，其变换矩阵和坐标变换矩阵相同。

必须指出，虽然代数等价系统有相同的传递函数矩阵，但是具有相同传递矩阵的系统未必是代数等价系统；同样，状态转移矩阵相似的系统也未必是代数等价系统.

在控制理论中，一个复合系统通常是由若干个子系统经过串联、并联和反馈联结形成的。这里研究由三种联结方式生成的复合系统的数学模型。

并联复合系统 已知两个线性系统

$$
\left\{ \begin{array}{l l} \dot {x} _ {i} (t) = A _ {i} x _ {i} (t) + B _ {i} u (t), \\ y _ {i} (t) = C _ {i} x _ {i} (t) + D _ {i} u (t), & i = 1, 2; \\ y (t) = y _ {1} (t) + y _ {2} (t), \end{array} \right.
$$

其中 $x_{i}(t)$ 是第 $i$ 个子系统的 $n_i$ 维状态， $u(t)$ 是 $r$ 维控制输入， $y_{i}(t)$ 是第 $i$ 个子系统的 $m$ 维量测输出， $y(t)$ 是复合系统的 $m$ 维量测输出， $A_{i}, B_{i}, C_{i}$ 和 $D_{i}$ 都是具有相应阶数的实常值矩阵。

设并联复合系统的状态变量为 $x(t) = [x_1^{\mathrm{T}}(t), x_2^{\mathrm{T}}(t)]^{\mathrm{T}}$ ，则并联复合系统的状态方程和量测方程为

$$
\left\{ \begin{array}{l} \dot {x} (t) = \left[ \begin{array}{c c} A _ {1} & 0 \\ 0 & A _ {2} \end{array} \right] x (t) + \left[ \begin{array}{c} B _ {1} \\ B _ {2} \end{array} \right] u (t), \\ y (t) = [ C _ {1} \quad C _ {2} ] x (t) + (D _ {1} + D _ {2}) u (t): \end{array} \right.
$$

并联复合系统的传递函数矩阵为

$$\boldsymbol {W} (s) = \boldsymbol {W} _ {1} (s) + \boldsymbol {W} _ {2} (s),$$

其中 $W_{i}(s) = C_{i}(sI_{n_{i}} - A_{i})^{-1}B_{i} + D_{i},\qquad i = 1,2.$

串联复合系统 已知两个线性系统

$$
\left\{ \begin{array}{l} \dot {x} _ {1} (t) = A _ {1} x _ {1} (t) + B _ {1} u (t), \\ y _ {1} (t) = C _ {1} x _ {1} (t) + D _ {1} u (t); \end{array} \right. \tag {1.2.12}

\left\{ \begin{array}{l} \dot {x} _ {2} (t) = A _ {2} x _ {2} (t) + B _ {2} y _ {1} (t), \\ y (t) = C _ {2} x _ {2} (t) + D _ {2} y _ {1} (t), \end{array} \right. \tag {1.2.13}
$$

其中 $x_{i}(t)$ 是第 $i$ 个子系统的 $n_i$ 维状态变量； $u(t)$ 是 $r$ 维控制输入； $y_1(t)$ 是第一个子系统 (1.2.12) 的 $m_1$ 维输出变量，又是第二个子系统 (1.2.13) 的输入； $y(t)$ 是 $m$ 维量测输出； $A_i, B_i, C_i$ 和 $D_i$ ( $i = 1, 2$ ) 是具有相应阶数的实常值矩阵。

若串联复合系统的状态变量为 $x(t) = [x_1^{\mathrm{T}}(t), x_2^{\mathrm{T}}(t)]^{\mathrm{T}}$ ，则串联复合系统的状态方程和量测方程为

$$
\left\{ \begin{array}{l} \dot {x} (t) = \left[ \begin{array}{c c} A _ {1} & 0 \\ B _ {2} C _ {1} & A _ {2} \end{array} \right] x (t) + \left[ \begin{array}{c} B _ {1} \\ B _ {2} D _ {1} \end{array} \right] u (t), \\ y (t) = \left[ \begin{array}{c c} D _ {2} C _ {1} & C _ {2} \end{array} \right] x (t) + D _ {2} D _ {1} u (t); \end{array} \right.
$$

串联复合系统的传递函数矩阵为

$$\boldsymbol {W} (s) = \boldsymbol {W} _ {2} (s) \boldsymbol {W} _ {1} (s),$$

其中 $W_{i}(s) = C_{i}(sI_{n_{i}} - A_{i})^{-1}B_{i} + D_{i}, i = 1,2.$

反馈联结的复合系统 设有线性系统
