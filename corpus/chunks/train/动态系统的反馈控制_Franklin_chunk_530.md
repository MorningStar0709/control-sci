对于一个常规 z 变换，我们可以利用部分分式法(见附录 A.1.2 节)将其展开成初等项的和的形式，并通过查表找到相应的时间序列。这些步骤与连续系统中的完全相同。然而，与连续系统一样，大多数设计者不用z反变换而是采用离散方程的数值计算来获得系统的时域序列。

如果无法直接查表，我们也可以通过长除法得到 z 反变换的表达式。给出 z 变换如下：

$$Y (z) = \frac {N (z)}{D _ {\mathrm{d}} (z)} \tag {8.5}$$

通过长除法将分母多项式除以分子多项式，就可得到一个 $z^{-1}$ 的幂序列（可能有无限项），然后根据式(8.2)即可求出相应的时域序列。

举例来说，一个一阶系统由下述差分方程描述：

$$y (k) = \alpha y (k - 1) + u (k) \tag {8.6}$$

其离散传递函数为

$$\frac {Y (z)}{U (z)} = \frac {1}{1 - \alpha z ^ {- 1}}$$

对于由下式定义的单位脉冲输入：

$$
\begin{array}{l} u (0) = 1 \\ u (k) = 0, k \neq 0 \\ \end{array}
$$

其 $z$ 变换为

$$U (z) = 1 \tag {8.7}$$

所以，

$$Y (z) = \frac {1}{1 - \alpha z ^ {- 1}} \tag {8.8}$$

因此，为求时域序列，我们采用长除法将式(8.8)中的分子多项式除以分母多项式，即

$$
\begin{array}{l} \frac {1 + \alpha z ^ {- 1} + \alpha^ {2} z ^ {- 2} + \alpha^ {3} z ^ {- 3} + \cdots}{1 - \alpha z ^ {- 1}) 1} \\ \frac {1 - \alpha z ^ {- 1}}{\alpha z ^ {- 1} + 0} \\ \frac {\alpha z ^ {- 1} - \alpha^ {2} z ^ {- 2}}{\alpha^ {2} z ^ {- 2} + 0} \\ \begin{array}{c} \alpha^ {2} z ^ {- 2} - \alpha 3 z ^ {- 3} \\ \hline \alpha 3 z ^ {- 3} \\ \ddots \end{array} \\ \end{array}
$$

从而得到无穷序列：

$$Y (z) = 1 + \alpha z ^ {- 1} + \alpha^ {2} z ^ {- 2} + \alpha^ {3} z ^ {- 3} + \dots \tag {8.9}$$

由式(8.9)和式(8.2)，可以得出 y 的采样时间序列为

$$
\begin{array}{l} y (0) = 1 \\ y (1) = \alpha \\ y (2) = \alpha^ {2} \\ \begin{array}{c c} \bullet & \bullet \\ \bullet & \bullet \\ \bullet & \bullet \end{array} \\ y (k) = \alpha^ {k} \\ \end{array}
$$

该序列可以直接由式(8.6)经过简单计算得出。
