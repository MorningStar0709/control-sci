and (1.58) again gives the necessary and sufficient conditions for the optimal solution

$$
\left[ \begin{array}{c c} \tilde {H} & - D ^ {\prime} \\ - D & 0 \end{array} \right] \left[ \begin{array}{l} \mathbf {z} \\ \boldsymbol {\lambda} \end{array} \right] = \left[ \begin{array}{c} 0 \\ - \tilde {A} _ {1} \end{array} \right] x _ {1} (0) + \left[ \begin{array}{c} - \tilde {A} _ {2} \\ 0 \end{array} \right] x _ {2} (0) + \left[ \begin{array}{c} - \tilde {B} _ {2 2} \\ - \tilde {B} _ {1 2} \end{array} \right] \mathbf {u} _ {2} \tag {6.13}
$$

in which

$$
\tilde {H} = H + E ^ {\prime} \mathcal {B} _ {2 1} ^ {\prime} \mathcal {Q} _ {2} \mathcal {B} _ {2 1} E \quad \tilde {B} _ {2 2} = E ^ {\prime} \mathcal {B} _ {2 1} ^ {\prime} \mathcal {Q} _ {2} \mathcal {B} _ {2 2} \quad \tilde {A} _ {2} = E ^ {\prime} \mathcal {B} _ {2 1} ^ {\prime} \mathcal {Q} _ {2} \mathcal {A} _ {2}
E = I _ {N} \otimes \left[ \begin{array}{c c} I _ {m _ {1}} & 0 _ {m _ {1}, n _ {1}} \end{array} \right]
$$

See also Exercise 6.13 for details on constructing the padding matrix E. Comparing the cooperative and noncooperative dynamic games, (6.13) and (6.12), we see the cooperative game has made three changes: (i) the quadratic penalty H has been modified, (ii) the effect of $x _ { 2 } ( 0 )$ has been included with the term $\tilde { \boldsymbol { A } } _ { 2 }$ , and (iii) the influence of $\mathbf { u } _ { 2 }$ has been modified with the term $\tilde { B } _ { 2 2 }$ . Notice that the size of the vector z has not changed, and we have accomplished the goal of keeping player $\mathrm { o n e ^ { \prime } s }$ dynamic model in the cooperative game the same size as his dynamic model in the noncooperative game.

Regardless of the implementation choice, the cooperative optimal control problem is no more complex than the noncooperative game considered previously. The extra information required by player one in the cooperative game is $x _ { 2 } ( 0 )$ . Player one requires $\mathbf { u } _ { 2 }$ in both the cooperative and noncooperative games. Only in decentralized control does player one not require player two’s input sequence $\mathbf { u } _ { 2 }$ . The other extra required information, $A _ { 2 } , B _ { 2 1 } , Q _ { 2 } , R _ { 2 } , P _ { 2 f }$ , are fixed parameters and making their values available to player one is a minor communication overhead.

Proceeding as before, we solve this equation for $\mathbf { z } ^ { 0 }$ and pick out the rows corresponding to the elements of ${ \bf u } _ { 1 } ^ { 0 }$ giving
