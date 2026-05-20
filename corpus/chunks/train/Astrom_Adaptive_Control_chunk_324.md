# THEOREM 5.7 Conditions for positive realness

A rational transfer function $G(s)$ with real coefficients is PR if and only if the following conditions hold.

(i) The function has no poles in the right half-plane.

(ii) If the function has poles on the imaginary axis or at infinity, they are simple poles with positive residues.

(iii) The real part of $G$ is nonnegative along the $i\omega$ axis, that is,

$$\operatorname{Re} (G (i \omega)) \geq 0 \tag {5.45}$$

A transfer function is SPR if conditions (i) and (iii) hold and if condition (ii) is replaced by the condition that $G(s)$ has no poles or zeros on the imaginary axis.

Proof: Assume that $G(s)$ is PR. Since it is rational, the only singularities are poles. A function assumes all values around a pole. According to Definition 5.5 the function has positive real part for $Re s \geq 0$ . Hence it cannot have poles in this region. Equation (5.45) follows by setting $s = i\omega$ in Definition 5.5. Furthermore, $G(s)$ cannot have multiple poles at infinity because the condition $\operatorname{Re} G(s) \geq 0$ for $Re s \geq 0$ would then be violated. For the same reason a pole at infinity must also have positive residue.

We have thus shown the necessity. To show sufficiency, we use the fact that a function that is analytic in a region assumes its largest values on the boundary. Consider the function

$$F (s) = e ^ {G (s)}$$

We have

$$| F (s) | = e ^ {\operatorname{Re} G (s)} \tag {5.46}$$

Let the region D be bounded by the imaginary axis and an infinite half-circle to the right with the imaginary axis as a diameter. Let $\Gamma$ be the boundary of D. Assume that conditions (i), (ii), and (iii) hold. Because of condition (iii) we have $|F(s)| > 1$ on the imaginary axis. It now remains to investigate the value of F on the large half-circle. It follows from condition (ii) that G has at most one pole at infinity. We have three cases: $G(s)$ may go to zero; it may go to a constant, which must be positive because of condition (iii); or it may go to infinity as ks, where the constant k must be positive because of condition (ii). We can thus conclude that $|F(s)| > 1$ on $\Gamma$ . Since F is analytic in D, the condition then also holds on D, and Eq. (5.45) then follows. Notice that it also follows that the function $G(s)$ does not have any zeros inside D.

We now illustrate the different passivity concepts on linear time-invariant systems.
