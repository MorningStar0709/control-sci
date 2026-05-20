We shall now describe a procedure that does result in a minimal realization by using partial fractional expansion (the resulting realization is sometimes called Gilbert’s realization due to E. G. Gilbert).

Let $G ( s )$ be a $p \times m$ transfer matrix and write it in the following form:

$$G (s) = \frac {N (s)}{d (s)}$$

with $d ( s )$ a scalar polynomial. For simplicity, we shall assume that $d ( s )$ has only real and distinct roots $\lambda _ { i } \neq \lambda _ { j }$ if $i \neq j$ and

$$d (s) = (s - \lambda_ {1}) (s - \lambda_ {2}) \dots (s - \lambda_ {r}).$$

Then $G ( s )$ has the following partial fractional expansion:

$$G (s) = D + \sum_ {i = 1} ^ {r} \frac {W _ {i}}{s - \lambda_ {i}}.$$

Suppose

$$\mathrm{rank} W _ {i} = k _ {i}$$

and let $B _ { i } \in \mathbb { R } ^ { k _ { i } \times m }$ and $C _ { i } \in \mathbb { R } ^ { p \times k _ { i } }$ be two constant matrices such that

$$W _ {i} = C _ {i} B _ {i}.$$

Then a realization for G(s) is given by

$$
G (s) = \left[ \begin{array}{c c c c} \lambda_ {1} I _ {k _ {1}} & & & B _ {1} \\ & \ddots & & \vdots \\ & & \lambda_ {r} I _ {k _ {r}} & B _ {r} \\ \hline C _ {1} & \dots & C _ {r} & D \end{array} \right].
$$

It follows immediately from PBH tests that this realization is controllable and observable, and thus it is minimal.

An immediate consequence of this minimal realization is that a transfer matrix with an rth order polynomial denominator does not necessarily have an rth order state-space realization unless $W _ { i }$ for each i is a rank one matrix.

This approach can, in fact, be generalized to more complicated cases where $d ( s )$ may have complex and/or repeated roots. Readers may convince themselves by trying some simple examples.
