# ALGORITHM 4.4 Indirect LQG-STR based on the Riccati equation

Data: Given specifications in the form of the parameters $Q_{0}$ , $Q_{1}$ , and $\rho$ in the loss function of Eq. (4.47) and the order of the system.

Step 1: Estimate the coefficients of the polynomials $A, B$ , and $C$ in Eq. (4.39).

Step 2: Replace A, B, and C with the estimates obtained in Step 1 and solve the algebraic Riccati equation or iterate Eqs. (4.49) to obtain $\bar{L}$ .

Step 3: Calculate the control signal from Eq. (4.48).

Repeat Steps 1, 2, and 3 at each sampling period.

Notice that if $Q_{1} = \hat{C}^{T}\bar{C}$ , the steady-state solution to Eqs. (4.49) will give the same result as the minimization of Eq. (4.40). Algorithms 4.3 and 4.4 are indirect algorithms that are able to handle nonminimum-phase systems and varying time delays. The computations are more extensive for these algorithms than for the simple self-tuning regulators discussed above.

Solution of the spectral factorization or the Riccati equation is the major computation in an LQG self-tuner. These calculations can be made in many different ways. The Riccati equation can be solved by using an eigenvalue method or by some iterative method. The iterative methods will in general lead to shorter code. In general the Riccati equation is iterated several steps. To guarantee that the calculations can be done in a prescribed sampling interval, it is necessary to truncate the iterations; it is important that a reasonable result be obtained when the iteration is truncated. For instance, the polynomial P in the spectral factorization must be stable. This is guaranteed for some algorithms. In some algorithms it is suggested that the Riccati equation be iterated only one step at each sampling.
