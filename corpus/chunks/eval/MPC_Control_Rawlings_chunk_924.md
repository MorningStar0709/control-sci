# Exercise A.41: Observability

Consider the linear system with zero input

$$x (k + 1) = A x (k)y (k) = C x (k)$$

with

$$
A = \left[ \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 2 & 1 & 1 \end{array} \right], \qquad C = \left[ \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \end{array} \right]
$$

(a) What is the observability matrix for this system? What is its rank?

(b) Consider a string of data measurements

$$y (0) = y (1) = \dots = y (n - 1) = 0$$

Now x(0) = 0 is clearly consistent with these data. Is this x(0) unique? If yes, prove it. If no, characterize the set of all x(0) that are consistent with these data.
