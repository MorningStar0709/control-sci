$$x (s) = - u (s) / \beta (s) = \frac {(s - 1) (s + 1) (s + 3)}{(s + 1 1 . 7 0 8 5) (s + 2 . 2 1 4) (s + 0 . 0 7 7)}y (s) = v (s) / \beta (s) = \frac {(s + 1) (s + 3) (s + 1 0)}{(s + 1 1 . 7 0 8 5) (s + 2 . 2 1 4) (s + 0 . 0 7 7)}$$

Matlab programs can be used to find the appropriate F and L matrices in statespace so that the desired coprime factorization can be obtained. Let $A \in \mathbb { R } ^ { n \times n } , B \in$ $\mathbb { R } ^ { \times m }$ and $C \in \mathbb { R } ^ { p \times n }$ . Then an $F$ and an L can be obtained from

$$\gg \mathrm{F} = - \operatorname{lqr} (\mathrm{A}, \mathrm{B}, \text {eye(n)}, \text {eye(m)}); \% \text {or}$$

F=-place(A, B, Pf); % Pf= poles of A+BF   
$\gg \mathbf { L } = - \mathbf { l q r } ( \mathbf { A } ^ { \prime } , \mathbf { C } ^ { \prime } , \mathbf { e y e ( n ) } , \mathbf { e y e ( p ) } ) ^ { \prime } ; \mathcal { Y } _ { 0 } \mathrm { ~ o r ~ }$   
L = −place(A0 , C0 , Pl)0 ; % Pl=poles of A+LC.
