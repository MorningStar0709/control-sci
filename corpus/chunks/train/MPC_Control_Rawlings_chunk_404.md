This equality follows from the fact that for all $x \in S$ , the constraint $x \in \{ z \}$ ⊕S in problem $\mathbb { P } _ { N } ^ { * } ( x )$ is satisfied by $z = 0$ since $0 \in S$ . Because $\bar { V } _ { N } ^ { 0 } ( 0 ) ~ = ~ 0$ , it follows that $V _ { N } ^ { * } ( x ) \ = \ \bar { V } _ { N } ^ { 0 } ( z ^ { * } ( x ) ) \ \le \ \bar { V } _ { N } ^ { 0 } ( 0 ) \ = \ 0 ;$ since $V _ { N } ^ { * } ( x ) \geq 0$ we deduce that $V _ { N } ^ { * } ( x ) = 0 $ . It also follows that $z ^ { * } ( x ) = 0$ for all $x \in S$ so that $z ^ { * } ( x )$ is a “measure” of how far x is from the set S .

For each $i \in \mathbb { I } _ { \geq 0 }$ , let $x ( i ) : = \phi ( i ; x ( 0 ) , \allowbreak \kappa _ { N } ( \cdot ) , \mathbf { w } )$ , the solution of $x ^ { + } = A x + B \kappa _ { N } ( x ) + w$ at time i if the initial state at time 0 is $x ( 0 )$ . It follows from $( 3 . 4 0 ) – ( 3 . 4 2 )$ that $V _ { N } ^ { * } ( x ( i ) ) ~ \le ~ \gamma ^ { i } V _ { N } ^ { * } ( x ( 0 ) )$ where $\gamma : =$ $1 - c _ { 1 } / c _ { 2 } \in ( 0 , 1 )$ . Hence there exist $c > 0$ and $\delta = \sqrt { \mathcal { Y } }$ such that

$$\left| z ^ {*} (x (i)) \right| \leq c \delta^ {i} \left| z ^ {*} (x (0)) \right| \tag {3.43}$$

for all $i \in \mathbb { I } _ { \geq 0 }$ . For all i, $~ , x ( i ) = z ^ { * } ( x ( i ) ) + e ( i )$ where $e ( i ) \in S$ so that $| x ( i ) | _ { S } = d ( z ^ { * } ( x ( i ) ) + e ( i ) , S ) \leq d ( z ^ { * } ( x ( i ) ) + e ( i ) , e ( i ) ) = | z ^ { * } ( x ( i ) ) | _ { S }$ . In fact, though this is harder to show, $d ( \{ z \} \oplus S , S ) = | z |$ . Hence

$$\left| x (i) \right| _ {S} \leq \left| z ^ {*} (x (i)) \right| \leq c \left| z ^ {*} (x (0)) \right| \delta^ {i}$$

so that $x ( i )$ converges robustly exponentially fast to S but S is not necessarily robustly exponentially stable for $x ^ { + } = A x + B \kappa _ { N } ( x ) + w$ , $w \in \mathbb { W } ,$ .

We define the sets X(i) for $i \in \mathbb { I } _ { \geq 0 }$ by

$$X (i) := \left\{z ^ {*} (x (i)) \right\} \oplus S \tag {3.44}$$

The Hausdorff distance between X(i) and S satisfies

$$d _ {H} (X (i), S) = | z ^ {*} (x (i)) | \leq c \delta^ {i} | z ^ {*} (x (0)) | = c \delta^ {i} d _ {H} (X (0), S)$$

for all $i \in \mathbb { I } _ { \geq 0 }$ . Exercise 3.4 shows that $d _ { H } ( \{ z \} \oplus S , S ) = | z |$ . We have therefore proved the following.

Proposition 3.17 (Exponential stability of tube-based MPC without nominal trajectory). The set S is exponentially stable with a region of attraction ${ \mathcal { Z } } _ { N } \oplus S$ for the set difference equation

$$X ^ {+} = F (X, \mathbb {W})$$

in which $F : 2 ^ { \mathbb { X } } \to 2 ^ { \mathbb { X } }$ is defined by

$$F (X) := \{A x + B \kappa_ {N} (x) + w \mid x \in X, w \in \mathbb {W} \}$$

Robust exponential stability of S for $X ^ { + } = F ( X , \mathbb { W } )$ is not as strong as robust exponential stability of S for $x ^ { + } = A x + B \kappa _ { N } ( x ) + w , w \in \mathbb { W }$ . To establish the latter, we would have to show that for some $c > 0$ and all $i \in \mathbb { I } _ { \geq 0 } , | x ( i ) | _ { S } \leq c \delta ^ { i } | x ( 0 ) | _ { S }$ . Instead we have merely shown that $| x ( i ) | _ { S } \leq c \delta ^ { i } | z ^ { * } ( x ( 0 ) ) |$ .
