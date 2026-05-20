# Exercise 4.25: Optimal importance function for a linear system

The optimal importance function is given in (4.60), repeated here

$$q (x _ {i} (k) | x _ {i} (k - 1), y (k)) = p (x _ {i} (k) | x _ {i} (k - 1), y (k))$$

For the linear time-invariant model, this conditional density is the following normal density (Doucet et al., 2000)

$$
\begin{array}{l} p (x _ {i} (k) | x _ {i} (k - 1), y (k)) \sim N (\overline {{x}} (k), \overline {{P}}) \\ \overline {{{x}}} (k) = \overline {{{P}}} Q ^ {- 1} (A x _ {i} (k - 1) + B u (k - 1)) + \overline {{{P}}} C ^ {\prime} R ^ {- 1} y (k) \\ \overline {{P}} = \left(Q ^ {- 1} + C ^ {\prime} R ^ {- 1} C\right) ^ {- 1} \\ \end{array}
$$

Establish this result by first considering the linear transformation between $( x _ { i } ( k ) , y ( k ) )$ and $x _ { i } ( k - 1 ) , w ( k ) , \nu ( k )$ , and then using the formulas for taking conditional densities of normals.
