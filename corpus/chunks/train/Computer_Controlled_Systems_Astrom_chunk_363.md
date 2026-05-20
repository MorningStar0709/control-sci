# 5.11 Conclusions

It is quite natural to approach pole-placement control by polynomial calculations. In this chapter we have investigated control of the system

$$A (q) y (k) = B (q) u (k)$$

A general controller can be represented as

$$R (q) u (k) = T (q) u _ {c} (k) - S (q) y (k)$$

and the design reduces to solving the Diophantine equation

$$A (z) R (z) + B (z) S (z) = A _ {c l} (z)$$

where $A_{cl}(z)$ is the desired closed-loop characteristic polynomial. By making analogies to the state-space approach we also found that for a simple design problem, the closed-loop characteristic polynomial $A_{cl}$ can be factored into a controller polynomial $A_{c}$ and an observer polynomial $A_{o}$ . This gives a very convenient way to compute Luenberger observers and other reduced order observers. The problem of cancellation of poles and zeros has also been discussed. It was shown that requirements on attenuation of disturbances and model following can be expressed by requiring that the polynomials R and S have specified factors.

With the polynomial approach we also obtain a natural way to discuss the effects of uncertainties in the process model used to design the controller. Finally we showed that many different design techniques can be conveniently interpreted as pole placement. In summary we find that the polynomial approach is a valuable complement to the state-space approach. It gives additional insight and other computational procedures.
