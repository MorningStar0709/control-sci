$$z (t) = \sum_ {k \text { odd }} b _ {k} \exp (j k \omega t)$$

考虑线性方程 Kx = z，并求出S上的解 x。把 x 表示为

$$x (t) = \sum_ {k \text { odd }} d _ {k} \exp (j k \omega t)$$

有 $\left(I + P_{h}g\frac{\beta + \alpha}{2}\right)x = x_{1} + \sum_{k\mathrm{odd};|k|\neq 1}\left[1 + \frac{\beta + \alpha}{2} G(jk\omega)\right]d_{k}\exp (jk\omega t)$

因此,如果 $\inf_{k\text{odd}; |k|\neq 1}\left|1 + \frac{\beta + \alpha}{2} G(jk\omega)\right|\neq 0$ (C.50)

则线性方程 Kx = z 有唯一解。换句话说，条件(C.50)保证了线性映射 K 存在逆映射。如果 $\omega \in \Omega$ ，该条件总能满足，因为只有当 $\rho(\omega) = 0$ 时，方程(C.50)的左边才为零。记 K 的逆映射为 $K^{-1}$ ，则方程(C.49)可重写为

$$y _ {h} = - K ^ {- 1} P _ {h} g \left[ \psi (y _ {1} + y _ {h}) - \frac {\beta + \alpha}{2} (y _ {1} + y _ {h}) \right] \stackrel {\mathrm{def}} {=} T y _ {h}$$

式中用到 $P_{h}gy_{1} = 0$ 。我们希望对方程 $y_{h} = Ty_{h}$ 应用压缩映射定理，显然， $T$ 是 $\mathcal{S}$ 到 $\mathcal{S}$ 的映射，还需验证 $T$ 是 $\mathcal{S}$ 上的压缩映射，为此考虑

$$T y ^ {(2)} - T y ^ {(1)} = K ^ {- 1} P _ {h} g \left[ \psi_ {T} (y _ {1} + y ^ {(2)}) - \psi_ {T} (y _ {1} + y ^ {(1)}) \right]$$

其中 $\psi_T(y) = \psi (y) - \frac{\beta + \alpha}{2} y$

设 $\psi_T(y_1 + y^{(2)}) - \psi_T(y_1 + y^{(1)}) = \sum_{k\text{odd}; |k|\neq 1}e_k\exp (jk\omega t)$

则

$$
\begin{array}{l} \left\| T y ^ {(2)} - T y ^ {(1)} \right\| ^ {2} = 2 \sum_ {k \text { odd }; | k | \neq 1} \left| \frac {G (j k \omega)}{1 + [ (\beta + \alpha) / 2 ] G (j k \omega)} \right| ^ {2} | e _ {k} | ^ {2} \\ \leqslant \left. \left\{\sup _ {k \text {odd}; | k | \neq 1} \left| \frac {G (j k \omega)}{1 + [ (\beta + \alpha) / 2 ] G (j k \omega)} \right| \right\} ^ {2} \right. \\ \times \left\| \psi_ {T} \left(y _ {1} + y ^ {(2)}\right) - \psi_ {T} \left(y _ {1} + y ^ {(1)}\right) \right\| ^ {2} \\ \end{array}
$$

根据对 $\psi$ 斜率的限制,有

$$\left| \psi_ {T} (y _ {1} + y ^ {(2)}) - \psi_ {T} (y _ {1} + y ^ {(1)}) \right| \leqslant \left(\frac {\beta - \alpha}{2}\right) \left| y ^ {(2)} - y ^ {(1)} \right|$$

另外有 $\sup_{k\mathrm{odd};|k|\neq 1}\left|\frac{G(jk\omega)}{1 + [(\beta + \alpha) / 2]G(jk\omega)}\right| \leqslant \frac{1}{\rho(\omega)}$

其中 $\rho(\omega)$ 由式(7.38)定义, 因此

$$\left\| T y ^ {(2)} - T y ^ {(1)} \right\| \leqslant \frac {1}{\rho (\omega)} \left(\frac {\beta - \alpha}{2}\right) \left\| y ^ {(2)} - y ^ {(1)} \right\|$$

由于 $\frac{1}{\rho(\omega)}\left(\frac{\beta - \alpha}{2}\right) < 1, \forall \omega \in \Omega$

可得出只要 $\omega \in \Omega, T$ 就是压缩映射。这样，根据压缩映射定理，方程 $y_{h} = Ty_{h}$ 有唯一解。由于 $T(-y_{1}) = 0$ ，把方程 $y_{h} = Ty_{h}$ 写为

$$y _ {h} = T y _ {h} - T (- y _ {1})$$
