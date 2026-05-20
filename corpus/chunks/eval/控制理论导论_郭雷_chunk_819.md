证明 首先根据定理 10.6.1, 10.6.4, $A - BR^{-1}B^{*}P(t)$ 生成 $X$ 中一温和发展算子 $S(s,t)$ . 于是从式 (10.6.1) 和式 (10.6.7) 得到 $x^{0}(s;t,x) = S(s,t)x$ . 因此对于任意 $x,y \in H$ , 利用式 (10.6.16), $(P(t)x,y)$ 可以写成

$$
\begin{array}{l} (P (t) x, y) = \left(G x ^ {0} \left(t _ {1}; t, x\right), x ^ {0} \left(t _ {1}; t, y\right)\right) + \int_ {t} ^ {t _ {1}} \left(Q x ^ {0} (s; t, x), x ^ {0} (s; t, y)\right) d s \\ + \int_ {t} ^ {t _ {1}} \left(P (s) B R ^ {- 1} B ^ {*} P (s) x ^ {0} (s; t, x), x ^ {0} (s; t, y)\right) d s \\ = \left(S ^ {*} (t _ {1}, t) G S (t _ {1}, t) x, y\right) + \int_ {t} ^ {t _ {1}} \left(S ^ {*} (s, t) Q S (s, t) x, y\right) d s \\ + \int_ {t} ^ {t _ {1}} (S ^ {*} (s, t) P (s) B R ^ {- 1} B ^ {*} P (s) S (s, t) x, y) d s. \\ \end{array}
$$

于是 $P(t)$ 满足方程

$$
\begin{array}{l} P (t) x = S ^ {*} \left(t _ {1}, t\right) G S \left(t _ {1}, t\right) x + \int_ {t} ^ {t _ {1}} S ^ {*} (s, t) Q S (s, t) x d s \\ + \int_ {t} ^ {t _ {1}} S ^ {*} (s, t) P (s) B R ^ {- 1} B ^ {*} P (s) S (s, t) x d s. \tag {10.6.19} \\ \end{array}
$$

注意到 $A - BR^{-1}B^{*}P(t)$ 是闭算子，利用等式

$$\frac {\partial}{\partial t} S (s, t) x = - S (s, t) \left(A - B R ^ {- 1} B ^ {*} P (t)\right) x, \quad \forall x \in \mathcal {D} (A),$$

(见定理 10.6.2) 我们可以推出

$$\frac {\mathrm{d}}{\mathrm{d} t} (P (t) x, y) = - \left(A - B R ^ {- 1} B ^ {*} P (t) x, P (t) y\right)- \left(P (t) x, A - B R ^ {- 1} B ^ {*} P (t) y\right) - (Q x, y) - \left(B R ^ {- 1} B ^ {*} P (t) x, P (t) y\right)= - (Q x, y) - (A x, P (t) y) - (P (t) x, A y) + \left(P (t) B R ^ {- 1} B ^ {*} P (t) x, y\right),$$

这里微分的合法性是很容易验证的。这样我们就证明了方程 (10.6.18).

现在我们证明方程 (10.6.18) 解的唯一性。事实上，如果方程 (10.6.18) 有两个解 $P_{1}(t)$ 和 $P_{2}(t)$ ，并令 $P(t) = P_{1}(t) - P_{2}(t)$ ，则对于任意 $x, y \in \mathcal{D}(A)$ ，有

$$
\left\{ \begin{array}{l} \frac {\mathrm{d}}{\mathrm{d} t} (P (t) x, y) = - ((A - K P _ {1} (t)) x, P (t) y) \\ - (P (t) x, (A - K P _ {1} (t)) y) - (P (t) K P (t) x, y), \\ P (t _ {1}) = 0. \end{array} \right. \tag {10.6.20}
$$

现在我们证明 $P(t) \equiv 0$ . 为此对于任意 $t \geqslant s$ , 记

$$V (t) = T ^ {*} (t - s) P (t) T (t - s).$$

于是对于任意 $x, y \in \mathcal{D}(A), (V(t)x, y)$ 对 $t$ 可微，并且满足

$$
\begin{array}{l} \frac {\mathrm{d}}{\mathrm{d} t} (V (t) x, y) = (P (t) T (t - s) x, K P _ {1} (t) T (t - s) y) \\ + (K P _ {1} (t) T (t - s) x, P (t) T (t - s) y) \\ - (P (t) K P (t) T (t - s) x, T (t - s) y). \\ \end{array}
$$

因此，由于 $\overline{\mathcal{D}(A)} = H$ ，对于所有 $x\in H$ ，有

$$
\begin{array}{l} (T ^ {*} (t - s) P (t) T (t - s) x, x) \\ \leqslant - \int_ {t} ^ {t _ {1}} \left((P _ {1} (\tau) K P (\tau) + P (\tau) K P _ {1} (\tau)) T (\tau - s) x, T (\tau - s) x\right) d \tau . \\ \end{array}
$$

在上式中让 $s \uparrow t$ , 得到

$$(P (t) x, x) \leqslant - \int_ {t} ^ {t _ {1}} \left((P _ {1} (\tau) K P (\tau) + P (\tau) K P _ {1} (\tau)) T (\tau - t) x, T (\tau - t) x\right) d \tau .$$

由于 $P(t)$ 是自伴的，我们有

$$\| P (t) \| = \sup _ {\| x \| = 1} | (P (t) x, x) | \leqslant C \int_ {t} ^ {t _ {1}} \| P (\tau) \| \mathrm{d} \tau ,$$

其中 $C$ 为某个正常数。这样根据 Gronwall 不等式， $P(t) \equiv 0$ 。证毕。
