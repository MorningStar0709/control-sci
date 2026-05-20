# Proof of the Kalman-Yakubovich Lemma

Having developed the notion of SPR, we can now give a proof of the Kalman-Yakubovic lemma, which was given as Lemma 5.2 in Section 5.5. Consider the linear system

$$\frac {d x}{d t} = A x + B u \tag {5.48}y = C x$$

which is assumed to be completely controllable and completely observable. The system has the transfer function

$$G (s) = C (s I - A) ^ {- 1} B \tag {5.49}$$

We will prove that a necessary and sufficient condition for $G(s)$ to be SPR is that there exist positive definite matrices P and Q such that

$$A ^ {T} P + P A = - Q \tag {5.50}$$

and

$$\boldsymbol {B} ^ {\mathrm{T}} \boldsymbol {P} = \boldsymbol {C} \tag {5.51}$$

We will first prove necessity. If we use $V = x^{T}Px$ as a Lyapunov function, it follows from Theorem 5.1 that the system (5.48) is stable. This implies that the transfer function $G(s)$ is analytic in the closed right half-plane. To prove that $G(s)$ is SPR, it remains to verify condition (iii) in Theorem 5.7. It follows from Eq. (5.50) that

$$- s P - A ^ {T} P + s P - P A = (- s I - A) ^ {T} P + P (s I - A) = Q$$

To obtain this equation, we have added and subtracted $sP$ . Multiplying the equation with $B^T(-sI - A)^{-T}$ from the left and $(sI - A)^{-1}B$ from the right gives

$$B ^ {T} P (s I - A) ^ {- 1} B + B ^ {T} (- s I - A) ^ {- T} P B = B ^ {T} (- s I - A) ^ {- T} Q (s I - A) ^ {- 1} B \tag {5.52}$$

Since $G^T(-s) = G(-s)$ , Eq. (5.49) now implies that

$$2 \operatorname{Re} G (i \omega) = G (i \omega) + G (- i \omega) = B ^ {T} (- i \omega I - A) ^ {- T} Q (i \omega I - A) ^ {- 1} B \geq 0$$

It now follows from Theorem 5.7 that $G(s)$ is PR. Replacing $s$ by $s - \varepsilon$ in the above calculations, we find in a similar way that

$$\operatorname{Re} G (i \omega - \varepsilon) \geq 0$$

Since the matrix $A$ has all its eigenvalues in the open left half-plane, it follows that the matrix $A + \varepsilon I$ is also stable. It now follows from Theorem 5.7 that $G(s)$ is SPR.

To prove sufficiency, we start with the assumption that the system (5.48) has a transfer function $G(s)$ that is SPR. The proof is based on a direct construction of the matrices P and Q. Consider the expression

$$G (s) + G (- s) = \frac {B (s)}{A (s)} + \frac {B (- s)}{A (- s)} = \frac {A (- s) B (s) + A (s) B (- s)}{A (s) A (- s)} = \frac {Q (s)}{A (s) A (- s)}$$

where

$$Q (s) = q _ {1} (- 1) ^ {n - 1} s ^ {2 (n - 1)} + q _ {2} (- 1) ^ {n - 2} s ^ {2 (n - 2)} + \dots + q _ {n}$$
