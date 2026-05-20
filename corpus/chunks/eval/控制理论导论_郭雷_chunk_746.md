$$
\begin{array}{l} \left\| F _ {n} u - F u \right\| = \left\| \sum_ {k = 1} ^ {n} \sum_ {j = 1} ^ {m} \int_ {t _ {k - 1}} ^ {t _ {k}} \langle u (t), u _ {j} ^ {*} \rangle \left[ T \left(t _ {k}\right) b _ {j} - T (t) b _ {j} \right] d t \right\| \\ \leqslant \varepsilon \sum_ {j = 1} ^ {m} \| u _ {j} ^ {*} \| \int_ {0} ^ {t _ {f}} \| u (t) \| d t \\ = \varepsilon \sum_ {j = 1} ^ {m} \| u _ {j} ^ {*} \| \| u \| _ {L ^ {1} (0, t _ {f}; U)}. \\ \end{array}
$$

因此 $F$ 作为一紧线性算子序列的一致极限本身也是紧的.

现在设 $\{B_n\}$ 是一列有穷秩有界线性算子，使得 $\lim_{n\to \infty}\| B_n - B\| = 0.$ 今定义算子 $\Lambda_{n}:L^{1}(0,t_{f};U)\to X$ 如下：

$$\Lambda_ {n} u = \int_ {0} ^ {t _ {f}} T (t) B _ {n} u (t) \mathrm{d} t.$$

依上述， $\Lambda_{n}$ 是紧算子。我们证明 $\Lambda_{n}$ 当 $n \to \infty$ 时按一致算子拓扑收敛于 $\Lambda$ 。事实上，对于 $u \in L^{1}(0, t_{f}; U)$ ，我们有

$$
\begin{array}{l} \left\| \Lambda_ {n} u - \Lambda u \right\| \leqslant \int_ {0} ^ {t _ {f}} \| T (t) (B _ {n} - B) u (t) \| d t \\ \leqslant \left\| B _ {n} - B \right\| \sup _ {0 \leqslant t \leqslant t _ {f}} \| T (t) \| \int_ {0} ^ {t _ {f}} \| u (t) \| \mathrm{d} t, \\ \end{array}
$$

即

$$\left\| \Lambda_ {n} - \Lambda \right\| \leqslant \left\| B _ {n} - B \right\| \sup _ {0 \leqslant t \leqslant t _ {f}} \| T (t) \|.$$

于是当 $n \to \infty$ 时 $\| \Lambda_n - \Lambda \| \to 0$ , 从而 $\Lambda$ 是紧算子.

因此在无穷维系统情形，有必要提出较弱的能控性定义.

定义 10.2.1 我们说系统 (10.2.1) 在有穷时间区间 $[0, t_f]$ 上是精确能控的，或简称 $(A, B)$ 在 $[0, t_f]$ 上是精确能控的，是指对于任意 $x, y \in X$ ，存在一控制 $u \in L^p(0, t_f; U)$ ( $p \geqslant 1$ 为…固定数)，使得

$$y = T (t _ {f}) x + \int_ {0} ^ {t _ {f}} T (t _ {f} - s) B u (s) \mathrm{d} s.$$

定义10.2.2 我们说系统(10.2.1)在有穷时间区间 $[0, t_f]$ 上是精确零能控的，或简称 $(A, B)$ 在 $[0, t_f]$ 上是精确零能控的，是指对于任意状态 $x \in X$ ，存在控制 $u \in L^p(0, t_f; U) (p \geqslant 1$ 为某固定数)，使得

$$0 = T (t _ {f}) x + \int_ {0} ^ {t _ {f}} T (t _ {f} - s) B u (s) d s.$$

定义 10.2.3 我们说系统 (10.2.1) 在有穷时间区间 $[0, t_f]$ 上是近似能控的，或简称 $(A, B)$ 在 $[0, t_f]$ 上是近似能控的，是指对于任意状态 $x \in X$ 和任意小数 $\varepsilon > 0$ ，存在控制 $u \in L^p(0, t_f; U)$ ( $p \geqslant 1$ 为某固定数)，使得

$$\left\| x - \int_ {0} ^ {t _ {f}} T (t _ {f} - s) B u (s) \mathrm{d} s \right\| < \varepsilon .$$

定义10.2.4 我们说系统(10.2.1)在有穷时间区间 $[0, t_f]$ 上是近似零能控的，或简称 $(A, B)$ 在 $[0, t_f]$ 上是近似零能控的，是指对于任意状态 $x \in X$ 和任意小数 $\varepsilon > 0$ ，存在一控制 $u \in L^p(0, t_f; U)$ ( $p \geqslant 1$ 为某固定数)，使得

$$\left\| T (t _ {f}) x + \int_ {0} ^ {t _ {f}} T (t _ {f} - s) B u (s) \mathrm{d} s \right\| < \varepsilon .$$

从定义 10.2.1\~10.2.4 我们看到，如果定义线性算子 $G(t_{f}):L^{p}(0,t_{f};U)\to X$ ,
