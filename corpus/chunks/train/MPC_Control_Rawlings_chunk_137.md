# Exercise 1.19: Stabilizability and controllability canonical forms

Consider the partitioned system

$$
\left[ \begin{array}{c} x _ {1} \\ x _ {2} \end{array} \right] ^ {+} = \left[ \begin{array}{c c} A _ {1 1} & A _ {1 2} \\ 0 & A _ {2 2} \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \end{array} \right] + \left[ \begin{array}{c} B _ {1} \\ 0 \end{array} \right] u
$$

with $( A _ { 1 1 } , B _ { 1 } )$ controllable. This form is known as controllability canonical form.

(a) Show that the system is not controllable by checking the rank of the controllability matrix.

(b) Show that the modes $x _ { 1 }$ can be controlled from any $x _ { 1 } ( 0 )$ to any $x _ { 1 } ( n )$ with a sequence of inputs $u ( 0 ) , \ldots , u ( n - 1 )$ , but the modes $x _ { 2 }$ cannot be controlled from any $x _ { 2 } ( 0 )$ to any $x _ { 2 } ( n )$ . The states $x _ { 2 }$ are termed the uncontrollable modes.

(c) If $A _ { 2 2 }$ is stable the system is termed stabilizable. Although not all modes can be controlled, the uncontrollable modes are stable and decay to steady state.

The following lemma gives an equivalent condition for stabilizability.

Lemma 1.12 (Hautus Lemma for stabilizability). A system is stabilizable if and only if

$$
\operatorname{rank} \left[ \begin{array}{c c} \lambda I - A & B \end{array} \right] = n \quad \text {   for   all   } | \lambda | \geq 1
$$

Prove this lemma using Lemma 1.2 as the condition for controllability.
