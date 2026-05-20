# Exercise 2.17: Equality for quadratic functions

Prove the following result which is useful for analyzing the unreachable setpoint problem.

Lemma 2.45 (An equality for quadratic functions). Let X be a nonempty compact subset $o f \mathbb { R } ^ { n }$ , and let $\ell ( \cdot )$ be a strictly convex quadratic function on X defined by $\ell ( x ) : =$ $( 1 / 2 ) x ^ { \prime } \underline { { Q } } x + q ^ { \prime } x + c , \quad Q > 0$ . Consider a sequence $\{ x ( i ) \mid i \in \mathbb { I } _ { 1 : P } \}$ with mean $\bar { x } _ { P } : =$ $\textstyle ( 1 / P ) \sum _ { i = 1 } ^ { P } x ( i )$ . Then the following holds

$$\sum_ {i = 1} ^ {P} \ell (x (i)) = (1 / 2) \sum_ {i = 1} ^ {P} | x (i) - \bar {x} _ {P} | _ {Q} ^ {2} + P \ell (\bar {x} _ {P})$$

It follows from this lemma that $\ell ( \bar { x } _ { P } ) \leq ( 1 / P ) \sum _ { i = 1 } ^ { P } \ell ( x ( i ) )$ , which is Jensen’s inequality for the special case of a quadratic function.
