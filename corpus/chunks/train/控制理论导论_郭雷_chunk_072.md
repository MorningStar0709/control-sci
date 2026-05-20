# 1.5 定常线性系统的实现

已知由定常线性系统的状态空间描述可以求出它的传递函数矩阵。反过来，如果给定一个系统的传递函数矩阵，是否能够找到它的一个状态空间描述呢？这就是传递函数矩阵的实现问题。这个问题的数学描述是，已知有理分式矩阵 $W(s)$ ，求满足

$$\boldsymbol {W} (s) = \boldsymbol {C} (s \boldsymbol {I} _ {n} - \boldsymbol {A}) ^ {- 1} \boldsymbol {B} + \boldsymbol {D} \tag {1.5.1}$$

的常值矩阵 A, B, C, D. 如果这个问题有解，则由矩阵 A, B, C, D 决定的定常线性系统

$$
\left\{ \begin{array}{l} \dot {x} (t) = A x (t) + B u (t), \\ y (t) = C x (t) + D u (t) \end{array} \right. \tag {1.5.2}
$$

叫做 $W(s)$ 的一个状态空间实现，简称实现。矩阵 $\pmb{A}$ 的阶数叫做 $W(s)$ 的实现的阶数。为简单起见，总是用 $(A, B, C, D)$ 或 $(A, B, C)$ 表示 $W(s)$ 的实现。实现问题是线性系统理论中的一个很有意义的问题。

首先要问，给定一个有理分式矩阵，怎样判断它能否实现？为此，有如下定理：

定理 1.5.1 $m \times r$ 有理分式矩阵 $W(s)$ 能实现的充要条件是它的每个元的分子次数不高于分母次数.

证明 必要性是显然的，下面证明充分性。首先假设 $W(s)$ 是一个标量传递函数的情况，这时，总可以把它写成

$$\boldsymbol {W} (s) = \frac {\beta_ {n - 1} s ^ {n - 1} + \beta_ {n - 2} s ^ {n - 2} + \cdots + \beta_ {1} s + \beta_ {0}}{s ^ {n} + \alpha_ {n - 1} s ^ {n - 1} + \cdots + \alpha_ {1} s + \alpha_ {0}} + d. \tag {1.5.3}$$

很容易说明，如果取

$$
\boldsymbol {A} = \left[ \begin{array}{c c c c c} 0 & 1 & 0 & \dots & 0 \\ 0 & 0 & 1 & \ddots & \vdots \\ \vdots & \vdots & \ddots & \ddots & 0 \\ 0 & 0 & \dots & 0 & 1 \\ - \alpha_ {0} & - \alpha_ {1} & \dots & - \alpha_ {n - 2} & - \alpha_ {n - 1} \end{array} \right],
\boldsymbol {b} = [ 0, \dots , 0, 1 ] ^ {\mathrm{T}}, \quad \boldsymbol {c} = [ \beta_ {n - 1}, \beta_ {n - 2}, \dots , \beta_ {0} ],
$$

那么由 $(A, b, c, d)$ 组成的系统就是 $W(s)$ 的一个实现.

当 $W(s)$ 为 $m \times r$ 真有理分式阵时，它的每个元都有这样的实现，从而 mr 个这样的实现就可决定 $W(s)$ 的一个实现.

推论 1.5.1 $m \times r$ 有理分式矩阵 $W(s)$ 存在使得 D = 0 的实现的充要条件是它为真有理分式矩阵，即它的每一个元的分母的次数比分子的次数高.

不失一般性，下面总是研究真有理分式阵的实现问题.

显然，给定一个传递函数矩阵 $W(s)$ 后，它的实现并不唯一。通常把 $W(s)$ 的所有实现中阶数最低的一个叫做它的最小实现。将要说明， $W(s)$ 的最小实现在代数等价意义下是唯一的。

已知单输入单输出定常线性系统

$$
\left\{ \begin{array}{l} \dot {x} (t) = A x (t) + b u (t), \\ y (t) = c x (t), \end{array} \right. \tag {1.5.4}
$$

其中诸符号的意义同前．它的传递函数为

$$\boldsymbol {W} (s) = c \left(s \boldsymbol {I} _ {n} - \boldsymbol {A}\right) ^ {- 1} b. \tag {1.5.5}$$

系统 (1.5.4) 的特征多项式为 $\Delta(s) = \det(sI_n - A)$ . 注意到

$$(s \boldsymbol {I} _ {n} - \boldsymbol {A}) ^ {- 1} = \frac {1}{\Delta (s)} \operatorname{Adj} (s \boldsymbol {I} _ {n} - \boldsymbol {A}), \tag {1.5.6}$$

这里 $\operatorname{Adj}(\cdot)$ 表示矩阵的伴随，它是由 $sI_{n} - A$ 的代数余子式组成的矩阵。若令

$$p (s) = c \mathrm{Adj} (s I _ {n} - A) b,$$

那么有

$$\boldsymbol {W} (s) = \frac {p (s)}{\Delta (s)}. \tag {1.5.7}$$

定理1.5.2 系统(1.5.4)完全能控和完全能观测的充要条件是 $W(s)$ 没有零极相消，即 $\Delta(s)$ 与 $p(s)$ 互质.
