Lemma 3.9 G(s) has full-column (row) normal rank if and only $i f \left[ \begin{array} { c c } { { A - s I } } & { { B } } \\ { { C } } & { { D } } \end{array} \right]$ has full-column (row) normal rank.

Proof. This follows by noting that

$$
\left[ \begin{array}{c c} A - s I & B \\ C & D \end{array} \right] = \left[ \begin{array}{c c} I & 0 \\ C (A - s I) ^ {- 1} & I \end{array} \right] \left[ \begin{array}{c c} A - s I & B \\ 0 & G (s) \end{array} \right]
$$

and

$$
\text { normalrank } \left[ \begin{array}{c c} A - s I & B \\ C & D \end{array} \right] = n + \text { normalrank } (G (s)).
$$

![](image/9e175809f1a18708dcbb200d8b6108af044f546e111dd9c0aa9907add48abc37.jpg)

Lemma 3.10 Let $G ( s ) \in \mathcal { R } _ { p } ( s )$ be a $p \times m$ transfer matrix and let $( A , B , C , D )$ be a minimal realization. If the system input is of the form $u ( t ) = u _ { 0 } e ^ { \lambda t }$ , where $\lambda \in \mathbb { C }$ is not a pole of $G ( s )$ and $u _ { 0 } \in \mathbb { C } ^ { m }$ is an arbitrary constant vector, then the output due to the input u(t) and the initial state $x ( 0 ) = ( \lambda I - A ) ^ { - 1 } B u _ { 0 }$ is $y ( t ) = G ( \lambda ) u _ { 0 } e ^ { \lambda t }$ , ∀t ≥ 0. In particular, if λ is a zero of $G ( s )$ , then $y ( t ) = 0$ .

Proof. The system response with respect to the input $u ( t ) = u _ { 0 } e ^ { \lambda t }$ and the initial condition $x ( 0 ) = ( \lambda I - A ) ^ { - 1 } B u _ { 0 }$ is (in terms of the Laplace transform)

$$
\begin{array}{l} Y (s) = C (s I - A) ^ {- 1} x (0) + C (s I - A) ^ {- 1} B U (s) + D U (s) \\ = C (s I - A) ^ {- 1} x (0) + C (s I - A) ^ {- 1} B u _ {0} (s - \lambda) ^ {- 1} + D u _ {0} (s - \lambda) ^ {- 1} \\ = C (s I - A) ^ {- 1} x (0) + C \left[ (s I - A) ^ {- 1} - (\lambda I - A) ^ {- 1} \right] B u _ {0} (s - \lambda) ^ {- 1} \\ + C (\lambda I - A) ^ {- 1} B u _ {0} (s - \lambda) ^ {- 1} + D u _ {0} (s - \lambda) ^ {- 1} \\ = C (s I - A) ^ {- 1} (x (0) - (\lambda I - A) ^ {- 1} B u _ {0}) + G (\lambda) u _ {0} (s - \lambda) ^ {- 1} \\ = G (\lambda) u _ {0} (s - \lambda) ^ {- 1}. \\ \end{array}
$$

Hence $y ( t ) = G ( \lambda ) u _ { 0 } e ^ { \lambda t }$ .

![](image/fcf89e9d4b9dda3b84162fac96684a36dafef8e4ce406d0fd0a9d15220af8ad6.jpg)

Example 3.3 Let

$$
G (s) = \left[ \begin{array}{c c} A & B \\ \hline C & D \end{array} \right] = \left[ \begin{array}{c c c c c c} - 1 & - 2 & 1 & 1 & 2 & 3 \\ 0 & 2 & - 1 & 3 & 2 & 1 \\ - 4 & - 3 & - 2 & 1 & 1 & 1 \\ \hline 1 & 1 & 1 & 0 & 0 & 0 \\ 2 & 3 & 4 & 0 & 0 & 0 \end{array} \right].
$$

Then the invariant zeros of the system can be found using the Matlab command
