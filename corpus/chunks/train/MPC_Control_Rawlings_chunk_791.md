Any face F of $\mathcal { U } ( x )$ with dimension d $\cdot \in \left\{ 1 , 2 , \ldots , m \right\}$ satisfies $M _ { i } u =$ $N _ { i } x + p _ { i }$ for all $i \in I _ { F }$ , all $u \in F$ for some index set $I _ { F } \subseteq \mathbb { I } _ { 1 : p }$ . The matrix $M _ { I _ { F } }$ with rows $M _ { i } , i \in I _ { F }$ , has rank $m - d$ , and the face F is defined by

$$F := \{u \mid M _ {i} u = N _ {i} x + p _ {i}, i \in I _ {F} \} \cap \mathcal {U} (x)$$

When $u ^ { 0 } ( x )$ is not unique, it is a face of dimension $d \ge 1$ and the set $I ^ { 0 } ( x )$ of active constraints is defined by

$$I ^ {0} (x) := \{i \mid M _ {i} u = N _ {i} x + p _ {i} \forall u \in u ^ {0} (x) \} = \{i \mid i \in I (x, u) \forall u \in u ^ {0} (x) \}$$

The set $\{ u \ | \ M _ { i } u = N _ { i } x + p _ { i } , \ i \in I ^ { 0 } ( x ) \}$ is an affine hyperplane in which $u ^ { 0 } ( x )$ lies. See Figure 7.8 where $u ^ { 0 } ( x _ { 1 } )$ is unique, a vertex of $\mathcal { U } ( x _ { 1 } )$ , and $I ^ { 0 } ( x _ { 1 } ) = \{ 2 , 3 \}$ . If, in Figure 7.8, $\boldsymbol { r } = - \boldsymbol { e } _ { 1 }$ , then $u ^ { 0 } ( x _ { 1 } ) = F _ { 2 } ( x _ { 1 } )$ , a face of dimension $1 ; u ^ { 0 } ( x _ { 1 } )$ is, therefore, set valued. Since u $\in \mathbb { R } ^ { m }$ where m $= 2 , u ^ { 0 } ( x _ { 1 } )$ is a facet, i.e., a face of dimension m−1 = 1. Thus $u ^ { 0 } ( x _ { 1 } )$ is a set defined by $u ^ { 0 } ( x _ { 1 } ) \ = \ \{ u \ \vert \ M _ { 1 } u \ \le N _ { 1 } x _ { 1 } + p _ { 1 } , \ M _ { 2 } u \ =$ $N _ { 2 } x _ { 1 } + p _ { 2 } , M _ { 3 } u \le N _ { 3 } x _ { 1 } + p _ { 3 } \}$ .

At each z = (x, u) ∈ Z, i.e., for each $( x , u )$ such that $x \in \ b { X }$ and $u \in \mathcal { U } ( x )$ , the cone $C ( z ) = C ( x , u )$ of first-order feasible variations is defined, as before, by

$$C (z) := \{h \in \mathbb {R} ^ {m} \mid M _ {i} h \leq 0, i \in I (z) \} = \{h \in \mathbb {R} ^ {m} \mid M _ {I (z)} h \leq 0 \}$$

If $I ( z ) = I ( x , u ) = \emptyset$ (no constraints are active), $C ( z ) = \mathbb { R } ^ { m }$ (all variations are feasible).

Since $u \mapsto V ( x , \cdot )$ is convex and differentiable, and $\mathcal { U } ( x )$ is polyhedral for all x, the parametric linear program $\mathbb { P } ( x )$ satisfies the assumptions of Proposition 7.8. Hence, repeating Proposition 7.8 for convenience, we have

Proposition 7.19 (Optimality conditions for parametric linear program). A necessary and sufficient condition for u to be a minimizer for the parametric linear program $\mathbb { P } ( x )$ is

$$u \in \mathcal {U} (x) \text { and } - \nabla_ {u} V (x, u) \in C ^ {*} (x, u)$$

where $\nabla _ { u } V ( x , u ) = r$ and $C ^ { * } ( x , u )$ is the polar cone of $C ( x , u )$ .

An important difference between this result and that for the parametric quadratic program is that $\nabla _ { u } V ( x , u ) = r$ and, therefore, does not vary with x or u. We now use this result to show that both $V ^ { 0 } ( \cdot )$ and $u ^ { 0 } ( \cdot )$ are piecewise affine. We consider the simple case when $u ^ { 0 } ( x )$ is unique for all $x \in { \mathcal { X } }$ .
