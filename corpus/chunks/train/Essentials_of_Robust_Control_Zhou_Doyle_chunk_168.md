# 7.1 Lyapunov Equations

Testing stability, controllability, and observability of a system is very important in linear system analysis and synthesis. However, these tests often have to be done indirectly. In that respect, the Lyapunov theory is sometimes useful. Consider the following Lyapunov equation:

$$A ^ {*} Q + Q A + H = 0 \tag {7.1}$$

with given real matrices A and H. It is well known that this equation has a unique solution iff $\lambda _ { i } ( A ) + \bar { \lambda } _ { j } ( A ) \neq 0 , \forall i , j$ . In this section, we shall study the relationships between the solution Q and the stability of A. The following results are standard.

Lemma 7.1 Assume that A is stable, then the following statements hold:

(i) $\begin{array} { r } { Q = \int _ { 0 } ^ { \infty } e ^ { A ^ { * } t } H e ^ { A t } d t . } \end{array}$   
(ii) $Q > 0 \ i f H > 0$ and $Q \geq 0 \ i f H \geq 0$ .

(iii) If $H \geq 0$ , then (H, A) is observable $i f Q > 0$ .

An immediate consequence of part (iii) is that, given a stable matrix A, a pair (C, A) is observable if and only if the solution to the following Lyapunov equation

$$A ^ {*} Q + Q A + C ^ {*} C = 0$$

is positive definite, where Q is the observability Gramian. Similarly, a pair $( A , B )$ is controllable if and only if the solution to

$$A P + P A ^ {*} + B B ^ {*} = 0$$

is positive definite, where P is the controllability Gramian.

In many applications, we are given the solution of the Lyapunov equation and need to conclude the stability of the matrix A.

Lemma 7.2 Suppose Q is the solution of the Lyapunov equation (7.1), then

(i) $\mathrm { R e } \lambda _ { i } ( A ) \leq 0 \ i f Q > 0$ and $H \geq 0$ .   
(ii) A is stable $i f Q > 0$ and $H > 0$ .   
(iii) A is stable $i f Q \ge 0 , H \ge 0$ , and $( H , A )$ is detectable.

Proof. Let λ be an eigenvalue of A and $v \neq 0$ be a corresponding eigenvector, then $A v = \lambda v$ . Premultiply equation (7.1) by $v ^ { * }$ and postmultiply equation (7.1) by v to get

$$2 \operatorname{Re} \lambda (v ^ {*} Q v) + v ^ {*} H v = 0.$$

Now if $Q > 0$ , then $v ^ { * } Q v > 0$ , and it is clear that $\operatorname { R e } \lambda \leq 0 { \mathrm { ~ i f ~ } } H \geq 0$ and $\mathrm { R e } \lambda < 0$ if $H > 0$ . Hence (i) and (ii) hold. To see (iii), we assume $\mathrm { R e } \lambda \geq 0 .$ . Then we must have $v ^ { * } H v = 0 \ ( \mathrm { i . e . , } \ H v = 0 )$ . This implies that λ is an unstable and unobservable mode, which contradicts the assumption that $( H , A )$ is detectable. ✷
