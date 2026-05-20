# (1) 齐次状态方程的解

状态方程

$$\dot {\boldsymbol {x}} (t) = \boldsymbol {A} \boldsymbol {x} (t) \tag {9-22}$$

称为齐次状态方程，通常采用幂级数法和拉普拉斯变换法求解。

1) 幂级数法。设状态方程式(9-22)的解是 $t$ 的向量幂级数

$$\boldsymbol {x} (t) = \boldsymbol {b} _ {0} + \boldsymbol {b} _ {1} t + \boldsymbol {b} _ {2} t ^ {2} + \dots + \boldsymbol {b} _ {k} t ^ {k} + \dots$$

式中， $x,b_{0},b_{1},\cdots,b_{k},\cdots$ 都是 n 维向量，则

$$
\begin{array}{l} \dot {\boldsymbol {x}} (t) = \boldsymbol {b} _ {1} + 2 \boldsymbol {b} _ {2} t + \dots + k \boldsymbol {b} _ {k} t ^ {k - 1} + \dots \\ = \boldsymbol {A} \left(\boldsymbol {b} _ {0} + \boldsymbol {b} _ {1} t + \boldsymbol {b} _ {2} t ^ {2} + \dots + \boldsymbol {b} _ {k} t ^ {k} + \dots\right) \\ \end{array}
$$

令上式等号两边 t 的同次项的系数相等, 则有

$$
\begin{array}{l} \boldsymbol {b} _ {1} = \boldsymbol {A b} _ {0} \\ \boldsymbol {b} _ {2} = \frac {1}{2} \boldsymbol {A} \boldsymbol {b} _ {1} = \frac {1}{2} \boldsymbol {A} ^ {2} \boldsymbol {b} _ {0} \\ \end{array}

\begin{array}{l} \boldsymbol {b} _ {3} = \frac {1}{3} \boldsymbol {A} \boldsymbol {b} _ {2} = \frac {1}{6} \boldsymbol {A} ^ {3} \boldsymbol {b} _ {0} \\ \begin{array}{c} \bullet \\ \bullet \\ \bullet \end{array} \\ \boldsymbol {b} _ {k} = \frac {1}{k} \boldsymbol {A} \boldsymbol {b} _ {k - 1} = \frac {1}{k !} \boldsymbol {A} ^ {k} \boldsymbol {b} _ {0} \\ \begin{array}{c} \bullet \\ \bullet \\ \bullet \end{array} \\ \end{array}
$$

且 $x(0) = b_0$ ，故

$$\boldsymbol {x} (t) = \left(\boldsymbol {I} + \boldsymbol {A} t + \frac {1}{2} \boldsymbol {A} ^ {2} t ^ {2} + \dots + \frac {1}{k !} \boldsymbol {A} ^ {k} t ^ {k} + \dots\right) \boldsymbol {x} (0) \tag {9-23}$$

定义 $e^{At}=I+A t+\frac{1}{2}A^{2}t^{2}+\cdots+\frac{1}{k!}A^{k}t^{k}+\cdots$

$$= \sum_ {k = 0} ^ {\infty} \frac {1}{k !} \mathbf {A} ^ {k} t ^ {k} \tag {9-24}$$

则 $\boldsymbol{x}(t)=\mathrm{e}^{\boldsymbol{A}t}\boldsymbol{x}(0)$ (9-25)

由于标量微分方程 $\dot{x} = ax$ 的解为 $x(t) = \mathrm{e}^{at}x(0),\mathrm{e}^{at}$ 称为指数函数，而向量微分方程式(9-22)具有相似形式的解（式(9-25))，故把 $\mathbf{e}^{\mathbf{A}t}$ 称为矩阵指数函数，简称矩阵指数。由于 $x(t)$ 是由 $x(0)$ 转移而来，对于线性定常系统， $\mathbf{e}^{\mathbf{A}t}$ 又称为状态转移矩阵，记为 $\Phi (t)$ ，即

$$\boldsymbol {\Phi} (t) = \mathrm{e} ^ {\boldsymbol {A} t} \tag {9-26}$$

2) 拉普拉斯变换法。将式(9-22)取拉氏变换，有

$$s \boldsymbol {X} (s) = \boldsymbol {A} \boldsymbol {X} (s) + \boldsymbol {x} (0)$$

则 $(sI - A)X(s) = x(0)$

$$\boldsymbol {X} (s) = (s \boldsymbol {I} - \boldsymbol {A}) ^ {- 1} \boldsymbol {x} (0) \tag {9-27}$$

进行拉氏反变换，有
