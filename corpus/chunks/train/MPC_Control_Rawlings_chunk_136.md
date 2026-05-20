# Exercise 1.18: Minimizing a partitioned quadratic function

Consider the partitioned constrained minimization

$$
\min _ {x _ {1}, x _ {2}} \left[ \begin{array}{c} x _ {1} \\ x _ {2} \end{array} \right] ^ {\prime} \left[ \begin{array}{c c} H _ {1} & \\ & H _ {2} \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \end{array} \right]
$$

subject to

$$
\left[ \begin{array}{c c} D & I \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \end{array} \right] = d
$$

The solution to this optimization is required in two different forms, depending on whether one is solving an estimation or regulation problem. Show that the solution can be expressed in the following two forms if both $H _ { 1 }$ and $H _ { 2 }$ are full rank.

• Regulator form

$$V ^ {0} (d) = d ^ {\prime} (H _ {2} - H _ {2} D (D ^ {\prime} H _ {2} D + H _ {1}) ^ {- 1} D ^ {\prime} H _ {2}) dx _ {1} ^ {0} (d) = \tilde {K} d \quad \tilde {K} = \left(D ^ {\prime} H _ {2} D + H _ {1}\right) ^ {- 1} D ^ {\prime} H _ {2}x _ {2} ^ {0} (d) = (I - D \tilde {K}) d$$

• Estimator form

$$V ^ {0} (d) = d ^ {\prime} \left(D H _ {1} ^ {- 1} D ^ {\prime} + H _ {2} ^ {- 1}\right) ^ {- 1} dx _ {1} ^ {0} (d) = \tilde {L} d \quad \tilde {L} = H _ {1} ^ {- 1} D ^ {\prime} (D H _ {1} ^ {- 1} D ^ {\prime} + H _ {2} ^ {- 1}) ^ {- 1}x _ {2} ^ {0} (d) = (I - D \tilde {L}) d$$
