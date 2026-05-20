where, for all $a > 0 , W ( a ) : = \mathrm { l e v } _ { a } V _ { f } = \{ x \mid V _ { f } ( x ) \leq a \}$ is a sublevel set of $V _ { f }$ . Since P is positive definite, W (a) is an ellipsoid with the origin as its center. Comparing inequality (2.34) with (2.33), we see that (2.34) is satisfied if

$$V _ {f} (f (x, K x)) - V _ {f} \left(A _ {K} x\right) \leq (1 / 2) x ^ {\prime} Q ^ {*} x \quad \forall x \in W (a) \tag {2.35}$$

Let $e ( \cdot )$ be defined as follows

$$e (x) := f (x, K x) - A _ {K} x$$

so that

$$V _ {f} (f (x, K x)) - V _ {f} \left(A _ {K} x\right) = \left(A _ {K} x\right) ^ {\prime} P e (x) + (1 / 2) e (x) ^ {\prime} P e (x) \tag {2.36}$$

By definition, $e ( 0 ) \ = \ f ( 0 , 0 ) - A _ { K } 0 \ = \ 0$ and $e _ { x } ( x ) ~ = ~ f _ { x } ( x , K x ) ~ +$ $f _ { u } ( x , K x ) K - A _ { K }$ . It follows that $e _ { x } ( 0 ) = 0 $ . Since $f ( \cdot )$ is twice continuously differentiable, for any $\delta > 0$ , there exists a $c _ { \delta } > 0$ such that $| e _ { x x } ( x ) | \le c _ { \delta }$ for all x in δB. From Proposition A.11 in Appendix $\mathrm { A } ,$

$$
\begin{array}{l} | e (x) | = \left| e (0) + e _ {x} (0) x + \int_ {0} ^ {1} (1 - s) x ^ {\prime} e _ {x x} (s x) x d s \right| \\ \leq \int_ {0} ^ {1} (1 - s) c _ {\delta} | x | ^ {2} d s \leq (1 / 2) c _ {\delta} | x | ^ {2} \\ \end{array}
$$

for all x in $\delta \mathcal { B } .$ . From (2.36), we see that there exists an $\varepsilon \in ( 0 , \delta ]$ such that (2.35), and, hence, (2.34), is satisfied for all $x \in \varepsilon { \mathcal { B } } ,$ . Because of our choice of $\ell ( \cdot )$ , there exists a $c _ { 1 } > 0$ such that $V _ { f } ( x ) \geq \ell ( x , K x ) \geq$ $c _ { 1 } | x | ^ { 2 }$ for all $\boldsymbol { x } \in \mathbb { R } ^ { n }$ . It follows that $x \in W ( a )$ implies $| x | \leq \sqrt { a / c _ { 1 } }$ . We can choose a to satisfy $\sqrt { a / c _ { 1 } } = \varepsilon$ . With this choice, $x \in W ( a )$ implies $| x | \leq \varepsilon \leq \delta$ , which, in turn, implies (2.34) is satisfied.
