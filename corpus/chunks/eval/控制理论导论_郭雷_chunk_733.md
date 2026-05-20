$$
\begin{array}{l} \left\| R (\sigma + \mathrm{i} \tau ; A) x \right\| ^ {2} = \left\langle \int_ {0} ^ {\infty} \mathrm{e} ^ {- (\sigma + \mathrm{i} \tau) t} T (t) x \mathrm{d} t, \int_ {0} ^ {\infty} \mathrm{e} ^ {- (\sigma + \mathrm{i} \tau) s} T (s) x \mathrm{d} s \right\rangle \\ = \int_ {0} ^ {\infty} \mathrm{e} ^ {- \mathrm{i} \tau \xi} \mathrm{d} \xi \int_ {0} ^ {\infty} \mathrm{e} ^ {- \sigma (\xi + 2 s)} \langle T (\xi + s) x, T (s) x \rangle \mathrm{d} s \\ + \int_ {- \infty} ^ {0} \mathrm{e} ^ {- \mathrm{i} \tau \xi} \mathrm{d} \xi \int_ {- \xi} ^ {\infty} \mathrm{e} ^ {- \sigma (\xi + 2 s)} \langle T (\xi + s) x, T (s) x \rangle \mathrm{d} s \\ = \int_ {- \infty} ^ {\infty} \mathrm{e} ^ {- \mathrm{i} \tau \xi} f (\xi) \mathrm{d} \xi , \\ \end{array}
$$

其中

$$
f (\xi) = \left\{ \begin{array}{l l} \int_ {0} ^ {\infty} \mathrm{e} ^ {- \sigma (\xi + 2 s)} \langle T (\xi + s) x, T (s) x \rangle \mathrm{d} s, & \quad \xi \geqslant 0, \\ \int_ {- \xi} ^ {\infty} \mathrm{e} ^ {- \sigma (\xi + 2 s)} \langle T (\xi + s) x, T (s) x \rangle \mathrm{d} s, & \quad \xi <   0. \end{array} \right.
$$

记 $\omega_0 = \omega(A)$ , 并取 $\varepsilon > 0$ 满足 $\omega_0 + \varepsilon < \sigma$ . 于是存在 $M_{\varepsilon} \geqslant 1$ 使得

$$\| T (t) \| \leqslant M _ {\varepsilon} \mathrm{e} ^ {(\omega_ {0} + \varepsilon) t}, \quad t \geqslant 0.$$

由此当 $\xi \geqslant 0$ 时，有

$$
\begin{array}{l} | f (\xi) | \leqslant \int_ {0} ^ {\infty} M _ {\varepsilon} ^ {2} \| x \| ^ {2} \mathrm{e} ^ {- \sigma (\xi + 2 s)} \mathrm{e} ^ {(\omega_ {0} + \varepsilon) (\xi + 2 s)} \mathrm{d} s \\ = \frac {M _ {\varepsilon} ^ {2} \| x \| ^ {2}}{2 (\sigma - \omega_ {0} - \varepsilon)} \mathrm{e} ^ {- (\sigma - \omega_ {0} - \varepsilon) \xi}. \\ \end{array}
$$

类似地，当 $\xi < 0$ 时有

$$
\begin{array}{l} | f (\xi) | \leqslant \int_ {- \xi} ^ {\infty} M _ {\varepsilon} ^ {2} \| x \| ^ {2} e ^ {- \sigma (\xi + 2 s)} e ^ {(\omega_ {0} + \varepsilon) (\xi + 2 s)} d s \\ = \frac {M _ {\varepsilon} ^ {2} \| x \| ^ {2}}{2 (\sigma - \omega_ {0} - \varepsilon)} \mathrm{e} ^ {(\sigma - \omega_ {0} - \varepsilon) \xi}. \\ \end{array}
$$

于是 $f(\cdot) \in L^{1}(\mathbb{R}) \cap L^{\infty}(\mathbb{R})$ ，并且 $f(\xi)$ 的 Fourier 变换是关于 $\tau$ 的非负函数 $\| R(\sigma + i\tau; A)x\|$ 。根据 Fourier 变换理论，有 $\| R(\sigma + i\tau; A)x\|^2 \in L^{1}(\mathbb{R})$ 。又依熟知的 Riemann-Lebesgue 引理，我们有 $\lim_{\tau \to \infty} \| R(\sigma + i\tau; A)x\| = 0$ 。证毕。

引理10.1.3 设 $T(t)$ 是Hilbert空间 $H$ 上闭稠定线性算子 $A$ 生成的 $C_0$ 半群．假定 $s_1 > s(A)$ .如果
