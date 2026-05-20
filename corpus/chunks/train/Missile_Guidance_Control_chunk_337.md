$$- \frac {d \mathbf {P} (t)}{d t} = - \mathbf {P} (t) \mathbf {B} (t) \mathbf {R} ^ {- 1} (t) \mathbf {B} ^ {T} (t) \mathbf {P} (t) + \mathbf {P} (t) \mathbf {A} (t) + \mathbf {A} ^ {T} (t) \mathbf {P} (t) + \mathbf {Q} (t) \tag {4.130}$$

satisfying the boundary condition at the terminal time $t = T$ ,

$$\mathbf {P} (T) = \mathbf {S}. \tag {4.131}$$

The matrix P(t) can in theory be found by integrating (4.130) backward (or sweep method) from the final condition (4.131). When P(t) has been found, since it is symmetric, using (4.128), and (4.129) we obtain [3], [25]

$$\mathbf {u} ^ {*} (\mathbf {x}, t) = - \mathbf {R} ^ {- 1} (t) \mathbf {B} ^ {T} (t) \mathbf {P} (t) \mathbf {x} (t). \tag {4.132}$$

Thus, there will be a unique absolute minimum of (4.122) only if the matrix Riccati equation, (4.130), has a unique solution. Equation (4.132) can also be written in the form

$$\mathbf {u} ^ {*} (\mathbf {x}, t) \triangleq - \mathbf {K} ^ {*} (t) \mathbf {x} (t), \tag {4.133}$$

where $\mathbf { K } ^ { * } ( t )$ is a matrix of feedback gains, also known as control gain. When $T \to \infty$ , Kalman has shown that for a linear time-invariant system that is completely controllable and with a performance index that is of the form

$$J = (1 / 2) \int_ {t _ {0}} ^ {T} (\mathbf {x} ^ {T} (\tau) \mathbf {Q x} (\tau) + \mathbf {u} ^ {T} (\tau) \mathbf {R u} (\tau)) d \tau \tag {4.134}$$

with Q and R both symmetric positive definite matrices, so that the condition

$$\lim _ {T \rightarrow \infty} \left(\frac {d \mathbf {P} (t)}{d t}\right) = 0 \tag {4.135}$$

holds, the matrix Riccati equation (4.130) is reduced to a nonlinear matrix algebraic equation of the form

$$- \mathbf {P} \mathbf {B} \mathbf {R} ^ {- 1} \mathbf {B} ^ {T} \mathbf {P} + \mathbf {P} \mathbf {A} + \mathbf {A} ^ {T} \mathbf {P} + \mathbf {Q} = 0. \tag {4.136}$$
