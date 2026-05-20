$$
\dot {\boldsymbol {x}} = (\overline {{A}} - \overline {{B}} \overline {{K}}) \boldsymbol {x} + \overline {{B}} L \boldsymbol {v} = \left[ \begin{array}{r r r r} 0 & 1 & 0 & 0 \\ - 8 & - 6 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & - 5 & - 4 \end{array} \right] \boldsymbol {x} + \left[ \begin{array}{l l} 0 & 0 \\ 1 & 0 \\ 0 & 0 \\ 0 & 1 \end{array} \right] \boldsymbol {v}

y = \overline {{C}} x = \left[ \begin{array}{c c c c} 1 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 \end{array} \right] x
$$

而其传递函数矩阵则为：

$$
G _ {K L} (s) = C (s I - A + B K) ^ {- 1} B L = \left[ \begin{array}{c c} \frac {1}{s ^ {2} + 6 s + 8} & 0 \\ 0 & \frac {1}{s ^ {2} + 4 s + 5} \end{array} \right]
$$

静态解耦控制问题 考虑输出维数和输入维数相等的线性定常受控系统

$$\dot {x} = A x + B uy = C x \tag {5.123}$$

如果存在状态反馈和输入变换 $\{K, L\}$ ，使得所导出的闭环控制系统

$$
\begin{array}{l} \dot {\boldsymbol {x}} = (A - B K) \boldsymbol {x} + B L \boldsymbol {v} \\ y = C x \tag {5.124} \\ \end{array}
$$

具有如下属性：

(i) 闭环控制系统 (5.124) 是渐近稳定的。

(ii) 尽管一般地说，闭环系统的传递函数矩阵 $G_{KL}(s) = C(sI - A + BK)^{-1}BL$ 为非对角线矩阵；但是，当 $s \to 0$ 时其为对角线非奇异常阵，即

$$
\lim _ {s \rightarrow 0} G _ {K L} (s) = \left[\begin{array}{c c c}\bar {g} _ {i i} (0)&&\\&\ddots&\\&&\bar {g} _ {p p} (0)\end{array}\right], \quad \bar {g} _ {i i} (0) \neq 0 \tag {5.125}
$$

则称受控系统(5.123)是静态能解耦的。与此相区别，通常称前面所研究的解耦问题为动态解耦问题。

静态解耦的概念只适用于参考输入 $\pmb{v}$ 的各个分量为阶跃信号的情况。令

$$
\boldsymbol {v} (t) = \left[ \begin{array}{c} \beta_ {1} 1 (t) \\ \vdots \\ \beta_ {p} 1 (t) \end{array} \right] \tag {5.126}
$$

其中， $\beta_{i}$ 为非零常数， $1(t)$ 为单位阶跃函数。则利用拉普拉斯变换的终值定理，在系统(5.124)为渐近稳定的前提下，可得到系统为稳态时的输出为：

$$
\lim _ {s \rightarrow \infty} y (s) = \lim _ {s \rightarrow 0} s G _ {K L} (s) \left[\begin{array}{c}\beta_ {1}\\\vdots\\\beta_ {p}\end{array}\right] \frac {1}{s} = [ \lim _ {s \rightarrow 0} G _ {K L} (s) ] \left[\begin{array}{c}\beta_ {1}\\\vdots\\\beta_ {p}\end{array}\right]

= \left[ \begin{array}{c c c} \bar {g} _ {1 1} (0) & & \\ & \ddots & \\ & & \bar {g} _ {p p} (0) \end{array} \right] \left[ \begin{array}{l} \beta_ {1} \\ \vdots \\ \beta_ {p} \end{array} \right] = \left[ \begin{array}{c} \bar {g} _ {1 1} (0) \beta_ {1} \\ \vdots \\ \bar {g} _ {p p} (0) \beta_ {p} \end{array} \right] \tag {5.127}
$$

也即有

$$\lim _ {t \rightarrow \infty} y _ {i} (t) = \tilde {g} _ {i i} (0) \beta_ {i}, \quad i = 1, 2, \dots , p \tag {5.128}$$

这表明,相对于分量为阶跃信号的参考输入,当系统实现静态解耦时,可做到稳态下每个输出都只受同序号的一个输入而完全控制。但在过渡过程中,则输出和输入间的交叉耦合关系并不能消除。这一点,也正是静态解耦和动态解耦之间的基本区别。

对于受控系统(5.123)，用以判断其是否可用状态反馈和输入变换实现静态解耦的判据，由下列结论给出。
