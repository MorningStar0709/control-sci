$$
J _ {1} = \left[ \begin{array}{c c c c c} \lambda & 1 & & & \\ & \lambda & 1 & & \\ & & \ddots & \ddots & \\ & & & \lambda & 1 \\ & & & & \lambda \end{array} \right], D _ {1} = \left[ \begin{array}{c c c c c} 1 & & & & \\ & k & & & \\ & & \ddots & & \\ & & & k ^ {n _ {1} - 2} & \\ & & & & k ^ {n _ {1} - 1} \end{array} \right] \in \mathbb {C} ^ {n _ {1} \times n _ {1}}.
$$

Then $\operatorname* { i n f } _ { D _ { 1 } \in \mathbb { C } ^ { n _ { 1 } \times n _ { 1 } } } \overline { { \sigma } } ( D _ { 1 } J _ { 1 } D _ { 1 } ^ { - 1 } ) \ = \ \operatorname* { l i m } _ { k \to \infty } \overline { { \sigma } } ( D _ { 1 } J _ { 1 } D _ { 1 } ^ { - 1 } ) \ = \ | \lambda | .$ (Note that by Remark 10.2, the scaling matrix does not need to be Hermitian.) The conclusion follows by applying this result to each Jordan block.

That $\mu$ equals to the preceding upper-bound in this case is also equivalent to the fact that Lyapunov asymptotic stability and exponential stability are equivalent for discrete time systems. This is because $\rho \left( M \right) < 1$ (exponential stability of a discrete time system matrix M ) implies for some nonsingular $D \in \mathbb { C } ^ { n \times n }$

$$\overline {{\sigma}} (D M D ^ {- 1}) < 1 \text {or} (D ^ {- 1}) ^ {*} M ^ {*} D ^ {*} D M D ^ {- 1} - I < 0,$$

which, in turn, is equivalent to the existence of a $P = D ^ { * } D > 0$ such that

$$M ^ {*} P M - P < 0$$

(Lyapunov asymptotic stability).

• $S = 0 , F = 2$ : This case was studied by Redheffer [1959].   
• $S = 1 , F = 1$ : This is equivalent to a state-space characterization of the $\mathcal { H } _ { \infty }$ norm of a discrete time transfer function.   
• $S = 2 , F = 0$ : This is equivalent to the fact that for multidimensional systems (two dimensional, in fact), exponential stability is not equivalent to Lyapunov stability.   
• $S = 0 , F \geq 4$ : For this case, the upper-bound is not always equal to $\mu .$ This is important, as these are the cases that arise most frequently in applications. Fortunately, the bound seems to be close to $\mu .$ . The worst known example has a ratio of $\mu$ over the bound of about .85, and most systems are close to 1.
