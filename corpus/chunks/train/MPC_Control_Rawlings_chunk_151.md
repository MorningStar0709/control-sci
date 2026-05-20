# Exercise 1.31: Detectability and observability canonical forms

Consider the partitioned system

$$
\left[ \begin{array}{c} x _ {1} \\ x _ {2} \end{array} \right] ^ {+} = \left[ \begin{array}{c c} A _ {1 1} & 0 \\ A _ {2 1} & A _ {2 2} \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \end{array} \right]

\mathcal {Y} = \left[ \begin{array}{c c} C _ {1} & 0 \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \end{array} \right]
$$

with $( A _ { 1 1 } , C _ { 1 } )$ observable. This form is known as observability canonical form.

(a) Show that the system is not observable by checking the rank of the observability matrix.

(b) Show that the modes $x _ { 1 }$ can be uniquely determined from a sequence of measuremen $^ { \mathrm { ~ \tiny ~ S , ~ } }$ but the modes $x _ { 2 }$ cannot be uniquely determined from the measurements. The states $x _ { 2 }$ are termed the unobservable modes.

(c) If $A _ { 2 2 }$ is stable the system is termed detectable. Although not all modes can be observed, the unobservable modes are stable and decay to steady state.

The following lemma gives an equivalent condition for detectability.

Lemma 1.13 (Hautus Lemma for detectability). A system is detectable if and only $i f$

$$
\operatorname{rank} \left[ \begin{array}{c} \lambda I - A \\ C \end{array} \right] = n \qquad f o r a l l | \lambda | \geq 1
$$

Prove this lemma using Lemma 1.4 as the condition for observability.
