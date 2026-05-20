# Determinant

The determinant $|A|$ of an nxn matrix A is evaluated in many ways. One of the ways for a 3x3 matrix A is as follows.

$$
\mathbf {A} = \left[ \begin{array}{c c c} a _ {1 1} & a _ {1 2} & a _ {1 3} \\ a _ {2 1} & a _ {2 2} & a _ {2 3} \\ a _ {3 1} & a _ {3 2} & a _ {3 3} \end{array} \right];

\begin{array}{l} | \mathbf {A} | = a _ {1 1} (- 1) ^ {1 + 1} \left| \begin{array}{c c} a _ {2 2} & a _ {2 3} \\ a _ {3 2} & a _ {3 3} \end{array} \right| + a _ {1 2} (- 1) ^ {1 + 2} \left| \begin{array}{c c} a _ {2 1} & a _ {2 3} \\ a _ {3 1} & a _ {3 3} \end{array} \right| \\ + a _ {1 3} (- 1) ^ {1 + 3} \left| \begin{array}{l l} a _ {2 1} & a _ {2 2} \\ a _ {3 1} & a _ {3 2} \end{array} \right|. \tag {A.2.14} \\ \end{array}
$$

Note that in (A.2.14), the sub-determinant associated with $a_{11}$ is formed by deleting the row and column containing $a_{11}$ . Thus, the 3x3 determinant $|A|$ is expressed in terms of the 2x2 sub-determinants. Once again, this 2x2 sub-determinant can be written, for example, as

$$
\left| \begin{array}{l l} a _ {2 2} & a _ {2 3} \\ a _ {3 2} & a _ {3 3} \end{array} \right| = a _ {2 2} a _ {3 3} - a _ {2 3} a _ {3 2}. \tag {A.2.15}
$$

Some useful results on determinants are

$$| \mathbf {A} | = | \mathbf {A} ^ {\prime} || \mathbf {A B} | = | \mathbf {A} |. | \mathbf {B} |\left| \mathbf {I} + \mathbf {A B} \right| = \left| \mathbf {I} + \mathbf {B A} \right|. \tag {A.2.16}$$
