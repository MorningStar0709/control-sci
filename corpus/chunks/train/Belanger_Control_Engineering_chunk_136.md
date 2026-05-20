# Example 3.16 (dc Servo)

For the dc servo of Example 2.1, let $y = \theta$ . Transform the given realization to diagonal Jordan form.

Solution Starting from the state equation, Equation 2.19 (Chapter 2), we compute the eigenvalues and the matrix $T$ of eigenvectors (MATLAB command eig). They are $s_1 = 0$ , $s_2 = -2.474$ , $s_3 = -21.526$ , and

$$
T = \left[ \begin{array}{c c c} 1 & -. 4 0 4 2 & . 0 0 9 6 \\ 0 & 1 & -. 2 0 6 2 \\ 0 & -. 5 5 7 5 & 1 \end{array} \right].
$$

The inverse of $T$ (MATLAB command inv) is

$$
T ^ {- 1} = \left[ \begin{array}{c c c} 1 & . 4 5 0 7 & . 0 8 3 3 \\ 0 & 1. 1 2 9 9 & . 2 3 2 9 \\ 0 & . 6 2 9 9 & 1. 1 2 9 9 \end{array} \right].
$$

It is verified that

$$T ^ {- 1} A T = \operatorname{diag} [ 0, - 2. 4 7 4, - 2 1. 5 2 6 ].$$

We compute

$$
T ^ {- 1} B = \left[ \begin{array}{l l} 1. 6 6 6 7 & - 3. 3 3 3 0 \\ 4. 6 5 8 8 & - 8. 3 5 6 4 \\ 2 2. 5 9 7 1 & - 4. 6 5 8 4 \end{array} \right]
$$

and, with $C = \left[ \begin{array}{lll}1 & 0 & 0 \end{array} \right]$ ,

$$
C T = \left[ \begin{array}{l l l} 1 & -. 4 0 4 2 & . 0 0 9 6 \end{array} \right].
$$

The diagonal Jordan form realization is

$$
\begin{array}{l} \dot {\mathbf {z}} = \left[ \begin{array}{c c c} 0 & 0 & 0 \\ 0 & - 2. 4 7 4 & 0 \\ 0 & 0 & - 2 1. 5 2 6 \end{array} \right] \dot {\mathbf {z}} + \left[ \begin{array}{c c} 1. 6 6 6 7 & - 3. 3 3 3 0 \\ 4. 6 5 8 8 & - 8. 3 5 6 4 \\ 2 2. 5 9 7 1 & - 4. 6 5 8 4 \end{array} \right] \left[ \begin{array}{l} v \\ T _ {L} \end{array} \right] \\ \theta = \left[ \begin{array}{l l l} 1 & -. 4 0 4 2 & . 0 0 9 6 \end{array} \right] \mathbf {z}. \\ \end{array}
$$

All three modes are observable and controllable. They are, in fact, controllable from each input taken separately, which means that both the control input v and the disturbance input $T_{L}$ are capable of exciting all modes.

Note that the state variables $z_{1}$ , $z_{2}$ , and $z_{3}$ do not have the direct physical significance of the state variables $\theta$ , $\omega$ , and i in the original realization. Of course, $\theta$ , $\omega$ , and i can be calculated from z by use of the relation $x = T^{-1}z$ .

If some of the eigenvalues are complex, so are the eigenvectors and so is the Jordan form. That is inconvenient, and requires some modification. Since complex eigenvalues and eigenvectors come in conjugate pairs, let us focus our attention on the two equations corresponding to complex conjugate eigenvalues:
