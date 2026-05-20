# 2.4.1 Introduction

To establish stability we employ Lyapunov theorems such as Theorem B.13 in Appendix B. Because we are considering the regulator problem in this chapter, we are concerned with asymptotic or exponential stability of the origin. Hence, we replace A in Theorem B.13 of Appendix B by {0}, the set consisting of a single point, the origin. Thus, the origin is asymptotically stable with a region of attraction X for the system $x ^ { + } = f ( x )$ if there exist: a Lyapunov function V , a positive invariant set X, two $\mathcal { K } _ { \infty }$ functions $\alpha _ { 1 } ( \cdot )$ and $\alpha _ { 2 } ( \cdot )$ , and a positive definite function $\alpha _ { 3 } ( \cdot )$ satisfying

$$V (x) \geq \alpha_ {1} (| x |) \tag {2.15}V (x) \leq \alpha_ {2} (| x |) \tag {2.16}V (f (x)) \leq V (x) - \alpha_ {3} (| x |) \tag {2.17}$$

for all $x \in X$ . Recall that $\alpha : \mathbb { R }  \mathbb { R } _ { \ge 0 }$ is a $\mathcal { K } _ { \infty }$ function if it is continuous, strictly increasing, zero at zero, and is unbounded; and α is a positive definite function if it is continuous and positive everywhere except at the origin. Our task in this chapter is to find a function $V ( \cdot )$ with these properties for the MPC system $x ^ { + } = f ( x , \kappa _ { N } ( x ) )$ .
