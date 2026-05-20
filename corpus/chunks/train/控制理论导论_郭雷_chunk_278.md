据上面定义，可测集对可列次交、并运算及取余集都封闭，并且Lebesgue测度 $\lambda$ 有以下性质：下面用 $A, A_{i}, i = 1,2,\dots$ ，等表示Lebesgue集.

(1) $\lambda(A) \geqslant 0$ ;   
(2) 如果 $A_{i}$ 互不相交，则 $\lambda\left(\bigcup_{i=1}^{\infty} A_{i}\right) = \sum_{i=1}^{\infty} \lambda(A_{i})$ .

有了可测集后，就可以定义可测函数。设 $f(\cdot)$ 定义在 $\mathbb{R}^1 \stackrel{\mathrm{def}}{=} (-\infty, \infty)$ 上。如果对任一Borel集 $B, \{x : f(x) \in B\}$ 为可测集，即

$$\{x: f (x) \in B \} \in \mathcal {L},$$

那么称 $f(\cdot)$ 为可测函数. 如果 $\{x : f(x) \in B\}$ 是 Borel 集, 即它属 $\mathcal{B}$ , 那么称 $f(\cdot)$ 为 Borel 函数. 这里 $\{x : f(x) \in B\} \in \mathcal{L}$ (或 $\mathcal{B}$ ) 等价于对任一实数 $a$ , $\{x : f(x) \leqslant a\} \in \mathcal{L}$ (或 $\mathcal{B}$ ).

设 $f(\cdot)$ 和 $g(\cdot)$ 为可测函数，如果 $\lambda(x: f(x) \neq g(x)) = 0$ ，则 $f(\cdot)$ 和 $g(\cdot)$ 属同一等价类，或叫 $f(\cdot)$ 和 $g(\cdot)$ 几乎处处相等，写作 $f(x) = g(x)$ a.e. 在以后的讨论中属同一等价类中的函数 $f(\cdot)$ 和 $g(\cdot)$ 将不作区分。例如，我们写 $f(\cdot) = 0$ ，实际上 $f(\cdot)$

可以在某一零测集上不等于0. 若除了一个零测集外，函数列 $f_{n}(\cdot)$ 收敛到 $f(\cdot)$ ，则称 $f_{n}(\cdot)$ 几乎处处收敛到 $f(\cdot)$ ，记作 $f_{n}(\cdot) \underset{n \to \infty}{\longrightarrow} f(\cdot)$ a.e.

对可测函数 $f(\cdot), \{x : f(x) > a\}$ 也是可测集：这因为 $\{x : f(x) > a\} = \{x : f(x) \leqslant a\}^c$ 。进而， $\{x : f(x) \geqslant a\}$ 也是可测集，这因为 $\{x : f(x) \geqslant a\} = \bigcap_{n=1}^{\infty} \left\{x : f(x) > a - \frac{1}{n}\right\}$ ，由此知 $\{x : f(x) = a\}$ 也是可测集。

由以上这些性质，可以推出可测函数集在算术运算及极限运算下是封闭的，也就是说若 $\{f_n(\cdot)\}$ 为可测函数列，则 $f_i(\cdot) \pm f_j(\cdot), f_i(\cdot)f_j(\cdot), f_i(\cdot)/f_j(\cdot) (f_j(\cdot) \neq 0)$ 都是可测函数，若 $f_n(x) \underset{n \to \infty}{\longrightarrow} f(x)$ a.e., 则 $f(\cdot)$ 也是可测函数.

除了几乎处处收敛外，依测度收敛是另一种重要的收敛形式，设 $\{f_n(\cdot)\}$ 是可测函数列，如果对任一 $\epsilon > 0$ 有 $\lim_{n \to \infty} \lambda\{x : |f_n(x) - f(x)| > \epsilon\} = 0$ ，则称 $f_n(\cdot)$ 依测度收敛到 $f(\cdot)$ .

设 $f_{n}(\cdot)$ 依测度收敛到 $f(\cdot)$ , 那么必可选子列 $\{f_{n_k}(\cdot)\}$ , 使

$$f _ {n _ {k}} (\cdot) \underset {k \rightarrow \infty} {\longrightarrow} f (\cdot) \quad \text { a.e. }$$

因此极限函数 $f(\cdot)$ 也是可测函数.

注意到分段常值函数是可测函数，而连续函数可用分段常值函数逼近 (a.e. 收敛)，所以连续函数一定是可测函数。这样，函数的概念从连续函数扩展到了可测函数。下面我们把 Riemann 积分扩展到对可测函数的 Lebesgue 积分。

设 $f(\cdot)$ 为定义在可测集 $C \subset (-\infty, +\infty)$ 上非负可测函数。 $f(\cdot)$ 的取值可能在 $[0, n]$ 上，也可能大于 $n$ 。把 $[0, n]$ 区间均分为 $n2^n$ 等份，每个小区间长度为 $2^{-n}$ 。因为 $f(\cdot)$ 为可测函数，所以
