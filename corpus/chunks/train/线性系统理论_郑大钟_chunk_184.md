这意味着， $d_{i}$ 是使 $c_{i}A^{k}B \neq 0$ 的正整数 k 的最小值，而当 $g_{i}(s) \equiv 0$ 时，也即 $c_{i}A^{k}B = 0$ $(i = 0, 1, \cdots, n - 1)$ 时，则规定为 $d_{i} \triangleq n - 1$ 。从而，(5.80) 得证。再根据 $E_{i}$ 的定义式 (5.79) 和 $g_{i}(s)$ 的关系式 (5.84)，并注意到 (5.87) 和 (5.86)，即得

$$E _ {i} = \lim _ {s \rightarrow \infty} s ^ {d _ {i} + 1} \mathbf {g} _ {i} (s) = \mathbf {c} _ {i} R _ {n - d _ {i} - 1} B = \mathbf {c} _ {i} A ^ {d _ {i}} B \tag {5.91}$$

于是，(5.81) 得证。

（2）对于任意的矩阵对 $\{L, K\}$ ，其中 $\det L \neq 0$ ，状态反馈闭环系统的传递函数矩阵 $G_{KL}(s)$ 的第 $i$ 个行传递函数向量可表为：

$$\boldsymbol {g} _ {K L i} (s) = \frac {1}{\bar {\alpha} (s)} \left[ \boldsymbol {c} _ {i} B L s ^ {n - 1} + \boldsymbol {c} _ {i} \bar {R} _ {n - 2} B L s ^ {n - 2} + \dots + \boldsymbol {c} _ {i} \bar {R} _ {1} B L s + \boldsymbol {c} _ {i} \bar {R} _ {0} B L \right] \tag {5.92}$$

其中

$$\bar {a} (s) = \det (s I - A + B K) = s ^ {n} + \bar {a} _ {n - 1} s ^ {n - 1} + \dots + \bar {a} _ {1} s + \bar {a} _ {0} \tag {5.93}$$

和

$$
\bar {R} _ {n - 2} = (A - B K) + \bar {\alpha} _ {n - 1} I
\begin{array}{l} \bar {R} _ {n - 3} = (A - B K) ^ {2} + \bar {\alpha} _ {n - 1} (A - B K) + \bar {\alpha} _ {n - 2} I \\ \dots \dots \end{array} \tag {5.94}
\bar {R} _ {0} = (A - B K) ^ {n - 1} + \bar {\alpha} _ {n - 1} (A - B K) ^ {n - 2} + \dots + \bar {\alpha} _ {1} I
$$

而 $G_{KL}(s)$ 的两个特征量 $\bar{d}_i$ 和 $\bar{E}_i$ 则可表为

$$
\bar {d} _ {i} = \left\{ \begin{array}{l l} \bar {\mu}, & \text {当} c _ {i} (A - B K) ^ {k} B L = 0, k = 0, 1, \dots , \bar {\mu} - 1, \\ & \text {而} c _ {i} (A - B K) ^ {\mu} B L \neq 0 \\ n - 1, & \text {当} c _ {i} (A - B K) ^ {k} B L = 0, k = 0, 1, \dots , n - 1 \end{array} \right.
i = 1, 2, \dots , p \tag {5.95}
$$

和

$$\bar {E} _ {i} = \mathbf {c} _ {i} (A - B K) ^ {d _ {i}} B L, \quad i = 1, 2, \dots , p \tag {5.96}$$

（3）对于任意的 $\{L, K\}$ ， $\det L \neq 0$ ，开环系统和闭环系统的传递函数矩阵的特征量之间存在如下的关系式：

$$\vec {d} _ {i} = d _ {i} \text {和} \vec {E} _ {i} = E _ {i} L, i = 1, 2, \dots , p \tag {5.97}$$

现来证明这个论断。对任一 $i$ ，由条件

$$\mathbf {c} _ {i} B = 0, \mathbf {c} _ {i} A B = 0, \dots , \mathbf {c} _ {i} A ^ {d _ {i} - 1} B = 0 \tag {5.98}$$

可以导出:
