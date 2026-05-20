# Extended LQR Problem

Let a dynamical system be given by

$$\dot {x} = A x + B _ {2} u, \quad x (0) = x _ {0} \text { given but arbitrary }z = C _ {1} x + D _ {1 2} u$$

with the following assumptions:

(A1) $( A , B _ { 2 } )$ is stabilizable;

(A2) $D _ { 1 2 }$ has full column rank with $\left[ \begin{array} { l l } { D _ { 1 2 } } & { D _ { \perp } } \end{array} \right]$ unitary;

$( \mathrm { A } 3 ) \left[ \begin{array} { c c } { A - j \omega I } & { B _ { 2 } } \\ { C _ { 1 } } & { D _ { 1 2 } } \end{array} \right] \mathrm { h a s ~ f u l l ~ c o l u m n ~ r a n k ~ f o r ~ a l l ~ } \omega .$

Find an optimal control law $u \in \mathcal { L } _ { 2 } [ 0 , \infty )$ such that the system is internally stable $( \mathrm { i . e . , } x \in \mathcal { L } _ { 2 } [ 0 , \infty ) )$ and the performance criterion $\left. { z } \right. _ { 2 } ^ { 2 }$ is minimized.

Assume the same notation as in the last section, we have:

Theorem 13.3 There exists a unique optimal control for the extended LQR problem, namely $u = F x$ . Moreover,

$$\min _ {u \in \mathcal {L} _ {2} [ 0, \infty)} \| z \| _ {2} = \| G _ {c} x _ {0} \| _ {2}.$$

Proof. The proof of this theorem is very similar to the proof of the standard LQR problem except that, in this case, the input/output stability may not necessarily imply the internal stability. Instead, the internal stability is guaranteed by the way of choosing control law.

Suppose that $u \in \mathcal { L } _ { 2 } [ 0 , \infty )$ is such a control law that the system is stable, i.e., $x \in \mathcal { L } _ { 2 } [ 0 , \infty )$ . Then $v = u - F x \in \mathcal { L } _ { 2 } [ 0 , \infty )$ . On the other hand, let $v \in \mathcal { L } _ { 2 } [ 0 , \infty )$ and consider

$$
\left[ \begin{array}{l} \dot {x} \\ z \end{array} \right] = \left[ \begin{array}{c c} A _ {F} & B _ {2} \\ C _ {F} & D _ {1 2} \end{array} \right] \left[ \begin{array}{l} x \\ v \end{array} \right], \qquad x (0) = x _ {0}.
$$

Then $x , z \in \mathcal { L } _ { 2 } [ 0 , \infty )$ and $x ( \infty ) = 0$ since $A _ { F }$ is stable. Hence $u = F x + v \in \mathcal { L } _ { 2 } [ 0 , \infty )$ . Again the mapping $v = u - F x$ between $v \in \mathcal { L } _ { 2 } [ 0 , \infty )$ and those $u \in \mathcal { L } _ { 2 } [ 0 , \infty )$ that make $z \in \mathcal { L } _ { 2 } [ 0 , \infty )$ and $x \in \mathcal { L } _ { 2 } [ 0 , \infty )$ is one to one and onto. Therefore,

$$\min _ {u \in \mathcal {L} _ {2} [ 0, \infty)} \| z \| _ {2} = \min _ {v \in \mathcal {L} _ {2} [ 0, \infty)} \| z \| _ {2}.$$

Using the same technique as in the proof of the standard LQR problem, we have

$$\| z \| _ {2} ^ {2} = x _ {0} ^ {*} X x _ {0} + \| v \| _ {2} ^ {2}.$$

Thus, the unique optimal control is $v = 0 , { \mathrm { i . e . , } } u = F x .$ .
