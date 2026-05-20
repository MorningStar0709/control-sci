# Bode Asymptotic Magnitude Plot (BAMP)

Single Pole We start by looking at a simple transfer function consisting of one pole:

$$G (s) = \frac {1}{(s + a)} \quad (\text { here, ourpoleis } p = - a)$$

In all frequency response analysis we assume that $R e ( p ) < 0$ . For now we assume $I m ( p ) = 0$

We consider $s = j \omega$ and there are three values of ω which are relevant.

$1 . \ \omega < < | p |$   
$2 , \ \omega = | p |$   
$3 . \ \omega > > \ | p |$

Ranges 1 and 3 are asympotic because they become more and more true as $| \omega |  0 \mathrm { o r } | \omega |  \infty$ . Value 2 is an exact value so we can easily compute an anchor point for the graph. For each region, as we plug in $s = j \omega$ , we can approximate $| G ( j \dot { \omega } ) |$ | as

![](image/01f78ac2f3320deeb76e9017c3f441be77eff0d2b6bebecffa62b3dfed840d86.jpg)

<details>
<summary>text_image</summary>

1G/dB
20log(α)
ρ -3dB
|G| = 1/ω
-20 dB/decade
ω = a
log(ω)
</details>

Figure 5.4: Bode Magnitude Plot of a single pole.

1. $\begin{array} { r } { | G ( j \omega ) | = \left| \frac { 1 } { j \omega + a } \right| \approx 1 / a } \end{array}$   
2. $\begin{array} { r } { | G ( j \omega ) | = \left| \frac { 1 } { a + j a } \right| = \frac { 1 } { \sqrt { a ^ { 2 } + a ^ { 2 } } } = \frac { 1 } { a } \frac { 1 } { \sqrt { 2 } } } \end{array}$   
3. $\begin{array} { r } { | G ( j \omega ) | = \left| \frac { 1 } { j \omega + a } \right| \approx \left| \frac { 1 } { j \omega } \right| = \frac { 1 } { \omega } } \end{array}$

Importantly, the Bode Magnitude plot is logarithmic in the Magnitude and we express Magnitude in dB. Therefore we can re-write the approximations as

1. $| G ( j \omega ) | \approx - d B ( a )$   
$\begin{array} { r } { 2 . \mathrm { ~ } | G ( j \omega ) | = | d B ( \frac { 1 } { a + j a } ) | = d B ( \frac { 1 } { \sqrt { a ^ { 2 } + a ^ { 2 } } ) = d B ( a - 1 } + d B ( \frac { 1 } { \sqrt { 2 } } - d B ( a ) - d B ( \sqrt { 2 } ) = - d B ( a ) - 3 d B ( \sqrt { 2 } ) ) | } \end{array}$   
3. $\begin{array} { r } { | G ( j \omega ) | \approx \left| d B ( \frac { 1 } { j \omega } ) \right| = - d B ( \omega ) } \end{array}$

If we plot this on a log-log scale, we get Figure 5.4. It's important to note a couple of things.
