# Example 4.3

Given the plant as

$$\dot {x} (t) = a x (t) + b u (t), \tag {4.3.32}$$

and the performance index as

$$J = \frac {1}{2} \int_ {t _ {0}} ^ {t _ {f}} [ q x ^ {2} (t) + r u ^ {2} (t) ] d t, \tag {4.3.33}$$

and, the boundary conditions as

$$x (t = 0) = x _ {0}; \quad x (t = t _ {f}) = 0, \tag {4.3.34}$$

find the closed-loop optimal control.

Solution: Follow the procedure of the inverse matrix DRE described in the last section. We see that with the boundary conditions (4.3.34), we need to use the scalar version of the inverse matrix DRE (4.3.15) having the boundary condition (4.3.17). The optimal control (4.3.20) is given by

$$u ^ {*} (t) = - r ^ {- 1} b m ^ {- 1} (t) x ^ {*} (t) \tag {4.3.35}$$

where, $m(t)$ is the solution of the scalar DRE (4.3.15)

$$\dot {m} (t) = 2 a m (t) + m ^ {2} (t) q - \frac {b ^ {2}}{r} \tag {4.3.36}$$
