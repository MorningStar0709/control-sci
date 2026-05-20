# 17.1 Gap Metric

In this section we briefly introduce the gap metric and discuss some of its applications in controller design.

Let $P ( s )$ be a p×m rational transfer matrix and let P have the following normalized right and left stable coprime factorizations:

$$P = N M ^ {- 1} = \tilde {M} ^ {- 1} \tilde {N}.$$

That is,

$$M ^ {\sim} M + N ^ {\sim} N = I, \quad \tilde {M} \tilde {M} ^ {\sim} + \tilde {N} \tilde {N} ^ {\sim} = I.$$

The graph of the operator P is the subspace of $\mathcal { H } _ { 2 }$ consisting of all pairs $( u , y )$ such that $y = P u$ . This is given by

$$
\left[ \begin{array}{c} M \\ N \end{array} \right] \mathcal {H} _ {2}
$$

and is a closed subspace of $\mathcal { H } _ { 2 }$ . The gap between two systems $P _ { 1 }$ and $P _ { 2 }$ is defined by

$$
\delta_ {g} (P _ {1}, P _ {2}) = \left\| \Pi_ {\left[ \begin{array}{l} M _ {1} \\ N _ {1} \end{array} \right] \mathcal {H} _ {2}} - \Pi_ {\left[ \begin{array}{l} M _ {2} \\ N _ {2} \end{array} \right] \mathcal {H} _ {2}} \right\|
$$

where $\Pi _ { K }$ denotes the orthogonal projection onto K and $P _ { 1 } = N _ { 1 } M _ { 1 } ^ { - 1 }$ and $P _ { 2 } =$ $N _ { 2 } M _ { 2 } ^ { - 1 }$ are normalized right coprime factorizations.

It is shown by Georgiou [1988] that the gap metric can be computed as follows:

Theorem 17.1 Let $P _ { 1 } = N _ { 1 } M _ { 1 } ^ { - 1 }$ and $P _ { 2 } = N _ { 2 } M _ { 2 } ^ { - 1 }$ be normalized right coprime factorizations. Then

$$\delta_ {g} (P _ {1}, P _ {2}) = \max \left\{\vec {\delta} (P _ {1}, P _ {2}), \vec {\delta} (P _ {2}, P _ {1}) \right\}$$

where $\vec { \delta } _ { g } ( P _ { 1 } , P _ { 2 } )$ is the directed gap and can be computed by

$$
\vec {\delta} _ {g} (P _ {1}, P _ {2}) = \inf _ {Q \in \mathcal {H} _ {\infty}} \left\| \left[ \begin{array}{c} M _ {1} \\ N _ {1} \end{array} \right] - \left[ \begin{array}{c} M _ {2} \\ N _ {2} \end{array} \right] Q \right\| _ {\infty}.
$$

The following procedures can be used in computing the directed gap $\vec { \delta _ { g } } ( P _ { 1 } , P _ { 2 } )$ .

Computing $\vec { \delta } _ { g } ( P _ { 1 } , P _ { 2 } )$ : Let

$$
P _ {1} = \left[ \begin{array}{c c} A _ {1} & B _ {1} \\ \hline C _ {1} & D _ {1} \end{array} \right], \quad P _ {2} = \left[ \begin{array}{c c} A _ {2} & B _ {2} \\ \hline C _ {2} & D _ {2} \end{array} \right].
$$

1. Let $P _ { i } = N _ { i } M _ { i } ^ { - 1 } , i = 1 , 2$ be normalized right coprime factorizations. Then
