# ■ Theorem 7.8

Let $(A, C)$ be observable. Then there exists an observer gain matrix $G$ such that $\widehat{\mathbf{x}}(t) \to \mathbf{x}(t)$ , asymptotically.

Proof: With $\widetilde{\mathbf{x}} = \mathbf{x} - \widehat{\mathbf{x}}$ as before, we write

$$
\begin{array}{l} \tilde {\mathbf {x}} = \dot {\mathbf {x}} - \hat {\mathbf {x}} \\ = A \mathbf {x} + B \mathbf {u} - A \widehat {\mathbf {x}} - B \mathbf {u} - G (\mathbf {y} - C \widehat {\mathbf {x}}) \\ = A (\mathbf {x} - \widehat {\mathbf {x}}) - G (C \mathbf {x} - C \widehat {\mathbf {x}}) \\ = (A - G C) (\mathbf {x} - \widehat {\mathbf {x}}) \\ \end{array}
$$

or

$$\tilde {\mathbf {x}} = (A - G C) \tilde {\mathbf {x}}. \tag {7.61}$$

It remains only to show that $A - GC$ can be made stable by a proper choice of $G$ ; if that is so, then $\widetilde{\mathbf{x}}(t) \to 0$ and $\widehat{\mathbf{x}}(t) \to \mathbf{x}(t)$ .

From Chapter 3, recall that the system of Equation 7.59 is observable if, and only if, the dual system

$$\dot {\mathbf {x}} = A ^ {T} \mathbf {x} + C ^ {T} \mathbf {u} \tag {7.62}$$

is controllable. If the system of Equation 7.59 is observable, then the system of Equation 7.62 is controllable and a state gain matrix $G^T$ (an $m \times n$ matrix) can be chosen for arbitrary placement of the eigenvalues of the matrix $A^T - C^T G^T$ . Since a matrix and its transpose have identical eigenvalues, and because $(A^T - C^T G^T)^T = A - GC$ , it follows that $A - GC$ can always be made to have only stable eigenvalues.

The proof has disclosed one way of choosing the observer gain G, as the solution to a pole-placement problem for a controllable system. That system is given by Equation 7.62, and the state feedback gain to be calculated is $G^{T}$ . To summarize:

1. Solve the pole-placement problem for the dual system $\dot{\mathbf{x}} = A^{T}\mathbf{x} + C^{T}\mathbf{u}$ , with the desired poles being those of the error system, given by Equation 7.61.   
2. Write the observer as $\widehat{\mathbf{x}} = A\widehat{\mathbf{x}} + B\mathbf{u} + G(\mathbf{y} - C\widehat{\mathbf{x}})$ .
