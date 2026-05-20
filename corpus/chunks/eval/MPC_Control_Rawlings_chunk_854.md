Assumptions (a) and (b) and their corollary (c), a growth condition on $f ( \cdot )$ , ensure that $f ^ { u } ( \cdot )$ satisfies the Caratheodory conditions stated earlier. Hence, our previous results apply, and there exists an interval $[ 0 , t _ { b } ]$ on which a unique solution $x ^ { u } ( \cdot )$ exists; moreover $| x ^ { u } ( t ) | $ ∞ as $t \nearrow \ t _ { b }$ . Since $x ^ { u } ( \cdot )$ satisfies

$$x ^ {u} (t) = x _ {0} + \int_ {0} ^ {t} f (x ^ {u} (s), u (s), s) d s$$

it follows from the growth condition that

$$
\begin{array}{l} \left| x ^ {u} (t) \right| \leq \left| x _ {0} \right| + \int_ {0} ^ {t} \left| f \left(x ^ {u} (s), u (s), s\right) \right| d s \\ \leq \left| x _ {0} \right| + c \int_ {0} ^ {t} (1 + \left| x ^ {u} (s) \right|) d s \\ \leq \left(\left| x _ {0} \right| + c\right) + c \int_ {0} ^ {t} \left| x ^ {u} (s) \right| d s \\ \end{array}
$$

Applying the Bellman-Gronwall Lemma yields

$$| x ^ {u} (t) | \leq (c + | x _ {0} |) e ^ {c t}$$

for all $t \in [ 0 , t _ { b } ) , u \in \mathcal { U }$ . If follows that the escape time $t _ { b }$ cannot be finite, so that, for all u in U, there exists a unique absolutely continuous solution $x ^ { u } ( \cdot )$ on T passing through $( x _ { 0 } , ( 0 ) )$ ). Moreover, for all u in $u ,$ all $t \in T$

$$| x ^ {u} (t) | \leq K$$

where $K : = ( c + | x _ { 0 } | ) e ^ { c }$ .
