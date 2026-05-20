由上式等式两边 $s^{i}(i=1,\cdots,n)$ 的系数阵必须相等，又可导出

$$
\left\{ \begin{array}{l} R _ {n - 1} = I \\ R _ {n - 2} = R _ {n - 1} A + \alpha_ {n - 1} I \\ \dots \dots \\ R _ {1} = R _ {2} A + \alpha_ {2} I \\ R _ {0} = R _ {1} A + \alpha_ {1} I \end{array} \right. \tag {1.98}
$$

从而，在(1.98)中，依次将上一个方程代入下一个方程，就可得到：

$$
\left\{ \begin{array}{l} R _ {n - 1} = I \\ R _ {n - 2} = A + \alpha_ {n - 1} I \\ R _ {n - 3} = A ^ {2} + \alpha_ {n - 1} A + \alpha_ {n - 2} I \\ \dots \dots \\ R _ {1} = A ^ {n - 2} + \alpha_ {n - 1} A ^ {n - 3} + \dots + \alpha_ {2} I \\ R _ {0} = A ^ {n - 1} + \alpha_ {n - 1} A ^ {n - 2} + \dots + \alpha_ {1} I \end{array} \right. \tag {1.99}
$$

进一步，利用（1.84）和（1.95），可得到

$$
\begin{array}{l} G (s) = C (s I - A) ^ {- 1} B + D \\ = \frac {1}{\alpha (s)} \left[ C R _ {n - 1} B s ^ {n - 1} + C R _ {n - 2} B s ^ {n - 2} + \dots + C \underline {{R _ {1}}} B s \right. \\ + C R _ {0} B ] + D \tag {1.100} \\ \end{array}
$$

再表 $E_{n-1}=CR_{n-1}B,\quad E_{n-2}=CR_{n-2}B,\cdots,E_{1}=CR_{1}B,E_{0}=CR_{0}B$ ，那么就导出了(1.94)。并且，由此并利用(1.99)，可知 $E_{i}(i=0,1,\cdots,n-1)$ 的关系式为(1.93)。于是，结论得证。

例 给定系统的状态空间描述为:

$$
\dot {x} = \left[ \begin{array}{l l l} 2 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 3 & 1 \end{array} \right] x + \left[ \begin{array}{l l} 1 & 2 \\ 1 & 0 \\ 3 & 1 \end{array} \right] u
y = [ 1 \quad 1 \quad 2 ] x
$$

现先定出系统的特征多项式为：

$$\alpha (s) = \det (s I - A) = (s - 2) ^ {2} (s - 1) = s ^ {3} - 5 s ^ {2} + 8 s - 4$$

再计算系数矩阵:

$$
E _ {2} = C B = [ 1 \quad 1 \quad 2 ] \left[ \begin{array}{l l} 1 & 2 \\ 1 & 0 \\ 3 & 1 \end{array} \right] = [ 8 \quad 4 ]

E _ {1} = C A B + \alpha_ {2} C B = [ 1 \quad 1 \quad 2 ] \left[ \begin{array}{l l l} 2 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 3 & 1 \end{array} \right] \left[ \begin{array}{l l} 1 & 2 \\ 1 & 0 \\ 3 & 1 \end{array} \right]
+ [ - 4 0 - 2 0 ] = [ - 2 4 - 1 4 ]
E _ {0} = C A ^ {2} B + \alpha_ {2} C A B + \alpha_ {1} C B = [ 1 1 2 ] \left[ \begin{array}{l l l} 2 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 3 & 1 \end{array} \right] \left[ \begin{array}{l l} 2 & 4 \\ 2 & 0 \\ 6 & 1 \end{array} \right]
+ [ - 8 0 - 3 0 ] + [ 6 4 3 2 ] = [ 1 6 1 2 ]
$$

从而，利用（1.94），即可得到传递函数矩阵为：

$$G (s) = \frac {1}{\alpha (s)} \left[ E _ {2} s ^ {2} + E _ {1} s + E _ {0} \right]= \left[ \frac {8 s ^ {2} - 2 4 s + 1 6}{s ^ {3} - 5 s ^ {2} + 8 s - 4} \quad \frac {4 s ^ {2} - 1 4 s + 1 2}{s ^ {3} - 5 s ^ {2} + 8 s - 4} \right]$$

计算特征多项式的算法 从上面的讨论中可以看到，在由状态空间描述 $\{A, B, C, D\}$ 确定传递函数矩阵 $G(s)$ 中，一个尚待解决的问题是定出矩阵 $A$ 的特征多项式 $\alpha(s)$ 。此外，在系统的一些分析和综合问题中，也都面临这个问题。现在我们简短地讨论这一问题，不加证明地介绍计算特征多项式的一种常用算法，通常称其为莱弗勒（Leverrier）算法。

给定 $n \times n$ 常阵 $A$ , 其特征多项式可表为:

$$\alpha (s) = \det (s l - A) = s ^ {n} + \alpha_ {n - 1} s ^ {n - 1} + \dots + \alpha_ {1} s + \alpha_ {0} \tag {1.101}$$

则其系数 $\alpha_{i}(i=n-1,n-2,\cdots,1,0)$ 可以按如下的顺序递推地来定出：

$$R _ {n - 1} = I, \quad \alpha_ {n - 1} = - \frac {\operatorname{tr} R _ {n - 1} A}{1}R _ {n - 2} = R _ {n - 1} A + \alpha_ {n - 1} I, \quad \alpha_ {n - 2} = - \frac {\operatorname{tr} R _ {n - 2} A}{2}R _ {n - 3} = R _ {n - 2} A + \alpha_ {n - 2} I, \quad \alpha_ {n - 3} = - \frac {\operatorname{tr} R _ {n - 3} A}{3}$$

● ● ● ● ● ●

$$R _ {1} = R _ {2} A + \alpha_ {2} I, \quad \alpha_ {1} = - \frac {\operatorname{tr} R _ {1} A}{n - 1}R _ {0} = R _ {1} A + \alpha_ {1} I, \quad \alpha_ {0} = - \frac {\operatorname{tr} R _ {0} A}{n}$$

其中，tr 表示矩阵的迹，其定义为矩阵的所有对角线元之和。
