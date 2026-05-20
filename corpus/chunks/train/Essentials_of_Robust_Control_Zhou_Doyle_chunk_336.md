$$
\begin{array}{l} H = \left[ \begin{array}{c c} A & 0 \\ - C _ {1} ^ {*} C _ {1} & - A ^ {*} \end{array} \right] - \left[ \begin{array}{c} B _ {2} \\ - C _ {1} ^ {*} D _ {1 2} \end{array} \right] \left[ \begin{array}{c c} D _ {1 2} ^ {*} C _ {1} & B _ {2} ^ {*} \end{array} \right] \\ = \left[ \begin{array}{c c} A - B _ {2} D _ {1 2} ^ {*} C _ {1} & - B _ {2} B _ {2} ^ {*} \\ - C _ {1} ^ {*} D _ {\perp} D _ {\perp} ^ {*} C _ {1} & - (A - B _ {2} D _ {1 2} ^ {*} C _ {1}) ^ {*} \end{array} \right]. \tag {13.8} \\ \end{array}
$$

Note also that if $D _ { 1 2 } ^ { * } C _ { 1 } = 0$ , then (A4) is implied by the detectability of $( C _ { 1 } , A )$ . ✸

Note that the Riccati equation corresponding to equation (13.8) is

$$(A - B _ {2} D _ {1 2} ^ {*} C _ {1}) ^ {*} X + X (A - B _ {2} D _ {1 2} ^ {*} C _ {1}) - X B _ {2} B _ {2} ^ {*} X + C _ {1} ^ {*} D _ {\perp} D _ {\perp} ^ {*} C _ {1} = 0. \tag {13.9}$$

Now let X be the corresponding stabilizing solution and define

$$F := - (B _ {2} ^ {*} X + D _ {1 2} ^ {*} C _ {1}). \tag {13.10}$$

Then $A + B _ { 2 } F$ is stable. Denote

$$A _ {F} := A + B _ {2} F, \quad C _ {F} := C _ {1} + D _ {1 2} F$$

and rearrange equation (13.9) to get

$$A _ {F} ^ {*} X + X A _ {F} + C _ {F} ^ {*} C _ {F} = 0. \tag {13.11}$$

Thus X is the observability Gramian of $( C _ { F } , A _ { F } )$ .

Consider applying the control law $u = F x$ to the system equations (13.6) and (13.7). The controlled system becomes

$$\dot {x} = A _ {F} x, \quad x (0) = x _ {0}z = C _ {F} x$$

or, equivalently,

$$\dot {x} = A _ {F} x + x _ {0} \delta (t), \quad x (0 _ {-}) = 0z = C _ {F} x.$$

The associated transfer matrix is

$$
G _ {c} (s) = \left[ \begin{array}{l l} A _ {F} & I \\ \hline C _ {F} & 0 \end{array} \right]
$$

and

$$\| G _ {c} x _ {0} \| _ {2} ^ {2} = x _ {0} ^ {*} X x _ {0}.$$

The proof of the following theorem requires a preliminary result about internal stability given input-output stability.

Lemma 13.1 If $u , z \in \mathcal { L } _ { 2 } [ 0 , \infty )$ and $( C _ { 1 } , A )$ is detectable in the system described by equations (13.6) and (13.7), then $x \in \mathcal { L } _ { 2 } [ 0 , \infty )$ . Furthermore, $x ( t ) \to 0$ as $t \to \infty$ .

Proof. Since $( C _ { 1 } , A )$ is detectable, there exists L such that $A + L C _ { 1 }$ is stable. Let ˆx be the state estimate of x given by

$$\dot {\hat {x}} = (A + L C _ {1}) \hat {x} + (L D _ {1 2} + B _ {2}) u - L z.$$

Then $\hat { x } \in \mathcal L _ { 2 } [ 0 , \infty )$ and $\hat { x } \to 0$ (see Problem 13.1) since z and u are in $\mathcal { L } _ { 2 } [ 0 , \infty )$ . Now let $e = x - { \hat { x } } ;$ then

$$\dot {e} = (A + L C _ {1}) e$$
