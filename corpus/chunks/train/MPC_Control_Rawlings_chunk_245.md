Assumption 2.26 (Properties of constraint sets; time-varying case). For all $i \in \mathbb { I } _ { \geq 0 } , \mathbb { X } ( i )$ and $\mathbb { X } _ { f } ( i )$ are closed, $\mathbb { X } _ { f } ( i ) \subset \mathbb { X } ( i )$ and U(i) are compact; each set contains the origin.

Because of the time-varying nature of the problem, we need to extend our definitions of invariance and control invariance.

Definition 2.27 (Time-varying control invariant sets). The sequence of sets $\{ X ( i ) \mid i \in \mathbb { I } _ { \geq 0 } \}$ is said to be time-varying control invariant for the time-varying system $x ^ { + } = f ( x , u , i )$ if, for each $i \in \mathbb { I } _ { \geq 0 }$ , for each $x \in \mathcal { X } ( i )$ , there exists a $u \in \mathbb { U } ( i )$ such that $x ^ { + } = f ( x , u , i ) \in \mathcal { X } ( i + 1 )$ . The sequence of sets $\{ X ( i ) \mid i \in \mathbb { I } _ { \geq 0 } \}$ is said to be time-varying positive invariant for the time-varying system $x ^ { + } = f ( x , i )$ if, for each $x \in \mathcal { X } ( i )$ , $x ^ { + } = f ( x , i ) \in \mathcal { X } ( i + 1 )$ .

A sequence of sets $\{ \mathcal { X } ( i ) \}$ is a tube, and time-varying positive invariance of the sequence is positive invariance of the tube. If $( x , i )$ lies in the tube, i.e., if $x \in X ( i )$ for some $i \in \mathbb { I } _ { \geq 0 }$ , then all solutions of $x ^ { + } = f ( x , i )$ starting at event $( x , i )$ remain in the tube. The following results, which are analogs of the results for time-invariant systems given previously, are stated without proof.

Proposition 2.28 (Continuous system solution; time-varying case). Suppose Assumptions 2.25 and 2.26 are satisfied. For each initial time i and final time j, the function $( x , \mathbf { u } ) \mapsto \phi ( j ; x , i , \mathbf { u } )$ is continuous.

Proposition 2.29 (Existence of solution to optimal control problem; time-varying case). Suppose Assumptions 2.25 and 2.26 are satisfied. Then for each time $i \in \mathbb { I } _ { \geq 0 }$

(a) The function $( x , \mathbf { u } ) \mapsto V _ { N } ( x , i , \mathbf { u } )$ is continuous in $\mathbb { Z } _ { N } ( i )$ .   
(b) For each $x \in \mathcal { X } _ { N } ( i )$ , the control constraint set $\mathcal { U } _ { N } ( x , i )$ is compact.   
(c) For each $x \in \mathcal { X } _ { N } ( i )$ , a solution to $\mathbb { P } _ { N } ( x , i )$ exists.

(d) $\mathcal { X } _ { N } ( i )$ is closed.

(e) $I f \left\{ \mathbb { X } _ { f } ( i ) \right\}$ is time-varying control invariant for $x ^ { + } = f ( x , u , i )$ , then $\{ \mathcal { X } _ { N } ( i ) \}$ is time-varying control invariant for $x ^ { + } = f ( x , u , i )$ and timevarying positive invariant for $x ^ { + } = f ( x , \kappa _ { N } ( x , i ) , i )$ .

$$(f) 0 \in \mathcal {X} _ {N} (i).$$

Stability. As before, the receding horizon control law $\kappa _ { N } ( \cdot )$ , which is now time varying, is not necessarily optimal or stabilizing. By choosing the time-varying “ingredients” $V _ { f } ( \cdot )$ and $\mathbb { X } _ { f }$ in the optimal control
