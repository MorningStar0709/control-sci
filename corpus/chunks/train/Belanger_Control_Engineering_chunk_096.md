Solving Equation 3.29 for $s_{0}$ and w involves polynomial manipulations and root finding. Whereas this is easily done by hand for low-order cases, it is unsuitable for computer calculation. Rewrite Equation 3.29 as

$$[ C (s _ {0} I - A) ^ {- 1} B + D ] \mathbf {w} = \mathbf {0} \tag {3.30}$$

and let

$$\theta = (s _ {0} I - A) ^ {- 1} B \mathbf {w}. \tag {3.31}$$

Then Equations 3.30 and 3.31 become

$$C \theta + D \mathbf {w} = \mathbf {0}$$

and

$$- (s _ {0} I - A) \theta + B \mathbf {w} = \mathbf {0}.$$

We write this as one matrix-vector equation,

$$
\left[ \begin{array}{c c} - s _ {0} I + A & B \\ C & D \end{array} \right] \left[ \begin{array}{l} \theta \\ \mathbf {w} \end{array} \right] = \mathbf {0}. \tag {3.32}
$$

The matrix in Equation 3.32 has dimensions $(n + m) \times (n + r)$ . For the case $m = r$ (equal numbers of inputs and outputs), then,

$$
\det \left[ \begin{array}{c c} - s _ {0} I + A & B \\ C & D \end{array} \right] = 0 \tag {3.33}
$$

which is also written as

$$
\det \left\{s _ {0} \left[ \begin{array}{c c} - I & 0 \\ 0 & 0 \end{array} \right] + \left[ \begin{array}{l l} A & B \\ C & D \end{array} \right] \right\} = 0. \tag {3.34}
$$

This latter equation defines a generalized eigenvalue problem, for which good algorithms are available.

Example 3.7 Calculate the poles and zeros for the system of Example 3.5 by computing the eigenvalues of $A$ for the poles and using Equation 3.33 for the zeros.

Solution The eigenvalues of the $A$ matrix have already been calculated and are equal to $-1$ and $-2$ . To calculate the zeros, apply Equation 3.33:

$$
\det \left[ \begin{array}{c c c} - s _ {0} & 1 & 1 \\ - 2 & - 3 - s _ {0} & 1 \\ \hdashline 1 & 0 & 0 \end{array} \right] = \mathbf {0}
$$

or

$$1 - (- 3 - s _ {0}) = 0s _ {0} = - 4$$

which tallies with the result of Example 3.5.
