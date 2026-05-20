$$\phi (X _ {1}, \dots , X _ {r}, \omega_ {1}, \dots , \omega_ {s}) = \omega_ {s} \otimes \dots \otimes \omega_ {1} \otimes \Gamma \otimes X _ {1} \otimes \dots \otimes X _ {r}. \tag {3.10.2}$$

定义3.10.2 设 $\phi \in T_s^r(V)$ 及 $\psi \in T_q^p(V)$ , 那么它们的张量积 $\phi \otimes \psi \in T_{s+q}^{r+p}(V)$ 定义作

$$
\begin{array}{l} \phi \otimes \psi (X _ {1}, \dots , X _ {r + p}, \omega_ {1}, \dots , \omega_ {s + q}) \\ = \phi (X _ {1}, \dots , X _ {r}, \omega_ {1}, \dots , \omega_ {s}) \psi (X _ {r + 1}, \dots , X _ {r + p}, \omega_ {s + 1}, \dots , \omega_ {s + q}). \\ \end{array}
$$

张量积的结构矩阵是结构矩阵的张量积. 我们将它叙述为一个命题. 证明留给读者.

命题3.10.1 设 $\phi$ 和 $\psi$ 为 $V$ 上的两个张量，其结构矩阵分别为 $M_{\phi}$ 及 $M_{\psi}$ . 那么 $\phi \otimes \psi$ 的结构矩阵为

$$M _ {\phi \otimes \psi} = M _ {\phi} \otimes M _ {\psi}. \tag {3.10.3}$$

协变阶 $r = 0$ 及逆变阶 $s = 0$ 是两个重要的特殊情况。我们简单地将它们分别记为 $\mathcal{T}^r (V)$ 及 $\mathcal{T}_s(V)$ 。下面进一步考虑 $\mathcal{T}^r (V)$ 。

定义3.10.3 $\phi \in T^r (V)$ 称为一个对称协变张量，如果它满足

$$\phi (X _ {1}, \dots , X _ {i}, \dots , X _ {j}, \dots , X _ {r}) = \phi (X _ {1}, \dots , X _ {j}, \dots , X _ {i}, \dots , X _ {r}), \quad \forall X _ {t} \in V.$$

$\phi$ 称为一个反对称协变张量，如果它满足

$$\phi (X _ {1}, \dots , X _ {i}, \dots , X _ {j}, \dots , X _ {r}) = - \phi (X _ {1}, \dots , X _ {j}, \dots , X _ {i}, \dots , X _ {r}), \quad \forall X _ {t} \in V.$$

记 $S^k (V)\subset T^k (V)$ 为 $\pmb{k}$ 阶对称协变张量集合，而 $\Omega^k (V)\subset T^k (V)$ 为 $\pmb{k}$ 阶反对称协变张量集合．我们先研究反对称情况．有

$$\Omega^ {k} (V) = \{0 \}, \quad k > n.$$

要证明这一点，考察一个反对称张量 $\phi$ 。如果 $X_{i} = X_{j}$ 那么

$$
\begin{array}{l} \phi (X _ {1}, \dots , X _ {i}, \dots , X _ {j}, \dots , X _ {r}) = - \phi (X _ {1}, \dots , X _ {j}, \dots , X _ {i}, \dots , X _ {r}) \\ = - \phi (X _ {1}, \dots , X _ {i}, \dots , X _ {j}, \dots , X _ {r}). \\ \end{array}
$$

因此它是零. 现在如果 $r > n$ , 设 $X_{i}$ 由基底 $\{e_1, \cdots, e_n\}$ 中选出, 显然 $\phi(e_{i_1}, \cdots, e_{i_r}) = 0$ . 由多线性性, $\phi(X_1, \cdots, X_r)$ 是基底项 $\phi(e_{i_1}, \cdots, e_{i_r})$ 的线性组合, 因此它是零. 于是我们得到

$$\Omega (V) = \Omega^ {0} (V) \oplus \Omega^ {1} (V) \oplus \dots \oplus \Omega^ {n} (V).$$

它是反对称张量空间，这里 $\Omega^0 (V)\stackrel {\mathrm{def}}{=}R.$

定义 3.10.4 对称映射 $\mathcal{P}: T^{r}(V) \to S^{r}(V)$ 定义为

$$\mathcal {P} (\phi) (X _ {1}, \dots , X _ {r}) = \frac {1}{r !} \sum_ {\sigma \in S _ {r}} (X _ {\sigma (1)}, \dots , X _ {\sigma (r)}).$$

反对称映射 $\mathcal{A}:\mathcal{T}^r (V)\to \Omega^r (V)$ 定义为
