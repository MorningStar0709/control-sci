# Exercise 1.46: More on conditional densities

In deriving the discrete time Kalman filter, we have $p _ { x | \mathbf { y } } ( x ( k ) | \mathbf { y } ( k ) )$ and we wish to calculate recursively $p _ { x | \mathbf { y } } ( x ( k + 1 ) | \mathbf { y } ( k + 1 ) )$ ) after we collect the output measurement at time $k + 1$ . It is straightforward to calculate $p _ { x , y | \mathbf { y } } ( x ( k + 1 ) , y ( k + 1 ) | \mathbf { y } ( k ) )$ from our established results on normal densities and knowledge of $p _ { x | \mathbf { y } } ( x ( k ) | \mathbf { y } ( k ) )$ , but we still need to establish a formula for pushing the $y ( k + 1 )$ to the other side of the conditional density bar. Consider the following statement as a possible lemma to aid in this operation.

$$p _ {a | b, c} (a | b, c) = \frac {p _ {a , b | c} (a , b | c)}{p _ {b | c} (b | c)}$$

If this statement is true, prove it. If it is false, give a counterexample.
