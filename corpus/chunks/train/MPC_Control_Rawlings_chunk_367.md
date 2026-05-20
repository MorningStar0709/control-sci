# 3.3.1 Introduction

In this section we show how robust RHC may be obtained, in principle, using DP. Our concern is to use DP to gain insight. The results we obtain here are not of practical use for complex systems, but reveal the nature of the problem and show what the ideal optimal control problem solved online should be.

In Section 3.2 we examined the inherent robustness of an asymptotically stable system. If uncertainty is present, and it always is, it is preferable to design the controller to be robust, i.e., able to cope with some uncertainty. In this section we discuss the design of a robust controller for the system

$$x ^ {+} = f (x, u, w) \tag {3.16}$$

in which a bounded disturbance input w models the uncertainty. The disturbance is assumed to satisfy $w \in \mathbb { W }$ where W is compact convex, and contains the origin in its interior. The controlled system is required to satisfy the same state and control constraints as above, namely $x \in \mathbb { X }$ and $u \in \mathbb { U }$ , as well as a terminal constraint $\boldsymbol { x } ( N ) \in \mathbb { X } _ { f } ,$ . The solution at time k of (3.16) with control and disturbance sequences $\mathbf { u } = \{ u ( 0 ) , \ldots , u ( N - 1 ) \}$ and $\mathbf { w } = \{ w ( 0 ) , \ldots , w ( N - 1 ) \}$ if the initial state is x at time 0 is $x ( k ; x , { \mathbf { u } } , { \mathbf { w } } )$ . Similarly, the solution at time k due to feedback policy $\pmb { \mu }$ and disturbance sequence w is denoted by $x ( k ; x , \pmb { \mu } , \mathbf { w } )$ . As discussed previously, the cost may be taken to be that of the nominal trajectory, or the average, or maximum taken over all possible realizations of the disturbance sequence. Here we employ, as is common in the literature, the maximum over all realizations of the disturbance sequence w, and define the cost due to policy $\pmb { \mu }$ with initial state x to be

$$V _ {N} (x, \boldsymbol {\mu}) := \max _ {\mathbf {w}} \{J _ {N} (x, \boldsymbol {\mu}, \mathbf {w}) \mid \mathbf {w} \in \mathcal {W} \} \tag {3.17}$$

in which $\mathcal { W } = \mathbb { W } ^ { N }$ is the set of admissible disturbance sequences, and $J _ { N } ( x , \pmb { \mu } , \mathbf { w } )$ is the cost due to an individual realization w of the disturbance process and is defined by

$$J _ {N} (x, \boldsymbol {\mu}, \mathbf {w}) := \sum_ {i = 0} ^ {N - 1} \ell (x (i), u (i), w (i)) + V _ {f} (x (N)) \tag {3.18}$$
