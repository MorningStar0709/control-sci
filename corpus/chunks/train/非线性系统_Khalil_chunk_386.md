总之,当且仅当存在函数 $h(x)$ , 使系统(13.28)\~(13.29)的相对阶为 n, 或 h 满足约束条件为式(13.35)的偏微分方程(13.34), 则系统(13.27)是可反馈线性化的。h 的存在性可由向量场 f 和 g 上的充分必要条件描述。这些条件用到了 Lie 括号和不变分布的概念, 下面将进行介绍。

对于 $D \subset R^{n}$ 上的两个向量场 f 和 g, Lie 括号 $[f, g]$ 是第三个向量场, 定义为

$$[ f, g ] (x) = \frac {\partial g}{\partial x} f (x) - \frac {\partial f}{\partial x} g (x)$$

其中 $\left[\partial g/\partial x\right]$ 和 $\left[\partial f/\partial x\right]$ 是雅可比矩阵。g对f的Lie括号可以重复，下面的表示法可简化该过程：

$$
\begin{array}{l} a d _ {f} ^ {0} g (x) = g (x) \\ a d _ {f} g (x) = [ f, g ] (x) \\ a d _ {f} ^ {k} g (x) = [ f, a d _ {f} ^ {k - 1} g ] (x), k \geqslant 1 \\ \end{array}
$$

显然 $[f,g]=-[g,f]$ ，且对常数向量场f和g，有 $[f,g]=0$ 。

例13.9 设 $f(x) = \left[ \begin{array}{c}x_{2}\\ -\sin x_{1} - x_{2} \end{array} \right],g = \left[ \begin{array}{c}0\\ x_{1} \end{array} \right]$

则

$$
\begin{array}{l} [ f, g ] (x) = \left[ \begin{array}{l l} 0 & 0 \\ 1 & 0 \end{array} \right] \left[ \begin{array}{c} x _ {2} \\ - \sin x _ {1} - x _ {2} \end{array} \right] - \left[ \begin{array}{c c} 0 & 1 \\ - \cos x _ {1} & - 1 \end{array} \right] \left[ \begin{array}{l} 0 \\ x _ {1} \end{array} \right] \\ = \left[ \begin{array}{c} - x _ {1} \\ x _ {1} + x _ {2} \end{array} \right] \stackrel {\text { def }} {=} a d _ {f} g \\ \end{array}

\begin{array}{l} a d _ {f} ^ {2} g = [ f, a d _ {f} g ] \\ = \left[ \begin{array}{r r} - 1 & 0 \\ 1 & 1 \end{array} \right] \left[ \begin{array}{c} x _ {2} \\ - \sin x _ {1} - x _ {2} \end{array} \right] - \left[ \begin{array}{c c} 0 & 1 \\ - \cos x _ {1} & - 1 \end{array} \right] \left[ \begin{array}{c} - x _ {1} \\ x _ {1} + x _ {2} \end{array} \right] \\ = \left[ \begin{array}{c} - x _ {1} - 2 x _ {2} \\ x _ {1} + x _ {2} - \sin x _ {1} - x _ {1} \cos x _ {1} \end{array} \right] \\ \end{array}
$$

△

例 13.10 如果 $f(x)=Ax$ ，且 g 是常数向量场，则

$$a d _ {f} g (x) = [ f, g ] (x) = - A ga d _ {f} ^ {2} g = [ f, a d _ {f} g ] = - A (- A g) = A ^ {2} g$$

和 $ad_{f}^{k}g = (-1)^{k}A^{k}g$

△

对 $D \subset R^{n}$ 上的向量场 $f_{1}, f_{2}, \cdots, f_{k}$ ，设

$$\Delta (x) = \operatorname{span} \left\{f _ {1} (x), f _ {2} (x), \dots , f _ {k} (x) \right\}$$

为 $R^{n}$ 的子空间, $R^{n}$ 由在任意固定的 $x \in D$ 的向量 $f_{1}(x)$ , $f_{2}(x)$ , $\cdots$ , $f_{k}(x)$ 张成。对 $x \in D$ , 所有向量空间 $\Delta(x)$ 的集合称为一个分布, 记为

$$\Delta = \operatorname{span} \left\{f _ {1}, f _ {2}, \dots , f _ {k} \right\}$$

$\Delta(x)$ 的维数定义为 $\dim(\Delta(x)) = \text{rank}[f_{1}(x), f_{2}(x), \cdots, f_{k}(x)]$
