$$
\begin{array}{l} \boldsymbol {G} _ {K L} (s) = \boldsymbol {G} (s) [ \boldsymbol {I} + \boldsymbol {K} (s \boldsymbol {I} - \boldsymbol {A}) ^ {- 1} \boldsymbol {B} ] ^ {- 1} \boldsymbol {L} \\ = G (s) \left[ L ^ {- 1} + L ^ {- 1} K (s I - A) ^ {- 1} B \right] ^ {- 1} \\ = \boldsymbol {G} (s) [ \boldsymbol {E} + \boldsymbol {F} (s \boldsymbol {I} - \boldsymbol {A}) ^ {- 1} \boldsymbol {B} ] ^ {- 1} \\ = \operatorname{diag} \left(\frac {1}{\Delta_ {1} (s)}, \dots , \frac {1}{\Delta_ {m} (s)}\right). \\ \end{array}
$$

以上讨论了控制系统的输入输出解耦问题，要求闭环控制系统的传递函数为对角阵。对于许多系统来说，这可能难于实现或不可能实现。退一步，考虑只要求闭环控制系统的输出达到稳态后输入输出是解耦的。具体而言，对输出输入维数相等的线性定常系统(1.9.1)，如果存在状态反馈和非奇异输入变换(1.9.2)，使得所导出的闭环控制系统

$$
\left\{ \begin{array}{l} \dot {x} = (A - B K) x + B L v \\ y = C x \end{array} \right. \tag {1.9.9}
$$

具有如下性质：

(i) 闭环控制系统 (1.9.9) 是渐近稳定的；

(ii) 当 $s \to 0$ 时，闭环系统的传递函数矩阵 $G_{KL}(s) = C(sI - A + BK)^{-1}BL$ 为非奇异对角阵，即

$$
\lim _ {s \rightarrow 0} \boldsymbol {G} _ {K L} (s) = \left[\begin{array}{c c c}\overline {{g}} _ {1 1} (0)&&\\&\ddots&\\&&\overline {{g}} _ {m m} (0)\end{array}\right], \quad \overline {{g}} _ {i i} (0) \neq 0,
$$

则称系统 (1.9.1) 静态能解耦的。与此相区别，通常称前面所研究的解耦问题为动态解耦问题。

静态解耦的概念只适用于参考输入 $v$ 的各个分量为阶跃信号的情况。令

$$
v (t) = \left[ \begin{array}{c} \beta_ {1} 1 (t) \\ \vdots \\ \beta_ {m} 1 (t) \end{array} \right],
$$

其中 $\beta_{i}$ 为非零常数，1(t)为单位阶跃函数。利用Laplace变换的终值定理，在系

统 (1.9.9) 为渐近问题的前提下，可得到系统为稳态时的输出为

$$
\begin{array}{l} \lim _ {t \rightarrow \infty} y (t) = \lim _ {s \rightarrow 0} s G _ {K L} (s) \left[\begin{array}{c}\beta_ {1}\\\vdots\\\beta_ {m}\end{array}\right] \frac {1}{s} = \left[ \lim _ {s \rightarrow 0} G _ {K L} (s) \right]\left[\begin{array}{c}\beta_ {1}\\\vdots\\\beta_ {m}\end{array}\right] \\ = \left[ \begin{array}{c c c} \overline {{g}} _ {1 1} (0) & & \\ & \ddots & \\ & & \overline {{g}} _ {m m} (0) \end{array} \right] \left[ \begin{array}{c} \beta_ {1} \\ \vdots \\ \beta_ {m} \end{array} \right] = \left[ \begin{array}{c} \overline {{g}} _ {1 1} (0) \beta_ {1} \\ \vdots \\ \overline {{g}} _ {m m} (0) \beta_ {m} \end{array} \right]. \\ \end{array}
$$

也即有

$$\lim _ {t \rightarrow \infty} y _ {i} (t) = \overline {{{g}}} _ {i i} (0) \beta_ {i}, \quad i = 1, 2, \dots , m.$$

这表明，相对于分量为阶跃信号的参考输入，当系统实现静态解耦时，可做到稳态下每个输出都只受同序号的一个输入而完全控制。但在过渡过程中，则输出和输入间的交叉耦合关系并没有消除。这也正是静态解耦和动态解耦之间的基本区别。

定理 1.9.3 存在形如式 (1.9.2) 的状态反馈加非奇异输入变换的控制律，使受控系统 (1.9.1) 实现静态解耦的充分必要条件是

(i) 系统 (1.9.1) 是用状态反馈能镇定的;
