# Exercise A.33: Positive semidefinite Q penalty and its square root

Consider the linear quadratic problem with system

$$
\begin{array}{l} x (k + 1) = A x (k) + B u (k) \\ \mathcal {Y} (k) = Q ^ {1 / 2} x (k) \\ \end{array}
$$

and infinite horizon cost function

$$
\begin{array}{l} \Phi = \sum_ {k = 0} ^ {\infty} x (k) ^ {\prime} Q x (k) + u (k) ^ {\prime} R u (k) \\ = \sum_ {k = 0} ^ {\infty} y (k) ^ {\prime} y (k) + u (k) ^ {\prime} R u (k) \\ \end{array}
$$

with $Q \geq 0 , R > 0$ , and (A, B) stabilizable. In Exercise A.31 we showed that if $( A , Q ^ { 1 / 2 } )$ is detectable and an input sequence has been found such that

$$u (k) \rightarrow 0 \quad y (k) \rightarrow 0$$

then $x ( k ) \to 0 .$ .

(a) Show that if $Q \ \geq \ 0 ,$ , then $Q ^ { 1 / 2 }$ is a well defined, real, symmetric matrix and $Q ^ { 1 / 2 } \geq 0 .$ .

Hint: apply Theorem A.1 to Q, using fact 3..

(b) Show that $( A , Q ^ { 1 / 2 } )$ is detectable (observable) if and only if $( A , Q )$ is detectable (observable). So we can express one of the LQ existence, uniqueness, and stability conditions using detectability of (A, Q) instead of $( A , Q ^ { 1 / 2 } )$ .
