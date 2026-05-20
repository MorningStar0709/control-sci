# THEOREM 5.9 Stability using augmented error

Consider a model-reference system for adaptation of a feedforward gain for a system with the transfer function G. Let $G_{1}G_{2}$ be a factorization of G such that $G_{1}$ is SPR. The parameter adjustment law

$$\frac {d \theta}{d t} = - \gamma \varepsilon \left(G _ {2} u _ {c}\right) \tag {5.59}$$

where

$$\varepsilon = e + G _ {1} \left(\theta G _ {2} u _ {\mathrm{c}}\right) - G \left(\theta u _ {\mathrm{c}}\right) \tag {5.60}$$

gives a closed-loop system in which the error goes to zero as t goes to infinity. Proof: Since $G_{1}$ is SPR, the discussion of the error model shows that $\varepsilon \in L_{2}$ . Remark 1. The trivial factorization with $G_{1} = 1$ is one possibility.

Remark 2. If the input signal is persistently exciting, it can be shown that the parameters also converge.

Remark 3. Notice that $G_{2}$ must be minimum phase to establish that $\theta$ converges to $\theta^{0}$ . The reason is that we have to go "backwards" through $G_{2}$ to show that $\theta - \theta^{0}$ goes to zero if the output $e$ goes to zero. That is, the inverse of $G_{2}$ must be stable. This is a condition that will be seen again in the general case in Section 5.8.

A block diagram of the system with augmented error is shown in Fig. 5.20. To implement the augmented error, it is necessary to introduce realizations of the transfer functions $G_{1}$ and $G_{2}$ . The augmented error was introduced by Monopoli. It was a key idea for adaptive control systems having pole excess larger than 1. Application of the idea to general linear systems is discussed in Section 5.8. In Section 5.9 we show that the augmented error appears naturally in the self-tuning regulator.
