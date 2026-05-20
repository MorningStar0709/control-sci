# Exercise 4.16: The resampling theorem

Generalize the proof of Theorem 4.35 to cover any number of samples.

Hint: you may find the multinomial expansion formula useful

$$(x _ {1} + x _ {2} + \dots + x _ {s}) ^ {k} = \sum_ {r _ {1} = 0} ^ {k} \sum_ {r _ {2} = 0} ^ {k} \dots \sum_ {r _ {s} = 0} ^ {k} a (r _ {1}, r _ {2}, \dots , r _ {s}) x _ {1} ^ {r _ {1}} x _ {2} ^ {r _ {2}} \dots x _ {s} ^ {r _ {s}}$$

in which the coefficients in the expansion formula are given by Feller (1968, p.37)

$$
a (r _ {1}, r _ {2}, \dots , r _ {s}) = \left\{ \begin{array}{c c} \frac {k !}{r _ {1} ! r _ {2} ! \cdots r _ {s} !} & r _ {1} + r _ {2} + \dots + r _ {s} = k \\ 0 & r _ {1} + r _ {2} + \dots + r _ {s} \neq k \end{array} \right. \tag {4.63}
$$
