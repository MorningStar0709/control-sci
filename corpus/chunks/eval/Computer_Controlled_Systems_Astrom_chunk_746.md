$$
\begin{array}{l} J _ {1} = \frac {1}{2 \pi i} \oint \frac {(B (z) B (z ^ {- 1}) + \rho A (z) A (z ^ {- 1})) R (z) R (z ^ {- 1})}{P (z) P (z ^ {- 1}) C (z) C (z ^ {- 1})} V (z) V (z ^ {- 1}) \frac {d z}{z} \\ = \frac {r}{2 \pi i} \oint \frac {R (z) R \left(z ^ {- 1}\right)}{C (z) C \left(z ^ {- 1}\right)} V (z) V \left(z ^ {- 1}\right) \frac {d z}{z} = r E \left(\frac {R (q)}{C (q)} v\right) ^ {2} \\ \end{array}
$$

For causal controllers with no time delay $v(t)$ can be expressed as $v(t) = V(q)e(t)$ , where $V(q)$ is a rational function with zero pole excess.

$$J _ {2} = \frac {\sigma^ {2}}{2 \pi i} \oint \frac {B (z) R (z) R (z ^ {- 1}) - \rho A (z) R (z) S (z ^ {- 1})}{P (z) C (z) P (z ^ {- 1})} V (z) \frac {d z}{z}$$

It follows from Equation (12.54) that

$$B (z) R \left(z ^ {- 1}\right) - \rho A (z) S \left(z ^ {- 1}\right) = P \left(z ^ {- 1}\right) X (z)$$

Hence

$$J _ {2} = \frac {\sigma^ {2}}{2 \pi i} \oint \frac {R (z) X (z)}{P (z) C (z)} V (z) \frac {d z}{z} = \mathbf {E} \left(\left(\frac {R (q) X (q)}{P (q) C (q)} v (k)\right) e (k)\right)$$

It was assumed that $P(z)$ and $C(z)$ are stable and it follows from Lemma 12.2 that $\deg X(z) < n$ . This implies that

$$\deg R (z) X (z) < \deg P (z) C (z) = 2 n$$

The quantity

$$\frac {R (q) X (q)}{P (q) C (q)} v (k)$$

is thus a function of $v(k - 1), v(k - 2), \ldots$ . Because all these terms are independent of $e(k), J_2$ becomes zero. The loss function can thus be written as

$$J = r \mathrm{E} \left(\frac {R (q)}{C (q)} v (k)\right) ^ {2} + \mathrm{E} \left(\frac {R (q)}{P (q)} e (k)\right) ^ {2} + \rho \mathrm{E} \left(\frac {S (q)}{P (q)} e (k)\right) ^ {2}$$

where P and C are stable polynomials. It follows that the loss function achieves its minimum (12.58) for $\upsilon = 0$ , which by (12.59) corresponds to the control law of (12.55). Equations (12.56) and (12.57) follow from (12.60) and (12.61), and Theorem 10.2 and (10.23) give the formula of (12.58).

Remark 1. The minimum-variance control law is a special case of Theorem 12.4 with $\rho = 0$ . It follows from (12.49) that $R^{*}(z)P(z) = -z^{d}B^{*}(z)X(z)$ . Because $\deg X(z) < n$ , we have $\deg R^{*}(z) < n$ for $\rho = 0$ . Because also $\deg S^{*}(z) < n$ the polynomials $R(z)$ and $S(z)$ have $z$ as a common factor. Introducing $B(z) = R^{+}(z)B^{-}(z)$ , where $B^{+}$ has all its zeros inside the unit disc and $B^{-}$ all its zeros outside the unit disc, we get

$$\sqrt {r} P (z) = z ^ {d} B ^ {+} (z) B ^ {- *} (z)$$

where $\sqrt{r} = B^{-}(0)$ . The Diophantine equation (12.47) then becomes
