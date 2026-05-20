# ■ Theorem 4.5

The 2-DOF configuration of Figure 4.27 is internally stable if, and only if, the transfer functions T, PS, $P^{-1}T$ , RS, $R^{-1}T$ , RPS, and $R^{-1}P^{-1}T$ are all stable.

Proof: Those are the transfer functions of the three-input, three-output system of Figure 4.27. Since the system is controllable and observable, the stability of these functions is both necessary and sufficient. Of course, the conditions of Theorem 4.5 are also applicable to Figure 4.26, because the choices of inputs and outputs do not affect internal stability. ■

Since $H_{wd}$ and $H_v$ are the same as in the 1-DOF case, the following is a convenient design procedure:

a. Create a 1-DOF design by selecting $F$ , concentrating on the responses to disturbances and observation noise. This part is independent of $R$ . It fixes $S$ and $T$ , which satisfy the first three conditions of Theorem 4.5; those conditions are precisely the stability conditions for the 1-DOF case.   
b. With $S$ in hand, choose $R$ to satisfy some design objective for $H_{d} = RPS$ .

From Theorem 4.5, we know that $H_{d} = RPS$ must be stable, but we must also see what restrictions, if any, are placed on $H_{d}$ by the requirements that $RS, R^{-1}T$ , and $R^{-1}P^{-1}T$ also be stable.

It is desirable to cancel out RHP zeros of PS by poles of R, so as to make $H_{d} = RPS$ a minimum-phase transfer function. The sensitivity S has zeros at the RHP poles of P; those do not appear in PS, due to the pole-zero cancellation. S may have other RHP zeros, which may be cancelled by poles of R, as this would satisfy the condition that both RS and RPS be stable. The RHP zeros of P may not be cancelled out. Such zeros cannot also be zeros of S, because S = 1 at RHP zeros of P. If we try to cancel an RHP zero of P with a pole of R, RPS will be stable, but not RS. It follows that $H_{d} = RPS$ , the set-point to output-transfer functions, must retain the RHP zeros of P. These are the only obligatory RHP zeros of $H_{d}$ , since the RHP zeros of S that are left in the product PS may be cancelled by R.

If one starts from the stability of $R^{-1}T$ and $R^{-1}P^{-1}T$ , a similar argument can be constructed about the RHP poles of $R^{-1}$ , i.e., the RHP zeros of R. The conclusion is that R may have RHP zeros only at those RHP zeros of T that are not also zeros of P. That result is somewhat academic, because it would rarely be desirable to give R any RHP zeros, as these would appear in $H_{d}=RPS$ .
