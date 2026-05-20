which is a differential equation for the signed length of the projection of the state $\mathbf{x}$ upon the vector $\mathbf{w}_i$ . The solution is $\mathbf{w}_i^T\mathbf{x}(t) = e^{s_i t}\mathbf{w}_i\mathbf{x}(0)$ , which is completely unaffected by the input. Hence, the mode is seen to be impervious to control, i.e., uncontrollable.

Example 3.13 Verify that the network of Example 3.2 is uncontrollable. Find the uncontrollable mode.

Solution The relevant matrices are

$$
A = \left[ \begin{array}{c c} - \frac {3}{2} & \frac {1}{2} \\ \frac {1}{2} & - \frac {3}{2} \end{array} \right] \quad B = \left[ \begin{array}{c} \frac {1}{2} \\ \frac {1}{2} \end{array} \right].
$$

Since $n = 2$ , the controllability matrix is

$$
\mathcal {C} = \left[ \begin{array}{l l} B & A B \end{array} \right] = \left[ \begin{array}{c c} \frac {1}{2} & - \frac {1}{2} \\ \frac {1}{2} & - \frac {1}{2} \end{array} \right].
$$

Since $\operatorname{det}\mathcal{C} = 0$ , its rank is less than 2 and the system is not controllable. Since

$$
\left[ \begin{array}{l l} a & - a \end{array} \right] \left[ \begin{array}{l l} \frac {1}{2} & - \frac {1}{2} \\ \frac {1}{2} & - \frac {1}{2} \end{array} \right] = 0
$$

the state $\left[ \begin{array}{c}a\\ -a \end{array} \right]$ is uncontrollable. It should be an eigenvector of $A^T$ ; indeed, $\mathcal{A}^T\left[ \begin{array}{c}a\\ -a \end{array} \right] = -2\left[ \begin{array}{c}a\\ -a \end{array} \right]$ , so the mode $s = -2$ is not controllable.
