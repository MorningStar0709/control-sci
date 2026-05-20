$$
\left[ \begin{array}{l} \alpha_ {0} (t) \\ \alpha_ {1} (t) \\ \alpha_ {2} (t) \\ \alpha_ {3} (t) \\ \alpha_ {4} (t) \\ \alpha_ {5} (t) \\ \vdots \\ \alpha_ {n - 1} (t) \end{array} \right] = \left[ \begin{array}{c c c c c c} 0 & 0 & 1 & 3 \lambda_ {1} & \dots & \frac {(n - 1) (n - 2)}{2 !} \lambda_ {1} ^ {n - 3} \\ 0 & 1 & 2 \lambda_ {1} & 3 \lambda_ {1} ^ {2} & \dots & \frac {(n - 1)}{1 !} \lambda_ {1} ^ {n - 2} \\ 1 & \lambda_ {1} & \lambda_ {1} ^ {2} & \lambda_ {1} ^ {3} & \dots & \lambda_ {1} ^ {n - 1} \\ \hline 0 & 1 & 2 \lambda_ {2} & 3 \lambda_ {2} ^ {2} & \dots & \frac {(n - 1)}{1 !} \lambda_ {2} ^ {n - 2} \\ 1 & \lambda_ {2} & \lambda_ {2} ^ {2} & \lambda_ {2} ^ {3} & \dots & \lambda_ {2} ^ {n - 1} \\ \hline 1 & \lambda_ {3} & \lambda_ {3} ^ {2} & \lambda_ {3} ^ {3} & \dots & \lambda_ {3} ^ {n - 1} \\ \vdots & \vdots & \vdots & \vdots & & \vdots \\ 1 & \lambda_ {n - 3} & \lambda_ {n - 3} ^ {2} & \lambda_ {n - 3} ^ {3} & \dots & \lambda_ {n - 3} ^ {n - 1} \end{array} \right] ^ {- 1} \left[ \begin{array}{l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l} \frac {1}{2 !} t ^ {2} e ^ {\lambda_ {1} t} \\ \frac {1}{1 !} t e ^ {\lambda_ {1} t} \\ e ^ {\lambda_ {1} t} \\ \frac {1}{1 !} t e ^ {\lambda_ {2} t} \\ e ^ {\lambda_ {2} t} \\ e ^ {\lambda_ {3} t} \\ \vdots \\ e ^ {\lambda_ {n - 3} t} \end{array} \right] (2. 3 8)
$$

容易证明关系式 (2.36)—(2.38) 的正确性。给定 $n \times n$ 常阵 $A$ ，表其特征多项式为：

$$\det (s I - A) = s ^ {n} + \alpha_ {n - 1} s ^ {n - 1} + \dots + \alpha_ {1} s + \alpha_ {0} \tag {2.39}$$

则据凯莱-哈密顿（Cayley-Hamilton）定理知，A必满足其本身的零化特征多项式，即成立

$$A ^ {n} + \alpha_ {n - 1} A ^ {n - 1} + \dots + \alpha_ {1} A + \alpha_ {0} I = 0 \tag {2.40}$$

这表明， $A^{n}$ 可表为 $A^{n-1},\cdots,A,I$ 的线性组合：

$$A ^ {n} = - \alpha_ {n - 1} A ^ {n - 1} - \dots - \alpha_ {1} A - \alpha_ {0} I \tag {2.41}$$

进而可知， $A^{n+1}$ ， $A^{n+2}$ ，…等均可表为 $A^{n-1}$ ，…，A, I 的线性组合。这样，利用这些结果，即可将 $e^{At}$ 的无穷多项表达式表示为 $A^{n-1}$ ，…，A, I 的有限项表达式，但其系数为时间 t 的函数，也即（2.36）。再来证明（2.37），为此利用（2.32）和（2.33），即可由（2.36）导出

$$
\left\{ \begin{array}{l} \alpha_ {0} (t) + \alpha_ {1} (t) \lambda_ {1} + \dots + \alpha_ {n - 1} (t) \lambda_ {1} ^ {n - 1} = e ^ {\lambda_ {1} t} \\ \alpha_ {0} (t) + \alpha_ {1} (t) \lambda_ {2} + \dots + \alpha_ {n - 1} (t) \lambda_ {2} ^ {n - 1} = e ^ {\lambda_ {2} t} \\ \dots \dots \\ \alpha_ {0} (t) + \alpha_ {1} (t) \lambda_ {n} + \dots + \alpha_ {n - 1} (t) \lambda_ {n} ^ {n - 1} = e ^ {\lambda_ {n} t} \end{array} \right. \tag {2.42}
$$

从而，由求解方程组（2.42）就得到（2.37）。而利用约当形下的关系式(例如(2.35)和(2.34))，可类似地证得关系式(2.38)，具体推证过程略去。
