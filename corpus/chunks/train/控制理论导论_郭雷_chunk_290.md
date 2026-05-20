$$
\begin{array}{l} F _ {\xi} \left(x ^ {\prime}\right) \leqslant F _ {\xi_ {k}} (x) + P \left[ \left| \xi_ {k} - \xi \right| \geqslant x - x ^ {\prime} \right], \\ F _ {\xi} (x ^ {\prime}) \leqslant \liminf _ {k \to \infty} F _ {\xi_ {k}} (x), \quad x ^ {\prime} <   x. \\ \end{array}
$$

类似地，有对 $x'' > x$

$$[ \xi_ {k} < x ] \subset [ \xi < x ^ {\prime \prime} ] \cup [ \xi \geqslant x ^ {\prime \prime}, \xi_ {k} < x ],F _ {\xi_ {k}} (x) \leqslant F _ {\xi} (x ^ {\prime \prime}) + P [ | \xi_ {k} - \xi | > x ^ {\prime \prime} - x ].$$

所以

$$\limsup _ {k \to \infty} F _ {\xi_ {k}} (x) \leqslant F _ {\xi} (x ^ {\prime \prime}).$$

因此

$$F _ {\xi} (x ^ {\prime}) \leqslant \liminf _ {k \to \infty} F _ {\xi_ {k}} (x) \leqslant \limsup _ {k \to \infty} F _ {\xi_ {k}} (x) \leqslant F _ {\xi} (x ^ {\prime \prime}).$$

令 $x^{\prime} \uparrow x, x^{\prime \prime} \downarrow x,$ 由于 $x$ 是 $F_{\xi}(\cdot)$ 的连续点，所以

$$\lim _ {k \rightarrow \infty} F _ {\xi_ {k}} (x) = F _ {\xi} (x),$$

也就是 $\xi_{k}\xrightarrow[k\to\infty]{w}\xi.$

收敛性之间的关系可总结成下面定理：

定理 4.1.4 成立如下包含关系:

$$\xi_ {k} \underset {k \rightarrow \infty} {\longrightarrow} \xi \text { a.s. } \Rightarrow \xi_ {k} \underset {k \rightarrow \infty} {\overset {P} {\longrightarrow}} \xi ,E \left| \xi_ {k} - \xi \right| ^ {p} \underset {k \rightarrow \infty} {\longrightarrow} 0, p > 0 \Rightarrow \xi_ {k} \underset {k \rightarrow \infty} {\overset {P} {\longrightarrow}} \xi ,\xi_ {k} \xrightarrow [ k \to \infty ]{P} \xi \Rightarrow \xi_ {k} \xrightarrow {w} \xi .$$

现在来看取极限和求期望的交换问题.

单调收敛定理 设 $0 \leqslant \xi_k \uparrow \xi$ , 那么 $E\xi_k \uparrow E\xi$ , 这里 $\uparrow$ 表示单调上升地收敛.

推论 4.1.1 当 $P(A_{k}) \rightarrow 0$ 时 $\int_{A_{k}} |\xi| dP \xrightarrow{k \to \infty} 0$ .

Fatou 引理 设 $E|\eta| < \infty, E|\zeta| < \infty$ . 当 $\eta \leqslant \xi_n$ (或 $\xi_n \leqslant \zeta$ ) 时,

$$E \lim _ {k \to \infty} \inf \xi_ {k} \leqslant \lim _ {k \to \infty} \inf E \xi_ {k} (\text {或} \lim _ {k \to \infty} \sup E \xi_ {k} \leqslant E \lim _ {k \to \infty} \sup \xi_ {k}).$$

如果 $\eta \leqslant \xi_k \uparrow \xi$ , 或 $\eta \leqslant \xi_k \leqslant \zeta$ 且 $\xi_k \underset{k \to \infty}{\longrightarrow} \xi$ a.s., 那么

$$E \xi_ {k} \rightarrow E \xi .$$

控制收敛定理 设 $|\xi_k| \leqslant \eta$ a.s., $E|\eta| < \infty$ , 且 $\xi_k \xrightarrow[k \to \infty]{P} \xi$ , 则 $E\xi_k \xrightarrow[k \to \infty]{\longrightarrow} E\xi, E|\xi_k - \xi|$ $\xrightarrow[k \to \infty]{0}$ .
