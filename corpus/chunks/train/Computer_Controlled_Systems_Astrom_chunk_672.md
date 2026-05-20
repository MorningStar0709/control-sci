The Riccati equation can now be used to rewrite an equation that corresponds to (11.35). This gives an expression for the closed-loop poles.

$$
\begin{array}{l} Q _ {2} + H ^ {T} \left(z ^ {- 1}\right) H (z) = Q _ {2} + \Gamma^ {T} \left(z ^ {- 1} I - \Phi\right) ^ {- T} C ^ {T} C (z I - \Phi) ^ {- 1} \Gamma \\ = Q _ {2} + \Gamma^ {T} (S + S \Phi (z I - \Phi) ^ {- 1} + (z ^ {- 1} I - \Phi) ^ {- T} \Phi^ {T} S \\ \left. + \left(z ^ {- 1} I - \Phi\right) ^ {- T} L ^ {T} R L (z I - \Phi) ^ {- 1}\right) \Gamma \\ = R + R L (z I - \Phi) ^ {- 1} \Gamma + \Gamma^ {T} (z ^ {- 1} I - \Phi) ^ {- T} L ^ {T} R \\ + \Gamma^ {T} (z ^ {- 1} I - \Phi) ^ {- T} L ^ {T} R L (z I - \Phi) ^ {- 1} \Gamma \\ = \left(I + L (z ^ {- 1} I - \Phi) ^ {- 1} \Gamma\right) ^ {T} R \left(I + L (z I - \Phi) ^ {- 1} \Gamma\right) \\ = \left(I + H _ {1} (z ^ {- 1})\right) ^ {T} R \left(I + H _ {1} (z)\right) \tag {11.37} \\ \end{array}
$$

where

$$H _ {1} (z) = L (z I - \Phi) ^ {- 1} \Gamma$$

Equation (11.37) gives a spectral factorization of

$$\boldsymbol {Q} _ {2} + \boldsymbol {H} ^ {T} (z ^ {- 1}) \boldsymbol {H} (z).$$

Consider the SISO case. Then

$$H (z) = C (z I - \Phi) ^ {- 1} \Gamma = \frac {B (z)}{A (z)}$$

and the closed-loop system is defined by

$$H _ {c} (z) = C \left(z I - (\Phi - \Gamma L)\right) ^ {- 1} \Gamma = \frac {B (z)}{P (z)}$$

Notice that H and $H_{c}$ have the same zeros. Compare with Sec. 4.6. Further, the return difference of the system with the LQ-controller is

$$1 + L (z I - \Phi) ^ {- 1} \Gamma = \frac {P (z)}{A (z)}$$

Hence

$$H _ {1} (z) = \frac {P (z) - A (z)}{A (z)}$$

Now assume that the controller in (11.18) is replaced by

$$u (k) = - \beta L x (k) \tag {11.38}$$

where $\beta$ is a positive scalar. The return difference when (11.38) is used is

$$1 + \beta H _ {1} (z)$$

Thus the stability of the closed-loop system when (11.38) is used is determined from

$$A (z) + \beta \left(P (z) - A (z)\right) = 0 \tag {11.39}$$

The gain margin can now be determined from (11.39) by using root locus or by plotting the Nyquist curve for $(P - A)/A$ . Because A and P are monic and $\deg A = \deg P$ , it follows that $\deg(P - A) \leq n - 1$ . This implies that the root locus of (11.39) with respect to $\beta$ goes to infinity along at least one asymptote. Hence the discrete-time LQ controller has a finite gain margin, as opposed to the continuous-time LQ-controller, which has infinite gain margin.

In the scalar case, (11.37) can be written as

$$\rho A (z ^ {- 1}) A (z) + B (z ^ {- 1}) B (z) = r P (z ^ {- 1}) P (z) \tag {11.40}$$

where $r = \Gamma^{T} S \Gamma + \rho$ .
