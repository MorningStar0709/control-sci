# Example 12.15 Elimination of a sinusoidal disturbance

A narrow-band sinusoidal disturbance with frequency centered at $\omega$ may be represented as white noise driving a system with the denominator

$$D (q) = q ^ {2} - 2 q \cos \omega h + 1$$

If the poles of the system dynamics do not correspond to D, the model becomes

$$A _ {1} (q) D (q) y (k) = B _ {1} (q) D (q) u (k) + C (q) e (k)$$

The optimal regulator is then such that $D(z)$ divides $R(z)$ .

Cancellation of process poles. A common factor of $A$ and $C$ corresponds to controllable modes that are not excited by the disturbances. Let $A_2$ be the greatest common divisor of $A$ and $C$ . The polynomial $A_2$ is stable because $C$ is stable, and it does not divide $B$ because there is no factor that divides all of $A, B$ , and $C$ . It follows from (12.47) that $A_2$ also divides the polynomial $S$ , which is the numerator of the regulator transfer function. Thus stable process poles that are not excited by the disturbances may be canceled.

Cancellation of process zeros. Common factors of B and C correspond to process zeros that block transmission both for the control signal u and for the disturbance e. Let $B_{2}$ be the greatest common divisor of B and C. The polynomial $B_{2}$ is stable and it does not divide A. It then follows from (12.47) that $B_{2}$ divides R. This means that the zeros corresponding to $B_{2} = 0$ are canceled by the regulator. Therefore, process zeros that are also transmission zeros for the disturbance C are canceled by the regulator.

For the minimum-variance control, it follows from (12.46) with $\rho = 0$ that

$$\sqrt {r} P = q ^ {d} B ^ {+} B ^ {- *}$$

where $\sqrt{r}=B^{-}(0)$ and from (12.47) that $B^{+}$ divides R. All stable zeros are thus canceled by the minimum-variance control law.

An analysis of the properties of the optimal-control law thus gives partial answers to the classic cancellation problem.
