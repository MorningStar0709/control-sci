# 6.6 Analyticity Constraints

Let $p _ { 1 } , p _ { 2 } , \ldots , p _ { m }$ and $z _ { 1 } , z _ { 2 } , \ldots , z _ { k }$ be the open right-half plane poles and zeros of L, respectively. Suppose that the closed-loop system is stable. Then

$$S (p _ {i}) = 0, \quad T (p _ {i}) = 1, i = 1, 2, \dots , m$$

and

$$S (z _ {j}) = 1, T (z _ {j}) = 0, j = 1, 2, \dots , k$$

The internal stability of the feedback system is guaranteed by satisfying these analyticity (or interpolation) conditions. On the other hand, these conditions also impose severe limitations on the achievable performance of the feedback system.

Suppose $S = ( I + L ) ^ { - 1 }$ and $T = L ( I + L ) ^ { - 1 }$ are stable. Then $p _ { 1 } , p _ { 2 } , \ldots , p _ { m }$ are the right-half plane zeros of S and $z _ { 1 } , z _ { 2 } , \ldots , z _ { k }$ are the right-half plane zeros of T . Let

$$B _ {p} (s) = \prod_ {i = 1} ^ {m} \frac {s - p _ {i}}{s + p _ {i}}, B _ {z} (s) = \prod_ {j = 1} ^ {k} \frac {s - z _ {j}}{s + z _ {j}}$$

Then $| B _ { p } ( j \omega ) | = 1$ and $| B _ { z } ( j \omega ) | = 1$ for all frequencies and, moreover,

$$B _ {p} ^ {- 1} (s) S (s) \in \mathcal {H} _ {\infty}, B _ {z} ^ {- 1} (s) T (s) \in \mathcal {H} _ {\infty}.$$

Hence, by the maximum modulus theorem, we have

$$\left\| S (s) \right\| _ {\infty} = \left\| B _ {p} ^ {- 1} (s) S (s) \right\| _ {\infty} \geq \left| B _ {p} ^ {- 1} (z) S (z) \right|$$

for any z with $\mathrm { R e } ( z ) > 0$ . Let z be a right-half plane zero of $L ;$ then

$$\| S (s) \| _ {\infty} \geq | B _ {p} ^ {- 1} (z) | = \prod_ {i = 1} ^ {m} \left| \frac {z + p _ {i}}{z - p _ {i}} \right|$$

Similarly, one can obtain

$$\| T (s) \| _ {\infty} \geq | B _ {z} ^ {- 1} (p) | = \prod_ {j = 1} ^ {k} \left| \frac {p + z _ {j}}{p - z _ {j}} \right|$$

where $p$ is a right-half plane pole of L.

The weighted problem can be considered in the same fashion. Let $W _ { e }$ be a weight such that $W _ { e } S$ is stable. Then

$$\| W _ {e} (s) S (s) \| _ {\infty} \geq | W _ {e} (z) | \prod_ {i = 1} ^ {m} \left| \frac {z + p _ {i}}{z - p _ {i}} \right|$$

Now suppose $W _ { e } ( s ) = \frac { s / M _ { s } + \omega _ { b } } { s + \omega _ { b } \epsilon } , \| W _ { e } S \| _ { \infty } \le 1$ , and z is a real right-half plane zero. Then

$$\frac {z / M _ {s} + \omega_ {b}}{z + \omega_ {b} \epsilon} \leq \prod_ {i = 1} ^ {m} \left| \frac {z - p _ {i}}{z + p _ {i}} \right| =: \alpha ,$$

which gives

$$\omega_ {b} \leq \frac {z}{1 - \alpha \epsilon} (\alpha - \frac {1}{M _ {s}}) \approx z (\alpha - \frac {1}{M _ {s}})$$

where $\alpha = 1$ if L has no right-half plane poles. This shows that the bandwidth of the closed-loop must be much smaller than the right-half plane zero. Similar conclusions can be arrived at for complex right-half plane zeros.
