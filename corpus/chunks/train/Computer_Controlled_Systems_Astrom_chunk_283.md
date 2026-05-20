# Solving the Design Problem

The solution of the design problem is straightforward. We will simply determine the characteristic equation of the closed-loop system and explore the conditions that it has to satisfy.

Eliminating $u(k)$ between the process model (5.1) and the controller (5.2) gives

$$\left(A (q) R (q) + B (q) S (q)\right) y (k) = B (q) T (q) u _ {c} (k) \tag {5.3}$$

The characteristic polynomial of the closed-loop system is

$$A _ {c l} (z) = A (z) R (z) + B (z) S (z) \tag {5.4}$$

Pole-placement design thus reduces to the algebraic problem of finding polynomials $R(z)$ and $S(z)$ that satisfy Eq. (5.4) for given $A(z), B(z)$ , and $A_{cl}(z)$ . Equation (5.4), which plays a central role in the polynomial approach, is called the Diophantine equation. A general discussion of this equation will be given later. Let it suffice for now that the problem always can be solved if the polynomials $A(z)$ and $B(z)$ do not have common factors.

Additional insight is obtained by comparing with the state-space solution to the design problem in Sec. 4.5. There we found that the characteristic polynomial $A_{cl}(z)$ could be factored as

$$A _ {c l} (z) = A _ {c} (z) A _ {o} (z) \tag {5.5}$$

where $A_{c}(z) = \det(zI - \Phi + \Gamma L)$ and $A_{o}(z) = \det(zI - \Phi + KC)$ . This factorization corresponds to the separation of the controller into a state feedback and an observer. For this reason we call $A_{c}(z)$ the controller polynomial and $A_{o}(z)$ as the observer polynomial. Recall that it was found in Sec. 4.3 that the arbitrary eigenvalues could be assigned to $A_{c}(z)$ if the system is reachable and that arbitrary eigenvalues could be assigned to $A_{c}(z)$ if the system is observable.

To complete the design it remains to determine the polynomial $T(z)$ . To do this we consider Eq. (5.3), which tells how the system reacts to command signals. The pulse-transfer function from command signal to output is given by

$$Y (z) = \frac {B (z) T (z)}{A _ {c l} (z)} U _ {c} (z) = \frac {B (z) T (z)}{A _ {c} (z) A _ {o} (z)} U _ {c} (z) \tag {5.6}$$

This equation shows that the zeros of the open-loop system are also zeros of the closed-loop system, unless the polynomials $B(z)$ and $A_{cl}(z)$ have common factors. By referring to the solution of the design problem in Sec. 4.6 it is natural to choose the polynomial $T(z)$ so that it cancels the observer polynomial $A_o(z)$ .

This implies that command signals are introduced in such a way that they do not generate observer errors. Hence

$$T (z) = t _ {0} A _ {o} (z) \tag {5.7}$$

The response to command signals is then given by

$$Y (z) = \frac {t _ {0} B (z)}{A _ {c} (z)} U _ {c} (z) \tag {5.8}$$

where the parameter $t_{0}$ is chosen to obtain the desired static gain of the system. For example, to have unit gain we have $t_{0} = A_{c}(1)/B(1)$ .
