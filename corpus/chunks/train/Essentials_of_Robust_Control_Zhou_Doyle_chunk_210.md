# 8.3.2 Multiplicative Uncertainty

In this section, we assume that the system model is described by the following set of multiplicative perturbations:

$$\Pi = (I + W _ {1} \Delta W _ {2}) P$$

with $W _ { 1 } , W _ { 2 } , \Delta \in \mathcal { R } \mathcal { H } _ { \infty }$ . Consider the feedback system shown in Figure 8.10.

Theorem 8.5 Let $\mathbf { I I } = \{ ( I + W _ { 1 } \Delta W _ { 2 } ) P : \Delta \in \mathcal { R H } _ { \infty } \}$ and let K be a stabilizing controller for the nominal plant P . Then the closed-loop system is well-posed and internally stable for all $\Delta \in \mathcal { R } \mathcal { H } _ { \infty }$ with $\| \Delta \| _ { \infty } < 1 ~ i f$ and only $i f \parallel W _ { 2 } T _ { o } W _ { 1 } \parallel _ { \infty } \leq 1$ .

Proof. We shall first prove that the condition is necessary for robust stability. Suppose $\| W _ { 2 } T _ { o } W _ { 1 } \| _ { \infty } > 1$ . Then by Lemma 8.3, for any given sufficiently small $\sigma > 0$ , there is a $\Delta \in \mathcal { R } \mathcal { H } _ { \infty }$ with $\| \Delta \| _ { \infty } < 1$ such that $( I + \Delta W _ { 2 } T _ { o } W _ { 1 } ) ^ { - 1 }$ has poles on the axis $\operatorname { R e } ( s ) = \sigma$ . This implies that

$$(I + \Pi K) ^ {- 1} = S _ {o} (I + W _ {1} \Delta W _ {2} T _ {o}) ^ {- 1}$$

has poles on the axis $\operatorname { R e } ( s ) = \sigma$ since σ can always be chosen so that the unstable poles are not cancelled by the zeros of $S _ { o }$ . Hence $\| W _ { 2 } T _ { o } W _ { 1 } \| _ { \infty } \leq 1$ is necessary for robust stability. The sufficiency follows from the small gain theorem. ✷
