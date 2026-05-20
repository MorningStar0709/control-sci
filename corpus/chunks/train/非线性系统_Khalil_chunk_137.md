下面的逆李雅普诺夫定理(定理4.16和定理4.17)是定理4.14在不同方向的扩展,但其证明比较复杂。定理4.16适用于一致渐近稳定性的更一般情况①,定理4.17适用于自治系统,并产生了定义在整个吸引区的李雅普诺夫函数。

定理4.16 设 $x = 0$ 是非线性系统 $\dot{x} = f(t,x)$

的平衡点, 其中 $f: [0, \infty) \times D \to R^{n}$ 连续可微, $D = \{x \in R^{n} \mid \| x \| < r\}$ , 雅可比矩阵 $[\partial f / \partial x]$ 在 D 上有界, 且对 t 一致。设 $\beta$ 是 KL 类函数, 且 $r_{0}$ 是正常数, 满足 $\beta(r_{0}, 0) < r_{0}$ 。设 $D_{0} = \{x \in R^{n} \mid \| x \| < r_{0}\}$ 。假设系统的轨线满足

$$\| x (t) \| \leqslant \beta (\| x (t _ {0}) \|, t - t _ {0}), \forall x (t _ {0}) \in D _ {0}, \forall t \geqslant t _ {0} \geqslant 0$$

则存在一个连续可微函数 $V: [0, \infty) \times D \to R$ ，满足不等式

$$
\begin{array}{l} \alpha_ {1} (\| x \|) \leqslant V (t, x) \leqslant \alpha_ {2} (\| x \|) \\ \frac {\partial V}{\partial t} + \frac {\partial V}{\partial x} f (t, x) \leqslant - \alpha_ {3} (\| x \|) \\ \left\| \frac {\partial V}{\partial x} \right\| \leqslant \alpha_ {4} (\| x \|) \\ \end{array}
$$

其中， $\alpha_{1},\alpha_{2},\alpha_{3}$ 和 $\alpha_{4}$ 是定义在 $[0,r_{0}]$ 上的 K 类函数。如果系统是自治的，则可以选择 V 与 t 无关。

证明: 见附录 C.7。

定理4.17 设 $x = 0$ 是非线性系统 $\dot{x} = f(x)$

的渐近稳定平衡点,其中 $f: D \rightarrow R^{n}$ 是局部利普希茨的,且 $D \subset R^{n}$ 是包含原点的定义域。设 $R_{A} \subset D$ 是 x = 0 的吸引区。那么,对于所有 $x \in R_{A}$ ,存在一个光滑的正定函数 $V(x)$ 和一个连续的正定函数 $W(x)$ ,使

$$
\begin{array}{l} V (x) \to \infty \qquad \text {当} x \to \partial R _ {A} \\ \frac {\partial V}{\partial x} f (x) \leqslant - W (x), \quad \forall x \in R _ {A} \\ \end{array}
$$

且对于任意 $c > 0, \{V(x) \leqslant c\}$ 是 $R_A$ 的一个紧子集。当 $R_A = R^n$ 时 $V(x)$ 径向有界。

证明: 见附录 C.8。

定理4.17的一个令人感兴趣的特性是，对于某个常数 $c > 0$ ，吸引区的任何有界子集 $S$ 都包含于 $\{V(x)\leqslant c\}$ 内。这一特性很有用，因为我们常常把分析局限于正的不变紧集 $\{V(x)\leqslant c\}$ 内。有了 $S\subset \{V(x)\leqslant c\}$ 的特性，则分析在整个 $S$ 集内都有效。另一方面，如果仅知道在 $S$ 上存在李雅普诺夫函数 $V_{1}(x)$ ，就必须选择一个常数 $c_{1}$ ，使 $\{V_{1}(x)\leqslant c_{1}\}$ 为紧集，且包含于 $S$ 内。于是，分析就限制在 $\{V_{1}(x)\leqslant c_{1}\}$ 内，它只是 $S$ 的子集。
