# Solution

The eigenvalues and eigenvectors are computed (MATLAB command eig) to be

$$
- 6. 1 5 2 3 \pm j 2 4. 5 3 3 9 \quad \text { and } \quad \left[ \begin{array}{c} - 2. 5 5 1 \times 1 0 ^ {- 3} \\ - 9. 6 1 7 \times 1 0 ^ {- 3} \\ - 2. 8 8 5 \times 1 0 ^ {- 2} \\ 1 \end{array} \right] \pm j \left[ \begin{array}{c} 1. 8 1 6 \times 1 0 ^ {- 3} \\ - 3. 8 3 5 \times 1 0 ^ {- 2} \\ - 7. 3 7 6 \times 1 0 ^ {- 2} \\ 0 \end{array} \right]

- 0. 8 4 7 7 \pm j 2. 9 4 2 8 \quad \text { and } \quad \left[ \begin{array}{c} - 9. 0 3 8 \times 1 0 ^ {- 2} \\ 8. 8 4 1 \times 1 0 ^ {- 3} \\ 1 \\ 8. 0 0 5 \times 1 0 ^ {- 2} \end{array} \right] \pm j \left[ \begin{array}{c} - 3. 1 3 8 \times 1 0 ^ {- 1} \\ - 2. 9 7 5 \times 1 0 ^ {- 2} \\ 0 \\ 5. 1 2 3 \times 1 0 ^ {- 2} \end{array} \right].
$$

The $C$ matrix is

$$
C = \left[ \begin{array}{c c c c} 1 & - 1 & 0 & 0 \\ 0 & 0 & 1 & - 1 \end{array} \right]
$$

and none of the eigenvectors is orthogonal to $C$ .

This shows that measurements of position and velocity differences between the vehicle body and the unsprung mass are sufficient to guarantee observability. That is a welcome conclusion, because such measurements are much easier—and less expensive—than measurements of, say, $x_{1}$ , $x_{2}$ , $v_{1}$ , and $v_{2}$ , all of which are referred to an inertial coordinate system.

This last example might lead one to think that unobservability is a fluke. Indeed, matrices A and C formed at random will yield an observable system with probability 1. In most cases, it is the locations of the zeros and ones that cause unobservability to occur; those are determined by the structure of the system, not by parameters taking on particular values.
