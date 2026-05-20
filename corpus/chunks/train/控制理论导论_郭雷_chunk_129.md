# 1.9 定常线性系统的解耦控制

解耦问题是多输入-多输出定常线性控制系统综合理论中的一个重要组成部分。寻求适当的反馈控制律和线性定常非奇异输入变换，使对多输入多输出受控系统所构成的闭环控制系统的每个输出仅由一个输入所完全控制，且不同的输出由不同的输入所控制，这样的问题称之为解耦问题。显然，在实现了解耦以后，一个多输入多输出系统，就化成了多个独立的单输入单输出系统。要完全解决上述问题，首先应确定系统能够被解耦的充分必要条件，这是要解决能解耦性的判别问题；其次应确定解耦控制律和解耦系统的结构，这是要解决系统的综合问题。本节我们将围绕这两个问题，介绍目前获得的有关定常线性控制系统解耦方面的主要研究成果。有兴趣的读者也可参看文献[6],[8],[9],[10],[15],[17]。

考虑多输入多输出线性定常系统

$$
\left\{ \begin{array}{l} \dot {x} = A x + B u, \\ y = C x, \end{array} \right. \tag {1.9.1}
$$

其中 $x$ 为 $n$ 维状态向量， $u, y$ 分别为系统的输入和输出，且具有相同的维数 $m$ .

设 $Y(s)$ 和 $U(s)$ 分别表示系统输出 $y$ 和输入 $u$ 的 Laplace 变换式，并令 $G(s) = C(sI - A)^{-1}B$ ，它是式 (1.9.1) 的传递函数阵，则有 $Y(s) = G(s)U(s)$ 。一般来讲， $G(s)$ 不是对角阵，因此系统的每一个输入都可能同时影响所有其他输出。我们称这种现象为输入输出耦合。此时，如果想调整系统的某一输出的话，需要同时协调系统的 $m$ 个输入。这可能会同时影响系统的某些其他输出。相反，如果 $G(s)$ 是一个对角阵的话，那么一个输入只对一个输出产生影响，一个输出只受一个输入的控制，我们称这种现象为输入输出解耦。此时，如果想调整某一输出，则只需改变相对应的那一个输入变量即可。

考虑状态反馈加非奇异输入变换的控制律，其形式为

$$u = - K x + L v, \tag {1.9.2}$$

其中 K 为 $m \times n$ 反馈增益阵，L 为 $m \times m$ 非奇异输入变换阵，v 为外加控制输入。解耦控制的问题是：找出一对矩阵 $(K, L)$ 使得在状态反馈加非奇异输入变换控制 (1.9.2) 下，闭环系统输入输出解耦，即 $G_{KL}(s) = C(sI - A + BK)^{-1}BL$ 为非奇异对角阵（有理分式阵）

$$\boldsymbol {G} _ {K L} (s) = \operatorname{diag} \left(g _ {1 1} (s), g _ {2 2} (s), \dots , g _ {m m} (s)\right), \quad g _ {i i} (s) \neq 0, \quad i = 1, 2, \dots , m.$$

引理1.9.1 闭环系统传递函数 $G_{KL}(s)$ 与开环传递函数 $G(s)$ 有如下关系：

$$
\begin{array}{l} \boldsymbol {G} _ {K L} (s) = \boldsymbol {G} (s) [ \boldsymbol {I} - \boldsymbol {K} (s \boldsymbol {I} - \boldsymbol {A} + \boldsymbol {B K}) ^ {- 1} \boldsymbol {B} ] \boldsymbol {L} \\ = G (s) \left[ I + K (s I - A) ^ {- 1} B \right] ^ {- 1} L. \tag {1.9.3} \\ \end{array}
$$

证明 由

$$
\begin{array}{l} \boldsymbol {G} _ {K L} (s) = \boldsymbol {C} (s \boldsymbol {I} - \boldsymbol {A} + \boldsymbol {B K}) ^ {- 1} B L \\ = C (s I - A) ^ {- 1} \left[ (s I - A + B K) - B K \right] (s I - A + B K) ^ {- 1} B L \\ = C (s I - A) ^ {- 1} [ I - B K (s I - A + B K) ^ {- 1} ] B L \\ = G (s) \left[ I - K (s I - A + B K) ^ {- 1} B \right] L, \\ \end{array}
$$

知式 (1.9.3) 的第一个等式成立。为证第二个等式，只需证明

$$\boldsymbol {I} - \boldsymbol {K} (s \boldsymbol {I} - \boldsymbol {A} + \boldsymbol {B K}) ^ {- 1} \boldsymbol {B} = \left[ \boldsymbol {I} + \boldsymbol {K} (s \boldsymbol {I} - \boldsymbol {A}) ^ {- 1} \boldsymbol {B} \right] ^ {- 1}.$$

此式是1.1节中的式(1.1.8)在 $A_{11} = I, A_{12} = -K, A_{21} = B$ 和 $A_{22} = sI - A$ 时的特例.

定理 1.9.1 采用形如式 (1.9.2) 的态反馈加非奇异输入变换控制使系统 (1.9.1) 输入输出解耦的充要条件是矩阵
