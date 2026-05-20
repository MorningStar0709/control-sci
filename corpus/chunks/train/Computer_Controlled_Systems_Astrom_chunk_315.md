# ALGORITHM 5.3 GENERAL POLE-PLACEMENT DESIGN

Data: A process model is specified by the pulse-transfer function $B(z)/A(z)$ , where $A(z)$ and $B(z)$ do not have any common factors; the closed-loop characteristic polynomial $A_{cl}(z)$ ; polynomials $R_{d}(z)$ and $S_{d}(z)$ , which specify given factors of $R(z)$ and $S(z)$ ; and the pulse-transfer function $B_{m}(z)/A_{m}(z)$ , which gives the desired response to command signals.

Pole excess condition: $\deg A_m(z) - \deg B_m(z) \geq \deg A(z) - \deg B(z)$ .

Model following condition: The factor $B^{-}$ of B that is not canceled by the controller then must be a factor of $B_{m}$ , that is, $B_{m} = B^{-}\bar{B}_{m}$ .

Degree condition:

$$\deg A _ {c l} = 2 \deg A + \deg A _ {m} + \deg R _ {d} + \deg S _ {d} - 1 \tag {5.42}$$

Step 1. Factor the polynomials A and B as $A = A^{+}A^{-}$ and $B = B^{+}B^{-}$ , where $A^{+}$ and $B^{+}$ are factors that can be canceled by the controller.

Step 2. Solve the Diophantine equation

$$A ^ {-} R _ {d} \bar {R} + B ^ {-} S _ {d} \bar {S} = \bar {A} _ {c l} \tag {5.43}$$

with respect to $\bar{S}$ and $\bar{R}$ .

Step 3. The controller is then given by

$$R u = T u _ {c} - S y \tag {5.44}$$

where

$$
R = A _ {m} B ^ {+} R _ {d} \bar {R}
\begin{array}{l} S = A _ {m} A ^ {+} S _ {d} \bar {S} \\ T = \bar {S} + \bar {I} \end{array} \tag {5.45}
\boldsymbol {T} = \bar {\boldsymbol {B}} _ {m} \boldsymbol {A} ^ {+} \bar {\boldsymbol {A}} _ {c l}B _ {m} = \bar {B} _ {m} B ^ {-}
$$

and the closed-loop characteristic polynomial is $A_{cl} = A^{+}B^{+}A_{m}\bar{A}_{cl}$ .

The degree condition is obtained in the following way. Equation (5.43) has a minimum-degree solution with $\deg\bar{S}=\deg A^{-}+\deg R_{d}-1$ . It then follows from Eq. (5.45) that

$$
\begin{array}{l} \deg S = \deg A ^ {-} + \deg A ^ {+} + \deg A _ {m} + \deg R _ {d} + \deg S _ {d} - 1 \\ = \deg A + \deg A _ {m} + \deg R _ {d} + \deg S _ {d} - 1 \\ \end{array}
$$

Because $\deg R = \deg S$ we obtain the condition (5.42). Comparing with the simple design procedure in Algorithm 5.1 we find that the order of the closed-loop system is increased with $\deg A_{m} + \deg R_{d} + \deg S_{d}$ . The requirements are thus coped with by increasing the order of the controller.
