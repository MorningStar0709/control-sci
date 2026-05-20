# 7.4 Frequency-Weighted Balanced Model Reduction

This section considers the extension of the balanced truncation method to the frequencyweighted case. Given the original full-order model $G \in \mathcal { R } \mathcal { H } _ { \infty }$ , the input weighting matrix $W _ { i } \in \mathcal { R } \mathcal { H } _ { \infty }$ , and the output weighting matrix $W _ { o } \in \mathcal { R } \mathcal { H } _ { \infty }$ , our objective is to find a lower-order model $G _ { r }$ such that

$$\left\| W _ {o} (G - G _ {r}) W _ {i} \right\| _ {\infty}$$

is made as small as possible. Assume that $G , W _ { i }$ , and $W _ { o }$ have the following state-space realizations:

$$
G = \left[ \begin{array}{c c} A & B \\ \hline C & 0 \end{array} \right], W _ {i} = \left[ \begin{array}{c c} A _ {i} & B _ {i} \\ \hline C _ {i} & D _ {i} \end{array} \right], W _ {o} = \left[ \begin{array}{c c} A _ {o} & B _ {o} \\ \hline C _ {o} & D _ {o} \end{array} \right]
$$

with $A \in \mathbb { R } ^ { n \times n }$ . Note that there is no loss of generality in assuming $D = G ( \infty ) = 0$ since otherwise it can be eliminated by replacing $G _ { r }$ with $D + G _ { r }$ .

Now the state-space realization for the weighted transfer matrix is given by

$$
W _ {o} G W _ {i} = \left[ \begin{array}{c c c c} A & 0 & B C _ {i} & B D _ {i} \\ B _ {o} C & A _ {o} & 0 & 0 \\ 0 & 0 & A _ {i} & B _ {i} \\ \hline D _ {o} C & C _ {o} & 0 & 0 \end{array} \right] =: \left[ \begin{array}{c c} \bar {A} & \bar {B} \\ \hline \bar {C} & 0 \end{array} \right]
$$

Let $\bar { P }$ and $\bar { Q }$ be the solutions to the following Lyapunov equations:

$$\bar {A} \bar {P} + \bar {P} \bar {A} ^ {*} + \bar {B} \bar {B} ^ {*} = 0 \tag {7.17}\bar {Q} \bar {A} + \bar {A} ^ {*} \bar {Q} + \bar {C} ^ {*} \bar {C} = 0 \tag {7.18}$$

Then the input weighted Gramian $P$ and the output weighted Gramian $Q$ are defined by

$$
P := \left[ \begin{array}{c c} I _ {n} & 0 \end{array} \right] \bar {P} \left[ \begin{array}{c} I _ {n} \\ 0 \end{array} \right], Q := \left[ \begin{array}{c c} I _ {n} & 0 \end{array} \right] \bar {Q} \left[ \begin{array}{c} I _ {n} \\ 0 \end{array} \right]
$$

It can be shown easily that $P$ and $Q$ satisfy the following lower-order equations:
