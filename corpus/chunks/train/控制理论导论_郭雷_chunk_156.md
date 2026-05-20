其中 $S = T \stackrel{\operatorname{def}}{=} [h_{1}, h_{2}, \cdots, h_{q_{1}}, \cdots, h_{q_{1} + q_{2} + \cdots + q_{l}}]^{-1}$ 由所有广义特征向量组成；

(4) A 有重复共轭特征值的情况。为简化书写，我们考虑只有一对重复共轭成双特征值的情况。不妨认为 $\lambda_{1}-\alpha_{1}+\mathrm{j}\beta_{1},\lambda_{2}=\alpha_{1}-\mathrm{j}\beta_{1}$ 。这时 $e^{At}$ 的形式为

$$
\mathrm{e} ^ {\boldsymbol {A} t} = \boldsymbol {S} ^ {- 1} \left[ \begin{array}{c c c c} \mathrm{e} ^ {J _ {1, 2} t} & & & \\ & \mathrm{e} ^ {J _ {3} t} & & \\ & & \ddots & \\ & & & \mathrm{e} ^ {J _ {l} t} \end{array} \right] \boldsymbol {S},
$$

$e^{J_{3}t}, e^{J_{4}t}, \cdots, e^{J_{i}t}$ 的形式与 (3) 中相同，而有 $e^{J_{1.2}}$ 下列形式：

$$
\mathrm{e} ^ {J _ {1, 2} t} = \left[ \begin{array}{c c c c} \mathrm{e} ^ {T _ {1} t} & & & \\ & \mathrm{e} ^ {T _ {2} t} & & \\ & & \ddots & \\ & & & \mathrm{e} ^ {T _ {m _ {1, 2}} t} \end{array} \right], \tag {2.3.16}

\mathrm{e} ^ {T _ {p} t} = \left[ \begin{array}{c c c c} M _ {2} & t M _ {2} & \dots & \frac {t ^ {n _ {p} - 1}}{(n _ {p} - 1) !} M _ {2} \\ & M _ {2} & \dots & \frac {t ^ {n _ {p} - 2}}{(n _ {p} - 2) !} M _ {2} \\ & & \ddots & \vdots \\ & & & M _ {2} \end{array} \right] \mathrm{e} ^ {\alpha_ {1} t}, \tag {2.3.17}
$$

其中 $p = 1,2,\dots ,m_{1,2},\sum_{p = 1}^{m_{1,2}}n_p = q_1.$ 而 $\pmb{M}_2$ 定义为

$$
\boldsymbol {M} _ {2} = \left[ \begin{array}{c c} \cos \beta_ {1} t & \sin \beta_ {1} t \\ - \sin \beta_ {1} t & \cos \beta_ {1} t \end{array} \right],
$$

其中

$$\boldsymbol {S} ^ {- 1} = \boldsymbol {T} \stackrel {\text { def }} {=} [ \xi_ {1}, \eta_ {1}, \xi_ {2}, \eta_ {2}, \dots , \xi_ {q _ {1}}, \eta_ {q _ {1}}, h _ {2 q _ {1} + 1}, \dots , h _ {q _ {1} + q _ {2} + \dots + q _ {l}} ]$$

由 $\pmb{A}$ 的广义特征向量组成。这里对应于 $\lambda_{1} = \alpha_{1} + \mathrm{j}\beta_{1},\lambda_{2} = \alpha_{1} - \mathrm{j}\beta_{1}$ 的广义特征向量也是共轭成双出现的，且

$$h _ {1} = \xi_ {1} + j \eta_ {1}, \quad h _ {q _ {1} + 1} = \xi_ {1} - j \eta_ {1},h _ {2} = \xi_ {2} + j \eta_ {2}, \quad h _ {q _ {1} + 2} = \xi_ {2} - j \eta_ {2}, \dots ,h _ {q _ {1}} = \xi_ {q _ {1}} + \mathrm{j} \eta_ {q _ {1}}, \quad h _ {q _ {1} + q _ {2}} = h _ {2 q _ {1}} = \xi_ {q _ {1}} - \mathrm{j} \eta_ {q _ {1}}.$$

现在讨论线性定常齐次微分方程解在 $[0, +\infty)$ 上的性质。根据方程 (2.3.12) 的状态转移阵 $\mathbf{e}^{A t}$ 的形式，能够依其系数矩阵 $A$ 的特征值的性质分别获得微分方程 (2.3.12) 的解在无穷时间区间 $0 \leqslant t < +\infty$ 上的性质：

(1) 如果 $\pmb{A}$ 的所有特征值的实部皆小于零，那么存在正数 $L$ 和 $\alpha$ ，使得方程 (2.3.12) 的解 $x(t;0,x_0)$ 满足

$$| x (t; 0, x _ {0}) | \leqslant L | x _ {0} | \mathrm{e} ^ {- \alpha t}, \quad \forall t \in [ 0, \infty); \tag {2.3.18}$$

(2) 如果 $A$ 的特征值中有一个 $\lambda_{k} = \alpha_{k} + \mathrm{j}\beta_{k}$ 的实部 $\alpha_{k} \geqslant 0$ , 并且对应于 $\lambda_{k}$ 的 Jordan 块 $T_{kp}$ 中至少有一块的阶数大于 1, 那么方程 (2.3.12) 必有无界解;

(3) 如果 $\pmb{A}$ 的特征值的实部都不大于零，并且其实部等于零的特征值对应的 Jordan 块都是一阶的，那么存在正数 $L$ ，使得方程 (2.3.12) 的解 $x(t;0,x_0)$ 满足

$$| x (t; 0, x _ {0}) | \leqslant L | x _ {0} |, \quad \forall t \geqslant 0.$$

(1), (2) 和 (3) 的证明见文献 [1].
