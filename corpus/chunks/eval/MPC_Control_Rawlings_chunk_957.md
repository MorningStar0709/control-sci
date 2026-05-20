The converse, i.e., input to state stability implies the existence of a smooth ISS-Lyapunov function for $x ^ { + } = f ( x , w )$ is also proved in Jiang and Wang (2002), Theorem 1. We now consider the case when the state satisfies the constraint $x \in \mathbb { X }$ where X is a closed subset of $\mathbb { R } ^ { n }$ . Accordingly, we assume that the disturbance w satisfies $w \in \mathbb { W }$ where W is a compact set containing the origin and that $X \subset \mathbb { X }$ is a closed robust positive invariant set for $x ^ { + } = f ( x , w ) , w \in \mathbb { W } \mathrm { o r }$ , equivalently, for $x ^ { + } \in F ( x , u )$ .

Definition B.36 (ISS (constrained)). Suppose that W is a compact set containing the origin and that $X \subset \mathbb { X }$ is a closed robust positive invariant set for $x ^ { + } = f ( x , w ) , w \in \mathbb { W }$ . The system $x ^ { + } = f ( x , w ) , w \in \mathbb { W }$ is ISS in X if there exists a class $\mathcal { K L }$ function $\beta ( \cdot )$ and a class K function $\sigma ( \cdot )$ such that, for all $x \in X$ , all $\mathbf { w } \in \mathcal { W }$ where W is the set of infinite sequences w satisfying $w ( i ) \in \mathbb { W }$ for all $i \in \mathbb { I } _ { \geq 0 }$

$$\left| \phi (i; x, \mathbf {w} _ {i}) \right| \leq \beta (\left| x \right|, i) + \sigma (\left\| \mathbf {w} _ {i} \right\|)$$

Definition B.37 (ISS-Lyapunov function (constrained)). A function $V :$ $X ~  ~ \mathbb { R } _ { \geq 0 }$ is an ISS-Lyapunov function in X for system $x ^ { + } = f ( x , w )$ if there exist $\mathcal { K } _ { \infty }$ functions $\alpha _ { 1 } ( \cdot ) , \alpha _ { 2 } ( \cdot ) , \alpha _ { 3 } ( \cdot )$ and a K function $\sigma ( \cdot )$ such that for all $x \in X$ , all $w \in \mathbb { W }$

$$V (| x |) \geq \alpha_ {1} (| x |)V (| x |) \leq \alpha_ {2} (| x |)V (f (x, w)) - V (x) \leq - \alpha_ {3} (| x |) + \sigma (| w |)$$

The following result is a trivial generalization of Lemma 3.5 in Jiang and Wang (2001).

Lemma B.38 (ISS-Lyapunov function implies ISS (constrained)). Suppose that W is a compact set containing the origin and that $X \subset \mathbb { X }$ is a closed robust positive invariant set for $x ^ { + } = f ( x , w ) , w \in \mathbb { W }$ . $I f f ( \cdot )$ is continuous and there exists a continuous ISS-Lyapunov function in X for the system $x ^ { + } = f ( x , w ) , w \in \mathbb { W }$ , then the system $x ^ { + } = f ( x , w )$ , $w \in \mathbb { W }$ is ISS in X.
