# ALGORITHM 3.3 Simple direct self-tuner

Data: Given specifications in terms of $A_{m}$ , $B_{m}$ , and $A_{o}$ and the relative degree $d_{0}$ of the system.

Step 1: Estimate the coefficients of the polynomials $R$ and $S$ in the model (3.27), that is,

$$y (t) = R ^ {*} u _ {f} \left(t - d _ {0}\right) + S ^ {*} y _ {f} \left(t - d _ {0}\right)$$

by recursive least squares, Eqs. (3.22).

Step 2: Compute the control signal from

$$R ^ {*} u (t) = T ^ {*} u _ {c} (t) - S ^ {*} y (t)$$

where $R$ and $S$ are obtained from the estimates in Step 1 and

$$T ^ {*} = A _ {0} ^ {*} A _ {m} (1) \tag {3.29}$$

with $\deg A_o = d_0 - 1$ . Repeat Steps 1 and 2 at each sampling period.

Equation (3.29) is obtained from the observation that the closed-loop transfer operator from command signal $u_{c}$ to process output is

$$\frac {T B}{A R + B S} = \frac {T b _ {0} B ^ {+}}{b _ {0} A _ {o} A _ {m} B ^ {+}} = \frac {T}{A _ {o} A _ {m}}$$

Requiring that this be equal to $q^{d_{0}}A_{m}(1)/A_{m}$ gives Eq. (3.29).

Remark 1. A comparison with Algorithm 3.2 shows that the step corresponding to control design is missing in Algorithm 3.3. This motivates the name "direct algorithm."

Remark 2. Notice that it is necessary to know the relative degree $d_0$ of the plant a priori.

Remark 3. The polynomials R and S contain the factor $b_{0}$ . Notice that the polynomial R is not monic and that the parameter $r_{0}$ must be different from zero. Otherwise, the control law given by Eq. (3.2) is not causal. Since $d_{0}$ is the relative degree of the plant, the true value of $r_{0} = b_{0}$ is different from zero. Any consistent estimate of the parameter will thus be different from zero. The estimate obtained for finite time may, however, be zero. In practice it is therefore essential to take some precautions.

Remark 4. Notice that the assumption $B^{-} = b_{0}$ implies that all process zeros are canceled. This is the reason why the algorithm requires the plant to be minimum phase.
