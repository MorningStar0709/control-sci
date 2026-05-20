$$
\begin{array}{l} u _ {o} (0) = \lim _ {t \rightarrow 0} u _ {o} (t) = \lim _ {s \rightarrow \infty} s \cdot U _ {o} (s) \\ = \lim _ {s \rightarrow \infty} \left[ \frac {1}{s \left(s ^ {2} + s + 1\right)} + \frac {0 . 1 s + 0 . 2}{s ^ {2} + s + 1} \right] = 0. 1 (\mathrm{V}) \\ \end{array}
$$

$u_{0}(t)$ 的终值为

$$
\begin{array}{l} u _ {o} (\infty) = \lim _ {t \rightarrow \infty} u _ {o} (t) = \lim _ {s \rightarrow 0} s \cdot U _ {o} (s) \\ = \lim _ {s \rightarrow 0} \left[ \frac {1}{s \left(s ^ {2} + s + 1\right)} + \frac {0 . 1 s + 0 . 2}{s ^ {2} + s + 1} \right] = 1 (\mathrm{V}) \\ \end{array}
$$

其结果与从式(2-31)中求得的数值一致。

于是，用拉氏变换法求解线性定常微分方程的过程可归结如下：

1) 考虑初始条件, 对微分方程中的每一项分别进行拉氏变换, 将微分方程转换为变量 $s$ 的代数方程。  
2）由代数方程求出输出量拉氏变换函数的表达式。  
3）对输出量拉氏变换函数求反变换，得到输出量的时域表达式，即为所求微分方程的解。
