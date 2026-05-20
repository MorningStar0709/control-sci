(5) 对准波波夫形 $D_{QE}(s)$ ，则其相应的常阵 $\mathcal{D}_{QE}^{\prime}$ 满足性质(2)，但是不满足性质(3)。

确定波波夫形的算法 给定 p 维的方多项式矩阵 $\overline{D}(s)$ ，则其波波夫形 $D_{E}(s)$ 可按照下列的步骤来求出：

(1) 如果 $\overline{D}(s)$ 为列既约, 则令 $\overline{D}(s) = D(s)$ , 且直接转入下一步。如果 $\overline{D}(s)$ 不是列既约的, 则寻找一个单模阵 $V(s)$ 使 $D(s) = \overline{D}(s)V(s)$ 为列既约, 然后再转入下一步。  
(2) 寻找一个单模阵 $U(s)$ , 使有 $D(s)U(s) = E(s)$ , 其中 $E(s)$ 为波波夫形或准波波夫形。关于确定 $E(s)$ 和 $U(s)$ 的问题, 有如下的两个结论:

结论1 给定多项式矩阵 $D(s)$ ，设其维数为 p，表 $L = \max\{k_{c1}, \cdots, k_{cp}\}$ ，再定义如下一个增广多项式矩阵：

$$\mathcal {B} (s) = [ D (s) s D (s) \dots s ^ {L} D (s) | - I _ {p} - s I _ {p} - \dots - s ^ {L} I _ {p} ] \tag {6.137}$$

其行数和列数分别为 $p$ 和 $2(L + 1)p$ 。则通过求出下述矩阵方程

$$\mathcal {B} (s) \mathcal {A} = 0 \tag {6.138}$$

的 $2(L + 1)p \times p$ 的常数矩阵解 $\mathcal{A}$ ，并将其作如下的分块表示

$$
\mathcal {A} \triangleq \left[ \begin{array}{c} U _ {0} \\ \vdots \\ U _ {L} \\ - - - \\ E _ {0} \\ \vdots \\ E _ {L} \end{array} \right], U _ {i}, E _ {i} \in \mathcal {R} ^ {p \times p} \tag {6.139}
$$

就即可定出：

$$E (s) = E _ {L} s ^ {L} + \dots + E _ {1} s + E _ {0} \tag {6.140}U (s) = U _ {1} s ^ {L} + \dots + U _ {1} s + U _ {0} \tag {6.141}$$

证 由 $D(s)U(s) = E(s)$ ，可导出

$$
[ D (s) - I _ {p} ] \left[ \begin{array}{l} U (s) \\ E (s) \end{array} \right] = 0 \tag {6.142}
$$

现将 $E(s)$ 和 $U(s)$ 表示为(6.140)和(6.141)的形式，并代入(6.142)，即得

$$
\begin{array}{l} 0 = [ D (s) - I _ {p} ] \left[ \begin{array}{l} U _ {0} \\ E _ {0} \end{array} \right] + [ s D (s) - s I _ {p} ] \left[ \begin{array}{l} U _ {1} \\ E _ {1} \end{array} \right] + \dots \\ + \left[ s ^ {L} D (s) - s ^ {L} I _ {p} \right] \left[ \begin{array}{l} U _ {L} \\ E _ {L} \end{array} \right] \\ = [ D (s) s D (s) \dots s ^ {L} D (s) - I _ {p} - s I _ {p} \dots - s ^ {L} I _ {p} ] \left[ \begin{array}{c} U _ {0} \\ \vdots \\ U _ {L} \\ E _ {0} \\ \vdots \\ E _ {I} \end{array} \right] \\ = \mathcal {B} (s) \mathcal {A} \tag {6.143} \\ \end{array}
$$

表明，只要求出方程(6.143)的解阵 $\mathcal{A}$ ，并将其分块化，即可由(6.140)和(6.141)分别来求出 $E(s)$ 和 $U(s)$ 。从而结论得证。

结论2 方程 $\mathcal{B}(s)\mathcal{A} = 0$ 的常数矩阵解 $\mathcal{A}$ ，可以通过搜索如下的多项式矩阵

$$\mathcal {B} (s) = [ D (s) \dots s ^ {L} D (s) - I _ {p} \dots - s ^ {L} I _ {p} ] \tag {6.144}$$

的 p 个首相关列来得到; 其中

① 相关列定义为 $\mathcal{B}(s)$ 中可表示为先前各列的且系数限制为常数的线性组合的那些列。

② 首相关列是指列位置指数为强意义下不相等的所有相关列。

③ 一般, 相关列将出现在 $\mathcal{B}(s)$ 的右半部分中, 即可从 $[-I_p - sI_p \cdots - s^2 I_p]$ 中去搜索。

(3) 如果所得到的 $E(s)$ 为波波夫形, 则即有 $D_E(s) = E(s)$ 。如果 $E(s)$ 为准波波夫形, 则通过初等运算将 $\mathcal{A}'$ 变换为阶梯形实常阵 $\tilde{\mathcal{A}}'$ , 再把 $\mathcal{A}$ 作分块表示并利用式(6.140)而定出波波夫形 $D_E(s)$ 。
