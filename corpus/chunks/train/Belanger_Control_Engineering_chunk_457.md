c. It was found in Problem 3.36 (Chapter 3) that this system is uncontrollable if $\ell_2 = \ell_1$ . It should be expected that control will be difficult if $\ell_2 \approx \ell_1$ . Repeat parts (a) and (b) for $\ell_1 = 1\mathrm{m}$ , $\ell_2 = 0.9\mathrm{m}$ .

d. It is desired to limit the travel of the cart to $\pm 4\mathrm{m}$ for the initial conditions of part (b). Use $\ell_1 = 1\mathrm{m}$ , $\ell_2 = 0.5\mathrm{m}$ , and

$$J = \int_ {0} ^ {\infty} [ Q _ {1 1} x ^ {2} + F ^ {2} ] d t$$

and adjust $Q_{11}$ until $|x(t)| \leq 4$ m. What is the maximum power required in this case?

![](image/657108bea4ebfdedc1ad2f6833eb8c6e8340e44932434e49f8ca918bbadd1e5a.jpg)

7.28 Maglev A linearized model for a magnetically levitated vehicle was derived in Problem 2.20 (Chapter 2). A control system is required to stabilize the vehicle and to maintain the gaps between the magnets and the guideway. (The nominal gap width is only $14\mathrm{mm}$ .) We wish to design an LQ control system such that gap changes are held within $\pm 6\mathrm{mm}$ with $|\Delta u_{L1}|$ , $|\Delta u_{L2}| \leq 700$ and $|\Delta u_{G1}|$ , $|\Delta u_{G2}| \leq 170$ .

a. Compute the optimal LQ gain, with

$$
\begin{array}{l} J = \int_ {0} ^ {\infty} [ \alpha (\Delta S _ {L 1} ^ {2} + \Delta S _ {L 2} ^ {2} + \Delta S _ {G 1} ^ {2} + \Delta S _ {G 2} ^ {2}) \\ \left. + r \left(\Delta u _ {L 1} ^ {2} + \Delta \dot {u} _ {L 2} ^ {2} + \Delta u _ {G 1} + \Delta u _ {G 2} ^ {2}\right) \right] d t. \\ \end{array}
$$

(To determine the Q matrix, you will need to use the expressions for the gap changes in terms of the changes in the state variables.) Use several increasing values of r. You will note that the gain tends to a limit as you increase r.

b. Repeat the work of Problem 7.16(e) for a value of $r$ sufficient to result in a gain near the asymptotic value.

7.29 Suppose the system in Equation 7.43 is stabilizable, and consider the LQ

$$
J = \int_ {0} ^ {\infty} \left\{\left[ \Delta \mathbf {x} ^ {T} \mathbf {z} _ {w} ^ {T} \mathbf {z} _ {y} ^ {T} \right] \left[ \begin{array}{c c c} Q _ {x x} & Q _ {x w} & Q _ {x y} \\ Q _ {x w} ^ {T} & Q _ {w w} & Q _ {w y} \\ Q _ {x y} ^ {T} & Q _ {w y} ^ {T} & Q _ {y y} \end{array} \right] \left[ \begin{array}{c} \Delta \mathbf {x} \\ \mathbf {z} _ {w} \\ \mathbf {z} _ {y} \end{array} \right] + \Delta \mathbf {u} ^ {T} R \Delta \mathbf {u} \right\} d t
$$

solution with the performance index where the partitioning of the Q matrix is compatible with that of the state vector.
