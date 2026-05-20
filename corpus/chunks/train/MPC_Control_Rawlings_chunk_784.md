$$I _ {i} (x, u) := \{j \mid M _ {j} ^ {i} u = N _ {j} ^ {i} x + p _ {j} ^ {i} \}, I _ {i} ^ {0} (x) := I _ {i} (x, u _ {i} ^ {0} (x))$$

denote, respectively, the active constraint set at $( x , u ) \in \mathbb { Z } _ { i }$ and the active constraint set for $\mathbb { P } _ { i } ( x )$ . Because we now use subscript i to specify $\mathbb { Z } _ { i }$ , we change our notation slightly and now let $C _ { i } ( x , u )$ denote the cone of first-order feasible variations for $\mathbb { P } _ { i } ( x )$ at $u \in { \mathcal { U } } _ { i } ( x )$ , i.e.,

$$C _ {i} (x, u) := \{h \in \mathbb {R} ^ {m} \mid M _ {j} ^ {i} h \leq 0 \forall j \in I _ {i} (x, u) \}$$

Similarly, we define the polar cone $C _ { i } ^ { * } ( x , u )$ of the cone $C _ { i } ( x , u )$ at

h = 0 by

$$
\begin{array}{l} C _ {i} ^ {*} (x, u) := \left\{v \in \mathbb {R} ^ {m} \mid v ^ {\prime} h \leq 0 \forall h \in C _ {i} (x, u) \right\} \\ = \left\{\sum_ {j \in I _ {i} (x, u)} \left(M _ {j} ^ {i}\right) ^ {\prime} \lambda_ {j} \mid \lambda_ {j} \geq 0, j \in I _ {i} (x, u) \right\} \\ \end{array}
$$

As shown in Proposition $7 . 7 ,$ a necessary and sufficient condition for the optimality of u for problem $\mathbb { P } _ { i } ( x )$ is

$$- \nabla_ {u} V _ {i} (x, u) \in C _ {i} ^ {*} (x, u), \quad u \in \mathcal {U} _ {i} (x) \tag {7.15}$$

If u lies in the interior of $\mathcal { U } _ { i } ( x )$ so that $I _ { i } ^ { 0 } ( x ) = \emptyset$ , condition (7.15) reduces to $\nabla _ { u } V _ { i } ( x , u ) = 0$ . For any $x \in { \mathcal { X } }$ , the solution $u ^ { 0 } ( x )$ of the piecewise parametric program $\mathbb { P } ( x )$ satisfies

$$M _ {j} ^ {i} u = N _ {j} ^ {i} x + p _ {j} ^ {i}, \forall j \in I _ {i} ^ {0} (x), \forall i \in S ^ {0} (x) \tag {7.16}$$

To simplify our notation, we rewrite the equality constraint (7.16) as

$$E _ {x} u = F _ {x} x + g _ {x}$$

where the subscript x denotes the fact that the constraints are precisely those constraints that are active for the problems $\mathbb { P } _ { i } ( x ) , i \in S ^ { 0 } ( x )$ . The fact that $u ^ { 0 } ( x )$ satisfies these constraints and is, therefore, the unique solution of the optimization problem

$$V ^ {0} (x) = \min _ {u} \{V (x, u) \mid E _ {x} u = F _ {x} x + g _ {x} \}$$

motivates us to define the equality constrained problem $\mathbb { P } _ { x } ( \boldsymbol { w } )$ for $w \in$ X near x by

$$V _ {x} ^ {0} (w) = \min _ {u} \{V _ {x} (w, u) \mid E _ {x} u = F _ {x} w + g _ {x} \}$$
