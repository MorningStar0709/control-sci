# 11.2 Parameterization of All Stabilizing Controllers

Consider again the standard system block diagram in Figure 11.1 with

$$
G (s) = \left[ \begin{array}{c c c} A & B _ {1} & B _ {2} \\ \hline C _ {1} & D _ {1 1} & D _ {1 2} \\ C _ {2} & D _ {2 1} & D _ {2 2} \end{array} \right] = \left[ \begin{array}{c c} G _ {1 1} (s) & G _ {1 2} (s) \\ G _ {2 1} (s) & G _ {2 2} (s) \end{array} \right].
$$

Suppose $( A , B _ { 2 } )$ is stabilizable and $( C _ { 2 } , A )$ is detectable. In this section we discuss the following problem:

Given a plant $G ,$ parameterize all controllers K that internally stabilize G.

This parameterization for all stabilizing controllers is usually called Youla parameterization. The parameterization of all stabilizing controllers is easy when the plant itself is stable.

Theorem 11.3 Suppose $G \in \mathcal { R } \mathcal { H } _ { \infty } $ ; then the set of all stabilizing controllers can be described as

$$K = Q (I + G _ {2 2} Q) ^ {- 1} \tag {11.2}$$

for any $Q \in \mathcal { R } \mathcal { H } _ { \infty }$ and $I + D _ { 2 2 } Q ( \infty )$ nonsingular.

Remark 11.2 This result is very natural considering Corollary 5.3, which says that a controller K stabilizes a stable plant $G _ { 2 2 }$ iff $K ( I - G _ { 2 2 } K ) ^ { - 1 }$ is stable. Now suppose $Q = K ( I - G _ { 2 2 } K ) ^ { - 1 }$ is a stable transfer matrix, then K can be solved from this equation which gives exactly the controller parameterization in the preceding theorem. ✸

Proof. Note that $G _ { 2 2 } ( s )$ is stable by the assumptions on $G .$ . Then it is straightforward to verify that the controllers given previously stabilize $G _ { 2 2 }$ . On the other hand, suppose $K _ { 0 }$ is a stabilizing controller; then $Q _ { 0 } : = K _ { 0 } ( I - G _ { 2 2 } K _ { 0 } ) ^ { - 1 } \in \mathcal { R } \mathcal { H } _ { \infty } ,$ , so $K _ { 0 }$ can be expressed as $K _ { 0 } = Q _ { 0 } ( I + G _ { 2 2 } Q _ { 0 } ) ^ { - 1 }$ . Note that the invertibility in the last equation is guaranteed by the well-posedness condition of the interconnected system with controller $K _ { 0 }$ since $I + D _ { 2 2 } Q _ { 0 } ( \infty ) = ( I - D _ { 2 2 } K _ { 0 } ( \infty ) ) ^ { - 1 }$ . ✷

However, if G is not stable, the parameterization is much more complicated. The results can be more conveniently stated using state-space representations.

Theorem 11.4 Let F and L be such that $A + L C _ { 2 }$ and $A + B _ { 2 } F$ are stable; then all controllers that internally stabilize G can be parameterized as the transfer matrix from y to u:

![](image/b5b3ce308ffd3d57a9a21c0524c63660e18713b5588b6405952bbe4cb2a58645.jpg)
