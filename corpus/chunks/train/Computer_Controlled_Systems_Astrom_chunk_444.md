# Control Design

We have thus found that predictive first-order-hold sampling is similar to zero-order-hold sampling. In both cases the behavior of a system at the sampling instants can be described as a time-invariant discrete-time system. The methods for designing controllers obtained can then be used with minor modifications. We will illustrate this by giving the results for pole-placement control.

Consider a system with the pulse-transfer function $H(z) = B(z)/A(z)$ obtained by predictive first-order-hold sampling. A general linear controller with a two-degree-of-freedom structure can be described by the triple $(R(z), S(z), T(z))$ .

With a predictive hold the controller must generate the signal $u(kh + h)$ at time kh. This means that the controller polynomials have the property

$$\deg R (z) \geq \deg S (z) + 1 \tag {7.22}\deg R (z) \geq \deg T (z) + 1$$

Specifying a desired closed-loop characteristic polynomial $A_{r}$ , we find that the Diophantine equation associated with the design problem becomes

$$A (z) R (z) + B (z) S (z) = A _ {c l} (z) \tag {7.23}$$

and the control design can then be done in the same way as in Chapter 5. The only difference is that the order condition (7.22) is different. We illustrate the procedure by an example.
