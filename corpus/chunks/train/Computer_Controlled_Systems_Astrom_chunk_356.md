# Error Feedback with Complete Cancellation

In some systems the process output y and the command signals $u_{c}$ are not available because only the error $e = u_{c} - y$ is measured. This case is called error feedback. A typical case is a CD player in which only the deviation from the track can be measured. This means that a two-degree-of-freedom controller cannot be used. Mathematically it means that the polynomials S and T in the controller are identical and the control law (5.2) becomes

$$R u = S (u _ {c} - y)$$

Several design schemes combine error feedback with cancellation of all poles and zeros of the process. To analyze a system assume that the process has the pulse-transfer function $B(z)/A(z)$ and that the desired closed-loop pulse transfer function is $B_{c}(z)/A_{c}(z)$ . The closed-loop characteristic polynomial is $A(z)B(z)A_{c}(z)$ and the Diophantine equation (5.4) becomes

$$A R + B S = A B A _ {c} \tag {5.55}$$

It follows from this equation that $R = B\bar{R}$ and $S = A\bar{S}$ . To obtain the desired closed-loop response $B_{c}$ must be a factor of $\bar{S}$ . The minimum-degree controller is then $\bar{S} = B_{c}$ , and it follows from (5.55) that

$$\bar {R} = A _ {c} - B _ {c}$$

The controller thus becomes

$$\frac {S}{R} = \frac {A B _ {c}}{R (A _ {c} - B _ {c})} \tag {5.56}$$

In this case we find that there is a very simple explicit solution to the poleplacement problem. A severe drawback of the method is that both poles and zeros of the process are canceled. To do this they must be stable and well damped. It must also be required that they are not heavily excited by disturbances.
