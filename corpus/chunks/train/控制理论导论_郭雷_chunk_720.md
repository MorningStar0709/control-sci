首先，对 $t = t_0$ ，利用式(9.6.22)及式(9.6.23)知

$$f (\beta_ {0}) \geqslant f _ {t _ {0}} (\beta_ {0}) - \gamma^ {2} \delta \geqslant (2 - \gamma^ {2}) \delta \geqslant \delta .$$

其次假定式 (9.6.21) 对 $t = k \geqslant t_0$ 成立. 我们考虑 $t = k + 1$ 的情形. 如果 $\beta_{k+1} = \beta_k$ , 则据归纳法假设知式 (9.6.21) 成立. 否则, 如果 $\beta_{k+1} \neq \beta_k$ , 则根据定义式 (9.6.16), 有

$$f _ {k + 1} \left(\beta_ {k + 1}\right) \geqslant (1 + \gamma) f _ {k + 1} \left(\beta_ {k}\right) \tag {9.6.24}$$

据此，式(9.6.23)及 $f(\beta_{k})\geqslant \delta$ 知

$$
\begin{array}{l} f \left(\beta_ {k + 1}\right) \geqslant f _ {k + 1} \left(\beta_ {k + 1}\right) - \gamma^ {2} \delta \\ \geqslant (1 + \gamma) f _ {k + 1} \left(\beta_ {k}\right) - \gamma^ {2} \delta \\ \geqslant (1 + \gamma) [ f (\beta_ {k}) - \gamma^ {2} \delta ] - \gamma^ {2} \delta \\ \geqslant [ (1 + \gamma) (1 - \gamma^ {2}) - \gamma^ {2} ] \delta \geqslant \delta , \tag {9.6.25} \\ \end{array}
$$

其中在最后一个不等式中利用了式 (9.6.15). 因此式 (9.6.21) 是正确的.

第四步：最后我们来证明定理9.6.1的正确性．我们首先证明极限 $\lim_{t\to \infty}f(\beta_t)$ $= f$ 存在且 $f > 0$ a.s..为此，我们仅需证明 $f(\beta_k)$ 对 $k\geqslant t_0$ 是递增的，而这又仅需考虑 $\beta_{k + 1}\neq \beta_k$ 的情形．当 $k\geqslant t_0$ 时，利用式(9.6.25）及式(9.6.21）知

$$
\begin{array}{l} f \left(\beta_ {k + 1}\right) \geqslant f \left(\beta_ {k}\right) + \gamma f \left(\beta_ {k}\right) - (1 + \gamma) \gamma^ {2} \delta - \gamma^ {2} \delta \\ \geqslant f \left(\beta_ {k}\right) + \delta \gamma [ 1 - 2 \gamma - \gamma^ {2} ] \\ \geqslant f (\beta_ {k}). \\ \end{array}
$$

进一步，由于 $f_{t}(x)$ 一致收敛于 $f(x)$ ，故有

$$\lim _ {t \rightarrow \infty} f _ {t + 1} (\beta_ {t}) = \lim _ {t \rightarrow \infty} f _ {t} (\beta_ {t}) = f > 0, \quad \text { a.s. }$$

该式与第一步中证明的结论相结合知定理的结论 (ii) 成立.

为了证明定理的第一个结论 (i)，我们只需证明对几乎所有的样本， $\beta_{t}$ 在有限步之后必是常数。我们采用反证法。如若不然，则根据定义式 (9.6.16)，不等式 (9.6.24) 就会对无穷多个 $k$ 成立。于是，令这样的 $k \to \infty$ ，则有

$$f \geqslant (1 + \gamma) f.$$

但这是不可能的，因为 $f > 0$ 故定理得证.

下面我们考虑自适应控制问题.

设 $\{\hat{\theta}_t\}$ 由式 (9.6.11) 给出，其中 $\beta_t$ 按式 (9.6.16) 选取。利用 $\hat{\theta}_t$ 可以用标准的方式构造下列估计多项式：

$$
\begin{array}{l} A _ {t} (z) = 1 + a _ {1} (t) z + \dots + a _ {n} (t) z ^ {n}, \\ D (z) = 1 + (t) - 2 \dots + (t) - 2. \end{array} \tag {9.6.26}
B _ {t} (z) = b _ {1} (t) z + \dots + b _ {n} (t) z ^ {n}.
$$

根据定理9.6.1知 $A_{t}(z)$ 与 $B_{t}(z)$ 一致互质，于是下列Diophantine方程：

$$A _ {t} (z) L _ {t} (z) + B _ {t} (z) R _ {t} (z) = A ^ {*} (z) \tag {9.6.27}$$

存在唯一的解 $L_{t}(z)$ 与 $R_{t}(z)$ , 其阶数均为 $(n - 1)$ , 且其系数是有界且收敛的. 进一步, 极点配置自适应控制律由下式产生:
