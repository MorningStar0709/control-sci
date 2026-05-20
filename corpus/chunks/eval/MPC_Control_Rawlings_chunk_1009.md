# C.3.2 Continuity of the Value Function

Our main reason for introducing set-valued functions is to provide us with tools for analyzing the continuity properties of the value function and optimal control law in constrained optimal control problems.

These problems have the form

$$V ^ {0} (x) = \min \{V (x, u) \mid u \in U (x) \} \tag {C.28}u ^ {0} (x) = \arg \min \{V (x, u) \mid u \in U (x) \} \tag {C.29}$$

where $U : \mathbb { R } ^ { n }  \mathbb { R } ^ { m }$ is a set-valued function and $V : \mathbb { R } ^ { n } \times \mathbb { R } ^ { m } \to \mathbb { R }$ is continuous; in optimal control problems arising from MPC, u should be replaced by $\mathbf { u } = \{ u ( 0 ) , u ( 1 ) , \ldots , u ( N - 1 ) \}$ and m by Nm. We are interested in the continuity properties of the value function $V ^ { 0 } : \mathbb { R } ^ { n } \to$ R and the control law $u ^ { 0 } : \mathbb { R } ^ { n }  \mathbb { R } ^ { m }$ ; the latter may be set-valued (if the minimizer in (C.28) is not unique).

The following max problem has been extensively studied in the literature

$$\phi^ {0} (x) = \max \left\{\phi (x, u) \mid u \in U (x) \right\}\mu^ {0} (x) = \arg \max \left\{\phi (x, u) \mid u \in U (x) \right\}$$

If we define $\phi ( \cdot )$ by $\phi ( x , u ) : = - V ( x , u )$ , we see that $\phi ^ { 0 } ( x ) = - V ^ { 0 } ( x )$ and $\mu ^ { 0 } ( x ) = u ^ { 0 } ( x )$ so that we can obtain the continuity properties of $V ^ { 0 } ( \cdot )$ and $u ^ { 0 } ( \cdot )$ from those of $\phi ^ { 0 } ( \cdot )$ and $\mu ^ { 0 } ( \cdot )$ respectively. Using this transcription and Corollary 5.4.2 and Theorem 5.4.3 in Polak (1997) we obtain the following result:

Theorem C.28 (Minimum theorem). Suppose that $V : \mathbb { R } ^ { n } \times \mathbb { R } ^ { m } \to \mathbb { R }$ is continuous, that $U : \mathbb { R } ^ { n }  \mathbb { R } ^ { m }$ is continuous, compact-valued and satisfies $U ( x ) \subset \mathbb { U }$ for all $x \in \mathcal { X }$ where U is compact. Then $V ^ { 0 } ( \cdot )$ is continuous and $u ^ { 0 } ( \cdot )$ is outer semicontinuous. If, in addition, $u ^ { 0 } ( x ) =$ $\{ \mu ^ { 0 } ( x ) \}$ (there is a unique minimizer $\mu ^ { 0 } ( x ) ,$ , then $\mu ^ { 0 } ( \cdot )$ is continuous.
