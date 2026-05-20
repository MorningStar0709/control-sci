# Heuristic Discussion

The LQG-problem will now be related to the pole-placement problem. We will first give the solution heuristically. A formal solution will be given later. First, recall that the pole-placement problem required specifications of the closed-loop characteristic polynomial, which were chosen as $A_{c}(z)A_{o}(z)$ when $A_{o}$ was interpreted as the observer polynomial. In the LQG-problem the observer polynomial is simply $A_{o}(z) = C(z)$ . Compare Theorem 12.1. The polynomial $A_{c}(z)$ is equal to the polynomial $P(z)$ obtained from the spectral factorization. When the polynomials $A_{o}(z) = C(z)$ and $A_{c}(z) = P(z)$ are specified we can now expect that

the optimal control law is given by

$$u (k) = - \frac {S (q)}{R (q)} y (k)$$

where $R(z)$ and $S(z)$ are solutions to the Diophantine equation

$$A (z) R (z) + B (z) S (z) = P (z) C (z) \tag {12.47}$$

The structure of the admissible control laws is determined by the polynomials $R(z)$ and $S(z)$ . To describe a control law such that $u(k)$ is a function of $y(k)$ , $y(k-1), \ldots$ , and $u(k-1), u(k-2), \ldots$ , that is, no delay in the controller, the polynomials $R(z)$ and $S(z)$ should have the same degree. To describe a control law such that $u(k)$ is a function of $y(k-1), y(k-2), \ldots$ , and $u(k-1), u(k-2), \ldots$ , that is, one sampling period delay in the controller, the pole excess of $S(z)/R(z)$ should be one. The complexity of the control law is determined by the orders of the polynomials $R(z)$ and $S(z)$ .

There are many polynomials $R(z)$ and $S(z)$ that satisfy (12.47). Compare the discussion in Sec. 5.3. Among all choices we will determine solutions that minimize the loss function (12.8). Before making a formal solution we will discuss the problem heuristically.

The solution to the LQG problem based on the state space approach gives the additional constraints that have to be imposed on the solution to (12.47). Equation (12.41) gave a polynomial interpretation of the state space solution. The optimal controller was in fact characterized by the following conditions on the controller polynomials: $\deg R(z) = n$ and $\deg S(z) < n$ . If A and B are relative prime the optimal LQG-controller is thus the unique solution to (12.47) with $\deg S(z) < \deg A(z)$ .
