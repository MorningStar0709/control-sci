# 1.4 Partial Fraction Expansion

A very useful property of polynomials is the partial fraction expansion:

$$\frac {\prod_ {j} (s - z _ {j})}{\prod_ {i} (s - p _ {i})} = \sum_ {i} \frac {A _ {i}}{(s - p _ {i})}$$

In the form on the left, we have terms called zeros on the top because any time $s = z _ { j }$ the ratio is zero. We also have terms called poles in the denominator, because any time $s = p _ { i } ,$ the ratio is innite.

The partial fraction expansion is very useful for ratios of polynomials in s (such as the left side above which we will encounter frequently) because such a ratio becomes a series of terms which have an easy inverse Laplace Transform

$$\frac {A _ {i}}{(s - p _ {i})} \leftrightarrow A _ {i} e ^ {p _ {i} t}$$
