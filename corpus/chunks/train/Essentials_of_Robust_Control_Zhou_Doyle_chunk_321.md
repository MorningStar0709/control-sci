# 12.2 Inner Functions

A transfer function N is called inner if $N \in \mathcal { R } \mathcal { H } _ { \infty }$ and $N ^ { \sim } N = I$ and co-inner if $N \in \mathcal { R } \mathcal { H } _ { \infty }$ and $N N ^ { \sim } = I$ . Note that N need not be square. Inner and co-inner are dual notions $( \mathrm { i . e . , } \ N$ is an inner iff $N ^ { T }$ is a co-inner). A matrix function $N \in \mathcal { R } \mathcal { L } _ { \infty }$ is called all-pass if N is square and $N ^ { \sim } N = I ;$ clearly a square inner function is all-pass. We will focus on the characterizations of inner functions here, and the properties of co-inner functions follow by duality.

Note that N inner implies that N has at least as many rows as columns. For N inner and any $q \in \mathbb { C } ^ { m } , v \in \mathcal { L } _ { 2 } , \| N ( j \omega ) q \| = \| q \|$ , ∀ω and $\lVert N v \rVert _ { 2 } = \lVert v \rVert _ { 2 }$ since $N ( j \omega ) ^ { * } N ( j \omega ) = I$ for all ω. Because of these norm preserving properties, inner matrices will play an important role in the control synthesis theory in this book. In this section, we present a state-space characterization of inner transfer functions.

Lemma 12.8 Suppose $N = \left[ { \frac { A \ } { C \ } } { \frac { B } { D } } \right] \in { \mathcal { R H } } _ { \infty }$ and $X = X ^ { * } \geq 0$ satisfies

$$A ^ {*} X + X A + C ^ {*} C = 0. \tag {12.19}$$

Then

(a) $D ^ { * } C + B ^ { * } X = 0$ implies $N ^ { \sim } N = D ^ { \ast } D$   
(b) (A, B) is controllable, and $N ^ { \sim } N = D ^ { \ast } D$ implies that $D ^ { * } C + B ^ { * } X = 0$

Proof. Conjugating the states of

$$
N ^ {\sim} N = \left[ \begin{array}{c c c} A & 0 & B \\ - C ^ {*} C & - A ^ {*} & - C ^ {*} D \\ \hline D ^ {*} C & B ^ {*} & D ^ {*} D \end{array} \right]
$$

$\left[ \begin{array} { c c } { I } & { 0 } \\ { - X } & { I } \end{array} \right]$ on the left and $\left[ \begin{array} { c c } { \boldsymbol { I } } & { \boldsymbol { 0 } } \\ { - \boldsymbol { X } } & { \boldsymbol { I } } \end{array} \right] ^ { - 1 } = \left[ \begin{array} { c c } { \boldsymbol { I } } & { \boldsymbol { 0 } } \\ { \boldsymbol { X } } & { \boldsymbol { I } } \end{array} \right]$

$$
\begin{array}{l} N ^ {\sim} N = \left[ \begin{array}{c c c} A & 0 & B \\ - (A ^ {*} X + X A + C ^ {*} C) & - A ^ {*} & - (X B + C ^ {*} D) \\ \hline B ^ {*} X + D ^ {*} C & B ^ {*} & D ^ {*} D \end{array} \right] \\ = \left[ \begin{array}{c c c} A & 0 & B \\ 0 & - A ^ {*} & - (X B + C ^ {*} D) \\ \hline B ^ {*} X + D ^ {*} C & B ^ {*} & D ^ {*} D \end{array} \right]. \\ \end{array}
$$

Then (a) and (b) follow easily.

✷
