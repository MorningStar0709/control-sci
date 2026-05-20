# Exercise 6.16: Monotonically decreasing cost

Consider again the iteration defined in Exercise 6.15.

(a) Prove that the cost function is monotonically decreasing when optimizing one variable at a time

$$V (u ^ {p + 1}) < V (u ^ {p}) \quad \forall u ^ {p} \neq - H ^ {- 1} c$$

(b) Show that the following expression gives the size of the decrease

$$V (u ^ {p + 1}) - V (u ^ {p}) = - (1 / 2) (u ^ {p} - u ^ {*}) ^ {\prime} P (u ^ {p} - u ^ {*})$$

in which

$$
P = H D ^ {- 1} \tilde {H} D ^ {- 1} H \qquad \tilde {H} = D - N \qquad D = \left[ \begin{array}{c c} H _ {1 1} & 0 \\ 0 & H _ {2 2} \end{array} \right] \qquad N = \left[ \begin{array}{c c} 0 & H _ {1 2} \\ H _ {2 1} & 0 \end{array} \right]
$$

and $u ^ { * } = - H ^ { - 1 } c$ is the optimum.

Hint: to simplify the algebra, first change coordinates and move the origin of the coordinate system to $u ^ { * }$ .
