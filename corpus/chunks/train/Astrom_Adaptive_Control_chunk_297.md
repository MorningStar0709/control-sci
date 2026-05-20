# LEMMA 5.1 Barbalat's lemma

If $g$ is a real function of a real variable $t$ , defined and uniformly continuous for $t \geq 0$ , and if the limit of the integral

$$\int_ {0} ^ {t} g (s) d s$$

as $t$ tends to infinity exists and is a finite number, then

$$\lim _ {t \rightarrow \infty} g (t) = 0$$

Remark. A consequence of Barbalat's lemma is that if $g \in L_{2}$ and dg/dt is bounded, then

$$\lim _ {t \rightarrow \infty} g (t) = 0$$

When applying Lyapunov theory to an adaptive control problem, we get a time derivative of the Lyapunov function V, which depends on the control signal and other signals in the system. If these signals are bounded, Lemma 5.1 and the remark that follows can be used on dV/dt to prove stability. We have the following theorem.
