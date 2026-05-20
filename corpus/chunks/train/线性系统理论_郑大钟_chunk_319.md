# 习题

8.1 确定下列各传递函数矩阵 $G(s)$ 的 MFD 的极点和零点:

$$
\text {(i)} \left[ \begin{array}{c c} s - 1 & 0 \\ 0 & s ^ {2} - 1 \end{array} \right] ^ {- 1} \left[ \begin{array}{c c c} 1 & s - 1 & s - 1 \\ 0 & s + 1 & s + 1 \end{array} \right]

\left[ \begin{array}{c c} s ^ {2} - 1 & 0 \\ 0 & s + 1 \end{array} \right] ^ {- 1} \left[ \begin{array}{c c} s ^ {2} & s - 1 \\ 2 & 1 \end{array} \right] \tag {ii}

\left[ \begin{array}{c c} 0 & s - 2 \\ s + 3 & 0 \\ s - 2 & s + 1 \end{array} \right] \left[ \begin{array}{c c} s ^ {3} & 0 \\ - s ^ {2} + s + 1 & - s + 1 \end{array} \right] ^ {- 1} \tag {iii}
$$

8.2 给定传递函数矩阵 $G(s)$ 如下:

$$
G (s) = \left[ \begin{array}{c c} \frac {2 s + 1}{s ^ {2} - 1} & \frac {s}{s ^ {2} + 5 s + 4} \\ \frac {1}{s + 3} & \frac {2 s + 5}{s ^ {2} + 7 s + 1 2} \end{array} \right] \tag {i}
G (s) = \left[ \frac {s + 2}{(s + 1) (s + 3)} \quad \frac {s + 1}{(s + 3) ^ {2} (s + 2)} \right] \tag {ii}
$$

试定出它们的极点和零点。

8.3 确定下列各多变量系统的极点和零点:

$$
\begin{array}{l} \dot {\boldsymbol {x}} = \left[ \begin{array}{r r r} 0 & 1 & 0 \\ 0 & 0 & 1 \\ - 2 & - 4 & - 3 \end{array} \right] \boldsymbol {x} + \left[ \begin{array}{r r} 1 & 0 \\ 0 & 1 \\ - 1 & 1 \end{array} \right] \boldsymbol {u} \tag {i} \\ \mathbf {y} = \left[ \begin{array}{l l l} 1 & 1 & 0 \\ 0 & 1 & 0 \end{array} \right] \mathbf {x} \\ \end{array}

\begin{array}{l} \dot {\boldsymbol {x}} = \left[ \begin{array}{l l l} 1 & 0 & 1 \\ 0 & 1 & 0 \\ 1 & 1 & 0 \end{array} \right] \boldsymbol {x} + \left[ \begin{array}{l l} 1 & 0 \\ 0 & 1 \\ 1 & 0 \end{array} \right] \boldsymbol {u} \tag {ii} \\ y = [ 1 4 1 ] x \\ \end{array}
$$

8.4 对上题所示的动态系统, 分别确定一个初始状态 $x_0$ 和输入函数 $\pmb{u}(t)$ , 使系统的输出 $\pmb{y}(t) \equiv 0$ 。

8.5 给定动态系统

$$
\begin{array}{l} \dot {\boldsymbol {x}} = \left[ \begin{array}{c c} 0 & 1 \\ - 2 & - 3 \end{array} \right] \boldsymbol {x} + \left[ \begin{array}{l} 0 \\ 1 \end{array} \right] \boldsymbol {u} \\ y = [ 2 1 ] x \\ \end{array}
$$

(i) 确定两个初始状态 $x_0$ ，使系统输出的零输入响应对所有 $t \geqslant 0$ 为 $y(t) = 5e^{-t}$ 。  
(ii) 确定两个初始状态 $x_0$ ，使系统相应于此初态和 $u(t) = e^{3t}$ 的输出响应对所有 $t \geqslant 0$ 为 $y(t) = \frac{1}{4} e^{3t}$ 。

8.6 给定系统的能控且能观测的状态空间描述为:

$$
\begin{array}{l} \dot {\boldsymbol {x}} = \boldsymbol {A} \boldsymbol {x} + \boldsymbol {B} \boldsymbol {u} \\ \mathbf {y} = C \mathbf {x} + E \mathbf {u} \\ \end{array}
$$

其传递函数矩阵表为 $G(s)$ ，试证明： $\lambda$ 为 $G(s)$ 的极点的充分必要条件是，存在一个初始状态 $\pmb{x}_0$ ，使系统输出的零输入响应为：

$$\mathbf {y} (t) = \beta e ^ {\lambda t}$$

其中 $\beta$ 为非零向量。
