Figure C.12 illustrates a subgradient. In the figure, g is one element of the subgradient because $f ( \nu ) \geq f ( u ) + \langle g , \nu - u \rangle$ for all $\nu ; g$ is the slope of the line passing through the point $( u , f ( u ) )$ . To obtain a bound on $d ( u , U ( x ) )$ we require the following result which is a special case of the much more general result of the theorem of Clarke et al.:

Theorem C.31 (Clarke et al. (1998)). Take a nonnegative valued, convex function $\psi : \mathbb { R } ^ { n } \times \mathbb { R } ^ { m } \to \mathbb { R }$ . Let $U ( \boldsymbol { x } ) : = \{ u \in \mathbb { R } ^ { m } \mathrm { ~ } | \mathrm { ~ } \psi ( \boldsymbol { x } , u ) = 0 \}$ and ${ \mathcal { X } } : = \{ x \in \mathbb { R } ^ { n } \mid U ( x ) \neq \emptyset \}$ . Assume there exists a $\delta > 0$ such that

$$u \in \mathbb {R} ^ {m}, x \in \mathcal {X}, \psi (x, u) > 0 \text { and } g \in \partial_ {u} \psi (x, u) \implies | g | > \delta$$

where $\partial _ { u } \psi ( x , u )$ denotes the convex subgradient of $\psi$ with respect to the variable u. Then, for each $x \in \mathcal { X } , d ( u , U ( x ) ) \leq \psi ( x , u ) / \delta$ for all $u \in \mathbb { R } ^ { m }$ .

The proof of this result is given in the reference cited above. We next use this result to bound the distance of u from $U ( x )$ where, for each $x , U ( x )$ is polyhedral.

Corollary C.32 (A bound on d $( u , U ( x ^ { \prime } ) )$ for $u \in U ( x ) ) . \ 7$ Suppose Z is a polyhedron in $\mathbb { R } ^ { n } \times \mathbb { R } ^ { m }$ and let X denote its projection on $\mathbb { R } ^ { n } ( \mathcal { X } = \{ x  $ $\exists u \in \mathbb { R } ^ { m }$ such that $( x , u ) \in \mathcal { Z } \}$ . Let $\mathcal { U } ( x ) : = \{ u \ | \ ( x , u ) \in \mathcal { Z } \}$ . Then there exists a $K > 0$ such that for all $x , x ^ { \prime } \in \mathcal { X } , d ( u , U ( x ^ { \prime } ) ) \leq K | x ^ { \prime } - x |$ for all $u \in U ( x )$ (or, for all $x , x ^ { \prime } \in \mathcal { X }$ , all $u \in U ( x )$ , there exists a $u ^ { \prime } \in U ( x ^ { \prime } )$ such that $| u ^ { \prime } - u | \leq K | x ^ { \prime } - x | )$ .
