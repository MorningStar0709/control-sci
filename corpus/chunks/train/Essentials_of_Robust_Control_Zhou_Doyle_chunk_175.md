Remark 7.1 It should be clear that the inequalities stated in the theorem do not depend on a particular state-space realization of $G ( s )$ . However, use of the balanced realization does make the proof simple. ✸

Proof. Let G(s) have the following state-space realization:

$$\dot {x} = A x + B wz = C x. \tag {7.4}$$

Assume without loss of generality that $( A , B )$ is controllable and $( C , A )$ is observable. Then Σ is nonsingular. Next, differentiate $x ( t ) ^ { * } \Sigma ^ { - 1 } x ( t )$ along the solution of equation (7.4) for any given input w as follows:

$$\frac {d}{d t} (x ^ {*} \Sigma^ {- 1} x) = \dot {x} ^ {*} \Sigma^ {- 1} x + x ^ {*} \Sigma^ {- 1} \dot {x} = x ^ {*} (A ^ {*} \Sigma^ {- 1} + \Sigma^ {- 1} A) x + 2 \langle w, B ^ {*} \Sigma^ {- 1} x \rangle$$

Using the equation involving controllability Gramian to substitute for $A ^ { * } \Sigma ^ { - 1 } + \Sigma ^ { - 1 } A$ and completion of the squares gives

$$\frac {d}{d t} (x ^ {*} \Sigma^ {- 1} x) = \| w \| ^ {2} - \| w - B ^ {*} \Sigma^ {- 1} x \| ^ {2}$$

Integration from t = −∞ to t = 0 with $x ( - \infty ) = 0$ and $x ( 0 ) = x _ { 0 }$ gives

$$x _ {0} ^ {*} \Sigma^ {- 1} x _ {0} = \| w \| _ {2} ^ {2} - \| w - B ^ {*} \Sigma^ {- 1} x \| _ {2} ^ {2} \leq \| w \| _ {2} ^ {2}$$

Let $w = B ^ { * } \Sigma ^ { - 1 } x ;$ then ${ \dot { x } } = ( A + B B ^ { * } \Sigma ^ { - 1 } ) x = - \Sigma A ^ { * } \Sigma ^ { - 1 } x \implies x \in \mathcal { L } _ { 2 } ( - \infty , 0 ]$ $\implies \boldsymbol { w } \in \mathcal { L } _ { 2 } ( - \infty , 0 ]$ and

$$\inf _ {w \in \mathcal {L} _ {2} (- \infty , 0 ]} \left\{\| w \| _ {2} ^ {2} \mid x (0) = x _ {0} \right\} = x _ {0} ^ {*} \Sigma^ {- 1} x _ {0}.$$

Given $x ( 0 ) = x _ { 0 }$ and $w = 0$ for $t \geq 0$ , the norm of $z ( t ) = C e ^ { A t } x _ { 0 }$ can be found from

$$\int_ {0} ^ {\infty} \left\| z (t) \right\| ^ {2} d t = \int_ {0} ^ {\infty} x _ {0} ^ {*} e ^ {A ^ {*} t} C ^ {*} C e ^ {A t} x _ {0} d t = x _ {0} ^ {*} \Sigma x _ {0}$$

To show $\sigma _ { 1 } \leq \| G \| _ { \infty }$ , note that

$$\| G \| _ {\infty} = \sup _ {w \in \mathcal {L} _ {2} (- \infty , \infty)} \frac {\| g * w \| _ {2}}{\| w \| _ {2}} = \sup _ {w \in \mathcal {L} _ {2} (- \infty , \infty)} \frac {\sqrt {\int_ {- \infty} ^ {\infty} \| z (t) \| ^ {2} d t}}{\sqrt {\int_ {- \infty} ^ {\infty} \| w (t) \| ^ {2} d t}}\geq \sup _ {w \in \mathcal {L} _ {2} (- \infty , 0 ]} \frac {\sqrt {\int_ {0} ^ {\infty} \| z (t) \| ^ {2} d t}}{\sqrt {\int_ {- \infty} ^ {0} \| w (t) \| ^ {2} d t}} = \sup _ {x _ {0} \neq 0} \sqrt {\frac {x _ {0} ^ {*} \Sigma x _ {0}}{x _ {0} ^ {*} \Sigma^ {- 1} x _ {0}}} = \sigma_ {1}$$

We shall now show the other inequalities. Since
