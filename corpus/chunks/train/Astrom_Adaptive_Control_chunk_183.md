# ALGORITHM 3.4 Direct self-tuning regulator for NMP systems

Data: Given specifications in terms of $A_{m}$ , $B_{m}$ , and $A_{o}$ and the relative degree $d_{0}$ of the system.

Step 1: Estimate the coefficients of the polynomials R and S in the model of Eq. (3.33) by recursive least squares.

Step 2: Cancel possible common factors in R and S to obtain R and S.

Step 3: Calculate the control signal from Eq. (3.2) where R and S are those obtained in Step 2 and T is given by Eq. (3.12).

Repeat Steps 1, 2, and 3 at each sampling period.

This algorithm avoids the nonlinear estimation problem, but more parameters have to be estimated than when Eq. (3.24) is used because the parameters of the polynomial $B^{-}$ are estimated twice. The estimation is straightforward, however, because the model is linear in the parameters. The Euclidean algorithm in Chapter 11 can be used in Step 2 to eliminate common factors of polynomials R and S. This step is crucial because an unstable common factor may cause instabilities.

Calculation of polynomial T should be avoided. To do this, notice that

$$y _ {m} = \frac {B ^ {\cdot} B _ {m} ^ {\prime}}{A _ {m}} u _ {c}$$

The error $e = y - y_{m}$ can then be written as

$$
\begin{array}{l} e (t) = \frac {B ^ {-}}{A _ {o} A _ {m}} (R u (t) + S y (t) - T u _ {c} (t)) \\ = \mathcal {R} ^ {*} u _ {f} (t - d _ {0}) + S ^ {*} y _ {f} (t - d _ {0}) - T ^ {*} u _ {c f} (t - d _ {0}) \tag {3.34} \\ \end{array}
$$

By basing parameter estimation on this equation, estimates of polynomials R, S, and T can be determined. Notice that to estimate coefficients of T, it is necessary that the command signal be persistently exciting.
