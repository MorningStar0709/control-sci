显然 $d_{i}$ 必为非负整数，当 $G(s)$ 给定后 $\{d_1, d_2, \dots, d_p\}$ 为唯一确定。 $G(s)$ 的第二个特征量 $E_{i}$ 定义为：

$$E _ {i} = \lim _ {s \rightarrow \infty} s ^ {d _ {i} + 1} g _ {i} (s), \quad i = 1, 2, \dots , p \tag {5.79}$$

它是 $1 \times p$ 的常量行向量。

下面，来指出这两个特征量 $d_{i}$ 和 $E_{i}$ 的一些基本属性：

(1) 如果 $G(s)$ 的相应的状态空间描述为 $\{A, B, C\}$ ，且表 $c_{i}$ 为 C 的第 i 个行向量，则有

$$
d _ {i} = \left\{ \begin{array}{l l} \mu , & \text {当} c _ {i} A ^ {k} B = 0, k = 0, 1, \dots , \mu - 1, \text {而} c _ {i} A ^ {\mu} B \neq 0 \\ n - 1, & \text {当} c _ {i} A ^ {k} B = 0, k = 0, 1, 2, \dots , n - 1 \end{array} \right. \tag {5.80}
$$

和

$$E _ {i} = \mathbf {c} _ {i} A ^ {d _ {i}} B \tag {5.81}$$

我们可很容易证明（5.80）和（5.81）。利用 $G(s) = C(sI - A)^{-1}B$ ，即可导出

$$\boldsymbol {g} _ {i} (s) = \boldsymbol {c} _ {i} (s I - A) ^ {- 1} B \tag {5.82}$$

再由(1.95)知

$$(s I - A) ^ {- 1} = \frac {1}{\alpha (s)} \left(R _ {n - 1} s ^ {n - 1} + \dots + R _ {1} s + R _ {0}\right) \tag {5.83}$$

从而，将（5.83）代入（5.82），可得

$$
\begin{array}{l} \mathbf {g} _ {i} (s) = \frac {1}{\alpha (s)} \left[ \mathbf {c} _ {i} R _ {n - 1} B s ^ {n - 1} + \mathbf {c} _ {i} R _ {n - 2} B s ^ {n - 2} + \dots + \mathbf {c} _ {i} R _ {n - d _ {i}} s ^ {n - d _ {i}} \right. \\ \left. + \mathbf {c} _ {i} R _ {n - d _ {j} - 1} B s ^ {n - d _ {j} - 1} + \dots + \mathbf {c} _ {i} R _ {1} B s + \mathbf {c} _ {i} R _ {0} B \right] \tag {5.84} \\ \end{array}
$$

其中

$$\alpha (s) = \det (s I - A) = s ^ {n} + \alpha_ {n - 1} s ^ {n - 1} + \dots + \alpha_ {1} s + \alpha_ {0} \tag {5.85}$$

和

$$
\begin{array}{l} R _ {n - 1} = I \\ R _ {n - 2} = A + \alpha_ {n - 1} I \\ \end{array}
R _ {n - 3} = A ^ {2} + \alpha_ {n - 1} A + \alpha_ {n - 2} I \tag {5.86}\bullet \quad \bullet \quad \bullet \quad \bullet \quad \bulletR _ {0} = A ^ {n - 1} + \alpha_ {n - 1} A ^ {n - 2} + \dots + \alpha_ {1} I
$$

但根据 $d_{i}$ 的定义式(5.78)可知， $\pmb{g}_i(s)$ 中各元传递函数的分母和分子多项式的次数之差的最小值为 $(d_{i} + 1)$ ，这表明式(5.84)中，与 $s^{n - 1}, s^{n - 2}, \dots, s^{n - d_{i}}$ 相关的各系数矩阵均为零，而与 $s^{n - d_{i} - 1}$ 相关的系数矩阵必不为零。于是，由此得到

$$\boldsymbol {c} _ {i} R _ {n - 1} B = \mathbf {0}, \boldsymbol {c} _ {i} R _ {n - 2} B = \mathbf {0}, \dots , \boldsymbol {c} _ {i} R _ {n - d _ {i}} B = \mathbf {0} \tag {5.87}$$

和

$$\boldsymbol {c} _ {i} R _ {n - d _ {j} - 1} B \neq \mathbf {0} \tag {5.88}$$

进而，利用（5.86），又可将（5.87）和（5.88）改写为：

$$\mathbf {c} _ {i} B = 0, \mathbf {c} _ {i} A B = 0, \dots , \mathbf {c} _ {i} A ^ {d _ {i} - 1} B = 0 \tag {5.89}$$

和

$$\mathbf {c} _ {i} A ^ {d _ {i}} B \neq 0 \tag {5.90}$$
