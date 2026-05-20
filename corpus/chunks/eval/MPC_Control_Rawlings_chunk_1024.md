# Exercise C.6: Dual problems and duality gap

Consider again the constrained optimization problem of Exercise C.5

$$\min _ {x \in \mathbb {R} ^ {n}} V (x) \quad \text { subject to } g (x) = 0$$

and its equivalent minmax formulation

$$\min _ {x \in \mathbb {R} ^ {n}} \max _ {\lambda \in \mathbb {R} ^ {m}} L (x, \lambda)$$

Switching the order of optimization gives the maxmin version of this problem

$$\max _ {\lambda \in \mathbb {R} ^ {m}} \min _ {x \in \mathbb {R} ^ {n}} L (x, \lambda)$$

Next define a new (dual) objective function $\boldsymbol { q } : \mathbb { R } ^ { m }  \mathbb { R }$ as the inner optimization

$$q (\lambda) = \min _ {x \in \mathbb {R} ^ {n}} L (x, \lambda)$$

Then the maxmin problem can be stated as

$$\max _ {\lambda \in \mathbb {R} ^ {m}} q (\lambda) \tag {C.31}$$

Problem (C.31) is known as the dual of the original problem (C.30), and the original problem (C.30) is then denoted as the primal problem in this context (Nocedal and Wright, 2006, p. 343–345), (Boyd and Vandenberghe, 2004, p. 223).

(a) Show that the solution to the dual problem is a lower bound for the solution to the primal problem

$$\max _ {\lambda \in \mathbb {R} ^ {m}} q (\lambda) \leq \min _ {x \in \mathbb {R} ^ {n}} V (x) \quad \text { subject to } g (x) = 0 \tag {C.32}$$

This property is known as weak duality (Nocedal and Wright, 2006, p. 345), (Boyd and Vandenberghe, 2004, p. 225).
