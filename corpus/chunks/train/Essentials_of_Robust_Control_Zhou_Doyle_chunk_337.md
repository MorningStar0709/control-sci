and $e \in \mathcal { L } _ { 2 } [ 0 , \infty )$ . Therefore, $x = e + \hat { x } \in \mathcal { L } _ { 2 } [ 0 , \infty )$ . It is easy to see that $e ( t ) \to 0$ as $t \to \infty$ for any initial condition e(0). Finally, $x ( t ) \to 0$ since $\hat { x } \to 0$ . ✷

Theorem 13.2 There exists a unique optimal control for the $L Q R$ problem, namely $u = F x$ . Moreover,

$$\min _ {u \in \mathcal {L} _ {2} [ 0, \infty)} \| z \| _ {2} = \| G _ {c} x _ {0} \| _ {2}.$$

Note that the optimal control strategy is a constant gain state feedback, and this gain is independent of the initial condition $x _ { 0 }$ .

Proof. With the change of variable $v = u - F x$ , the system can be written as

$$
\left[ \begin{array}{l} \dot {x} \\ z \end{array} \right] = \left[ \begin{array}{c c} A _ {F} & B _ {2} \\ C _ {F} & D _ {1 2} \end{array} \right] \left[ \begin{array}{l} x \\ v \end{array} \right], \quad x (0) = x _ {0}. \tag {13.12}
$$

Now if $v \in \mathcal { L } _ { 2 } [ 0 , \infty )$ , then $x , z \ \in \ \mathcal { L } _ { 2 } [ 0 , \infty )$ and $x ( \infty ) = 0$ since $A _ { F }$ is stable. Hence $u = F x + v \in \mathcal { L } _ { 2 } [ 0 , \infty )$ . Conversely, if $u , z \in \mathcal { L } _ { 2 } [ 0 , \infty )$ , then from Lemma 13.1 $x \in \mathcal { L } _ { 2 } [ 0 , \infty )$ . So $v \in \mathcal { L } _ { 2 } [ 0 , \infty )$ . Thus the mapping $v = u - F x$ between $v \in \mathcal { L } _ { 2 } [ 0 , \infty )$ and those $u \in \mathcal { L } _ { 2 } [ 0 , \infty )$ that make $z \in \mathcal { L } _ { 2 } [ 0 , \infty )$ is one-to-one and onto. Therefore,

$$\min _ {u \in \mathcal {L} _ {2} [ 0, \infty)} \| z \| _ {2} = \min _ {v \in \mathcal {L} _ {2} [ 0, \infty)} \| z \| _ {2}.$$

By differentiating $x ( t ) ^ { * } X x ( t )$ with respect to t along a solution of the differential equation (13.12) and by using equation (13.9) and the fact that $C _ { F } ^ { * } D _ { 1 2 } = - X B _ { 2 }$ , we see that

$$
\begin{array}{l} \frac {d}{d t} x ^ {*} X x = \dot {x} ^ {*} X x + x ^ {*} X \dot {x} = x ^ {*} (A _ {F} ^ {*} X + X A _ {F}) x + 2 x ^ {*} X B _ {2} v \\ { = } { - x ^ { * } C _ { F } ^ { * } C _ { F } x + 2 x ^ { * } X B _ { 2 } v } \\ = - \left(C _ {F} x + D _ {1 2} v\right) ^ {*} \left(C _ {F} x + D _ {1 2} v\right) + 2 x ^ {*} C _ {F} ^ {*} D _ {1 2} v + v ^ {*} v + 2 x ^ {*} X B _ {2} v \\ = - \| z \| ^ {2} + \| v \| ^ {2}. \tag {13.13} \\ \end{array}
$$

Now integrate equation (13.13) from 0 to ∞ to get

$$\| z \| _ {2} ^ {2} = x _ {0} ^ {*} X x _ {0} + \| v \| _ {2} ^ {2}.$$

Clearly, the unique optimal control is $v = 0 , { \mathrm { i . e . , } } u = F x .$
