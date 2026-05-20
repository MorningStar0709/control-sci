The problem can be solved using the extended-interval Kalman filter (EIKF). This $E I K F$ can be represented by the linear, discrete-time, time-varying nominal dynamic observation system [6]

$$\mathbf {x} _ {k + 1} = \mathbf {A} _ {k} \mathbf {x} _ {\mathbf {k}} + \mathbf {B} _ {k} \xi_ {k}, \tag {6.285a}\mathbf {y} _ {k} = \mathbf {C} _ {k} \mathbf {x} _ {k} + \eta_ {k} \quad k = 0, 1, 2, \dots , \tag {6.285b}$$

where $\mathbf { X } _ { k } \in R ^ { n }$ and $\mathbf { y } _ { k } \in R ^ { m }$ are state and output vectors, respectively, with a Gaussian initial state $\mathbf { X } _ { O }$ of known mean $E \{ \mathbf { x } _ { o } \}$ and covariance $P _ { o } = V \{ \mathbf { x } _ { o } \} ; \mathbf { A } _ { k } \in R ^ { n x n } , \mathbf { B } _ { k } \in$ $R ^ { n x p }$ and $\mathbf { C } _ { k } \in R ^ { m x n }$ are known constant matrices; and $\{ \xi _ { k } \}$ and $\{ \eta _ { k } \}$ are mutually independent zero-mean Gaussian noise sequences, with known covariance matrices $\{ Q _ { k } \}$ and $\{ R _ { k } \}$ , respectively, which are all independent of the initial state, namely,

$$E \{\xi_ {k}, \xi_ {l} \} = Q _ {k} \delta_ {k l}, \quad E \{\eta_ {k}, \eta_ {l} \} = R _ {k} \delta_ {k l},E \{\xi_ {k}, \eta_ {l} \} = E \{\xi_ {k}, \mathbf {x} _ {o} \} = E \{\eta_ {k}, \mathbf {x} _ {o} \} = 0 \quad \forall k, l = 0, 1, 2, \dots ,$$

where $\delta _ { k l } = 1$ if $k = l$ and $\delta _ { k l } = 0$ otherwise. The optimal estimates are uniquely determined by the conditional expectations

$$\hat {\mathbf {x}} _ {k} = E \{\mathbf {x} _ {k} | \mathbf {y} _ {1}, \dots , \mathbf {y} _ {k} \}. \tag {6.286}$$

It is well known that the state update at the end of the filter cycle requires $\mathbf { x } ( k + 1 / k )$ , the predicted state at $k + 1$ based on the estimated state at $k .$ . This prediction uses a predictor/corrector integration of the nonlinear equations of motion implemented in range, azimuth, and elevation coordinates. Assuming the transpose of the state vector to consist of position and velocity terms, we can write the state vector as

$$\mathbf {x} ^ {T} = [ r, \alpha , \varepsilon , \dot {r}, \dot {\alpha}, \dot {\varepsilon}, \beta ],$$

where $r$ is the range, α the azimuth, ε the elevation, and $\beta$ the ballistic or drag coefficient. The state transition matrix  is computed as

$$\Phi = I + J (k) * T,$$

where I is the identity matrix, $J ( k )$ is the Jacobian matrix $= d f / d x | _ { x = x ( k / k - 1 ) }$ , and $T$ is the filter update interval. The Jacobian matrix has the form
