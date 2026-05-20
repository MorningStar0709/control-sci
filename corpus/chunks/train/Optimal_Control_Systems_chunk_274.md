# 5.3 Discrete-Time Linear State Regulator System

problem of linear state regulator and summarize the results derived in Section 5.2.

Consider the linear, time-varying discrete-time control system described by the plant (5.2.1) and the performance index (5.2.3). We are given the initial and final conditions as

$$\mathbf {x} (k = k _ {0}) = \mathbf {x} (k _ {0}); \quad \mathbf {x} (k _ {f}) \text { is free, and } k _ {f} \text { is fixed. } \tag {5.3.1}$$

Then the optimal control (5.2.20) and the state and costate equations (5.2.22) are reproduced, respectively here for convenience as

$$\mathbf {u} ^ {*} (k) = - \mathbf {R} ^ {- 1} (k) \mathbf {B} ^ {\prime} (k) \boldsymbol {\lambda} ^ {*} (k + 1) \tag {5.3.2}$$

and

$$\mathbf {x} ^ {*} (k + 1) = \mathbf {A} (k) \mathbf {x} ^ {*} (k) - \mathbf {E} (k) \boldsymbol {\lambda} ^ {*} (k + 1), \tag {5.3.3}\boldsymbol {\lambda} ^ {*} (k) = \mathbf {Q} (k) \mathbf {x} ^ {*} (k) + \mathbf {A} ^ {\prime} (k) \boldsymbol {\lambda} ^ {*} (k + 1), \tag {5.3.4}$$

where, $\mathbf{E}(k) = \mathbf{B}(k)\mathbf{R}^{-1}(k)\mathbf{B}'(k)$ , and the final costate relation (5.2.38) is given by

$$\boldsymbol {\lambda} (k _ {f}) = \mathbf {F} (k _ {f}) \mathbf {x} (k _ {f}). \tag {5.3.5}$$
