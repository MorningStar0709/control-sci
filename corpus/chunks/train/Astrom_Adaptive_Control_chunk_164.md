# ALGORITHM 3.2 Indirect self-tuning regulator using RLS and MDPP

Data: Given specifications in the form of a desired closed-loop pulse transfer operator $B_{m}/A_{m}$ and a desired observer polynomial $A_{n}$ .

Step 1: Estimate the coefficients of the polynomials A and B in Eq. (3.1) using the recursive least-squares method given by Eqs. (3.22).

Step 2: Apply the minimum-degree pole placement method given by Algorithm 3.1 where polynomials A and B are the estimates obtained in Step 1. The polynomials R, S, and T of the control law are then obtained.

Step 3: Calculate the control variable from Eq. (3.2), that is,

$$R u (t) = T u _ {z} (t) - S y (t)$$

Repeat Steps 1, 2, and 3 at each sampling period. Notice that there are some variations in the algorithm depending on the cancellations of the process zeros. Also notice that it is not necessary to perform Steps 1 and 2 at each sampling interval.
