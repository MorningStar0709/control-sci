# B.3 Lyapunov Stability Theory

Energy in a passive electrical or mechanical system provides a useful analogy to Lyapunov stability theory. In a lumped mechanical system, the total stored energy is the sum of the potential and kinetic energies. As time proceeds, this energy is dissipated in friction and the total energy decays to zero at which point the system state is in equilibrium.

To establish stability or asymptotic stability, Lyapunov theory follows a similar path. If a real-valued function can be found which is positive and decreasing if the state does not lie in the set A, then the state converges to this set. We now make this intuitive idea more precise.

Definition B.10 (Lyapunov function). A function $V : \mathbb { R } ^ { n } \to \mathbb { R } _ { \geq 0 }$ is said to be a Lyapunov function for the system $x ^ { + } = f ( x )$ and set A if there exist functions $\alpha _ { i } \in \mathcal { K } _ { \infty } , i = 1 , 2$ and $\alpha _ { 3 } ~ \in ~ \mathcal { P D }$ such that for any $\boldsymbol { x } \in \mathbb { R } ^ { n }$ ,

$$V (x) \geq \alpha_ {1} (| x | _ {\mathcal {A}}) \tag {B.2}V (x) \leq \alpha_ {2} (| x | _ {\mathcal {A}}) \tag {B.3}V (f (x)) - V (x) \leq - \alpha_ {3} (| x | _ {\mathcal {A}}) \tag {B.4}$$

If V (·) satisfies Equations B.2–B.4 for all $x \in X$ where $X \supset \mathcal { A }$ is a positive invariant set for $x ^ { + } = f ( x )$ , then $V ( \cdot )$ is said to be a Lyapunov function in X for the system $x ^ { + } = f ( x )$ and set A.

The existence of a Lyapunov function is a sufficient condition for global asymptotic stability as shown in the next result which we prove under the assumption, common in MPC, that $\alpha _ { 3 } ( \cdot )$ is $\mathcal { K } _ { \infty }$ function.

Theorem B.11 (Lyapunov function and GAS). Suppose V (·) is a Lyapunov function for $x ^ { + } ~ = ~ f ( x )$ and set A with $\alpha _ { 3 } ( \cdot )$ a $\mathcal { K } _ { \infty }$ function. Then A is globally asymptotically stable.
