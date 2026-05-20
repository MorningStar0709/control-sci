# 6.2.2 Decentralized Control

Centralized and decentralized control define the two extremes in distributing the decision making in a large-scale system. Centralized control has full information and optimizes the full control problem over all decision variables. Decentralized control, on the other hand, optimizes only the local objectives and has no information about the actions of the other subsystems. Player one’s objective function is

$$V _ {1} \left(x _ {1} (0), \mathbf {u} _ {1}\right) = \sum_ {k = 0} ^ {N - 1} \ell_ {1} \left(x _ {1} (k), u _ {1} (k)\right) + V _ {1 f} \left(x _ {1} (N)\right)$$

We then have player one’s decentralized control problem

$$\min _ {\mathbf {u} _ {1}} V _ {1} (x _ {1} (0), \mathbf {u} _ {1})\text { s.t. } x _ {1} ^ {+} = A _ {1} x _ {1} + \overline {{B}} _ {1 1} u _ {1}$$

We know the optimal solution for this kind of LQ problem is a linear feedback law

$$u _ {1} ^ {0} = K _ {1} x _ {1} (0)$$

Notice that in decentralized control, player one’s model does not account for the inputs of player two, and already contains model error. In the decentralized problem, player one requires no information about player two. The communication overhead for decentralized control is therefore minimal, which is an implementation advantage, but the resulting performance may be quite poor for systems with reasonably strong coupling. We compute an optimal $K _ { 1 }$ for system one $( A _ { 1 } , \overline { { B } } _ { 1 1 } , Q _ { 1 } , R _ { 1 } )$ and optimal $K _ { 2 }$ for system 2. The closed-loop system evolution is then

$$
\left[ \begin{array}{c} x _ {1} \\ x _ {2} \end{array} \right] ^ {+} = \left[ \begin{array}{c c} A _ {1} + \overline {{B}} _ {1 1} K _ {1} & \overline {{B}} _ {1 2} K _ {2} \\ \overline {{B}} _ {2 1} K _ {1} & A _ {2} + \overline {{B}} _ {2 2} K _ {2} \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \end{array} \right]
$$

and we know only that $A _ { 1 1 } + \overline { { B } } _ { 1 1 } K _ { 1 }$ and $A _ { 2 2 } + \overline { { B } } _ { 2 2 } K _ { 2 }$ are stable matrices. Obviously the stability of the closed-loop, decentralized system is fragile and depends in a sensitive way on the sizes of the interaction terms $\overline { { B } } _ { 1 2 }$ and $\overline { { B } } _ { 2 1 }$ and feedback gains $K _ { 1 } , K _ { 2 }$ .
