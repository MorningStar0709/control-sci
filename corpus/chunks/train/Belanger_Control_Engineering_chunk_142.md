# Example 3.18 (Pendulum on a Cart)

For the values $M = m = \ell = 1, g = 9.8$ , the system of Example 3.10 has the matrices

$$
A = \left[ \begin{array}{c c c c} 0 & 1 & 0 & 0 \\ 0 & 0 & - 9. 8 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 1 9. 6 & 0 \end{array} \right] \qquad B = \left[ \begin{array}{c} 0 \\ 1 \\ 0 \\ - 1 \end{array} \right].
$$

Assuming, for example, that the position $x$ and the angle $\theta$ are measured,

$$
C = \left[ \begin{array}{c c c c} 1 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 \end{array} \right].
$$

Transform this realization to Jordan form.

Solution The eigenvalues of $A$ are $0, 0, \pm 4.4272$ . The vector $[1\quad 0\quad 0\quad 0]^{T}$ is the only eigenvector corresponding to the double eigenvalue $s = 0$ . We calculate the generalized eigenvector through Equation 3.75:

$$
(A - 0 I) \mathbf {v} _ {1} ^ {1} = \left[ \begin{array}{c} 1 \\ 0 \\ 0 \\ 0 \end{array} \right].
$$

The solution is

$$
\mathbf {v} _ {1} ^ {1} = \left[ \begin{array}{l} x \\ 1 \\ 0 \\ 0 \end{array} \right]
$$

where $x$ is arbitrary. Choose $x = 0$ .

The eigenvectors corresponding to $\pm4.4272$ are computed in the normal manner. From Equation 3.72,

$$
T = \left[ \begin{array}{l l l l} 1 & 0 & 1 & 1 \\ 0 & 1 & 4. 4 2 7 2 & - 4. 4 2 7 2 \\ 0 & 0 & - 2 & - 2 \\ 0 & 0 & - 8. 8 5 4 4 & 8. 8 5 4 4 \end{array} \right]
$$

whose inverse is

$$
T ^ {- 1} = \left[ \begin{array}{c c c c} 1 & 0 & . 5 & 0 \\ 0 & 1 & 0 & . 5 \\ 0 & 0 & -. 2 5 & -. 0 5 6 5 \\ 0 & 0 & -. 2 5 & . 0 5 6 5 \end{array} \right].
$$

As expected,

$$
T ^ {- 1} A T = \left[ \begin{array}{c c c c} 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 4. 4 2 7 2 & 0 \\ 0 & 0 & 0 & - 4. 4 2 7 2 \end{array} \right].
$$

We obtain

$$
\begin{array}{l} T ^ {- 1} B = \left[ \begin{array}{c} 0 \\ . 5 \\ . 0 5 6 5 \\ -. 0 5 6 5 \end{array} \right] \\ C T = \left[ \begin{array}{c c c c} 1 & 0 & 1 & 1 \\ 0 & 0 & - 2 & - 2 \end{array} \right]. \\ \end{array}
$$

Figure 3.9 shows a block diagram of this system. The system is seen to be controllable and observable. Note, however, that the system would not be observable from $\theta$ alone.
