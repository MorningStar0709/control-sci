# ALGORITHM 4.3 Indirect LQG-STR based on spectral factorization

Data: Given specifications in the form of the parameter $\rho$ in the loss function of Eq. (4.40) and the order of the system.

Step 1: Estimate the coefficients of the polynomials A, B, and C in Eq. (4.39).

Step 2: Replace A, B, and C with the estimates obtained in Step 1 and solve the spectral factorization problem of Eq. (4.45) to obtain $P(q)$ .

Step 3: Solve the Diophantine equation of Eq. (4.43).

Step 4: Calculate the control signal from Eq. (4.41).

Repeat Steps 1, 2, 3, and 4 at each sampling period.

The state space formulation gives the following algorithm.
