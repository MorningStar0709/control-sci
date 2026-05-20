# C. 6 证明引理 4.5

一致稳定性: 假设存在一个K类函数 $\alpha$ , 满足

$$\| x (t) \| \leqslant \alpha (\| x (t _ {0}) \|), \forall t \geqslant t _ {0} \geqslant 0, \forall \| x (t _ {0}) \| < c$$

给定 $\varepsilon > 0$ ，设 $\delta = \min \{c, \alpha^{-1}(\varepsilon)\}$ ，则对于 $\|x(t_0) \| < \delta$ ，有

$$\| x (t) \| \leqslant \alpha (\| x (t _ {0}) \|) < \alpha (\delta) \leqslant \alpha (\alpha^ {- 1} (\varepsilon)) = \varepsilon$$

现在假设给定 $\varepsilon > 0$ ，存在 $\delta = \delta(\varepsilon) > 0$ ，使得

$$\| x (t _ {0}) \| < \delta \Rightarrow \| x (t) \| < \varepsilon , \forall t \geqslant t _ {0}$$

对于固定的 $\varepsilon$ ，设 $\bar{\delta}(\varepsilon)$ 是所有适用的 $\delta(\varepsilon)$ 的上确界，函数 $\bar{\delta}(\varepsilon)$ 为正且非减，但不必连续。选择一个 $\mathcal{K}$ 类函数 $\zeta(r)$ ，满足 $\zeta(r) \leqslant k\,\bar{\delta}(r), 0 < k < 1$ 。设 $\alpha(r) = \zeta^{-1}(r)$ ，则 $\alpha(r)$ 是 $\mathcal{K}$ 类函数。设 $c = \lim_{r \to \infty} \zeta(r)$ ，给定 $x(t_0)$ ，且 $\|x(t_0)\| < c$ ，又设 $\varepsilon = \alpha(\|x(t_0)\|)$ ，则 $\|x(t_0)\| < \bar{\delta}(\varepsilon)$ ，且

$$\| x (t) \| < \varepsilon = \alpha (\| x \left(t _ {0}\right) \|) \tag {C.7}$$

一致渐近稳定性: 假设存在一个KL类函数 $\beta(r,s)$ ，使式(4.20)成立，则

$$\| x (t) \| \leqslant \beta (\| x (t _ {0}) \|, 0)$$

说明 $x = 0$ 是一致稳定的。而且，对于 $\| x(t_0)\| < c$ ，其解满足

$$\| x (t) \| \leqslant \beta (c, t - t _ {0})$$

上式说明当 $t$ 趋于无穷时， $x(t)$ 趋于零，且对于 $t_0$ 是一致的。现在假设 $x = 0$ 是一致稳定的，当 $t$ 趋于无穷时， $x(t)$ 趋于零，且对于 $t_0$ 是一致的，证明存在一个 $\mathcal{KL}$ 类函数 $\beta(r, s)$ 使式(4.20)成立。由一致稳定性可知，存在一个常数 $c > 0$ 及一个 $\mathcal{K}$ 类函数 $\alpha$ ，使得对于任意 $r \in (0, c]$ ，解 $x(t)$ 满足

$$\| x (t) \| \leqslant \alpha \left(\| x \left(t _ {0}\right) \|\right) < \alpha (r), \forall t \geqslant t _ {0}, \forall \| x \left(t _ {0}\right) \| < r \tag {C.8}$$

此外，给定 $\eta > 0$ ，存在 $T = T(\eta, r) \geqslant 0$ （与 $\eta$ 和 $r$ 有关，但与 $t_0$ 无关），满足

$$\| x (t) \| < \eta , \forall t \geqslant t _ {0} + T (\eta , r)$$

设 $\bar{T} (\eta ,r)$ 是所有可用 $T(\eta ,r)$ 的下确界，函数 $\bar{T} (\eta ,r)$ 关于 $\eta$ 是非负非增的，关于 $r$ 是非减的，且对于所有 $\eta \geqslant \alpha (r),\bar{T} (\eta ,r) = 0$ 。设

$$W _ {r} (\eta) = \frac {2}{\eta} \int_ {\eta / 2} ^ {\eta} \bar {T} (s, r) d s + \frac {r}{\eta} \geqslant \bar {T} (\eta , r) + \frac {r}{\eta}$$

函数 $W_{r}(\eta)$ 是正的，且具有以下性质：

- 对于每个固定的 $r, W_r(\eta)$ 是连续且严格递减的，当 $\eta$ 趋于无穷时， $W_r(\eta)$ 趋于零；  
- 对于每个固定的 $\eta, W_r(\eta)$ 关于 $r$ 是严格递增的。

取 $U_{r} = W_{r}^{-1}$ ，则 $U_{r}$ 同样具有前述 $W_{r}$ 的两个性质，且有 $\bar{T}(U_r(s),r) <   W_r(U_r(s)) = s$ 。因此
