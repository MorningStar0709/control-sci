$$\gg \mathbf {G} = \operatorname{pck} (\mathbf {A}, \mathbf {B}, \mathbf {C}, \mathbf {D}), \quad \mathbf {z _ {0}} = \operatorname{szeros} (\mathbf {G}), \% \text { or }\gg \mathbf {z _ {0}} = \operatorname{tzero} (\mathbf {A}, \mathbf {B}, \mathbf {C}, \mathbf {D})$$

which gives $z _ { 0 } = 0 . 2$ . Since G(s) is full-row rank, we can find y and v such that

$$
\left[ \begin{array}{c c} y ^ {*} & v ^ {*} \end{array} \right] \left[ \begin{array}{c c} A - z _ {0} I & B \\ C & D \end{array} \right] = 0,
$$

which can again be computed using a Matlab command:

$$
\gg \text {null} ([ \mathbf {A} - \mathbf {z _ {0}} * \text {eye} (\mathbf {3}), \mathbf {B}; \mathbf {C}, \mathbf {D} ] ^ {\prime}) \implies \left[ \begin{array}{c} y \\ v \end{array} \right] = \left[ \begin{array}{c} 0. 0 4 6 6 \\ 0. 0 4 6 6 \\ - 0. 1 8 6 6 \\ - 0. 9 7 0 2 \\ 0. 1 3 9 9 \end{array} \right].
$$

Related MATLAB Commands: spoles, rifd
