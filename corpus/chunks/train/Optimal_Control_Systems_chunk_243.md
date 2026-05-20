# 4.5.1 Gain Margin and Phase Margin

We know that in classical control theory, the features of gain and phase margins are important in evaluating the system performance with respect to robustness to plant parameter variations and uncertainties. The engineering specifications often place lower bounds on the phase and gain margins. Here, we interpret some of the classical control features such as gain margin and phase margin for the closed-loop optimal control system [3]. For ready reference let us rewrite the return-difference result (4.5.13)) with $s = j\omega$ here as

$$
\begin{array}{l} \mathbf {B} ^ {\prime} \left[ - j \omega \mathbf {I} - \mathbf {A} ^ {\prime} \right] ^ {- 1} \mathbf {Q} [ j \omega \mathbf {I} - \mathbf {A} ] ^ {- 1} \mathbf {B} + \mathbf {R} \\ = \left[ \mathbf {I} + \bar {\mathbf {K}} [ - j \omega \mathbf {I} - \mathbf {A} ] ^ {- 1} \mathbf {B} \right] ^ {\prime} \mathbf {R} [ \mathbf {I} + \bar {\mathbf {K}} [ j \omega \mathbf {I} - \mathbf {A} ] ^ {- 1} \mathbf {B} ]. \tag {4.5.14} \\ \end{array}
$$

The previous result can be viewed as

$$\mathbf {M} (j \omega) = \mathbf {W} ^ {\prime} (- j \omega) \mathbf {W} (j \omega) \tag {4.5.15}$$

where,

$$
\begin{array}{l} \mathbf {W} (j \omega) = \mathbf {R} ^ {1 / 2} \left[ \mathbf {I} + \bar {\mathbf {K}} [ j \omega \mathbf {I} - \mathbf {A} ] ^ {- 1} \mathbf {B} \right] \\ \mathbf {M} (j \omega) = \mathbf {R} + \mathbf {B} ^ {\prime} [ - j \omega \mathbf {I} - \mathbf {A} ^ {\prime} ] ^ {- 1} \mathbf {Q} [ j \omega \mathbf {I} - \mathbf {A} ] ^ {- 1} \mathbf {B}. \tag {4.5.16} \\ \end{array}
$$

Note that $\mathbf{M}(j\omega) \geq \mathbf{R} > 0$ . Using $Q = CC'$ , $R = DD' = I$ and the notation

$$\mathbf {W} ^ {\prime} (- j \omega) \mathbf {W} (j \omega) = | | \mathbf {W} (j \omega) | | ^ {2}, \tag {4.5.17}$$

the factorization result (4.5.14) can be written in neat form as

$$\left. \left| \left| \mathbf {I} + \bar {\mathbf {K}} ^ {\prime} [ j \omega \mathbf {I} - \mathbf {A} ] ^ {- 1} \mathbf {B} \right| \right| ^ {2} = \mathbf {I} + \left| \left| \mathbf {C} ^ {\prime} [ j \omega \mathbf {I} - \mathbf {A} ] ^ {- 1} \mathbf {B} \right| \right| ^ {2}. \right| \tag {4.5.18}$$

This result can be used to find the optimal feedback matrix $\bar{K}$ given the other quantities A, B, Q, R = I. Note that in (4.5.18), we need not solve for the Riccati coefficient matrix $\bar{P}$ , instead we directly obtain the feedback matrix $\bar{K}$ .
