It then follows, as shown in Proposition 7.9, that for any $x \in \mathcal { X } , u _ { x } ^ { 0 } ( w )$ is optimal for $\mathbb { P } ( \boldsymbol { w } )$ for all $w ~ \in ~ R _ { x } ^ { 0 }$ . Because $\mathbb { P } ( \boldsymbol { w } )$ is a parametric linear program, however, rather than a parametric quadratic program, it is possible to simplify the definition of $R _ { x } ^ { 0 }$ . We note that $\nabla _ { u } V ( w , u _ { x } ^ { 0 } ( w ) ) = r$ for all $x \in { \mathcal { X } }$ , all $\boldsymbol { w } \in \mathbb { R } ^ { m }$ . Also, it follows from Proposition $7 . 8$ , since $u ^ { 0 } ( x )$ is optimal for $\mathbb { P } ( x )$ , that $- \nabla _ { u } V ( x , u ^ { 0 } ( x ) ) =$ $- r \in C ^ { * } ( x )$ so that the second condition in the definition above for

$R _ { x } ^ { 0 }$ is automatically satisfied. Hence we may simplify our definition for $R _ { x } ^ { 0 }$ ; for the parametric linear program, $R _ { x } ^ { 0 }$ may be defined by

$$R _ {x} ^ {0} := \{w \in \mathbb {R} ^ {n} \mid u _ {x} ^ {0} (w) \in \mathcal {U} (w) \} \tag {7.22}$$

Because $u _ { x } ^ { 0 } ( \cdot )$ is affine, it follows from the definition of $\mathcal { U } ( \boldsymbol { \omega } )$ that $R _ { x } ^ { 0 }$ is polyhedral. The next result follows from the discussion in Section 7.3.4:

Proposition 7.20 (Solution of P). For any $x \in \mathcal { X } , u _ { x } ^ { 0 } ( w )$ is optimal for $\mathbb { P } ( \boldsymbol { w } )$ for all w in the set $R _ { x } ^ { 0 }$ defined in (7.22).

Finally, the next result characterizes the solution of the parametric linear program $\mathbb { P } ( x )$ when the minimizer is unique.

Proposition 7.21 (Piecewise affine cost and solution).

(a) There exists a finite set of points X in X such that $\{ R _ { x } ^ { 0 } \ | \ x \in X \}$ is a polyhedral partition of X.

(b) The value function $V ^ { 0 } ( \cdot ) f o r { \mathbb { P } } ( x )$ and the minimizer $u ^ { 0 } ( \cdot )$ are piecewise affine in X being equal, respectively, to the affine functions $V _ { x } ^ { 0 } ( \cdot )$ and $u _ { x } ^ { 0 } ( \cdot )$ in each region $R _ { x } , x \in \mathcal { X }$ .

(c) The value function $V ^ { 0 } ( \cdot )$ and the minimizer $u ^ { 0 } ( \cdot )$ are continuous in X .

Proof. The proof of parts (a) and (b) follows, apart from minor changes, the proof of Proposition 7.10. The proof of part (c) uses the fact that $u ^ { 0 } ( x )$ is unique, by assumption, for all $x \in \mathcal { X }$ and is similar to the proof of Proposition 7.13. 
