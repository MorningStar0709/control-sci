The subscript x indicates that the equality constraints in $\mathbb { P } _ { x } ( \boldsymbol { w } )$ depend on x. Problem $\mathbb { P } _ { x } ( \boldsymbol { w } )$ is an optimization problem with a quadratic cost function and linear equality constraints and is, therefore, easily solved; see the exercises at the end of this chapter. Its solution is

$$V _ {x} ^ {0} (w) = (1 / 2) w ^ {\prime} Q _ {x} w + r _ {x} ^ {\prime} w + s _ {x} \tag {7.3}u _ {x} ^ {0} (w) = K _ {x} w + k _ {x} \tag {7.4}$$

for all w such that $I ^ { 0 } ( w ) = I ^ { 0 } ( x )$ where $Q _ { x } \in \mathbb { R } ^ { n \times n } , r _ { x } \in \mathbb { R } ^ { n } , s _ { x } \in \mathbb { R }$ , $K _ { x } \in \mathbb { R } ^ { m \times n }$ and $k _ { x } \in \mathbb { R } ^ { m }$ are easily determined. Clearly, $u _ { x } ^ { 0 } ( x ) =$ $u ^ { 0 } ( x ) ;$ ; but, is $u _ { x } ^ { 0 } ( w )$ , the optimal solution to $\mathbb { P } _ { x } ( \boldsymbol { w } )$ , the optimal solution $u ^ { 0 } ( \boldsymbol { w } )$ to $\mathbb { P } ( \boldsymbol { w } )$ in some region containing x and, if it is, what is the region? Our optimality condition answers this question. For all $x \in { \mathcal { X } }$ , let the region $R _ { x } ^ { 0 }$ be defined by

$$
R _ {x} ^ {0} := \left\{w \left| \begin{array}{c} u _ {x} ^ {0} (w) \in \mathcal {U} (w) \\ - \nabla_ {u} V (w, u _ {x} ^ {0} (w)) \in C ^ {*} (x, u ^ {0} (x)) \end{array} \right. \right\} \tag {7.5}
$$

Because of the equality constraint $M _ { x } ^ { 0 } u = N _ { x } ^ { 0 } w + p _ { x } ^ { 0 }$ in problem $\mathbb { P } _ { x } ( \boldsymbol { w } )$ , it follows that $I ( w , u _ { x } ^ { 0 } ( w ) ) ~ \supseteq ~ I ( x , u ^ { 0 } ( x ) )$ , and that $C ( w , u _ { x } ^ { 0 } ( w ) ) \subseteq$ $C ( x , u ^ { 0 } ( x ) )$ and $C ^ { * } ( w , u _ { x } ^ { 0 } ( w ) ) \supseteq C ^ { * } ( x , u ^ { 0 } ( x ) )$ for all $w \in R _ { x } ^ { 0 }$ . Hence $w \in R _ { x } ^ { 0 }$ implies $u _ { x } ^ { 0 } ( w ) \in \mathcal { U } ( w )$ and $- \nabla _ { u } V \big ( w , u _ { x } ^ { 0 } ( w ) \big ) \in C ^ { * } \big ( w , u _ { x } ^ { 0 } ( w ) \big )$ for all $w \in R _ { x } ^ { 0 }$ which, by Proposition 7.8, is a necessary and sufficient condition for $u _ { x } ^ { 0 } ( w )$ to be optimal for $\mathbb { P } ( \boldsymbol { w } )$ . In fact, $I ( w , u _ { x } ^ { 0 } ( w ) ) =$ $I ( x , u ^ { 0 } ( x ) )$ so that $C ^ { * } ( w , u _ { x } ^ { 0 } ( w ) ) = C ^ { * } ( x , u ^ { 0 } ( x ) )$ for all w in the interior of $R _ { x } ^ { 0 }$ . The obvious conclusion of this discussion is

Proposition 7.9 (Solution of $\mathbb { P } ( w ) , w \in R _ { x } ^ { 0 } )$ . For any $x \in \mathcal { X } , u _ { x } ^ { 0 } ( w )$ is optimal $f o r \mathbb { P } ( \boldsymbol { \boldsymbol { w } } )$ for all $w \in R _ { x } ^ { 0 }$ .

The constraint $u _ { x } ^ { 0 } ( w ) \in \mathcal { U } ( w )$ may be expressed as

$$M (K _ {x} w + k _ {x}) \leq N w + p$$
