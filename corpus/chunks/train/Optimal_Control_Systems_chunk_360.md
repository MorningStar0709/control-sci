# 6.5 LQR System Using H-J-B Equation

which upon solving with the boundary condition (6.4.28) becomes

$$p (t) = \frac {(\sqrt {5} - 2) + (\sqrt {5} + 2) \left[ \frac {3 - \sqrt {5}}{3 + \sqrt {5}} \right] e ^ {2 \sqrt {5} (t - t _ {f})}}{1 - \left[ \frac {3 - \sqrt {5}}{3 + \sqrt {5}} \right] e ^ {2 \sqrt {5} (t - t _ {f})}}. \tag {6.4.33}$$

Note, the relation (6.4.32) is the scalar version of the matrix DRE (3.2.34) for the finite-time LQR system.

\- Step 5: Using the relation (6.4.33), we have the closed-loop optimal control (6.4.30).

Note: Let us note that as $t_f \to \infty$ , $p(t)$ in (6.4.33) becomes $p(\infty) = \bar{p} = \sqrt{5} - 2$ , and the optimal control (6.4.30) is

$$u (t) = - (\sqrt {5} - 2) x (t). \tag {6.4.34}$$
