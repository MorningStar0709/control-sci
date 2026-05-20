# Exercise 6.24: Optimality conditions for constrained optimization

Consider the convex quadratic optimization problem

$$\min _ {u} V (u) \quad \text { subject to } \quad u \in \mathbb {U}$$

in which V is a convex quadratic function and U is a convex set. Show that $u ^ { * }$ is an optimal solution if and only if

$$\langle z - u ^ {*}, - \nabla V | _ {u ^ {*}} \rangle \leq 0 \quad \forall z \in \mathbb {U} \tag {6.32}$$

Figure 6.9(a) depicts this condition for $u \in \mathbb { R } ^ { 2 }$ . This condition motivates defining the normal cone (Rockafellar, 1970) to U at $u ^ { * }$ as follows

$$N (\mathbb {U}, u ^ {*}) = \{y \mid \langle z - u ^ {*}, y - u ^ {*} \rangle \leq 0 \quad \forall z \in \mathbb {U} \}$$

The optimality condition can be stated equivalently as $u ^ { * }$ is an optimal point if and only if the negative gradient is in the normal cone to U at u∗

$$- \nabla V | _ {u ^ {*}} \in N (\mathbb {U}, u ^ {*})$$

This condition and the normal cone are depicted in Figure 6.9(b).
