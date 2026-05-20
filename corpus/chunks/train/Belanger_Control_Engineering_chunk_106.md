# 3.5.3 Observability Tests

Our results so far suggest that system observability be tested by searching for a vector $\mathbf{x}_0$ such that $Ce^{At}\mathbf{x}_0 = 0$ for all $t \geq 0$ . That is feasible, but difficult. Better tests are available, and shall be developed presently.

We shall need the Cayley–Hamilton theorem, which states that a matrix satisfies its own characteristic equation. If the characteristic equation of a matrix A is

$$s ^ {n} + a _ {n - 1} s ^ {n - 1} + \dots + a _ {1} s + a _ {0} = 0$$

then the Cayley–Hamilton theorem states that

$$A ^ {n} + a _ {n - 1} A ^ {n - 1} + \dots + a _ {1} A + a _ {0} I = 0.$$

We now derive a result that will lead to our first observability test.

■ Theorem 3.2 The vector $\mathbf{x}^*$ is an unobservable state if, and only if,

$$
\left[ \begin{array}{c} C \\ C A \\ C A ^ {2} \\ \vdots \\ C A ^ {n - 1} \end{array} \right] \mathbf {x} ^ {*} = \mathbf {0}. \tag {3.39}
$$

Proof: To show necessity ("only if"), let $\mathbf{x}^*$ be an unobservable state. Then $Ce^{At}\mathbf{x}^* = 0, t \geq 0$ . Since $Ce^{At}\mathbf{x}^*$ is analytic, all its derivatives exist and must be zero at $t = 0$ . Using Property VI of the matrix exponential,

$$C e ^ {A t} \mathbf {x} ^ {*} \mid_ {t = 0} = C \mathbf {x} ^ {*} = 0\frac {d}{d t} C e ^ {A t} \mathbf {x} ^ {*} \mid_ {t = 0} = C A e ^ {A t} \mathbf {x} ^ {*} \mid_ {t = 0} = C A \mathbf {x} ^ {*} = 0\frac {d ^ {2}}{d t ^ {2}} C e ^ {A t} \mathbf {x} ^ {*} \mid_ {t = 0} = C A ^ {2} e ^ {A t} \mathbf {x} ^ {*} \mid_ {t = 0} = C A ^ {2} \mathbf {x} ^ {*} = 0$$

:    :    :

$$\frac {d ^ {k}}{d t ^ {k}} C d ^ {A t} \mathbf {x} ^ {*} \mid_ {t = 0} = C A ^ {k} e ^ {A t} \mathbf {x} ^ {*} \mid_ {t = 0} = C A ^ {k} \mathbf {x} ^ {*} = 0 \tag {3.40}$$

which is precisely what Equation 3.39 expresses in matrix form.

To show sufficiency (“if”), assume that Equation 3.39 holds for some $x^{*}$ . We show that $Ce^{At}x^{*}=0$ for all t; i.e., $x^{*}$ is an unobservable state. From Equation 3.39,

$$C \mathbf {x} ^ {*} = C A \mathbf {x} ^ {*} = C A ^ {2} \mathbf {x} ^ {*} = \dots = C A ^ {n - 1} \mathbf {x} ^ {*} = \mathbf {0}. \tag {3.41}$$

From the Cayley–Hamilton theorem,

$$A ^ {n} = - a _ {n - 1} A ^ {n - 1} - a _ {n - 2} A ^ {n - 2} - \dots - a _ {1} A - a _ {0} I \tag {3.42}$$

and

$$
\begin{array}{l} C A ^ {n} \mathbf {x} ^ {*} = - a _ {n - 1} C A ^ {n - 1} \mathbf {x} ^ {*} - \dots - a _ {1} C A \mathbf {x} ^ {*} - a _ {0} C \mathbf {x} ^ {*} \\ = 0 \\ \end{array}
$$

by Equation 3.41. Multiplying each side of Equation 3.42 by $A$ yields

$$A ^ {n + 1} = - a _ {n - 1} A ^ {n} - \dots - a _ {1} A ^ {2} - a _ {0} A$$

and therefore
