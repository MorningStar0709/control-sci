# 7.2 Balanced Realizations

Although there are infinitely many different state-space realizations for a given transfer matrix, some particular realizations have proven to be very useful in control engineering and signal processing. Here we will only introduce one class of realizations for stable transfer matrices that are most useful in control applications. To motivate the class of realizations, we first consider some simple facts.

Lemma 7.3 Let $\left[ { \frac { A \mid B } { C \mid D } } \right]$ be a state-space realization of a (not necessarily stable) transfer matrix $G ( \bar { s } )$ . Suppose that there exists a symmetric matrix

$$
P = P ^ {*} = \left[ \begin{array}{c c} P _ {1} & 0 \\ 0 & 0 \end{array} \right]
$$

with $P _ { 1 }$ nonsingular such that

$$A P + P A ^ {*} + B B ^ {*} = 0.$$

Now partition the realization (A, B, C, D) compatibly with P as

$$
\left[ \begin{array}{c c c} A _ {1 1} & A _ {1 2} & B _ {1} \\ A _ {2 1} & A _ {2 2} & B _ {2} \\ \hline C _ {1} & C _ {2} & D \end{array} \right].
$$

Then $[ { \frac { A _ { 1 1 } } { C _ { 1 } } } | { \frac { B _ { 1 } } { D } } ]$ is also a realization of G. Moreover, $( A _ { 1 1 } , B _ { 1 } )$ is controllable if $A _ { 1 1 }$ is stable.

Proof. Use the partitioned P and $( A , B , C )$ to get

$$
0 = A P + P A ^ {*} + B B ^ {*} = \left[ \begin{array}{c c} A _ {1 1} P _ {1} + P _ {1} A _ {1 1} ^ {*} + B _ {1} B _ {1} ^ {*} & P _ {1} A _ {2 1} ^ {*} + B _ {1} B _ {2} ^ {*} \\ A _ {2 1} P _ {1} + B _ {2} B _ {1} ^ {*} & B _ {2} B _ {2} ^ {*} \end{array} \right],
$$

which gives $B _ { 2 } = 0$ and $A _ { 2 1 } = 0$ since $P _ { 1 }$ is nonsingular. Hence, part of the realization is not controllable:

$$
\left[ \begin{array}{c c c} A _ {1 1} & A _ {1 2} & B _ {1} \\ A _ {2 1} & A _ {2 2} & B _ {2} \\ \hline C _ {1} & C _ {2} & D \end{array} \right] = \left[ \begin{array}{c c c} A _ {1 1} & A _ {1 2} & B _ {1} \\ 0 & A _ {2 2} & 0 \\ \hline C _ {1} & C _ {2} & D \end{array} \right] = \left[ \begin{array}{c c c} A _ {1 1} & B _ {1} \\ \hline C _ {1} & D \end{array} \right].
$$

Finally, it follows from Lemma 7.1 that $( A _ { 1 1 } , B _ { 1 } )$ is controllable if $A _ { 1 1 }$ is stable.

![](image/291f05258a174702de39518f801f5587fb3bc5ac4dc749ace7822ee577bc08e8.jpg)

We also have the following:

Lemma 7.4 $L e t ~ \left[ \frac { A \mid B } { C \mid D } \right]$ be a state-space realization of a (not necessarily stable) transfer matrix $G ( \bar { s } )$ . Suppose that there exists a symmetric matrix

$$
Q = Q ^ {*} = \left[ \begin{array}{c c} Q _ {1} & 0 \\ 0 & 0 \end{array} \right]
$$

with $Q _ { 1 }$ nonsingular such that

$$Q A + A ^ {*} Q + C ^ {*} C = 0.$$
