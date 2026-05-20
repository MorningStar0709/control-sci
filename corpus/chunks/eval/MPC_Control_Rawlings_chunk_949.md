# B.4.2 Robustness

We turn now to stability conditions for systems subject to bounded disturbances (not vanishingly small) and described by

$$x ^ {+} = f (x, w) \tag {B.6}$$

where the disturbance w lies in the compact set W. This system may equivalently be described by the difference inclusion

$$x ^ {+} \in F (x) \tag {B.7}$$

where the set ${ \cal F } ( { \boldsymbol { x } } ) : = \{ f ( { \boldsymbol { x } } , { \boldsymbol { w } } ) ~ | ~ { \boldsymbol { w } } \in \mathbb { W } \}$ . Let S(x) denote the set of all solutions of (B.6) or (B.7) with initial state x. We require, in the sequel, that the set A is positive invariant for (B.6) (or for $x ^ { + } \in F ( x ) )$ :

Definition B.18 (Positive invariance with disturbances). The set A is positive invariant for $x ^ { + } = f ( x , w ) , w \in \mathbb { W } \operatorname { i f } x \in \mathcal { A }$ implies $f ( x , w ) \in$ A for all $w \in \mathbb { W }$ ; it is positive invariant for $x ^ { + } \in F ( x ) \operatorname { i f } x \in { \mathcal { A } }$ implies $F ( x ) \subseteq { \mathcal { A } }$ .

Clearly the two definitions are equivalent; A is positive invariant for $x ^ { + } \ = \ f ( x , w ) , w \in \mathbb { W }$ , if and only if it is positive invariant for $x ^ { + } \in F ( x )$ . In Definitions B.19-B.21, we use “positive invariant” to denote “positive invariant for $x ^ { + } = f ( x , w ) , w \in \mathbb { W } ^ { mathfrak { n } }$ or for $x ^ { + } \in F ( x )$ .

Definition B.19 (Local stability (disturbances)). The closed positive invariant set A is locally stable for $x ^ { + } = f ( x , w )$ , $w \in \mathbb { W }$ (or for $x ^ { + } \in$ $F ( x ) )$ if, for all $\varepsilon > 0$ , there exists a $\delta > 0$ such that, for each x satisfying $| x | _ { \mathcal { A } } < \delta$ , each solution $\phi \in S ( x )$ satisfies $| \phi ( i ) | _ { \mathcal { A } } < \varepsilon$ for all $i \in \mathbb { I } _ { \geq 0 }$ .

Definition B.20 (Global attraction (disturbances)). The closed positive invariant set A is globally attractive for the system $x ^ { + } = f ( x , w )$ , w ∈ W (or for $x ^ { + } \in F ( x ) )$ if, for each $x \in \mathbb { R } ^ { n }$ , each solution $\phi ( \cdot ) \in S ( x )$ satisfies $| \phi ( i ) | _ { \mathcal { A } }  0$ as $i  \infty$ .

Definition B.21 (GAS (disturbances)). The closed positive invariant set A is globally asymptotically stable for $x ^ { + } = f ( x , w ) , w \in \mathbb { W }$ (or for $x ^ { + } \in F ( x ) )$ if it is locally stable and globally attractive.
