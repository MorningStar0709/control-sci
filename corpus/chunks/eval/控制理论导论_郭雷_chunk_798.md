从式 (10.4.34), (10.4.43), (10.4.53), 并利用 Cauchy 不等式, 得到

$$
\begin{array}{l} K q \left| w _ {n} ^ {\prime} \right| ^ {2} (x) + E I q \left| \varphi_ {n} ^ {\prime} \right| ^ {2} (x) + \rho q \omega_ {n} ^ {2} \left| u _ {n} \right| ^ {2} (x) + \left(I _ {\rho} \omega_ {n} ^ {2} - K\right) q \left| \varphi_ {n} \right| ^ {2} (x) \\ \leqslant 2 \varepsilon \left(\left| \omega_ {n} w _ {n} (x) \right| ^ {2} + \left| \omega_ {n} \varphi_ {n} (x) \right| ^ {2}\right) + C _ {\varepsilon}, \tag {10.4.54} \\ \end{array}
$$

这表明 $w_{n}^{\prime}(x)$ 和 $\varphi_n^\prime (x)$ 在 $[0,\ell ]$ 上一致有界，并且

$$\lim _ {n \rightarrow \infty} w _ {n} (x) = 0, \quad \lim _ {n \rightarrow \infty} \varphi_ {n} (x) = 0.$$

于是利用Cauchy不等式，我们得到

$$\lim _ {n \rightarrow \infty} P _ {n} = 0, \quad \lim _ {n \rightarrow \infty} Q _ {n} = 0. \tag {10.4.55}$$

现在若在式 (10.4.47) 中取 $q = \mathrm{e}^{m_1x}$ , 其中

$$m _ {1} = \max _ {x \in [ 0, \ell ]} \left\{\frac {K ^ {\prime}}{K}, \frac {E I ^ {\prime}}{E I}, - \frac {\rho^ {\prime}}{\rho}, - \frac {I _ {\rho} ^ {\prime}}{I _ {\rho}} \right\} + 1.$$

则可得当 $n$ 充分大时 $I_{n}(x) > 0$ . 因此, 若在式 (10.4.47) 中取 $\alpha = c, \beta = d$ , 并把式 (10.4.42) 和式 (10.4.55) 代入式 (10.4.47), 则我们得到

$$
\begin{array}{l} 2 \mathrm{e} ^ {m _ {1} \ell} \liminf _ {n \to \infty} \left(\int_ {c} ^ {d} \rho | \omega_ {n} w _ {n} | ^ {2} \mathrm{d} x + \int_ {c} ^ {d} (I _ {\rho} - K \omega_ {n} ^ {- 2}) | \omega_ {n} \varphi_ {n} | ^ {2} \mathrm{d} x\right) \\ \geqslant (d - c) \liminf _ {n \rightarrow \infty} (K (0) | w _ {n} ^ {\prime} (0) | ^ {2} + E I (0) | \varphi_ {n} ^ {\prime} (0) | ^ {2}). \\ \end{array}
$$

最后，由于 $\lim_{n\to \infty}\| \tilde{Y}_n\|_{\mathcal{H}} = 0,$ 可知存在常数 $\delta >0$ 使得

$$\liminf _ {n \to \infty} \int_ {0} ^ {f} (\rho b _ {1} | z _ {n} | ^ {2} + I _ {\rho} b _ {2} | \psi_ {n} | ^ {2}) \mathrm{d} x \geqslant \delta .$$

这与式 (10.4.30) 矛盾. 这样我们证明了所讨论的闭环 Timoshenko 梁系统能量是指数衰减的.
