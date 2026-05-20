# 14.2 A Simplified $\mathcal { H } _ { \infty }$ Control Problem

The realization of the transfer matrix G is taken to be of the form

$$
G (s) = \left[ \begin{array}{c c c} A & B _ {1} & B _ {2} \\ \hline C _ {1} & 0 & D _ {1 2} \\ C _ {2} & D _ {2 1} & 0 \end{array} \right].
$$

The following assumptions are made:

(i) $( A , B _ { 1 } )$ is controllable and $( C _ { 1 } , A )$ is observable;   
(ii) $( A , B _ { 2 } )$ is stabilizable and $( C _ { 2 } , A )$ is detectable;

(iii) $D _ { 1 2 } ^ { * } \left[ \begin{array} { l l } { C _ { 1 } } & { D _ { 1 2 } } \end{array} \right] = \left[ \begin{array} { l l } { 0 } & { I } \end{array} \right]$

${ \left[ \begin{array} { l } { B _ { 1 } } \\ { D _ { 2 1 } } \end{array} \right] } D _ { 2 1 } ^ { * } = { \left[ \begin{array} { l } { 0 } \\ { I } \end{array} \right] } .$

Two additional assumptions that are implicit in the assumed realization for $G ( s )$ are that $D _ { 1 1 } = 0$ and $D _ { 2 2 } = 0$ . As we mentioned in the last chapter, $D _ { 2 2 } \neq 0$ does not pose any problem since it is easy to form an equivalent problem with $D _ { 2 2 } = 0$ by a linear fractional transformation on the controller $K ( s )$ . However, relaxing the assumption $D _ { 1 1 } = 0$ complicates the formulas substantially.

The $\mathcal { H } _ { \infty }$ solution involves the following two Hamiltonian matrices:

$$
H _ {\infty} := \left[ \begin{array}{c c} A & \gamma^ {- 2} B _ {1} B _ {1} ^ {*} - B _ {2} B _ {2} ^ {*} \\ - C _ {1} ^ {*} C _ {1} & - A ^ {*} \end{array} \right], \quad J _ {\infty} := \left[ \begin{array}{c c} A ^ {*} & \gamma^ {- 2} C _ {1} ^ {*} C _ {1} - C _ {2} ^ {*} C _ {2} \\ - B _ {1} B _ {1} ^ {*} & - A \end{array} \right].
$$

The important difference here from the $\mathcal { H } _ { 2 }$ problem is that the (1,2)-blocks are not sign definite, so we cannot use Theorem 12.4 in Chapter 12 to guarantee that $H _ { \infty } \in \mathrm { d o m } ( \mathrm { R i c } )$ or $\mathrm { R i c } ( H _ { \infty } ) \geq 0$ . Indeed, these conditions are intimately related to the existence of $\mathcal { H } _ { \infty }$ suboptimal controllers. Note that the (1,2)-blocks are a suggestive combination of expressions from the $\mathcal { H } _ { \infty }$ norm characterization in Chapter 4 (or bounded real lemma in Chapter 12) and from the $\mathcal { H } _ { 2 }$ synthesis of Chapter 13. It is also clear that if γ approaches infinity, then these two Hamiltonian matrices become the corresponding $\mathcal { H } _ { 2 }$ control Hamiltonian matrices. The reasons for the form of these expressions should become clear through the discussions and proofs for the following theorem.
