# ◆ ◆ ◆ REMARK

Since $S(s) = 1 - T(s)$ , $S$ and $T$ have identical poles, so the stability of one implies the stability of the other. Thus, the condition that $T$ be stable may be replaced by the condition that $S$ be stable.

If $P(s)S(s)$ is to be stable, S must cancel out the RHP poles of $P(s)$ . If P has a pole of multiplicity m at $s = p_{0}$ , S must have a zero of the same multiplicity at the same point. It can be shown that this implies that

$$S (p _ {0}) = \frac {d S}{d s} (p _ {0}) = \dots = \frac {d ^ {m - 1}}{d s ^ {m - 1}} S (p _ {0}) = 0. \tag {4.42}$$

This condition may also be expressed in terms of $T(s) = 1 - S(s)$ , as follows:

$$T (p _ {0}) = 1 - S (p _ {0}) = 1\frac {d ^ {i} T}{d s ^ {i}} (p _ {0}) = 0, \quad i = 1, 2, \dots , m - 1. \tag {4.43}$$

Similarly, if $P^{-1}(s)T(s)$ is to be stable, T must cancel the RHP zeros of P (i.e., the RHP poles of $P^{-1}$ ). If $z_{0}$ is a zero of P with multiplicity m, then

$$T (z _ {0}) = \frac {d T}{d s} (z _ {0}) = \dots = \frac {d ^ {m - 1} T}{d s ^ {m - 1}} (z _ {0}) = 0 \tag {4.44}$$

and

$$S (z _ {0}) = 1\frac {d ^ {i} S}{d s ^ {i}} (z _ {0}) = 0, \quad i = 1, 2, \dots , m - 1. \tag {4.45}$$

These so-called interpolation conditions are important, because they show how the system dynamics constrain the choices of S and T. That is, for simple RHP poles and zeros, S is 0 at RHP poles and 1 at RHP zeros; T is 1 at RHP poles and 0 at RHP zeros.

We now have in place the theoretical elements required to define a synthesis procedure.

a. If $P(s)$ has neither poles nor zeros in the closed RHP (i.e., including the $j$ -axis), arbitrarily choose either $T$ or $S$ , and calculate the other through the relation $T + S = 1$ . The choice must be such as to ensure that $F$ is at least proper (because our stability result was proved for the case where $F$ has a realization). Then use Equation 4.37 to calculate the compensator $F$ from $P, T,$ and $S$ .
