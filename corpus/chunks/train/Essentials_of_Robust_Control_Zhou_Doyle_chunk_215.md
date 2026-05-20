Then the robust performance criterion in this case can be described as requiring that the closed-loop system be robustly stable and that

$$\left\| T _ {e \tilde {d}} \right\| _ {\infty} \leq 1, \quad \forall P _ {\Delta} \in \boldsymbol {\Pi}. \tag {8.5}$$

More specifically, an output multiplicatively perturbed system will be analyzed first. The analysis for other classes of models can be done analogously. The perturbed model can be described as

$$\boldsymbol {\Pi} := \{(I + W _ {1} \Delta W _ {2}) P: \Delta \in \mathcal {R H} _ {\infty}, \| \Delta \| _ {\infty} < 1 \} \tag {8.6}$$

with $W _ { 1 } , W _ { 2 } \in \mathcal { R } \mathcal { H } _ { \infty }$ . The explicit system diagram is as shown in Figure 8.10. For this class of models, we have

$$T _ {e \tilde {d}} = W _ {e} S _ {o} (I + W _ {1} \Delta W _ {2} T _ {o}) ^ {- 1} W _ {d},$$

and the robust performance is satisfied iff

$$\left\| W _ {2} T _ {o} W _ {1} \right\| _ {\infty} \leq 1$$

and

$$\left\| T _ {e \tilde {d}} \right\| _ {\infty} \leq 1, \forall \Delta \in \mathcal {R H} _ {\infty}, \| \Delta \| _ {\infty} < 1.$$

The exact analysis for this robust performance problem is not trivial and will be given in Chapter 10. However, some sufficient conditions are relatively easy to obtain by bounding these two inequalities, and they may shed some light on the nature of these problems. It will be assumed throughout that the controller K internally stabilizes the nominal plant P .

Theorem 8.7 Suppose $P _ { \Delta } \ \in \ \{ ( I + W _ { 1 } \Delta W _ { 2 } ) P \colon \Delta \in \mathcal { R H } _ { \infty } , \ \| \Delta \| _ { \infty } < 1 \}$ and K internally stabilizes P . Then the system robust performance is guaranteed if either one of the following conditions is satisfied:

(i) for each frequency ω

$$\overline {{{\sigma}}} (W _ {d}) \overline {{{\sigma}}} (W _ {e} S _ {o}) + \overline {{{\sigma}}} (W _ {1}) \overline {{{\sigma}}} (W _ {2} T _ {o}) \leq 1; \tag {8.7}$$

(ii) for each frequency ω

$$\kappa (W _ {1} ^ {- 1} W _ {d}) \overline {{{\sigma}}} (W _ {e} S _ {o} W _ {d}) + \overline {{{\sigma}}} (W _ {2} T _ {o} W _ {1}) \leq 1 \tag {8.8}$$

where $W _ { 1 }$ and $W _ { d }$ are assumed to be invertible and $\kappa ( W _ { 1 } ^ { - 1 } W _ { d } )$ is the condition number.
