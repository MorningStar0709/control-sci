Finally, assume that the system is input/output-to-state stable (IOSS). This property is given in Definition 2.40 (or Definition B.42). We can then state an MPC stability theorem that applies to the case of unbounded constraint sets.

Theorem 7 (MPC stability – unbounded constraint sets).

(a) Suppose that Assumptions 2.2, 5, 2.12, 2.13, and 6(a) hold and that the system $x ^ { + } \ = \ f ( x , u ) , y \ = \ h ( x )$ is IOSS. Then the origin is asymptotically stable (under Definition 9) with a region of attraction XN for the system $x ^ { + } = f ( x , \kappa _ { N } ( x ) )$ .

(b) Suppose that Assumptions $2 . 2 , \ 5 , \ 2 . 1 2 , \ 2 . 1 3 ,$ and 6(b) hold and that the system $x ^ { + } = f ( x , u ) , y = h ( x )$ is IOSS. Then the origin is exponentially stable with a region of attraction $x _ { N }$ for the system $x ^ { + } = f ( x , \kappa _ { N } ( x ) )$ .

In particular, setting up the MPC theory with these assumptions subsumes the LQR problem as a special case.
