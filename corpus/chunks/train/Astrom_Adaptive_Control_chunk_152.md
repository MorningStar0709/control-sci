# ALGORITHM 3.1 Minimum-degree pole placement (MDPP)

Data: Polynomials A, B.

Specifications: Polynomials $A_{m}$ , $B_{m}$ , and $A_{o}$ .

Compatibility Conditions:

$$\deg A _ {m} = \deg A\deg B _ {m} = \deg B\deg A _ {o} = \deg A - \deg B ^ {+} - 1B _ {m} = B ^ {-} B _ {m} ^ {\prime}$$

Step 1: Factor $B$ as $B = B^{+}B^{-}$ , where $B^{\dagger}$ is monic.

Step 2: Find the solution $R'$ and $S$ with $\deg S < \deg A$ from

$$A R ^ {\prime} + B ^ {-} S = A _ {0} A _ {m}$$

Step 3: Form $R = R'B^{+}$ and $T = A_{o}B_{m}'$ , and compute the control signal from the control law

$$R u = T u _ {c} - S y$$

There are special cases of the design procedure that are of interest.

All zeros are canceled The design procedure simplifies significantly in the special case in which all process zeros are canceled; then $\deg A_{o} - \deg A - \deg B - 1$ . It is natural to choose $B_{m} = A_{m}(1)q^{d_{0}}$ . Then the factorization in Step 1 is very simple, and we get $B^{-} = b_{0}$ , $B^{+} = B/b_{0}$ . Furthermore,

$T = A_{m}(1)q^{d_{0}}/b_{0}$ , and the closed-loop characteristic polynomial becomes $A_{c} = B^{+}A_{c}^{\prime}$ . The Diophantine equation in Step 2 reduces to

$$A R ^ {\prime} + b _ {0} S = A _ {c} ^ {\prime} = A _ {o} A _ {m}$$

This equation is easy to solve because $R'$ is the quotient and $b_{0}S$ is the remainder when $A_{o}A_{m}$ is divided by A. However, all process zeros must be stable and well damped to allow cancellation.

No zeros are canceled The factorization in Step 2 also becomes very simple if no zeros are canceled. We have $B^{+} = 1$ , $B^{-} = B$ , and $B_{m} = \beta B$ , where $\beta - A_{m}(1) / B(1)$ . Furthermore, $\deg A_{o} = \deg A - \deg B - 1$ and $T = \beta A_{o}$ . The closed-loop characteristic polynomial is $A_{c} = A_{o}A_{m}$ , and the Diophantine equation in Step 2 becomes

$$A R + B S = A _ {c} = A _ {o} A _ {m}$$
