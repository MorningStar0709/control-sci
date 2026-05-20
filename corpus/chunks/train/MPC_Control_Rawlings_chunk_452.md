Because the system is i-IOSS, we have the following inequality for all $x _ { 0 } , \hat { x } ( 0 | k ) , \mathbf { w } , \hat { \mathbf { w } } _ { k }$ , and $k \geq 0$ ,

$$\left| x (k; x _ {0}, \mathbf {w}) - x (k; \hat {x} (0 | k), \hat {\mathbf {w}} _ {k}) \right| \leq \beta (\left| x _ {0} - \hat {x} (0 | k) \right|, k) +\gamma_ {1} \big (\left| \left| \mathbf {w} - \widehat {\mathbf {w}} _ {k} \right| \right| _ {0: k - 1} \big) + \gamma_ {2} \big (\left| \left| h (\mathbf {x}) - h (\widehat {\mathbf {x}} _ {k}) \right| \right| _ {0: k} \big) \tag {4.7}$$

Since $w ( k )$ converges to zero, $w ( k ) - \hat { w } ( k )$ converges to zero, and $h ( x ( k ) ) - h ( \hat { x } ( k ) )$ converges to zero. From Proposition 4.2 we conclude that $\left| x ( k ; x _ { 0 } , { \bf w } ) - x ( k ; \hat { x } ( 0 | k ) , \hat { \bf w } _ { k } ) \right.$ converges to zero. Since the state estimate is $\hat { x } ( k ) : = x ( k ; \hat { x } ( 0 | k ) , \hat { \mathbf { w } } _ { k } )$ and the state is $x ( k ) = x ( k ; x _ { 0 } , { \bf w } )$ , we have that

$$\hat {x} (k) \rightarrow x (k) \qquad k \rightarrow \infty$$

and the estimate converges to the system state. This establishes part (a) of the robust GAS definition.3

(b) Assume that (4.6) holds for some arbitrary $\delta > 0$ . This gives immediately an upper bound on the optimal full information cost function for all $T , 0 \leq T \leq \infty$ , i.e, $V _ { \infty } = \delta$ . We then have the following bounds on the initial state estimate for all $k \geq 0$ , and the initial state

$$\underline {{\gamma}} _ {x} (| \hat {x} (0 | k) - \overline {{x}} _ {0} |) \leq \delta \quad \gamma_ {x} (| x _ {0} - \overline {{x}} _ {0} |) \leq \delta$$

These two imply a bound on the initial estimate error, $| x _ { 0 } - \hat { x } ( 0 | k ) | \le$ $\underline { { \gamma } } _ { x } ^ { - 1 } ( \delta ) + \gamma _ { x } ^ { - 1 } ( \delta )$ . The process disturbance bounds are for all $k \geq 0$ $0 \leq i \leq k$

$$\underline {{\gamma}} _ {w} (| \hat {w} (i | k) |) \leq \delta \quad \gamma_ {w} (| w (k) |) \leq \delta$$

and we have that $| w ( i ) - \hat { w } ( i | k ) | \leq \gamma _ { w } ^ { - 1 } ( \delta ) + \gamma _ { w } ^ { - 1 } ( \delta )$ . A similar argument gives for the measurement disturbance $| \nu ( i ) - \hat { \nu } ( i | k ) | \leq \underline { { \gamma } } _ { w } ^ { - 1 } ( \delta ) +$ $\gamma _ { w } ^ { - 1 } ( \delta )$ . Since $- ( \nu ( i ) - \hat { \nu } ( i | k ) ) = h ( x ( i ) ) - h ( \hat { x } ( i | k ) )$ , we have that

$$| h (x (i)) - h (\hat {x} (i | k)) | \leq \underline {{\gamma}} _ {w} ^ {- 1} (\delta) + \gamma_ {w} ^ {- 1} (\delta)$$

We substitute these bounds in (4.7) and obtain for all $k \geq 0$
