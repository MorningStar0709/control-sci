$$
\left[ \begin{array}{c c} A & B \\ \hline C & D \end{array} \right] \longmapsto \left[ \begin{array}{c c} - A ^ {*} & - C ^ {*} \\ \hline B ^ {*} & D ^ {*} \end{array} \right].
$$

In particular, we have $G ^ { * } ( j \omega ) : = \left[ G ( j \omega ) \right] ^ { * } = G ^ { \sim } ( j \omega )$ .

A real rational matrix $\hat { G } ( s )$ is called an inverse of a transfer matrix $G ( s )$ if $G ( s ) { \hat { G } } ( s ) =$ ${ \hat { G } } ( s ) G ( s ) = I$ . Suppose $G ( s )$ is square and D is invertible. Then

$$
G ^ {- 1} = \left[ \begin{array}{c c} A - B D ^ {- 1} C & - B D ^ {- 1} \\ \hline D ^ {- 1} C & D ^ {- 1} \end{array} \right].
$$

The corresponding Matlab commands are

$$
G _ {1} G _ {2} \iff \operatorname{mmult} (\mathbf {G} _ {1}, \mathbf {G} _ {2}), \quad \left[ \begin{array}{c c} G _ {1} & G _ {2} \end{array} \right] \iff \operatorname{sbs} (\mathbf {G} _ {1}, \mathbf {G} _ {2})
G _ {1} + G _ {2} \iff \operatorname{madd} \left(\mathbf {G} _ {\mathbf {1}}, \mathbf {G} _ {\mathbf {2}}\right), \quad G _ {1} - G _ {2} \iff \operatorname{msub} \left(\mathbf {G} _ {\mathbf {1}}, \mathbf {G} _ {\mathbf {2}}\right)
\left[ \begin{array}{c} G _ {1} \\ G _ {2} \end{array} \right] \iff \mathbf {a b v} (\mathbf {G _ {1}}, \mathbf {G _ {2}}), \quad \left[ \begin{array}{c c} G _ {1} & \\ & G _ {2} \end{array} \right] \iff \mathbf {d a u g} (\mathbf {G _ {1}}, \mathbf {G _ {2}}),
G ^ {T} (s) \iff \operatorname{transp} (\mathbf {G}), \quad G ^ {\sim} (s) \iff \operatorname{cjt} (\mathbf {G}), \quad G ^ {- 1} (s) \iff \min (\mathbf {G})\alpha G (s) \iff \operatorname{mscl} (\mathbf {G}, \alpha), \quad \alpha \text { is a scalar. }
$$

Related MATLAB Commands: append, parallel, feedback, series, cloop, sclin, sclout, sel
