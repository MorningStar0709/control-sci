# 6.2.3 Noncooperative Game

In the noncooperative game, player one optimizes $V _ { 1 } ( x _ { 1 } ( 0 ) , { \mathbf { u } } _ { 1 } , { \mathbf { u } } _ { 2 } )$ over $\mathbf { u } _ { 1 }$ and player two optimizes $V _ { 2 } ( x _ { 2 } ( 0 ) , { \mathbf { u } } _ { 1 } , { \mathbf { u } } _ { 2 } )$ over $\mathbf { u } _ { 2 }$ . From player one’s perspective, player two’s planned inputs $\mathbf { u } _ { 2 }$ are known disturbances affecting player one’s output through the dynamic model. Part of player one’s optimal control problem is therefore to compensate for player two’s inputs with his optimal $\mathbf { u } _ { 1 }$ sequence in order to optimize his local objective $V _ { 1 }$ . Similarly, player two considers player $\mathrm { o n e ^ { \prime } s }$ inputs as a known disturbance and solves an optimal control problem that removes their effect in his local objective $V _ { 2 }$ . Because this game is noncooperative $( V _ { 1 } \neq V _ { 2 } )$ , the struggle between players one and two can produce an outcome that is bad for both of them as we show subsequently. Notice that unlike decentralized control, there is no model error in the noncooperative game. Player one knows exactly the effect of the actions of player two and vice versa. Any poor nominal performance is caused by the noncooperative game, not model error.

Summarizing the noncooperative control problem statement, player one’s model is

$$x _ {1} ^ {+} = A _ {1} x _ {1} + \overline {{B}} _ {1 1} u _ {1} + \overline {{B}} _ {1 2} u _ {2}$$

and player one’s objective function is

$$V _ {1} \left(x _ {1} (0), \mathbf {u} _ {1}, \mathbf {u} _ {2}\right) = \sum_ {k = 0} ^ {N - 1} \ell_ {1} \left(x _ {1} (k), u _ {1} (k)\right) + V _ {1 f} \left(x _ {1} (N)\right)$$

Note that $V _ { 1 }$ here depends on $\mathbf { u } _ { 2 }$ because the state trajectory $x _ { 1 } ( k ) , k \geq$ 1 depends on $\mathbf { u } _ { 2 }$ as shown in player one’s dynamic model. We then have player one’s noncooperative control problem

$$
\begin{array}{l} \min _ {\mathbf {u} _ {1}} V _ {1} (x _ {1} (0), \mathbf {u} _ {1}, \mathbf {u} _ {2}) \\ \text { s.t. } x _ {1} ^ {+} = A _ {1} x _ {1} + \overline {{B}} _ {1 1} u _ {1} + \overline {{B}} _ {1 2} u _ {2} \\ \end{array}
$$

Solution to player one’s optimal control problem. We now solve player one’s optimal control problem. Proceeding as in Section 6.1.1 we define
