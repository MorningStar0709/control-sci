中，任意地选取 $k$ 个线性无关的列，记为 $\pmb{q}_1, \pmb{q}_2, \dots, \pmb{q}_k$ 。此外，又在 $n$ 维实数空间中 $^{1)}$ 任意地选择 $n - k$ 个列向量，记为 $\pmb{q}_{k+1}, \dots, \pmb{q}_n$ ，使它们和 $\{\pmb{q}_1, \pmb{q}_2, \dots, \pmb{q}_k\}$ 为线性无关。这样，就可组成变换矩阵

$$P ^ {- 1} \triangleq Q = [ q _ {1}, \dots , q _ {k}; q _ {k + 1}, \dots , q _ {n} ] \tag {3.238}$$

并且其必是非奇异的。在此基础上，就可给出系统结构按能控性进行分解的基本结论。

结论 对（3.236）的不完全能控系统，引入线性非奇异变换 $\bar{x}=Px$ ，即可导出系统结构按能控性分解的规范表达式：

$$
\left[ \begin{array}{l} \dot {\bar {x}} _ {c} \\ \dot {\bar {x}} _ {c} \end{array} \right] = \left[ \begin{array}{l l} \bar {A} _ {c} & \bar {A} _ {1 2} \\ 0 & \bar {A} _ {c} \end{array} \right] \left[ \begin{array}{l} \bar {x} _ {c} \\ \bar {x} _ {c} \end{array} \right] + \left[ \begin{array}{l} \bar {B} _ {e} \\ 0 \end{array} \right] u \tag {3.239}

\boldsymbol {y} = \left[ \begin{array}{l l} \bar {C} _ {e} & \bar {C} _ {i} \end{array} \right] \left[ \begin{array}{c} \bar {\boldsymbol {x}} _ {e} \\ \bar {\boldsymbol {x}} _ {i} \end{array} \right]
$$

其中， $\bar{x}_{c}$ 为 k 维能控分状态向量， $\bar{x}_{i}$ 为 n-k 维不能控分状态向量， $k=\operatorname{rank}Q_{c}$ 。

证表

$$
P = Q ^ {- 1} = \left[ \begin{array}{c} \boldsymbol {p} _ {1} ^ {T} \\ \vdots \\ \boldsymbol {p} _ {n} ^ {T} \end{array} \right] \tag {3.240}
$$

则由 $PP^{-1} = I$ ，可导出

$$p _ {i} ^ {T} q _ {i} = 0, \quad \forall i \neq j \tag {3.241}$$

进而又知，对于 $i \leqslant k, Aq_{j}$ 是 $\{q_{1}, q_{2}, \cdots, q_{k}\}$ 的线性组合。所以，由此并利用(3.241)，还可得到

$$\boldsymbol {p} _ {i} ^ {T} A \boldsymbol {q} _ {j} = 0, \quad i = k + 1, \dots , n, j = 1, 2, \dots , k \tag {3.242}$$

于是，利用(3.240)，(3.238)和(3.242)，即得

$$
\begin{array}{l} \vec {A} = P A P ^ {- 1} = \left[ \begin{array}{c c c c c c} p _ {1} ^ {T} A q _ {1} & \dots \dots & p _ {1} ^ {T} A q _ {k} & p _ {1} ^ {T} A q _ {k + 1} & \dots \dots & p _ {1} ^ {T} A q _ {n} \\ \vdots & & \vdots & \vdots & & \vdots \\ p _ {k} ^ {T} A q _ {1} & \dots \dots & p _ {k} ^ {T} A q _ {k} & p _ {k} ^ {T} A q _ {k + 1} & \dots \dots & p _ {k} ^ {T} A q _ {n} \\ \hline p _ {k + 1} ^ {T} A q _ {1} & \dots \dots & p _ {k + 1} ^ {T} A q _ {k} & p _ {k + 1} ^ {T} A q _ {k + 1} & \dots \dots & p _ {k + 1} ^ {T} A q _ {n} \\ \vdots & & \vdots & \vdots & & \vdots \\ p _ {n} ^ {T} A q _ {1} & \dots \dots & p _ {n} ^ {T} A q _ {k} & p _ {n} ^ {T} A q _ {k + 1} & \dots \dots & p _ {n} ^ {T} A q _ {n} \end{array} \right] \\ = \left[ \begin{array}{l l} \bar {A} _ {0} & \bar {A} _ {1 2} \\ 0 & \bar {A} _ {1} \end{array} \right] \tag {3.243} \\ \end{array}
$$

同样，B的所有列也均可表为 $\{q_{1}, q_{2}, \cdots, q_{k}\}$ 的线性组合，因而由(3.240)和(3.241)，可得
