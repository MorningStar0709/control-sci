# Exercise 1.29: Symmetry in regulation and estimation

In this exercise we display the symmetry of the backward DP recursion for regulation, and the forward DP recursion for estimation. In the regulation problem we solve at stage k

$$\min _ {x, u} \ell (z, u) + V _ {k} ^ {0} (x) \quad \text { s . t . } x = A z + B u$$

In backward DP, x is the state at the current stage and z is the state at the previous stage. The stage cost and cost to go are given by

$$\ell (z, u) = (1 / 2) (z ^ {\prime} Q z + u ^ {\prime} R u) \qquad V _ {k} ^ {0} (x) = (1 / 2) x ^ {\prime} \Pi (k) x$$

and the optimal cost is $V _ { k - 1 } ^ { 0 } ( z )$ since z is the state at the previous stage.

In estimation we solve at stage k

$$\min _ {x, w} \ell (z, w) + V _ {k} ^ {0} (x) \quad \text { s.t. } z = A x + w$$

In forward DP, x is the state at the current stage, z is the state at the next stage. The stage cost and arrival cost are given by

$$\ell (z, w) = (1 / 2) \left(\left| y (k + 1) - C z \right| _ {R ^ {- 1}} ^ {2} + w ^ {\prime} Q ^ {- 1} w\right) \quad V _ {k} ^ {0} (x) = (1 / 2) | x - \hat {x} (k) | _ {P (k) - 1} ^ {2}$$

and we wish to find $V _ { k + 1 } ^ { 0 } ( z )$ in the estimation problem.

(a) In the estimation problem, take the z term outside the optimization and solve

$$\min _ {x, w} \frac {1}{2} \left(w ^ {\prime} Q ^ {- 1} w + (x - \hat {x} (k)) ^ {\prime} P (k) ^ {- 1} (x - \hat {x} (k))\right) \quad \text { s.t. } z = A x + w$$

using the inverse form in Exercise 1.18, and show that the optimal cost is given by

$$V ^ {0} (z) = (1 / 2) \left(z - A \hat {x} (k)\right) ^ {\prime} \left(P ^ {-} (k + 1)\right) ^ {- 1} \left(z - A \hat {x} (k)\right)P ^ {-} (k + 1) = A P (k) A ^ {\prime} + Q$$

Add the z term to this cost using the third part of Example 1.1 and show that

$$V _ {k + 1} ^ {0} (z) = (1 / 2) \left(z - \hat {x} (k + 1)\right) ^ {\prime} P ^ {- 1} (k + 1) \left(z - \hat {x} (k + 1)\right)P (k + 1) = P ^ {-} (k + 1) - P ^ {-} (k + 1) C ^ {\prime} \left(C P ^ {-} (k + 1) C ^ {\prime} + R\right) ^ {- 1} C P ^ {-} (k + 1)\hat {x} (k + 1) = A \hat {x} (k) + L (k + 1) (\mathcal {Y} (k + 1) - C A \hat {x} (k))L (k + 1) = P ^ {-} (k + 1) C ^ {\prime} \left(C P ^ {-} (k + 1) C ^ {\prime} + R\right) ^ {- 1}$$

(b) In the regulator problem, take the z term outside the optimization and solve the remaining two-term problem using the regulator form of Exercise 1.18. Then

add the z term and show that

$$V _ {k - 1} ^ {0} (z) = (1 / 2) z ^ {\prime} \Pi (k - 1) z\Pi (k - 1) = Q + A ^ {\prime} \Pi (k) A - A ^ {\prime} \Pi (k) B (B ^ {\prime} \Pi (k) B + R) ^ {- 1} B ^ {\prime} \Pi (k) Au ^ {0} (z) = K (k - 1) zx ^ {0} (z) = (A + B K (k - 1)) zK (k - 1) = - \left(B ^ {\prime} \Pi (k) B + R\right) ^ {- 1} B ^ {\prime} \Pi (k) A$$

This symmetry can be developed further if we pose an output tracking problem rather than zero state regulation problem in the regulator.
