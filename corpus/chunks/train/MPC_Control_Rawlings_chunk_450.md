Next we define estimator stability. Again, because the system is nonlinear, we must define stability of a solution. Consider the zero estimate error solution for all $k \geq 0$ . This solution arises when the system’s initial state is equal to the estimator’s prior and there are zero disturbances, $x _ { 0 } = \overline { { { x } } } _ { 0 } , ( w ( i ) , \nu ( i ) ) = 0$ all $i \geq 0$ . In this case, the optimal solution to the full information problem is $\hat { x } ( 0 | T ) = \overline { { x } } _ { 0 }$ and $\hat { w } ( i \vert T ) = 0$ for all $0 \leq i \leq T , T \geq 1$ , which also gives perfect agreement of estimate and measurement $h ( \hat { x } ( i \vert T ) ) = y ( i )$ for $0 \leq i \leq$ $T , T \geq 1$ . The perturbation to this solution are: the system’s initial state (distance from $\overline { { x } } _ { 0 } )$ , and the process and measurement disturbances. We next define stability properties so that asymptotic stability considers the case $x _ { 0 } \neq \overline { { x } } _ { 0 }$ with zero disturbances, and robust stability considers the case in which $( \boldsymbol { w } ( i ) , \boldsymbol { \nu } ( i ) ) \neq 0$ .

Definition 4.6 (Global asymptotic stability). The estimate is based on the noise-free measurement $\mathbf { y } = h ( \mathbf { x } ( x _ { 0 } , 0 ) )$ . The estimate is (nominally) globally asymptotically stable (GAS) if there exists a KL-function $\beta ( \cdot )$ such that for all $x _ { 0 } , { \overline { { x } } } _ { 0 }$ and $k \in  { \mathbb { I } } _ { \geq 0 }$

$$\left| x (k; x _ {0}, 0) - \hat {x} (k) \right| \leq \beta \left(\left| x _ {0} - \overline {{x}} _ {0} \right|, k\right)$$

It bears mentioning that the standard definition of estimator stability for linear systems is consistent with Definition 4.6.

Definition 4.7 (Robust global asymptotic stability). The estimate is based on the noisy measurement $\mathbf { y } = h ( \mathbf { x } ( x _ { 0 } , \mathbf { w } ) ) + \mathbf { v }$ . The estimate is robustly GAS if for all $x _ { 0 }$ and $\overline { { x } } _ { 0 }$ , and $( \mathbf { w } , \mathbf { v } )$ satisfying Assumption 4.3, the following hold.

(a) The estimate converges to the state; as $k \to \infty$

$$\hat {x} (k) \rightarrow x (k; x _ {0}, \mathbf {w})$$

(b) For every $\varepsilon > 0$ there exists $\delta > 0$ such that

$$\gamma_ {x} (| x _ {0} - \overline {{{x}}} _ {0} |) + \sum_ {i = 0} ^ {\infty} \gamma_ {w} (| (w (i), v (i)) |) \leq \delta \tag {4.6}$$

implies $| x ( k ; x _ { 0 } , { \mathbf w } ) - \hat { x } ( k ) | \le \varepsilon$ for all $k \in  { \mathbb { I } } _ { \geq 0 }$ .
