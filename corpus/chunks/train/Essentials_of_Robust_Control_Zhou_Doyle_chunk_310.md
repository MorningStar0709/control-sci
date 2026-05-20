# Algebraic Riccati Equations

We studied the Lyapunov equation in Chapter 7 and saw the roles it played in some applications. A more general equation than the Lyapunov equation in control theory is the so-called algebraic Riccati equation or ARE for short. Roughly speaking, Lyapunov equations are most useful in system analysis while AREs are most useful in control system synthesis; particularly, they play central roles in $\mathcal { H } _ { 2 }$ and $\mathcal { H } _ { \infty }$ optimal control.

Let $A , Q ,$ and R be real $n \times n$ matrices with $Q$ and R symmetric. Then an algebraic Riccati equation is the following matrix equation:

$$A ^ {*} X + X A + X R X + Q = 0. \tag {12.1}$$

Associated with this Riccati equation is a $2 n \times 2 n$ matrix:

$$
H := \left[ \begin{array}{c c} A & R \\ - Q & - A ^ {*} \end{array} \right]. \tag {12.2}
$$

A matrix of this form is called a Hamiltonian matrix. The matrix H in equation (12.2) will be used to obtain the solutions to the equation (12.1). It is useful to note that the spectrum of H is symmetric about the imaginary axis. To see that, introduce the $2 n \times 2 n$ matrix:

$$
J := \left[ \begin{array}{c c} 0 & - I \\ I & 0 \end{array} \right]
$$

having the property $J ^ { 2 } = - I .$ Then

$$J ^ {- 1} H J = - J H J = - H ^ {*}$$

so H and $- H ^ { * }$ are similar. Thus λ is an eigenvalue $\mathrm { i f } - \bar { \lambda }$ is.

This chapter is devoted to the study of this algebraic Riccati equation.
