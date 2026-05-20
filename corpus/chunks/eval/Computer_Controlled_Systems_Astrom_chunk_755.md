$$r P _ {1} (z) P _ {1} \left(z ^ {- 1}\right) = \rho A _ {1} (z) A _ {2} ^ {-} (z) A _ {1} \left(z ^ {- 1}\right) A _ {2} ^ {-} \left(z ^ {- 1}\right) + B _ {1} (z) B _ {1} \left(z ^ {- 1}\right) \tag {12.69}$$

with $\deg P_1(z) = \deg A_1(z) + \deg A_2^- (z)$ .

Proof. Introducing the signal (12.65), the model (12.5) can be written as

$$A (q) y (k) = \tilde {B} (q) q ^ {m} w (k) + C (q) e (k)$$

The polynomials $A(q)$ and $\bar{B}(q)$ have the common factor $A_{2}^{+}(z)$ , which has all its zeros inside the unit disc, but no other common factors with zeros outside the unit disc or on the unit circle. It then follows from Theorem 12.4 that the optimal control law

$$w (k) = - \frac {\bar {S} (q)}{\bar {R} (q)} y (k)$$

is obtained from (12.47). Because $A(z)$ and $\bar{B}(z)$ have the stable common factor $A_2^+(z)$ , the polynomial $P(z)$ has the form

$$P (z) = A _ {2} ^ {+} (z) P _ {1} (z)$$

where $P_{1}(z)$ is the solution to the spectral-factorization problem (12.69). From Lemma 12.2 the polynomials $\bar{R}(z)$ and $\hat{S}(z)$ satisfy the equations

$$
\begin{array}{l} A (z) \bar {R} (z) + z ^ {m} \tilde {B} (z) \tilde {S} (z) = A _ {2} ^ {+} (z) P _ {1} (z) C (z) \\ A ^ {*} (z) X (z) + r P (z) \tilde {S} ^ {*} (z) = q ^ {m} \tilde {B} (z) C ^ {*} (z) \\ \end{array}
$$

with $\deg \tilde{R}(z) = \deg \tilde{S}(z) = n$ . Because $A_2^+$ divides $A(z)$ and $\tilde{B}(z)$ we get (12.68). Using (12.65) to express the control law in terms of the control variable $u$ gives the result.

Remark. Notice that using (12.67), Eq. (12.68) can be written as

$$A (z) R (z) + B (z) S (z) = A _ {2} (z) P _ {1} (z) C (z)$$

The LQG-solution can thus be interpreted as a pole-placement controller, where the poles are positioned at the zeros of $A_{2}$ , $P_{1}$ , and C. The controller also has the property that $A_{2}^{-}$ divides R. This is an example of the internal model principle.
