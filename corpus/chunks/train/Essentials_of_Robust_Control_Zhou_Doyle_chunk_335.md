# Standard LQR Problem

Let a dynamical system be described by

$$\dot {x} = A x + B _ {2} u, \quad x (0) = x _ {0} \text { given but arbitrary } \tag {13.6}z = C _ {1} x + D _ {1 2} u \tag {13.7}$$

and suppose that the system parameter matrices satisfy the following assumptions:

(A1) $( A , B _ { 2 } )$ is stabilizable;

(A2) $D _ { 1 2 }$ has full column rank with $\left[ \begin{array} { l l } { D _ { 1 2 } } & { D _ { \perp } } \end{array} \right]$ unitary;

(A3) $( C _ { 1 } , A )$ is detectable;

$( \mathrm { A } 4 ) \left[ \begin{array} { c c } { A - j \omega I } & { B _ { 2 } } \\ { C _ { 1 } } & { D _ { 1 2 } } \end{array} \right] \mathrm { h a s ~ f u l l ~ c o l u m n ~ r a n k ~ f o r ~ a l l ~ } \omega .$

Find an optimal control law $u \in \mathcal { L } _ { 2 } [ 0 , \infty )$ such that the performance criterion $\left. { z } \right. _ { 2 } ^ { 2 }$ is minimized.

Remark 13.1 Assumption (A1) is clearly necessary for the existence of a stabilizing control function u. The assumption (A2) is made for simplicity of notation and is actually a restatement that $R = D _ { 1 2 } ^ { * } D _ { 1 2 } = I .$ . Note also that $D _ { \perp }$ drops out when $D _ { 1 2 }$ is square. It is interesting to point out that (A3) is not needed in the Extended LQR problem. The assumption (A3) enforces that the unconditional optimization problem will result in a stabilizing control law. In fact, the assumption (A3) together with (A1) guarantees that the input/output stability implies the internal stability; that is, $u \in { \mathcal { L } } _ { 2 }$ and $z \in { \mathcal { L } } _ { 2 }$ imply $x \in { \mathcal { L } } _ { 2 }$ , which will be shown in Lemma 13.1. Finally note that (A4) is equivalent to the condition that $\left( D _ { \bot } ^ { \ast } C _ { 1 } , A - B _ { 2 } D _ { 1 2 } ^ { \ast } C _ { 1 } \right)$ has no unobservable modes on the imaginary axis and is weaker than the popular assumption of detectability of $\left( D _ { \bot } ^ { \ast } C _ { 1 } , A - B _ { 2 } D _ { 1 2 } ^ { \ast } C _ { 1 } \right)$ . (A4), together with the stabilizability of $( A , B _ { 2 } )$ , guarantees by Corollary 12.7 that the following Hamiltonian matrix belongs to dom(Ric) and that $X = \operatorname { R i c } ( H ) \geq 0 { \mathrm { : } }$
