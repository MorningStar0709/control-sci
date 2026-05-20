# C.2.7 Constraint Set Defined by Equalities and Inequalities

Finally, we consider the case when the set U is specified by a set of differentiable equalities and inequalities:

$$U := \{u \mid g _ {i} (u) \leq 0 \forall i \in \mathcal {I}, h _ {i} (u) = 0 \forall i \in \mathcal {E} \}$$

where, for each $i \in { \mathcal { I } }$ , the function $g _ { i } : \mathbb { R } ^ { m }  \mathbb { R }$ is differentiable and for each $i \in { \mathcal { F } }$ , the function $h _ { i } : \mathbb { R } ^ { m }  \mathbb { R }$ is differentiable. For each $u \in U$

$$\mathcal {I} ^ {0} (u) := \{i \in \mathcal {I} \mid g _ {i} (u) = 0 \}$$

the index set of active inequality constraints is defined as before. We wish to obtain necessary conditions for the problem of minimizing a differentiable function $f ( \cdot )$ over the set U. The presence of equality constraints makes this objective more difficult than for the case when U is defined merely by differentiable inequalities. The result we wish to prove is a natural extension of Proposition C.21 in which the equality constraints are included in the set of active constraints:

Proposition C.22 (Fritz-John necessary conditions). Suppose u is a local minimizer for the problem of minimizing $f ( u )$ subject to the constraint $u \in U$ where U is defined in (C.22). Then there exist multipliers $\mu _ { 0 }$ , $\mu _ { i } , ~ i \in \mathcal { I }$ and $\lambda _ { i } , ~ i \in { \mathcal { F } }$ , not all zero, such that

$$\mu_ {0} \nabla f (u) + \sum_ {i \in \mathcal {I}} \mu_ {i} \nabla g _ {i} (u) + \sum_ {j \in \mathcal {E}} \lambda_ {j} \nabla h _ {j} (u) = 0 \tag {C.26}$$

and

$$\mu_ {i} g _ {i} (u) = 0 \forall i \in \mathcal {I}$$

where $\mu _ { 0 } \geq 0$ and $\mu _ { i } \geq 0$ for all $i \in \mathcal { I } ^ { 0 }$ .

The condition $\mu _ { i } g _ { i } ( u ) = 0$ for all $i \in { \mathcal { I } }$ is known as the complementarity conditions and implies $\mu _ { i } = 0$ for all $i \in { \mathcal { I } }$ such that $g _ { i } ( u ) < 0$ . If $\mu _ { 0 } > 0$ , then (C.26) may be normalized by dividing each term by µ0 yielding the more familiar expression

$$\nabla f (u) + \sum_ {i \in \mathcal {I}} \mu_ {i} \nabla g _ {i} (u) + \sum_ {j \in \mathcal {E}} \nabla h _ {j} (u) = 0$$
