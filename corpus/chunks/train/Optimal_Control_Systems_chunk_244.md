In the single-input case, the various matrices become scalars or vectors as $B = b, R = r, \bar{K} = \bar{k}$ . Then, the factorization result (4.5.14) boils down to

$$
\begin{array}{l} r + \mathbf {b} ^ {\prime} \left[ - j \omega \mathbf {I} - \mathbf {A} ^ {\prime} \right] ^ {- 1} \mathbf {Q} [ j \omega \mathbf {I} - \mathbf {A} ] ^ {- 1} \mathbf {b} \\ = r \left| 1 + \bar {\mathbf {k}} [ j \omega \mathbf {I} - \mathbf {A} ] ^ {- 1} \mathbf {b} \right| ^ {2}. \tag {4.5.19} \\ \end{array}
$$

In case $\mathbf{Q} = \mathbf{cc}'$ , we can write (4.5.19) as

$$r + \left| \mathbf {c} ^ {\prime} \left[ j \omega \mathbf {I} - \mathbf {A} ^ {\prime} \right] ^ {- 1} \mathbf {b} \right| ^ {2} = r \left| (1 + \bar {\mathbf {k}} [ j \omega \mathbf {I} - \mathbf {A} ] ^ {- 1} \mathbf {b}) \right| ^ {2}. \tag {4.5.20}$$

The previous result may be called another version of the Kalman equation in frequency domain. The previous relation (also from (4.5.18) for a scalar case) implies that

$$\left| \left(1 + \bar {\mathbf {k}} [ j \omega \mathbf {I} - \mathbf {A} ] ^ {- 1} \mathbf {b}\right) \right| ^ {2} \geq 1. \tag {4.5.21}$$

Thus, the return difference is lower bounded by 1 for all $\omega$ .
