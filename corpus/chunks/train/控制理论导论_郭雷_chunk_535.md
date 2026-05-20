$$u (t) = - \frac {\sum_ {i = 1} ^ {n} \psi_ {i} (t) \Phi_ {3 i} (x (t))}{\sum_ {i = 1} ^ {n} \psi_ {i} (t) \Psi_ {3 i} (x (t))};$$

而若 $\sum_{i=1}^{n} \psi_i(t) \Psi_{3i}(x(t)) = 0, \forall t \in [t_1, t_2]$ , 则又可对式 (7.2.52) 两端求导。这一过程可继续进行下去。一般说来，当快速控制存在时，必定有 $m$ , 使得 $l = m + 1$ 时

$$\sum_ {i = 1} ^ {n} \psi_ {i} (t) \Phi_ {(m + 1) i} (x (t)) + u (t) \sum_ {i = 1} ^ {n} \psi_ {i} (t) \Psi_ {(m + 1) i} (x (t)) = 0, \quad \forall t \in [ t _ {1}, t _ {2} ],$$

并且 $\sum_{i=1}^{n} \psi_i(t) \Psi_{(m+1)i}(x(t)) \neq 0$ . 由此求得 $u(t)$ 为

$$u (t) = - \frac {\sum_ {i = 1} ^ {n} \psi_ {i} (t) \Phi_ {(m + 1) i} (x (t))}{\sum_ {i = 1} ^ {n} \psi_ {i} (t) \Psi_ {(m + 1) i} (x (t))}, \tag {7.2.53}$$

并且

$$\left| \frac {\sum_ {i = 1} ^ {n} \psi_ {i} (t) \Phi_ {(m + 1) i} (x (t))}{\sum_ {i = 1} ^ {n} \psi_ {i} (t) \Psi_ {(m + 1) i} (x (t))} \right| \leqslant 1. \tag {7.2.54}$$

于是，奇异快速控制 $u(t)$ ，奇异快速轨线 $x(t)$ 和 $\psi(t)$ 在奇异区间 $[t_1, t_2]$ 上满足

$$
\left\{ \begin{array}{l} \sum_ {i = 1} ^ {n} \psi_ {i} (t) f _ {i} (x (t)) = 1, \\ \sum_ {i = 1} ^ {n} \psi_ {i} (t) b _ {i} (x (t)) = 0, \\ \sum_ {i = 1} ^ {n} \psi_ {i} (t) \Phi_ {1 i} (x (t)) = 0, \\ \vdots \\ \sum_ {i = 1} ^ {n} \psi_ {i} (t) \Phi_ {m i} (x (t)) = 0. \end{array} \right. \tag {7.2.55}
$$

注意方程 (7.2.55) 是奇异快速控制和奇异快速轨线满足的必要条件。当求解奇异快速问题时，应考察下列方程组：

$$
\left\{ \begin{array}{l} \sum_ {i = 1} ^ {n} \psi_ {i} f _ {i} (x) = 1, \\ \sum_ {i = 1} ^ {n} \psi_ {i} b _ {i} (x) = 0, \\ \sum_ {i = 1} ^ {n} \psi_ {i} \Phi_ {1 i} (x) = 0, \\ \vdots \\ \sum_ {i = 1} ^ {n} \psi_ {i} \Phi_ {m i} (x) = 0. \end{array} \right. \tag {7.2.56}
$$

方程组 (7.2.56) 是关于 $\psi_1, \psi_2, \cdots, \psi_n$ 的线性方程组。易知，当 $1 \leqslant m \leqslant n - 2$ 时，从方程组 (7.2.56) 有可能解得一组或多组依赖于 $x$ 的 $\psi_1(x), \psi_2(x), \cdots, \psi_n(x)$ 。因此当快速控制存在时，应有 $1 \leqslant m \leqslant n - 2$ 。

综上所述，关系式 (7.2.53)，(7.2.54) 和 (7.2.55) 组成了在奇异区间 $[t_1, t_2] \subset [t_0, t_f]$ 上由最大值原理导出的奇异快速控制满足的必要条件。只要关系式 (7.2.53)，(7.2.54) 和 (7.2.55) 中有一个不满足，奇异快速控制一定不存在。关系式 (7.2.53)，(7.2.54) 和 (7.2.55) 确定出的控制 $u(t)$ 称为奇异极值控制，关系式 (7.2.39) 相应于 $u(t)$ 的轨线称为奇异极值轨线。这里不再详述如何从这组必要条件中具体求得奇异极值控制和奇异极值轨线的过程。
