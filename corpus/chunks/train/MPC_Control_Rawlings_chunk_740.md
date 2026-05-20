# Exercise 6.18: Monotonically decreasing cost with convex step

Consider again the problem of optimizing one variable at a time with the convex step given in Exercise 6.17.

(a) Prove that the cost function is monotonically decreasing

$$V (u ^ {p + 1}) < V (u ^ {p}) \quad \forall u ^ {p} \neq - H ^ {- 1} c$$

(b) Show that the following expression gives the size of the decrease

$$V (u ^ {p + 1}) - V (u ^ {p}) = - (1 / 2) \left(u ^ {p} - u ^ {*}\right) ^ {\prime} P \left(u ^ {p} - u ^ {*}\right)$$

in which

$$
P = H D ^ {- 1} \tilde {H} D ^ {- 1} H \quad \tilde {H} = D - N
D = \left[ \begin{array}{c c} w _ {1} ^ {- 1} H _ {1 1} & 0 \\ 0 & w _ {2} ^ {- 1} H _ {2 2} \end{array} \right] \qquad N = \left[ \begin{array}{c c} - w _ {1} ^ {- 1} w _ {2} H _ {1 1} & H _ {1 2} \\ H _ {2 1} & - w _ {1} w _ {2} ^ {- 1} H _ {2 2} \end{array} \right]
$$

and $u ^ { * } = - H ^ { - 1 } c$ is the optimum.

Hint: to simplify the algebra, first change coordinates and move the origin of the coordinate system to $u ^ { * }$ .
