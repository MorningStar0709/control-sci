# ALGORITHM 5.1 SIMPLE POLE-PLACEMENT DESIGN

Data: A process model is specified by the pulse-transfer function $B(z)/A(z)$ , where $A(z)$ and $B(z)$ do not have any common factors. Specifications are given in terms of a desired closed-loop characteristic polynomial $A_{cl}(z)$ .

Step 1. Find polynomials $R(z)$ and $S(z)$ , such that $\deg S(z) \leq \deg R(z)$ , which satisfy the equation

$$A (z) R (z) + B (z) S (z) = A _ {c l} (z)$$

Step 2. Factor the closed-loop characteristic polynomial as $A_{cl}(z) = A_c(z)A_o(z)$ , where $\deg A_o(z) \leq \deg R(z)$ , and choose

$$T (z) = t _ {0} A _ {o} (z)$$

where $t_0 = A_c(1) / B(1)$ . The control law is

$$R (q) u (k) = T (q) u _ {c} (k) - S (q) y (k)$$

and the response to command signals is given by

$$A _ {c} (q) y (k) = t _ {0} B (q) u _ {c} (k)$$

There are several details that have to be investigated. The most important is the solution of the Diophantine equation (5.4). Before doing this we will, however, consider an example.
