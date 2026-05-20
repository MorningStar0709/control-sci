Taking the set A to be the origin $( \mathcal { A } = \{ 0 \} )$ so that $| x | _ { \mathcal { A } } = | x |$ , we see that if the origin is robustly asymptotically stable for $x ^ { + } = f ( x )$ , then, for each $\varepsilon > 0$ , there exists a $\delta > 0$ such that every trajectory of the perturbed system $x ^ { + } = f ( x + e ) + w$ with max $\left\{ \left\| \mathbf { e } \right\| , \left\| \mathbf { w } \right\| \right\} \leq \delta$ converges to εB (B is the closed unit ball); this is the attractivity property. Also, if the initial state x satisfies $| x | \le \beta ^ { - 1 } ( \varepsilon , 0 )$ , then $| \phi ( k ; x ) | \ \le$ $\beta ( \beta ^ { - 1 } ( \varepsilon , 0 ) , 0 ) + \varepsilon = 2 \varepsilon$ for all $k \in \mathbb { I } _ { \geq 0 }$ and for all $\phi \in S _ { \delta }$ , which is the Lyapunov stability property. Here the function $\beta ^ { - 1 } ( \cdot , 0 )$ is the inverse of the function $\alpha \mapsto \beta ( \alpha , 0 )$ .

We return to the question: under what conditions is asymptotic stability robust? This is answered by the following important result (Teel, 2004; Kellet and Teel, 2004):

Theorem 3.2 (Lyapunov function and robust GAS). Suppose A is compact and that $f ( \cdot )$ is locally bounded.3 The set A is robustly globally asymptotically stable for the system $x ^ { + } = f ( x )$ if and only if the system admits a continuous global Lyapunov function for A.

It is shown in Appendix B that for the system $x ^ { + } = f ( x ) , V : \mathbb { R } ^ { n } \to$ $\mathbb { R } _ { \geq 0 }$ is a global Lyapunov function for set A if there exist $\mathcal { K } _ { \infty }$ functions $\alpha _ { 1 } ( \cdot )$ and $\alpha _ { 2 } ( \cdot )$ , and a continuous positive definite function $\rho ( \cdot )$ , such that for all $\boldsymbol { x } \in \mathbb { R } ^ { n }$

$$
\begin{array}{l} \alpha_ {1} (| x | _ {\mathcal {A}}) \leq V (x) \leq \alpha_ {2} (| x | _ {\mathcal {A}}) \\ V (f (x)) \leq V (x) - \rho (| x | _ {\mathcal {A}}) \\ \end{array}
$$

in which $| x | _ { \mathcal { A } } : = d ( x , \mathcal { A } )$ , the distance of x from the set A. In MPC, the value function of the finite horizon optimal control problem that is solved online is used as a Lyapunov function. In certain cases, such as linear systems with polyhedral constraints, the value function is known to be continuous; see Proposition 7.13. Theorem 3.2, suitably modified because the region of attraction is not global, shows that asymptotic stability is robust, i.e., that asymptotic stability is not destroyed by small perturbations.
