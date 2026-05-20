# Exercise C.1: Nested optimization and switching order of optimization

Consider the optimization problem in two variables

$$\min _ {(x, y) \in \mathbb {Z}} V (x, y)$$

in which $x \in \mathbb { R } ^ { n } , y \in \mathbb { R } ^ { m }$ , and $V : \mathbb { R } ^ { n } \times \mathbb { R } ^ { m } \to \mathbb { R }$ . Assume this problem has a solution. This assumption is satisfied, for example, if V is continuous and Z is compact, but, in general, we do not require either of these conditions.

Define the following four sets

$$\mathbb {X} (y) = \{x \mid (x, y) \in \mathbb {Z} \} \quad \mathbb {Y} (x) = \{y \mid (x, y) \in \mathbb {Z} \}\mathbb {B} = \{y \mid \mathbb {X} (y) \neq \emptyset \} \quad \mathbb {A} = \{x \mid \mathbb {Y} (x) \neq \emptyset \}$$

Note that A and B are the projections of Z onto $\mathbb { R } ^ { n }$ and $\mathbb { R } ^ { m }$ , respectively. Projection is defined in Section C.3. Show the solutions of the following two nested optimization problems exist and are equal to the solution of the original problem

$$\min _ {x \in \mathbb {A}} \left(\min _ {y \in \mathbb {Y} (x)} V (x, y)\right)\min _ {y \in \mathbb {B}} \left(\min _ {x \in \mathbb {X} (y)} V (x, y)\right)$$
