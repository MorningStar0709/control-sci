# Properties of the Optimal Regulator

Some properties of the model influence the optimal-control laws. The basic model used is given by (12.5)—that is,

$$A (q) y (k) = B (q) u (k) + C (q) e (k) \tag {12.70}$$

The ratio B/A represents the pulse-transfer function of the process, and the ratio C/A represents the pulse-transfer function that generates the disturbance of the process output. The polynomials A, B, and C may have common factors that reflect the way the control signal and the disturbance are coupled to the system. There are, however, no factors common to all three polynomials. Compare this with the discussion in Sec. 12.2, where the model is derived. The presence of common factors that will directly influence the properties of the regulators will now be investigated.

The internal-model principle. Factors that are common to polynomials A and B correspond to disturbance modes that are not controllable from u. Such modes will appear as factors of P. Let

$$A _ {2} = \operatorname * {g c d} (A, B)$$

be the greatest common divisor of polynomials $A$ and $B$ . If $A_2$ is stable, it follows from Theorem 12.4 that $A_2$ also divides $P$ . If $A_2$ has a factor $A_2^-$ with all its zeros outside the unit disc, the corresponding result follows from Theorem 12.5. In this case it also follows from Theorem 12.5 that $A_2$ divides $R$ . This observation is called the internal-model principle; it says that to regulate a system with unstable disturbances, the disturbance dynamics must also appear in the dynamics of the regulator. A few examples illustrate this idea.
