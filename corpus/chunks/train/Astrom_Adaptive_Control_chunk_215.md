# LQG Control

The pole placement and LQG problems are closely related. In the LQG formulation a loss function is specified. Minimization of the loss function leads to a fixed-gain controller that can be interpreted in terms of pole placement. The details are given in Section 4.5. To obtain the LQG solution, it is first necessary to solve the spectral factorization problem, that is, to find the nth-order monic, stable polynomial $P(q)$ that satisfies

$$r P (q) P (q ^ {- 1}) = \rho A (q) A (q ^ {- 1}) + B (q) B (q ^ {- 1}) \tag {4.19}$$

The LQG-controller is then obtained as the solution to the Diophantine equation

$$C (q) P (q) = A (q) R (q) + B (q) S (q) \tag {4.20}$$

To get a unique solution with $\deg R = \deg S = n$ , it is necessary to make some further restrictions to the solution given by Eq. (4.20). See Theorem 4.3 in Section 4.5. The interpretation of Eq. (4.20) is that the LQG-controller places the closed-loop poles in $P(q)$ , given by the spectral factorization, and in $C(q)$ , which characterizes the disturbances.
