# Any Stage $k$

Now we are in a position to generalize the previous set of relations for any $k$ . Thus, the optimal control is given by

$$\mathbf {u} ^ {*} (k) = - \mathbf {L} (k) \mathbf {x} ^ {*} (k), \tag {6.3.28}$$

where, the Kalman gain $\mathbf{L}(k)$ is given by

$$\mathbf {L} (k) = \left[ \mathbf {R} + \mathbf {B} ^ {\prime} \mathbf {P} (k + 1) \mathbf {B} \right] ^ {- 1} \mathbf {B} ^ {\prime} \mathbf {P} (k + 1) \mathbf {A}, \tag {6.3.29}$$

the matrix $\mathbf{P}(k)$ , also called the Riccati matrix, is the backward solution of

$$
\begin{array}{l} \mathbf {P} (k) = \left[ \mathbf {A} - \mathbf {B L} (k) \right] ^ {\prime} \mathbf {P} (k + 1) [ \mathbf {A} - \mathbf {B L} (k) ] \\ + \mathbf {L} ^ {\prime} (k) \mathbf {R L} (k) + \mathbf {Q} \tag {6.3.30} \\ \end{array}
$$

with the final condition $\mathbf{P}(k_f) = \mathbf{F}$ , and the optimal cost function as

$$J _ {k} ^ {*} = \frac {1}{2} \mathbf {x} ^ {* \prime} (k) \mathbf {P} (k) \mathbf {x} ^ {*} (k). \tag {6.3.31}$$

We notice that these are the same set of relations we obtained in Chapter 5 by using Pontryagin principle.
