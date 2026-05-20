$$
e ^ {\mathbf {A} t} = \left[ \begin{array}{c c} 1 & 1 \\ 0 & - 2 \end{array} \right] \left[ \begin{array}{c c} e ^ {0} & 0 \\ 0 & e ^ {- 2 t} \end{array} \right] \left[ \begin{array}{c c} 1 & \frac {1}{2} \\ 0 & - \frac {1}{2} \end{array} \right] = \left[ \begin{array}{c c} 1 & \frac {1}{2} (1 - e ^ {- 2 t}) \\ 0 & e ^ {- 2 t} \end{array} \right]
$$

Method 2. Since

$$
s \mathbf {I} - \mathbf {A} = \left[ \begin{array}{c c} s & 0 \\ 0 & s \end{array} \right] - \left[ \begin{array}{c c} 0 & 1 \\ 0 & - 2 \end{array} \right] = \left[ \begin{array}{c c} s & - 1 \\ 0 & s + 2 \end{array} \right]
$$

we obtain

$$
(s \mathbf {I} - \mathbf {A}) ^ {- 1} = \left[ \begin{array}{c c} \frac {1}{s} & \frac {1}{s (s + 2)} \\ 0 & \frac {1}{s + 2} \end{array} \right]
$$

Hence,

$$
e ^ {\mathbf {A} t} = \mathcal {L} ^ {- 1} \big [ (s \mathbf {I} - \mathbf {A}) ^ {- 1} \big ] = \left[ \begin{array}{c c} 1 & \frac {1}{2} \big (1 - e ^ {- 2 t} \big) \\ 0 & e ^ {- 2 t} \end{array} \right]
$$

Computation of eAt : Method 3. The third method is based on Sylvester’s interpolation method. (For Sylvester’s interpolation formula, see Problem A–9–12.) We shall first consider the case where the roots of the minimal polynomial $\phi ( \lambda )$ of A are distinct. Then we shall deal with the case of multiple roots.

Case 1: Minimal Polynomial of A Involves Only Distinct Roots. We shall assume that the degree of the minimal polynomial of A is m. By using Sylvester’s interpolation formula, it can be shown that $e ^ { \mathbf { A } t }$ can be obtained by solving the following determinant equation:

$$
\left| \begin{array}{c c c c c c} 1 & \lambda_ {1} & \lambda_ {1} ^ {2} & \dots & \lambda_ {1} ^ {m - 1} & e ^ {\lambda_ {1} t} \\ 1 & \lambda_ {2} & \lambda_ {2} ^ {2} & \dots & \lambda_ {2} ^ {m - 1} & e ^ {\lambda_ {2} t} \\ \cdot & \cdot & \cdot & & \cdot & \cdot \\ \cdot & \cdot & \cdot & & \cdot & \cdot \\ \cdot & \cdot & \cdot & & \cdot & \cdot \\ 1 & \lambda_ {m} & \lambda_ {m} ^ {2} & \dots & \lambda_ {m} ^ {m - 1} & e ^ {\lambda_ {m} t} \\ \mathbf {I} & \mathbf {A} & \mathbf {A} ^ {2} & \dots & \mathbf {A} ^ {m - 1} & e ^ {\mathbf {A} t} \end{array} \right| = \mathbf {0} \tag {9-47}
$$

By solving Equation (9–47) for $e ^ { \mathbf { A } t } , e ^ { \mathbf { A } t }$ can be obtained in terms of the $\mathbf { A } ^ { k } \left( k = 0 , 1 \right.$ , $2 , \ldots , m - 1 )$ and the $e ^ { \lambda _ { i } t } ( i = 1 , 2 , 3 , \ldots , m )$ . [Equation (9–47) may be expanded, for example, about the last column.]

Notice that solving Equation (9–47) for $e ^ { \mathbf { A } t }$ is the same as writing
