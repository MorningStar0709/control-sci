# Notch Filter Design

The frequency associated with the mechanical resonance $\omega_{o}=1$ is close to the desired closed-loop frequency $\omega_{c}=0.5$ . It is then necessary to take the mechanical resonance into account when designing the control loop. A classic method for doing this is to introduce a compensating network that avoids unnecessary excitation of the oscillatory process poles. The filter that accomplishes this is called a notch filter because its Bode diagram has a notch at the frequency of the undesired modes. This approach ensures that the oscillatory modes will not be excited by the command signals or the control action. However, it does not introduce any damping of the oscillatory modes. This means that the system will respond to excitation of the oscillatory modes in the same way as the open-loop system. A notch filter can be designed using pole placement simply by canceling the factor $A^{+}(z)$ corresponding to the oscillatory modes. In the particular case we have

$$A ^ {+} (z) = z ^ {2} - 1. 7 1 2 4 z + 0. 9 5 1 2$$

The Diophantine equation (5.28) is

$$A R + B S = A ^ {+} A _ {c} A _ {o}$$

It follows from the degree condition of the general pole-placement procedure, Algorithm 5.3, that the closed-loop system is of order 9. The polynomial $A^{+}$ is of second order, $A_{c}$ is of fifth order, and the observer polynomial $A_{o}$ is thus of second order. We choose $A_{o}$ to have the same poles as the antialiasing filter. The controller polynomials $R$ and $S$ are of fourth order. Introducing $S = A^{+}\bar{S}$ into the preceding equation gives the following Diophantine equation for $R$ and $\bar{S}$ .

$$\boldsymbol {A} ^ {-} \boldsymbol {R} + \boldsymbol {B} \bar {\boldsymbol {S}} = \boldsymbol {A} _ {c} \boldsymbol {A} _ {o}$$

The response to command signals is given by the transfer function $BT/A^{+}A_{c}A_{o}$ . If we choose

$$T (z) = \frac {A _ {c} (1) A ^ {+} (z) A _ {o} (z)}{B (1)}$$
