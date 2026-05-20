试确定两个不同的状态反馈阵 $K_{1}$ 和 $K_{2}$ ，使闭环极点配置为 $\lambda_{1,2}^{*} = -2 \pm j3$ 和 $\lambda_{3,4}^{*} = -5 \pm j6$ 。

5.9 判断下列各系统能否用状态反馈实现镇定：

(i) $\dot{x}=\begin{bmatrix}1 & 3 \\ 2 & 1\end{bmatrix}x+\begin{bmatrix}0 \\ 1\end{bmatrix}u$

(ii) $\dot{\pmb{x}} = \left[ \begin{array}{cc}4 & 2\\ 0 & -2 \end{array} \right]\pmb {x} + \left[ \begin{array}{c}1\\ 0 \end{array} \right]u$

(iii) $\dot{\pmb{x}} = \begin{bmatrix} 1 & 0 & 0 \\ 0 & -2 & 1 \\ 0 & 0 & -2 \end{bmatrix} \pmb{x} + \begin{bmatrix} 1 & 0 \\ 0 & 1 \\ 0 & 0 \end{bmatrix} \pmb{u}$

5.10 判断下列各系统能否用输出反馈实现镇定：

(i) $\dot{x}=\begin{bmatrix}1 & 3 \\ 2 & 1\end{bmatrix}x+\begin{bmatrix}0 \\ 1\end{bmatrix}u$

$$
\boldsymbol {y} = \left[ \begin{array}{l l} 0 & 2 \\ 1 & 0 \end{array} \right] \boldsymbol {x}
$$

(ii) $\dot{\pmb{x}} = \begin{bmatrix} 4 & 2 \\ 0 & -2 \end{bmatrix} \pmb{x} + \begin{bmatrix} 1 \\ 0 \end{bmatrix} u$

$$
\mathbf {y} = \left[ \begin{array}{l l} 1 & 1 \\ 0 & 2 \end{array} \right] \mathbf {x}
$$

(iii) $\dot{\pmb{x}} = \begin{bmatrix} 4 & 0 & 0 \\ 0 & -1 & 1 \\ 0 & 0 & -1 \end{bmatrix} \pmb{x} + \begin{bmatrix} 0 & 1 \\ 1 & 0 \\ 0 & 0 \end{bmatrix} \pmb{u}$

$$
\boldsymbol {y} = \left[ \begin{array}{l l l} 1 & 0 & 1 \\ 1 & 1 & 0 \\ 2 & 4 & 3 \end{array} \right] \boldsymbol {x}
$$

5.11 设某系统的传递函数为:

$$g _ {0} (s) = \frac {(s + 2) (s + 3)}{(s + 1) (s - 2) (s + 4)}$$

试问是否存在状态反馈阵 K 使闭环传递函数为:

$$g (s) = \frac {(s + 3)}{(s + 2) (s + 4)}$$

如果存在,求出此状态反馈阵 K.

5.12 给定受控系统为:

$$
\dot {\boldsymbol {x}} = \left[ \begin{array}{l l l} 2 & 1 & 0 \\ 0 & 1 & 0 \\ 1 & 0 & 1 \end{array} \right] \boldsymbol {x} + \left[ \begin{array}{l} 0 \\ 1 \\ 0 \end{array} \right] \boldsymbol {u}
$$

试求一个状态反馈阵 K，使得 $(A - bK)$ 相似于

$$
F = \left[ \begin{array}{c c c} - 3 & 0 & 0 \\ 0 & - 2 & 0 \\ 0 & 0 & - 1 \end{array} \right]
$$

5.13 判断下列各系统能否用状态反馈和输入变换进行解耦：

(i) $G_{0}(s) = \left[ \begin{array}{cc}\frac{3}{s^{2} + 2} & \frac{2}{s^{2} + s + 1}\\ \frac{4s + 1}{s^{3} + 2s + 1} & \frac{1}{s} \end{array} \right]$

(ii) $\dot{\pmb{x}} = \begin{bmatrix} 3 & 1 & 0 \\ 0 & 0 & -1 \\ 0 & 1 & -1 \end{bmatrix} \pmb{x} + \begin{bmatrix} 0 & 0 \\ 1 & 0 \\ 0 & 1 \end{bmatrix} \pmb{\alpha}$

$$
\mathbf {y} = \left[ \begin{array}{c c c} 2 & - 1 & 1 \\ 0 & 2 & 1 \end{array} \right] \mathbf {x}
$$

5.14 给定受控系统为:

$$
\dot {\boldsymbol {x}} = \left[ \begin{array}{r r r} - 1 & 0 & 0 \\ 0 & - 2 & - 3 \\ 1 & 0 & 1 \end{array} \right] \boldsymbol {x} + \left[ \begin{array}{r r} 1 & 0 \\ 0 & 1 \\ 0 & - 1 \end{array} \right] \boldsymbol {u}
