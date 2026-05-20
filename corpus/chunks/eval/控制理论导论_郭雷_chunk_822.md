$$
\begin{array}{l} \lim _ {n \rightarrow \infty} \left[ (Q x _ {n} (t), x _ {n} (t)) + \left(R ^ {- 1} B ^ {*} P _ {n} (t) x _ {n} (t), B ^ {*} P _ {n} (t) x _ {n} (t)\right)\right. \\ = (Q x (t), x (t)) + \left(R ^ {- 1} B ^ {*} P (t) x (t), B ^ {*} P (t) x (t)\right). \\ \end{array}
$$

由此利用Lebesgue控制收敛定理可以证明

$$
\begin{array}{l} \lim _ {n \rightarrow \infty} \int_ {0} ^ {t} \left((Q + P _ {n} (s) B R ^ {- 1} B ^ {*} P _ {n} (s)) x _ {n} (s), x _ {n} (s)\right) d s \\ = \int_ {0} ^ {t} \left((Q + P B R ^ {- 1} B ^ {*} P) x (s), x (s)\right) \mathrm{d} s, \quad \forall t \in \mathbb {R} ^ {+}. \tag {10.6.29} \\ \end{array}
$$

利用引理 10.6.3 和方程 (10.6.29), 我们有

$$
\begin{array}{l} (P x _ {0}, x _ {0}) = \lim _ {n \rightarrow \infty} (P _ {n} (0) x _ {0}, x _ {n} (0)) = \lim _ {n \rightarrow \infty} m (t _ {n}, x _ {0}) \\ \geqslant \lim _ {t \rightarrow \infty} \int_ {0} ^ {t} \left((Q + P B R ^ {- 1} B ^ {*} P) x (s), x (s)\right) \mathrm{d} s. \tag {10.6.30} \\ \end{array}
$$

如果在式 (10.6.30) 中严格不等号成立，则必存在一自然数 $n$ 使得

$$m (t _ {n}, x _ {0}) > \int_ {0} ^ {t _ {n}} \left((Q + P B R ^ {- 1} B ^ {*} P) x (s), x (s)\right) d s.$$

设 $\bar{u}(t) = -R^{-1}B^{*}Px(t)$ ，则从式(10.6.24)得到

$$\boldsymbol {x} (t) = T (t) \boldsymbol {x} _ {0} + \int_ {0} ^ {t} T (t - s) B \bar {u} (s) d s.$$

因此

$$J (\bar {u}; 0, t _ {n}, x _ {0}) = \min \left\{J (\bar {u}; 0, t _ {n}, x _ {0}) \mid u \in L ^ {2} (t _ {0}, t _ {1}; U) \right\}.$$

但这是不可能的．从而在式(10.6.30)中等号成立.

(4) 是 (3) 的直接结果，这是因为如果存在 $\bar{u}$ 使得 $J(\bar{u}, x_0) < (Px_0, x_0)$ ，则对于某个 $n$ ，必成立

$$J (\bar {u}; 0, t _ {n}, x _ {0}) \leqslant J (\bar {u}, x _ {0}) < (P _ {n} (0) x _ {0}, x _ {0}) = m (t _ {n}, x _ {0}),$$

但这显然是不可能的，证毕.

推论 10.6.1 假定 $Q \in \mathcal{L}(H)$ 是正定的，并且假设 A 成立。那么由 $A - BR^{-1}B^{*}P$ 生成的 $C_{0}$ 半群 $S(t)$ 是指数稳定的。

证明 由于 $Q$ 是正定的，故存在两正常数 $\mu_7$ 和 $\mu_8$ 使得

$$\mu_ {7} \| x \| ^ {2} \leqslant \left((Q + P B R ^ {- 1} B ^ {*} P) x, x\right) \leqslant \mu_ {8} \| x \| ^ {2}, \quad \forall x \in H.$$

由于 $S(t)x_0 = x(t,x_0)$ ，从定理10.6.6可得

$$\int_ {0} ^ {\infty} \| S (t) x _ {0} \| ^ {2} \mathrm{d} t < \infty , \quad \forall x _ {0} \in H.$$

根据定理 10.1.1, 这蕴含 $S(t)$ 指数稳定. 证毕.

推论10.6.2 假定 $Q \in \mathcal{L}(H)$ 是正定的，并且假设 $A$ 成立。如果 $x_0 \in \mathcal{D}(A)$ ，则关于性能指标 $J(\cdot, x_0)$ 的最优轨线 $x^0(t, x_0)$ 是可微的，并且满足微分方程

$$\frac {\mathrm{d} x ^ {0} (t , x _ {0})}{\mathrm{d} t} = (A - B R ^ {- 1} B ^ {*} P) x ^ {0} (t, x _ {0}).$$

分布参数系统控制涉及的内容和知识相当广泛。本章仅仅介绍了最基本的内容。即使这样，要在这样不大的篇幅里，作出这方面内容的取舍也是相当困难的，肯定会是挂一漏万。一些重要的问题，例如最优控制，无穷维随机系统控制，无穷维非线性系统控制，以及在一定程度上能刻划边界控制的适定线性系统控制等问题，我们基本上都没有涉及或者很少涉及。特别是有关分布参数系统的最优控制，读者可参考专著[26]。当然，我们希望，读者在掌握了本章的大部分内容以后，能够更方便更快地进入新内容的学习和新问题的研究。
