# Partial-Fraction Expansion

Before we present MATLAB approach to the partial-fraction expansions of transfer functions, we discuss the manual approach to the partial-fraction expansions of transfer functions.

Partial-Fraction Expansion when $F ( s )$ Involves Distinct Poles Only. Consider $F ( s )$ written in the factored form

$$F (s) = \frac {B (s)}{A (s)} = \frac {K (s + z _ {1}) (s + z _ {2}) \cdots (s + z _ {m})}{(s + p _ {1}) (s + p _ {2}) \cdots (s + p _ {n})}, \quad \text { for } m < n$$

where $p _ { 1 } , p _ { 2 } , \ldots , p _ { n }$ and $z _ { 1 } , z _ { 2 } , \ldots , z _ { m }$ are either real or complex quantities, but for each complex $p _ { i } \mathbf { o r } z _ { j }$ there will occur the complex conjugate of $p _ { i }$ or $z _ { j } .$ , respectively. If $F ( s )$ involves distinct poles only, then it can be expanded into a sum of simple partial fractions as follows:

$$F (s) = \frac {B (s)}{A (s)} = \frac {a _ {1}}{s + p _ {1}} + \frac {a _ {2}}{s + p _ {2}} + \dots + \frac {a _ {n}}{s + p _ {n}} \tag {B-1}$$

where $a _ { k } \left( k = 1 , 2 , \ldots , n \right)$ are constants.The coefficient $a _ { k }$ is called the residue at the pole at $s = - p _ { k }$ . The value of $a _ { k }$ can be found by multiplying both sides of Equation (B–1) by $\left( s + p _ { k } \right)$ and letting $s = - p _ { k }$ , which gives

$$
\begin{array}{l} \left[ (s + p _ {k}) \frac {B (s)}{A (s)} \right] _ {s = - p _ {k}} = \left[ \frac {a _ {1}}{s + p _ {1}} (s + p _ {k}) + \frac {a _ {2}}{s + p _ {2}} (s + p _ {k}) \right. \\ \left. + \dots + \frac {a _ {k}}{s + p _ {k}} (s + p _ {k}) + \dots + \frac {a _ {n}}{s + p _ {n}} (s + p _ {k}) \right] _ {s = - p _ {k}} \\ = a _ {k} \\ \end{array}
$$

We see that all the expanded terms drop out with the exception of $a _ { k }$ . Thus the residue $a _ { k }$ is found from

$$a _ {k} = \left[ (s + p _ {k}) \frac {B (s)}{A (s)} \right] _ {s = - p _ {k}}$$

Note that, since $f ( t )$ is a real function of time, if $p _ { 1 }$ and $p _ { 2 }$ are complex conjugates, then the residues $a _ { 1 }$ and $a _ { 2 }$ are also complex conjugates. Only one of the conjugates, $a _ { 1 }$ or $a _ { 2 }$ , needs to be evaluated, because the other is known automatically.

Since

$$\mathcal {L} ^ {- 1} \left[ \frac {a _ {k}}{s + p _ {k}} \right] = a _ {k} e ^ {- p _ {k} t}$$

$f ( t )$ is obtained as

$$f (t) = \mathscr {L} ^ {- 1} [ F (s) ] = a _ {1} e ^ {- p _ {1} t} + a _ {2} e ^ {- p _ {2} t} + \dots + a _ {n} e ^ {- p _ {n} t}, \quad \text { for } t \geq 0$$

EXAMPLE B–1 Find the inverse Laplace transform of

$$F (s) = \frac {s + 3}{(s + 1) (s + 2)}$$

The partial-fraction expansion of $F ( s )$ is
