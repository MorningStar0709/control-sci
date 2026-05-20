# 7.8 Constrained Linear Control

The previous results on parametric linear programming may be applied to obtain the optimal receding horizon control law when the system is linear, the constraints polyhedral, and the cost linear as is done in a similar fashion in Section 7.4 where the cost is quadratic. The optimal control problem is therefore defined as in Section 7.4, except that the stage cost $\ell ( \cdot )$ and the terminal cost $V _ { f } ( \cdot )$ are now defined by

$$\ell (x, u) := q ^ {\prime} x + r ^ {\prime} u, \quad V _ {f} (x) := q _ {f} ^ {\prime} x$$

As in Section 7.4, the optimal control problem $\mathbb { P } _ { N } ( x )$ may be expressed as

$$V _ {N} ^ {0} (x) = \min _ {\mathbf {u}} \left\{V _ {N} (x, \mathbf {u}) \mid \mathbf {M u} \leq \mathbf {N} x + \mathbf {p} \right\}$$

where, now

$$V _ {N} (x, \mathbf {u}) = \mathbf {q} ^ {\prime} x + \mathbf {r} ^ {\prime} \mathbf {u}$$

Hence the problem has the same form as that discussed in Section 7.7 and may be solved as shown there.

It is possible, using a simple transcription, to use the solution of $\mathbb { P } _ { N } ( x )$ to solve the optimal control problem when the stage cost and terminal cost are defined by

$$\ell (x, u) := | Q x | _ {p} + | R u | _ {p}, \quad V _ {f} (x) := | Q _ {f} x | _ {p}$$

where $| \cdot | _ { p }$ denotes the p-norm and p is either 1 or ∞.
