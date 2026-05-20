$$F (s) = \frac {s + 3}{(s + 1) (s + 2)} = \frac {a _ {1}}{s + 1} + \frac {a _ {2}}{s + 2}$$

where $a _ { 1 }$ and $a _ { 2 }$ are found as

$$a _ {1} = \left[ (s + 1) \frac {s + 3}{(s + 1) (s + 2)} \right] _ {s = - 1} = \left[ \frac {s + 3}{s + 2} \right] _ {s = - 1} = 2a _ {2} = \left[ (s + 2) \frac {s + 3}{(s + 1) (s + 2)} \right] _ {s = - 2} = \left[ \frac {s + 3}{s + 1} \right] _ {s = - 2} = - 1$$

Thus

$$
\begin{array}{l} f (t) = \mathscr {L} ^ {- 1} [ F (s) ] \\ = \mathcal {L} ^ {- 1} \left[ \frac {2}{s + 1} \right] + \mathcal {L} ^ {- 1} \left[ \frac {- 1}{s + 2} \right] \\ = 2 e ^ {- t} - e ^ {- 2 t}, \quad \text {   for   } t \geq 0 \\ \end{array}
$$

EXAMPLE B–2 Obtain the inverse Laplace transform of

$$G (s) = \frac {s ^ {3} + 5 s ^ {2} + 9 s + 7}{(s + 1) (s + 2)}$$

Here, since the degree of the numerator polynomial is higher than that of the denominator polynomial, we must divide the numerator by the denominator.

$$G (s) = s + 2 + \frac {s + 3}{(s + 1) (s + 2)}$$

Note that the Laplace transform of the unit-impulse function $\delta ( t )$ is 1 and that the Laplace transform of $d \delta ( t ) / d t$ is s. The third term on the right-hand side of this last equation is $F ( s )$ in Example $\mathrm { B } { - } 1$ . So the inverse Laplace transform of $G ( s )$ is given as

$$g (t) = \frac {d}{d t} \delta (t) + 2 \delta (t) + 2 e ^ {- t} - e ^ {- 2 t}, \quad \text { for } t \geq 0 -$$

EXAMPLE B–3 Find the inverse Laplace transform of

$$F (s) = \frac {2 s + 1 2}{s ^ {2} + 2 s + 5}$$

Notice that the denominator polynomial can be factored as

$$s ^ {2} + 2 s + 5 = (s + 1 + j 2) (s + 1 - j 2)$$

If the function $F ( s )$ involves a pair of complex-conjugate poles, it is convenient not to expand $F ( s )$ into the usual partial fractions but to expand it into the sum of a damped sine and a damped cosine function.

Noting that $s ^ { 2 } + 2 s + 5 = ( s + 1 ) ^ { 2 } + 2 ^ { 2 }$ and referring to the Laplace transforms of $e ^ { - \alpha t }$ sin vt and $e ^ { - \alpha t }$ cos vt, rewritten thus,

$$\mathcal {L} \left[ e ^ {- \alpha t} \sin \omega t \right] = \frac {\omega}{(s + \alpha) ^ {2} + \omega^ {2}}\mathscr {L} \left[ e ^ {- \alpha t} \cos \omega t \right] = \frac {s + \alpha}{(s + \alpha) ^ {2} + \omega^ {2}}$$

the given $F ( s )$ can be written as a sum of a damped sine and a damped cosine function:

$$F (s) = \frac {2 s + 1 2}{s ^ {2} + 2 s + 5} = \frac {1 0 + 2 (s + 1)}{(s + 1) ^ {2} + 2 ^ {2}}= 5 \frac {2}{(s + 1) ^ {2} + 2 ^ {2}} + 2 \frac {s + 1}{(s + 1) ^ {2} + 2 ^ {2}}$$

It follows that
