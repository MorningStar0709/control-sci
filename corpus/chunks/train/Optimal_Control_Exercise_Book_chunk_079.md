# Solution:

We first find the Hamilton-Jacobi-Bellman equation which can be written as following:

$$- \frac {\partial \hat {V} (t , x)}{\partial t} = \inf _ {u \in \mathbb {R} ^ {m}} \left[ L (t, x, u) + \left\langle \frac {\partial}{\partial x} \hat {V} (t, x, u), f (t, x, u) \right\rangle \right] \tag {345}$$

A candidate value function is like in the hint:

$$\hat {V} (x, t) = x ^ {T} S _ {2} (t) x + s _ {1} ^ {T} (t) x + s _ {0} (t), \quad S _ {2} (t) = S _ {2} (t) ^ {T} > 0, \quad s _ {1} (t) \in \mathbb {R} ^ {n}, \quad s _ {0} (t) \in \mathbb {R} \tag {346}$$

We can calculate its partial derivatives

$$\frac {\partial \hat {V} (x , t)}{\partial t} = x ^ {\top} \dot {S} _ {2} (t) x + x ^ {\top} \dot {s} _ {1} (t) + \dot {s} _ {0} (t) \tag {347}\frac {\partial \hat {V} (x , t)}{\partial x} = 2 x ^ {\top} S _ {2} (t) x + s _ {1} (t) \tag {348}$$

and then we can rearrange the HJB by substituting. We notice that, given the problem’s convexity, we can obtain a global minimum $u ^ { * } ( t )$ and therefore replace the infimum with the minimum:

$$
\begin{array}{l} x ^ {\top} \dot {S} _ {2} (t) x + x ^ {\top} \dot {s} _ {1} (t) + \dot {s} _ {0} (t) = \min _ {u \in \mathbb {R} ^ {m}} \left[ (x - x _ {d} (t)) ^ {\top} Q (x - x _ {d} (t)) \right. \\ + \left(u - u _ {d} (t)\right) ^ {\top} R \left(u - u _ {d} (t)\right) \\ \left. + \left(2 x ^ {\top} S _ {2} (t) x + s _ {1} (t)\right) (A x + B u) \right] \\ \end{array}
$$

and we can also set the first the first derivative of the HJB to zero as a sufficient condition for finding the optimal control policy:

$$\frac {\partial}{\partial u} = 2 (u - u _ {d} (t)) ^ {\top} R + \left(2 x ^ {\top} S _ {2} (t) + s _ {1} ^ {\top} (t)\right) B = 0 \tag {349}\Longrightarrow u ^ {*} (t) = u _ {d} (t) - R ^ {- 1} B ^ {\top} \left(S _ {2} (t) x + \frac {1}{2} s _ {1} (t)\right) \tag {350}$$

Plugging this result back in the HJB equation, we can get the conditions for the coefficients as following:

$$- \dot {S} _ {2} (t) = Q - S _ {2} (t) B R ^ {- 1} B ^ {T} S _ {2} (t) + S _ {2} (t) A + A ^ {\top} S _ {2} (t) \tag {351}- \dot {s} _ {1} (t) = - 2 Q x _ {d} (t) + \left(A ^ {\top} - S _ {2} B R ^ {- 1} B ^ {\top}\right) s _ {1} (t) + 2 S _ {2} (t) B u _ {d} (t) \tag {352}- \dot {s} _ {0} = x _ {d} (t) ^ {\top} Q x _ {d} (t) - \frac {1}{4} s _ {1} ^ {\top} (t) B R ^ {- 1} B ^ {\top} s _ {1} (t) + s _ {1} (t) ^ {\top} B u _ {d} (t) \tag {353}$$

Subject to the final conditions:

$$S _ {2} (T) = Q _ {f} \tag {355}s _ {1} (T) = - 2 Q _ {f} x _ {d} (T) \tag {356}s _ {0} (T) = x _ {d} (T) ^ {\top} Q _ {f} x _ {d} (T) \tag {357}$$

We also notice that the solution for $S _ { 2 }$ is the same as the simpler LQR problem; hence as expected it is also positive semidefinite.
