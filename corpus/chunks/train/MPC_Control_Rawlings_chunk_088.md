The density of $( x ( k ) , \nu ( k ) )$ follows from (1.24) since measurement noise $\nu ( k )$ is independent of $x ( k )$ and $\mathbf { y } ( k - 1 )$

$$
\left[ \begin{array}{c} x (k) \\ v (k) \end{array} \right] \sim N \left(\left[ \begin{array}{c} \hat {x} ^ {-} (k) \\ 0 \end{array} \right], \left[ \begin{array}{c c} P ^ {-} (k) & 0 \\ 0 & R \end{array} \right]\right)
$$

Equation (1.25) then gives the joint density

$$
\left[ \begin{array}{c} x (k) \\ y (k) \end{array} \right] \sim N \left(\left[ \begin{array}{c} \hat {x} ^ {-} (k) \\ C \hat {x} ^ {-} (k) \end{array} \right], \left[ \begin{array}{c c} P ^ {-} (k) & P ^ {-} (k) C ^ {\prime} \\ C P ^ {-} (k) & C P ^ {-} (k) C ^ {\prime} + R \end{array} \right]\right)
$$

We note $\left\{ \mathbf { y } ( k - 1 ) , \gamma ( k ) \right\} \ = \ \mathbf { y } ( k )$ , and using the conditional density result (1.26) gives

$$p _ {x (k) | \mathbf {y} (k)} (x (k) | \mathbf {y} (k)) = n (x (k), \hat {x} (k), P (k))$$

in which

$$\hat {x} (k) = \hat {x} ^ {-} (k) + L (k) (\mathcal {Y} (k) - C \hat {x} ^ {-} (k))L (k) = P ^ {-} (k) C ^ {\prime} \left(C P ^ {-} (k) C ^ {\prime} + R\right) ^ {- 1}P (k) = P ^ {-} (k) - P ^ {-} (k) C ^ {\prime} \left(C P ^ {-} (k) C ^ {\prime} + R\right) ^ {- 1} C P ^ {-} (k)$$

We forecast from k to $k + 1$ using the model

$$
x (k + 1) = \left[ \begin{array}{c c} A & I \end{array} \right] \left[ \begin{array}{c} x (k) \\ w (k) \end{array} \right]
$$

Because $w ( k )$ is independent of $x ( k )$ and $\mathbf { y } ( k )$ , the joint density of $( x ( k ) , w ( k ) )$ follows from a second use of (1.24)

$$
\left[ \begin{array}{c} x (k) \\ w (k) \end{array} \right] \sim N \left(\left[ \begin{array}{c} \hat {x} (k) \\ 0 \end{array} \right], \left[ \begin{array}{c c} P (k) & 0 \\ 0 & Q \end{array} \right]\right)
$$

and a second use of the linear transformation result (1.25) gives

$$p _ {x (k + 1) | \mathbf {y} (k)} (x (k + 1) | \mathbf {y} (k)) = n (x (k + 1), \hat {x} ^ {-} (k + 1), P ^ {-} (k + 1))$$

in which

$$
\begin{array}{l} \hat {x} ^ {-} (k + 1) = A \hat {x} (k) \\ P ^ {-} (k + 1) = A P (k) A ^ {\prime} + Q \\ \end{array}
$$

and the recursion is complete.
