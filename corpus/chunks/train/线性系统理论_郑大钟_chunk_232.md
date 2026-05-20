$$
\left[ \begin{array}{l} \dot {\boldsymbol {x}} \\ \dot {\boldsymbol {z}} \end{array} \right] = \left[ \begin{array}{c c} A - B K Q _ {1} C & - B K Q _ {2} \\ G C - H K Q _ {1} C & F - H K Q _ {2} \end{array} \right] \left[ \begin{array}{l} \boldsymbol {x} \\ \boldsymbol {z} \end{array} \right] + \left[ \begin{array}{l} B \\ H \end{array} \right] \boldsymbol {v}

\mathbf {y} = \left[ \begin{array}{l l} C & \mathbf {0} \end{array} \right] \left[ \begin{array}{l} x \\ z \end{array} \right] \tag {5.374}
$$

包含观测器的状态反馈系统的特性 下面,我们从动态方程(5.374)出发,来讨论包含观测器的状态反馈系统的一些特性。

（1）引入观测器的结果，提高了状态反馈系统的维数。表 $\Sigma$ 为包含观测器的状态反馈系统， $\Sigma_0$ 和 $\Sigma_{\omega}$ 分别为受控系统和观测器，则它们的维数之间成立：

$$\dim (\Sigma) = \dim \left(\Sigma_ {0}\right) + \dim \left(\Sigma_ {a b}\right) \tag {5.375}$$

(2) 包含观测器的状态反馈系统的特征值集合具有分离性, 即成立

$\Sigma$ 的特征值集合 = $\{\lambda_{i}(A - BK), i = 1, 2, \cdots n;\}$

$$\lambda_ {j} (F), j = 1, 2, \dots , n - q \} \tag {5.376}$$

我们很容易证明这一点。引入非奇异的变换矩阵

$$
P = \left[ \begin{array}{c c} I _ {n} & 0 \\ - T & I _ {n - q} \end{array} \right], \quad P ^ {- 1} = \left[ \begin{array}{c c} I _ {n} & 0 \\ T & I _ {n - q} \end{array} \right] \tag {5.377}
$$

对（5.374）的系统矩阵作线性非奇异变换，并利用关系式（5.370）和（5.371），可得到

$$
\begin{array}{l} \left[ \begin{array}{c c} I _ {n} & 0 \\ - T & I _ {n - q} \end{array} \right] \left[ \begin{array}{c c} A - B K Q _ {1} C & - B K Q _ {2} \\ G C - H K Q _ {1} C & F - H K Q _ {2} \end{array} \right] \left[ \begin{array}{c c} I _ {n} & 0 \\ T & I _ {n - q} \end{array} \right] \\ = \left[ \begin{array}{c c} A - B K \left(Q _ {1} C + Q _ {2} T\right) & - B K Q _ {2} \\ (G C - T A + F T) + (T B - H) K Q _ {1} C + (T B - H) K Q _ {2} T & F + (T B - H) K Q _ {2} \end{array} \right] \\ - \left[ \begin{array}{c c} A - B K & - B K Q _ {2} \\ 0 & F \end{array} \right] \tag {5.378} \\ \end{array}
$$

再考虑到矩阵的特征值在线性非奇异变换下保持不变,于是由(5.378)即可导出(5.376)。证明完成。

(3) 作为上述论断的一个推论, 可知: 观测器的引入, 不影响由状态反馈阵 $K$ 所配置的系统特征值 $\{\lambda_i(A - BK), i = 1, 2, \cdots, n\}$ ; 状态反馈的引入, 也不影响已设计好的观测器的特征值 $\{\lambda_j(F), j = 1, 2, \cdots, n - q\}$ . 因此, 对于包含观测器的状态反馈系统, 其设计可分离地来进行, 即状态反馈控制律的设计和观测器的设计可以独立地分开进行。通常, 称这个性质为分离性原理。显然, 分离性原理为闭环控制系统的设计提供了很大的方便。

（4）观测器的引入不改变原状态反馈系统的传递函数矩阵。也即：表直接状态反馈系统的传递函数矩阵为：

$$G _ {K} (s) = C (s I - A + B K) ^ {- 1} B \tag {5.379}$$

而包含观测器的状态反馈系统的传递函数矩阵为:

$$G _ {K B} (s) = \bar {C} (s I - \bar {A}) ^ {- 1} \bar {B} \tag {5.380}$$

其中， $\overline{A}, \overline{B}$ 和 $\overline{C}$ 分别表示 (5.374) 中的增广系统矩阵、增广输入矩阵和增广输出矩阵，则必定成立：

$$G _ {K B} (s) = G _ {K} (s) \tag {5.381}$$
