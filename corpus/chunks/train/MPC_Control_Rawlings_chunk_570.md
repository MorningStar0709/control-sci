# Exercise 4.12: Dynamic programming recursion for Kalman predictor

In the Kalman predictor, we use forward DP to solve at stage k

$$\min _ {x, w} \ell (x, w) + V _ {k} ^ {-} (x) \quad \text { s . t . } z = A x + w$$

in which x is the state at the current stage and z is the state at the next stage. The stage cost and arrival cost are given by

$$\ell (x, w) = (1 / 2) \left(\left| y (k) - C x \right| _ {R ^ {- 1}} ^ {2} + w ^ {\prime} Q ^ {- 1} w\right) \quad V _ {k} ^ {-} (x) = (1 / 2) \left| x - \hat {x} ^ {-} (k) \right| _ {(P ^ {-} (k)) ^ {- 1}} ^ {2}$$

and we wish to find the value function $V ^ { 0 } ( z )$ , which we denote $V _ { k + 1 } ^ { - } ( z )$ in the Kalman predictor estimation problem.

(a) Combine the two x terms to obtain

$$\min _ {x, w} \frac {1}{2} \left(w ^ {\prime} Q ^ {- 1} w + (x - \hat {x} (k)) ^ {\prime} P (k) ^ {- 1} (x - \hat {x} (k))\right) \quad \text { s.t. } z = A x + w$$

and, using the third part of Example 1.1, show

$$P (k) = P ^ {-} (k) - P ^ {-} (k) C ^ {\prime} \left(C P ^ {-} (k) C ^ {\prime} + R\right) ^ {- 1} C P ^ {-} (k)L (k) = P ^ {-} (k) C ^ {\prime} \left(C P ^ {-} (k) C ^ {\prime} + R\right) ^ {- 1} C ^ {\prime} R ^ {- 1}\hat {x} (k) = \hat {x} ^ {-} (k) + L (k) (\mathcal {Y} (k) - C \hat {x} ^ {-} (k))$$

(b) Add the w term and use the inverse form in Exercise 1.18 to show the optimal cost is given by

$$V ^ {0} (z) = (1 / 2) \left(z - A \hat {x} ^ {-} (k + 1)\right) ^ {\prime} \left(P ^ {-} (k + 1)\right) ^ {- 1} \left(z - A \hat {x} ^ {-} (k + 1)\right)\hat {x} ^ {-} (k + 1) = A \hat {x} (k)P ^ {-} (k + 1) = A P (k) A ^ {\prime} + Q$$
