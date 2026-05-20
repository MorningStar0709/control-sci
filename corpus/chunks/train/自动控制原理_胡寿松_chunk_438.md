# (1) 采样拉氏变换的两个重要性质

1) 采样函数的拉氏变换具有周期性，即

$$G ^ {*} (s) = G ^ {*} \left(s + j k \omega_ {s}\right) \tag {7-57}$$

其中， $\omega_{s}$ 为采样角频率。

证明 由式(7-10)知

$$G ^ {*} (s) = \frac {1}{T} \sum_ {n = - \infty} ^ {\infty} G (s + j n \omega_ {s}) \tag {7-58}$$

其中 $T$ 为采样周期。因此，令 $s = s + \mathrm{j}k\omega_s$ ，必有

$$G ^ {*} (s + \mathrm{j} k \omega_ {s}) = \frac {1}{T} \sum_ {n = - \infty} ^ {\infty} G [ s + \mathrm{j} (n + k) \omega_ {s} ]$$

在上式中，令 $l = n + k$ ，可得

$$G ^ {*} (s + \mathrm{j} k \omega_ {s}) = \frac {1}{T} \sum_ {l = - \infty} ^ {\infty} G (s + \mathrm{j} l \omega_ {s})$$

由于求和与符号无关，再令 $l = n$ ，证得

$$G ^ {*} (s + \mathrm{j} k \omega_ {s}) = \frac {1}{T} \sum_ {n = - \infty} ^ {\infty} G (s + \mathrm{j} n \omega_ {s}) = G ^ {*} (s)$$

2) 若采样函数的拉氏变换 $E^{*}(s)$ 与连续函数的拉氏变换 $G(s)$ 相乘后再离散化，则 $E^{*}(s)$ 可以从离散符号中提出来，即

$$\left[ G (s) E ^ {*} (s) \right] ^ {*} = G ^ {*} (s) E ^ {*} (s) \tag {7-59}$$

证明 根据式(7-58)，有

$$[ G (s) E ^ {*} (s) ] ^ {*} = \frac {1}{T} \sum_ {n = - \infty} ^ {\infty} [ G (s + j n \omega_ {s}) E ^ {*} (s + j n \omega_ {s}) ]$$

再由式(7-57)知

$$E ^ {*} (s + \mathrm{j} n \omega_ {s}) = E ^ {*} (s)$$

于是 $[G(s)E^{*}(s)]^{*} = \frac{1}{T}\sum_{n = -\infty}^{\infty}[G(s + jn\omega_{s})E^{*}(s)]$

$$= E ^ {*} (s) \cdot \frac {1}{T} \sum_ {n = - \infty} ^ {\infty} G (s + j n \omega_ {s})$$

再由式(7-58)，即证得

$$\left[ G (s) E ^ {*} (s) \right] ^ {*} = G ^ {*} (s) E ^ {*} (s)$$
