# 5.4.9 Complex Conjugate Poles

The BAMPs above were restricted to real-valued poles and zeros. In this section we consider the BAMP of transfer functions having at least one pair of complex conjugate poles:

$$p _ {i} = a \pm j b$$

As before, we are only interested in the case where $a < 0$ so that the response is stable (does not grow with time). A more typical system has a mixture of real and complex poles and zeros such as

$$G (s) = \frac {(s + 5)}{(s + 0 . 1) (s + 1 + 3 j) (s + 1 - 3 j)}$$

we will see that it is more convenient to do the BAMP as well as the phase plot when the complex conjugate poles are represented in polar form, that is in terms of $\omega _ { n }$ and ζ. Multiplying the complex poles, $( s + 1 + 3 j )$ and $( s + 1 - 3 j )$ together,

$$G (s) = \frac {(s + 5)}{(s + 0 . 1) (s ^ {2} + 2 s + 1 0)}$$

Using the standard polar form for the second order term in the demoninator we have

$$G (s) = \frac {(s + 5)}{(s + 0 . 1) (s ^ {2} + 2 \zeta \omega_ {n} s + \omega_ {n} ^ {2})}$$

where $\omega _ { n } = \sqrt { 1 0 } = 3 . 1$ and $\begin{array} { r } { 2 \zeta \omega _ { n } = 2  \zeta = 1 / \omega _ { n } = \frac { 1 } { \sqrt { 1 0 } } } \end{array}$

Let's focus in on the second order poles:

$$P _ {2} (s) = \frac {1}{s ^ {2} + 2 \zeta \omega_ {n} s + \omega_ {n} ^ {2}}$$

The key idea is to analyze the asymptotes of the 2nd order poles, $P _ { 2 } ( s )$ , as we did above, considering three cases for the value of ω:

1. $\omega < < \omega _ { n }$   
2. $\omega = \omega _ { n }$   
3. $\omega > > \omega _ { n }$

plugging in $s = j \omega$ we derive the magnitude for each case:

1. $\begin{array} { r } { | P _ { 2 } ( j \omega ) | \approx \frac { 1 } { \omega _ { n } ^ { 2 } } } \end{array}$ ω2n (remember $0 < \zeta < 1 )$   
2. |P2(jωn)| = 1|j2ω2n+2ζjω2n+ω2n| = 1|−ω2n+2ζjω2n+ω2n| $\begin{array} { r } { | P _ { 2 } ( j \omega _ { n } ) | = \frac { 1 } { | j ^ { 2 } \omega _ { n } ^ { 2 } + 2 \zeta j \omega _ { n } ^ { 2 } + \omega _ { n } ^ { 2 } | } = \frac { 1 } { | - \omega _ { n } ^ { 2 } + 2 \zeta j \omega _ { n } ^ { 2 } + \omega _ { n } ^ { 2 } | } = \frac { 1 } { 2 \zeta \omega _ { n } ^ { 2 } } } \end{array}$   
3. $\begin{array} { r } { | P _ { 2 } ( j \omega ) | \approx \frac { 1 } { \omega ^ { 2 } } } \end{array}$

For case $1 \ ( \omega < < \omega _ { n } )$ ,

$$d B (| \frac {1}{\omega_ {n} ^ {2}} |) = - 2 d B (\omega_ {n}) \quad \mathrm{(aconstant)}$$

For case $2 \ ( \omega = \omega _ { n } )$ ,

$$| P _ {2} (j \omega_ {n}) | = \frac {1}{2 \zeta \omega_ {n} ^ {2}} \quad (\text { also a constant })$$

For now, lets assume $\zeta = 1 \ \mathrm { g i v i n g }$

$$| P _ {2} (j \omega_ {n}) | = \frac {1}{2 \omega_ {n} ^ {2}}$$

in dB
