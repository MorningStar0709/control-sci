# 6.2 Unconstrained Two-Player Game

To introduce clearly the concepts and notation required to analyze distributed MPC, we start with a two-player game. We then generalize to an M-player game in the next section.

Let $( A _ { 1 1 } , B _ { 1 1 } , C _ { 1 1 } )$ be a minimal state space realization of the $( u _ { 1 } , y _ { 1 } )$ input-output pair. Similarly, let $( A _ { 1 2 } , B _ { 1 2 } , C _ { 1 2 } )$ be a minimal state space realization of the $( u _ { 2 } , y _ { 1 } )$ input-output pair. The dimensions are $u _ { 1 } \in$ $\mathbb { R } ^ { m _ { 1 } } , y _ { 1 } \in \mathbb { R } ^ { p _ { 1 } } , x _ { 1 1 } \in \mathbb { R } ^ { n _ { 1 1 } } , x _ { 1 2 } \in \mathbb { R } ^ { n _ { 1 2 } }$ with $n _ { 1 } = n _ { 1 1 } + n _ { 1 2 }$ . Output $y _ { 1 }$ can then be represented as the following, possibly nonminimal, state space model

$$
\begin{array}{l} \left[ \begin{array}{c} x _ {1 1} \\ x _ {1 2} \end{array} \right] ^ {+} = \left[ \begin{array}{c c} A _ {1 1} & 0 \\ 0 & A _ {1 2} \end{array} \right] \left[ \begin{array}{c} x _ {1 1} \\ x _ {1 2} \end{array} \right] + \left[ \begin{array}{c} B _ {1 1} \\ 0 \end{array} \right] u _ {1} + \left[ \begin{array}{c} 0 \\ B _ {1 2} \end{array} \right] u _ {2} \\ y _ {1} = \left[ \begin{array}{c c} C _ {1 1} & C _ {1 2} \end{array} \right] \left[ \begin{array}{c} x _ {1 1} \\ x _ {1 2} \end{array} \right] \\ \end{array}
$$

Proceeding in an analogous fashion with output $y _ { 2 }$ and inputs $u _ { 1 }$ and $u _ { 2 }$ , we model $y _ { 2 }$ with the following state space model

$$
\begin{array}{l} \left[ \begin{array}{c} x _ {2 2} \\ x _ {2 1} \end{array} \right] ^ {+} = \left[ \begin{array}{c c} A _ {2 2} & 0 \\ 0 & A _ {2 1} \end{array} \right] \left[ \begin{array}{c} x _ {2 2} \\ x _ {2 1} \end{array} \right] + \left[ \begin{array}{c} B _ {2 2} \\ 0 \end{array} \right] u _ {2} + \left[ \begin{array}{c} 0 \\ B _ {2 1} \end{array} \right] u _ {1} \\ y _ {2} = \left[ \begin{array}{c c} C _ {2 2} & C _ {2 1} \end{array} \right] \left[ \begin{array}{c} x _ {2 2} \\ x _ {2 1} \end{array} \right] \\ \end{array}
$$

We next define player one’s local cost functions

$$V _ {1} (x _ {1} (0), \mathbf {u} _ {1}, \mathbf {u} _ {2}) = \sum_ {k = 0} ^ {N - 1} \ell_ {1} (x _ {1} (k), u _ {1} (k)) + V _ {1 f} (x _ {1} (N))$$

in which

$$
x _ {1} = \left[ \begin{array}{c} x _ {1 1} \\ x _ {1 2} \end{array} \right]
$$

Note that the first local objective is affected by the second player’s inputs through the model evolution of $x _ { 1 } , \mathbf { i . e . }$ , through the $x _ { 1 2 }$ states. We choose the stage cost to account for the first player’s inputs and outputs
