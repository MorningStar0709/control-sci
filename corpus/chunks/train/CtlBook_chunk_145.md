1. The low frequency asymptote is horizontal because it is constant with respect to ω, $\left( - d B ( a ) \right)$ .   
2. The high frequency asymptote $\displaystyle \bigl ( \ - d B ( \omega ) \bigr )$ intersects the low frequency asymptote $\displaystyle \bigl ( \ - d B ( a ) \bigr )$ at $\omega =$ $a , | G ( j \bar { a } ) | = \bar { - } d B ( \bar { a } )$ .   
3. The actual curve is smooth and intersects the point $\{ \omega = \log ( a ) , | G | = - d B ( a ) - 3 d B \}$ in accordance with the calculation for $\omega = a$ .   
4. As ω gets greater than a, the magnitude drops with frequency according to

$$M = - d B (\omega)$$

In log-log coordinates, $- d B ( \omega )$ is a straight line with a slope of -1. When we say slope $\mathrm { o f \ - 1 ^ { \ 9 } } .$ , we mean the magnitude drops a factor of 10 for every factor of 10 increase in ω. We express this slope as $\frac { - 2 0 d B } { \mathrm { d e c a d e } }$ . The term decade refers to an order of magnitude change of frequency.

Single Zero Now we consider the case of a system represented by

$$G (s) = \frac {(s + a)}{1}$$

As before, we assume $R e ( p ) < 0$ . For now we assume $I m ( p ) = 0$ .

The same three ranges of ω are relevant:

1. $\omega < < | a |$   
2. $\omega = | a |$

![](image/f459c72d24922547e15f0fbae71d665a83c06e6e6f579296733ab71cd4f14291.jpg)

<details>
<summary>text_image</summary>

1G/dB
20log(a)
ω = a
log(w)
y = log(w)
20 db/decoale
p + 3db
</details>

Figure 5.5: Bode Magnitude Plot of a single zero.

3. $\omega > > | a |$

For each region, as we plug in $s = j \omega$ , we can approximate $| G ( j \omega ) |$ as

1. $| G ( j \omega ) | \approx a$   
2. $| G ( j \omega ) | \approx | a + j a | = a \sqrt { 2 }$   
3. $| G ( j \omega ) | \approx | j \omega | = \omega$

Again, the Bode Magnitude plot is logarithmic in the Magnitude and we express Magnitude in dB. Therefore we can re-write the approximations as

1. $| G ( j \omega ) | \approx d B ( a )$   
2. $| G ( j \omega ) | \approx \left| d B ( \textstyle { \frac { 1 } { { a } + { j a } } } ) \right| = d B ( a ) + 3 d B$   
3. $| G ( j \omega ) | \approx \left| d B ( \textstyle { \frac { 1 } { j \omega } } ) \right| = d B ( \omega )$

If we plot this we get Figure 5.5.

The zero plot is identical to the pole plot except inverted (reected around the line $| G | = 0 d B )$ . The slope of the high-frequency asymptote is now +1 or +20dB/decade.

Note that these graphs are generic for any value of a. If they are multiplied by any dierent amplitude, A, then they can be decomposed as follows:

$$\left| G _ {A} (s) \right| = \left| \frac {A}{(s + a)} \right| = | A | \left| \frac {1}{(s + a)} \right| = d B (A) + d B \left(\left| \frac {1}{(s + a)} \right|\right)$$

In other words they are shifted up or down by $d B ( A )$ .
