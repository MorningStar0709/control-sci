\boldsymbol {y} = \left[ \begin{array}{c c c} 1 & 2 & 0 \\ 0 & 1 & 1 \end{array} \right] \boldsymbol {x}
$$

(i) 系统是否能解耦；

(ii) 若能解耦, 定出实现积分型解耦的输入变换阵和状态反馈阵 $\{L, K\}$ .

5.15 对于上题给出的受控系统,试问:

(i) 能否实现静态解耦；

(ii) 若能, 定出输入变换阵和状态反馈阵 $\{L, K\}$ 。

5.16 给定受控系统

$$
\dot {\boldsymbol {x}} = \left[ \begin{array}{l l} 0 & 1 \\ 0 & 0 \end{array} \right] \boldsymbol {x} + \left[ \begin{array}{l} 0 \\ 1 \end{array} \right] u, \quad \boldsymbol {x} (0) = \left[ \begin{array}{l} 1 \\ 2 \end{array} \right]
$$

和性能指标

$$J = \int_ {0} ^ {\infty} (2 x _ {1} ^ {2} + 2 x _ {1} x _ {2} + x _ {1} ^ {2} + u ^ {2}) d t$$

试确定最优状态反馈增益阵 $K^{*}$ 和最优性能值 $J^{*}$ 。

5.17 给定受控系统

$$
\dot {\boldsymbol {x}} = \left[ \begin{array}{l l} 1 & 0 \\ 0 & 2 \end{array} \right] \boldsymbol {x} + \left[ \begin{array}{l} 1 \\ 1 \end{array} \right] u, \quad \boldsymbol {x} (0) = \left[ \begin{array}{l} 2 \\ 1 \end{array} \right]

y = \left[ \begin{array}{l l} 1 & 2 \end{array} \right] x
$$

和性能指标

$$J = \int_ {0} ^ {\infty} (y ^ {2} + 2 u ^ {2}) d t$$

试确定最优状态反馈增益阵 $K^{*}$ 和最优性能值 $J^{*}$ 。

5.18 给定线性定常系统为:

$$
\dot {\boldsymbol {x}} = \left[ \begin{array}{l l} 0 & 1 \\ 0 & 0 \end{array} \right] \boldsymbol {x} + \left[ \begin{array}{l} 0 \\ 1 \end{array} \right] \boldsymbol {u}

y = \left[ \begin{array}{l l} 1 & 0 \end{array} \right] x
$$

试用两种不同的方法确定其全维观测器，且规定其特征值为 $\lambda_{1} = -2$ 和 $\lambda_{2} = -4$ 。

5.19 给定线性定常系统为:

$$
\dot {\boldsymbol {x}} = \left[ \begin{array}{l l} 1 & 3 \\ 2 & 1 \end{array} \right] \boldsymbol {x} + \left[ \begin{array}{l} 1 \\ 2 \end{array} \right] u
y = [ 0 \quad 1 ] x
$$

试用两种不同的方法确定其降维观测器，且规定其特征值为 $\lambda_{1} = -3$ 。

5.20 给定线性定常系统为:

$$
\dot {\boldsymbol {x}} = \left[ \begin{array}{c c c} - 1 & - 2 & - 2 \\ 0 & - 1 & 1 \\ 1 & 0 & - 1 \end{array} \right] \boldsymbol {x} + \left[ \begin{array}{l} 2 \\ 0 \\ 1 \end{array} \right] u
y = [ 1 \quad 1 \quad 0 ] x
$$

(i) 确定一个具有特征值 -3, -3, -4 的三维状态观测器:

(ii) 确定一个具有特征值 -3 和 -4 的二维状态观测器。

5.21 给定单输入一单输出受控系统的传递函数为:

$$g _ {0} (s) = \frac {1}{s (s + 1) (s + 2)}$$

(i) 确定一个状态反馈增益阵 $K$ ，使闭环系统的极点为 $\lambda_1^* = -3$ 和 $\lambda_{i,j}^* = -\frac{1}{2} \pm j \frac{\sqrt{3}}{2}$ ;

(ii) 确定一个降维观测器, 使其特征值均为 -5;

(iii) 画出整个系统的结构图；

(iv) 确定整个闭环系统的传递函数 $g(s)$ 。

5.22 根据上题的计算结果，确定满足极点配置要求的串联补偿器和并联补偿器的传递函数，并且画出整个输出反馈系统的结构图。

5.23 给定受控系统为
