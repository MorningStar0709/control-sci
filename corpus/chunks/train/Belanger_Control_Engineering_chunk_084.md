$$
\dot {\mathbf {x}} = \left[ \begin{array}{l l} - \frac {3}{2} & \frac {1}{2} \\ \frac {1}{2} & - \frac {3}{2} \end{array} \right] \mathbf {x} + \left[ \begin{array}{l} \frac {1}{2} \\ \frac {1}{2} \end{array} \right] i _ {s}.
$$

To calculate the eigenvalues, write

$$
\begin{array}{l} \det (s I - A) = \det \left[ \begin{array}{c c} s + \frac {3}{2} & - \frac {1}{2} \\ - \frac {1}{2} & s + \frac {3}{2} \end{array} \right] \\ = s ^ {2} + 3 s + 2 \\ = (s + 1) (s + 2). \\ \end{array}
$$

The eigenvalues are -1 and -2.

The eigenvectors satisfy

$$A \mathbf {v} _ {i} = s _ {i} \mathbf {v} _ {i}.$$

For the eigenvalue $s_1 = -1$ ,

$$
\left[ \begin{array}{l l} - \frac {3}{2} & \frac {1}{2} \\ \frac {1}{2} & - \frac {3}{2} \end{array} \right] \left[ \begin{array}{l} v _ {1 1} \\ v _ {1 2} \end{array} \right] = - \left[ \begin{array}{l} v _ {1 1} \\ v _ {1 2} \end{array} \right]
$$

or

$$
\begin{array}{l} - \frac {3}{2} v _ {1 1} + \frac {1}{2} v _ {1 2} = - v _ {1 1} \\ \frac {1}{2} v _ {1 1} - \frac {3}{2} v _ {1 2} = - v _ {1 2}. \\ \end{array}
$$

The first equation yields $v_{12} = v_{11}$ . So does the second equation; when we solve for an eigenvector, one equation is always redundant. The reason is that an eigenvector is not unique: if $\mathbf{v}_i$ is an eigenvector, so is $\alpha \mathbf{v}_i$ , for any nonzero constant $\alpha$ . (A numerical algorithm will return a single vector, to be scaled if desired.)

The eigenvector corresponding to $s_{i} = -1$ is thus

$$
\mathbf {v} _ {1} = \alpha \left[ \begin{array}{l} 1 \\ 1 \end{array} \right]
$$

where $\alpha$ is any nonzero constant.

Corresponding to $s_2 = -2$ , we have

$$
\left[ \begin{array}{c c} - \frac {3}{2} & \frac {1}{2} \\ \frac {1}{2} & - \frac {3}{2} \end{array} \right] \left[ \begin{array}{l} v _ {2 1} \\ v _ {2 2} \end{array} \right] = - 2 \left[ \begin{array}{l} v _ {2 1} \\ v _ {2 2} \end{array} \right]
$$

which yields $v_{22} = -v_{21}$ . The eigenvector corresponding to $s_2 = -2$ is

$$
\mathbf {v} _ {2} = \beta \left[ \begin{array}{c} 1 \\ - 1 \end{array} \right]
$$

where $\beta$ is an arbitrary constant.

For $\mathbf{x}(0) = \alpha \left[ \begin{array}{l}1\\ 1 \end{array} \right]$ , the solution follows immediately from Equation 3.13; it is

$$
\mathbf {x} (t) = e ^ {- t} \alpha \left[ \begin{array}{c} 1 \\ 1 \end{array} \right].
$$

For $\mathbf{x}(0) = \beta \left[ \begin{array}{c}1\\ -1 \end{array} \right]$ , the solution is
