# THEOREM 6.4 Exponential stability

The difference equation (Eq. 6.23) is globally exponentially stable if there exist positive constants $\beta_{1},\beta_{2}$ , and $N$ such that for all $t$ ,

$$0 < \beta_ {1} I \leq \sum_ {k = t} ^ {t + N - 1} \varphi (k) \varphi^ {T} (k) \leq \beta_ {2} I < \infty \tag {6.26}$$

Proof: Choose $P = I$ and

$$C (t) = \frac {\sqrt {\gamma (2 \alpha + (2 - \gamma) \varphi^ {T} \varphi)}}{\alpha + \varphi^ {T} \varphi} \varphi^ {T}$$

where the argument t of $\varphi$ is suppressed. A straightforward calculation shows that Eq. (6.25) is satisfied, so the system is stable. To prove exponential stability, first observe that uniform observability of $(A(k), C(k))$ is equivalent to uniform observability of $((A(k) - B(k)C(k)), C(k))$ . Choosing

$$B (k) = - \frac {\gamma}{\sqrt {(\gamma (2 \alpha + (2 - \gamma) \varphi^ {T} \varphi)}} \varphi$$

we find that $A(k) - B(k)C(k) = I$ , and uniform asymptotic stability then corresponds to Eq. (6.26).

Notice that Eq. (6.26) is closely related to persistent excitation. (Compare with Definition 2.1.) It is thus found that exponential convergence of the gradient algorithm is closely connected to whether the input signal to the system is persistently exciting of sufficiently high order.

It should be pointed out that condition (6.26) is a persistent excitation condition for the regressors, not the external reference signal for the system. The excitation can be provided by the command signals and by the disturbances acting on the process. Notice, however, that excitation may be lost by feedback, which can introduce relations between the variables appearing in the regression vector. We discuss this later in this section.
