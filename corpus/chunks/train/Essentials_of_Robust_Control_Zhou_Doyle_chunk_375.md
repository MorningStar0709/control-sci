J _ {\infty} := \left[ \begin{array}{c c} A ^ {*} & 0 \\ - B _ {1} B _ {1} ^ {*} & - A \end{array} \right] - \left[ \begin{array}{c} C ^ {*} \\ - B _ {1} D _ {\bullet 1} ^ {*} \end{array} \right] \tilde {R} ^ {- 1} \left[ \begin{array}{c c} D _ {\bullet 1} B _ {1} ^ {*} & C \end{array} \right]
X _ {\infty} := \operatorname{Ric} (H _ {\infty}) \qquad Y _ {\infty} := \operatorname{Ric} (J _ {\infty})
F := \left[ \begin{array}{l} F _ {1 \infty} \\ F _ {2 \infty} \end{array} \right] := - R ^ {- 1} [ D _ {1 \bullet} ^ {*} C _ {1} + B ^ {*} X _ {\infty} ]

L := \left[ \begin{array}{c c} L _ {1 \infty} & L _ {2 \infty} \end{array} \right] := - [ B _ {1} D _ {\bullet 1} ^ {*} + Y _ {\infty} C ^ {*} ] \tilde {R} ^ {- 1}
$$

Partition $D , F _ { 1 \infty }$ , and $L _ { \mathrm { 1 \infty } }$ are as follows:

$$
\left[ \begin{array}{c c} & F ^ {\prime} \\ \hline L ^ {\prime} & D \end{array} \right] = \left[ \begin{array}{c c c c} & F _ {1 1 \infty} ^ {*} & F _ {1 2 \infty} ^ {*} & F _ {2 \infty} ^ {*} \\ \hline L _ {1 1 \infty} ^ {*} & D _ {1 1 1 1} & D _ {1 1 1 2} & 0 \\ L _ {1 2 \infty} ^ {*} & D _ {1 1 2 1} & D _ {1 1 2 2} & I \\ L _ {2 \infty} ^ {*} & 0 & I & 0 \end{array} \right].
$$

Remark 14.3 In the above matrix partitioning, some matrices may not exist depending on whether $D _ { 1 2 }$ or $D _ { 2 1 }$ is square. This issue will be discussed further later. For the time being, we shall assume that all matrices in the partition exist. ✸

Theorem 14.7 Suppose G satisfies the assumptions $( A 1 ) { - } ( A 4 )$ .

(a) There exists an admissible controller $K ( s )$ such that $| | \mathcal { F } _ { \ell } ( G , K ) | | _ { \infty } < \gamma ~ ( i . e . _ { ; }$ $\| T _ { z w } \| _ { \infty } < \gamma ) \ i f$ and only if

(i) $\gamma > \operatorname* { m a x } ( \overline { \sigma } [ D _ { 1 1 1 1 } , D _ { 1 1 1 2 } , ] , \overline { \sigma } [ D _ { 1 1 1 1 } ^ { * } , D _ { 1 1 2 1 } ^ { * } ] )$ ;

(ii) $H _ { \infty } \in \mathrm { d o m } ( \mathrm { R i c } ) \ w i t h \ X _ { \infty } = \mathrm { R i c } ( H _ { \infty } ) \ge 0 ;$

(iii) $J _ { \infty } \in \mathrm { d o m } ( \mathrm { R i c } )$ with $Y _ { \infty } = \operatorname { R i c } ( J _ { \infty } ) \geq 0 ,$

(iv) $\rho ( X _ { \infty } Y _ { \infty } ) < \gamma ^ { 2 }$ .

(b) Given that the conditions of part $( a )$ are $s a t i s f i e d ,$ then all rational internally stabilizing controllers K(s) satisfying $| | \mathcal { F } _ { \ell } ( G , K ) | | _ { \infty } < \gamma$ are given by

$$K = \mathcal {F} _ {\ell} (M _ {\infty}, Q) \quad \text { for arbitrary } Q \in \mathcal {R H} _ {\infty} \quad \text { such that } \| Q \| _ {\infty} < \gamma$$

where
