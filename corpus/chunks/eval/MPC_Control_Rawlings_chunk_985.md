Proposition C.7 (Relation of normal and tangent cones).

(a) At any point $\bar { u } \in U \subset \mathbb { R } ^ { m }$ ,

$$\hat {N} _ {U} (\bar {u}) = \mathcal {T} _ {U} (\bar {u}) ^ {*} := \{g \mid \langle g, h \rangle \leq 0 \forall h \in \mathcal {T} _ {U} (\bar {u}) \}$$

where, for any cone V , $V ^ { * } : = \{ g \mid \langle g , h \rangle \leq 0 \forall h \in V \}$ denotes the polar cone $o f V$ .

(b) $I f U$ is convex, then, at any point ${ \bar { u } } \in U$

$$\hat {N} _ {U} (\bar {u}) = \{g \mid \langle g, u - \bar {u} \rangle \leq 0 \forall u \in U \} \tag {C.16}$$

Proof. (a) To prove $\hat { N } _ { U } ( \bar { u } ) \subset \mathcal { T } _ { U } ( \bar { u } ) ^ { * }$ , we take an arbitrary point g in $\hat { N } _ { U } ( \bar { u } )$ and show that $\langle g , h \rangle \ \leq \ 0$ for all $h \in \mathcal T ( \bar { u } )$ implying that $g \in \mathcal { T } _ { U } ^ { * } ( \bar { u } )$ . For, if h is tangent to U at u¯, there exist, by definition, sequences $u { \xrightarrow [ { U } ] { \nu } } { \bar { u } }$ and $\lambda ^ { \nu } \searrow 0$ such that

$$h ^ {\nu} := (u ^ {\nu} - \bar {u}) / \lambda^ {\nu} \rightarrow h$$

Since $g \in \hat { N } _ { U } ( \bar { u } )$ , it follows from (C.15) that $\langle g , h ^ { \nu } \rangle \leq o ( \vert ( u ^ { \nu } - \bar { u } ) \vert ) =$ $o ( \lambda ^ { \nu } | h ^ { \nu } | )$ ; the limit as $\nu \to \infty$ yields $\langle g , h \rangle \leq 0$ , so that $g \in \mathcal { T } _ { U } ^ { * } ( \bar { u } )$ . Hence $\hat { N } _ { U } ( \bar { u } ) \subset \mathcal { T } _ { U } ( \bar { u } ) ^ { * }$ . The proof of this result, and the more subtle proof of the converse, that $\mathcal { T } _ { U } ( \bar { u } ) ^ { * } \subset \hat { N } _ { U } ( \bar { u } )$ , are given in Rockafellar and Wets (1998), Proposition 6.5.

(b) This part of the proposition is proved in (Rockafellar and Wets, 1998, Theorem 6.9).

We wish to derive optimality conditions for problems of the form $\mathbb { P } : \operatorname* { i n f } _ { u } \{ f ( u ) \mid u \in U \}$ . The value of the problem is defined to be

$$f ^ {0} := \inf _ {u} \{f (u) \mid u \in U \}$$

There may not exist a $u \in U$ such that $f ( u ) = f ^ { 0 }$ . If, however, $f ( \cdot )$ is continuous and U is compact, there exists a minimizing u in U, i.e.,

$$f ^ {0} = \inf _ {u} \{f (u) \mid u \in U \} = \min _ {u} \{f (u) \mid u \in U \}$$

The minimizing u, if it exists, may not be unique so

$$u ^ {0} := \arg \min _ {u} \{f (u) \mid u \in U \}$$

may be a set. We say u is feasible if $u \in U$ . A point u is globally optimal for problem P if u is feasible and $f ( \nu ) \geq f ( u )$ for all $\nu \in U$ . A point u is locally optimal for problem P if u is feasible and there exists $\mathtt { a } \varepsilon > 0$ such that $f ( \nu ) \geq f ( u )$ for all v in $( u \oplus \varepsilon { \mathcal { B } } ) \cap U$ where B is the closed unit ball $\{ u \mid \operatorname* { m i n } \left| u \right| \leq 1 \}$ .
