# Central limit theorem.

The central limit theorem states that if a set of n random variables $x _ { i } , i = 1 , 2 , \ldots ,$ n are independent, then under general conditions the density $p _ { y }$ of their sum

$$y = x _ {1} + x _ {2} + \dots + x _ {n}$$

properly normalized, tends to a normal density as $n  \infty$ . (Papoulis, 1984, p. 194).

![](image/0bb4a2e4777bb358b15cbaad2b98dd9290fecfd2f262ca9207d76a021c60d7ff.jpg)

<details>
<summary>line</summary>

| x | σ = 1/2 | σ = 1 | σ = 2 |
| --- | --- | --- | --- |
| -5 | 0.0000 | 0.0000 | 0.0000 |
| -4 | 0.0000 | 0.0000 | 0.0000 |
| -3 | 0.0000 | 0.0000 | 0.0000 |
| -2 | 0.0000 | 0.0000 | 0.0000 |
| -1 | 0.0000 | 0.0000 | 0.0000 |
| 0 | 0.2500 | 0.1500 | 0.1800 |
| 1 | 0.7900 | 0.3900 | 0.2100 |
| 2 | 0.2500 | 0.1500 | 0.1800 |
| 3 | 0.0625 | 0.0625 | 0.1250 |
| 4 | 0.0188 | 0.0188 | 0.0625 |
| 5 | 0.0044 | 0.0044 | 0.0250 |
| 6 | 0.0011 | 0.0011 | 0.0111 |
| 7 | 0.0002 | 0.0002 | 0.0044 |
</details>

Figure A.8: Normal distribution, $p _ { \xi } ( x ) = { \frac { 1 } { \sqrt { 2 \pi \sigma ^ { 2 } } } } \exp { \left( - { \frac { 1 } { 2 } } { \frac { ( x - m ) ^ { 2 } } { \sigma ^ { 2 } } } \right) }$ Mean is one and standard deviations are 1/2, 1 and 2.

Notice that we require only mild restrictions on how the $x _ { i }$ themselves are distributed for the sum y to tend to a normal. See Papoulis (1984, p. 198) for one set of sufficient conditions and a proof of this theorem.

Fourier transform of the density function. It is often convenient to handle the algebra of density functions, particularly normal densities, by using the Fourier transform of the density function rather than the density itself. The transform, which we denote as $\varphi _ { \xi } ( u )$ , is often called the characteristic function or generating function in the statistics literature. From the definition of the Fourier transform

$$\varphi_ {\xi} (u) = \int_ {- \infty} ^ {\infty} e ^ {i u x} p _ {\xi} (x) d x$$

The transform has a one-to-one correspondence with the density function, which can be seen from the inverse transform formula

$$p _ {\xi} (x) = \frac {1}{2 \pi} \int_ {- \infty} ^ {\infty} e ^ {- i u x} \varphi_ {\xi} (u) d u$$

Example A.36: Fourier transform of the normal density.

Show the Fourier transform of the normal density is

$$\varphi_ {\xi} (u) = \exp \Big (i u m - \frac {1}{2} u ^ {2} \sigma^ {2} \Big).$$
