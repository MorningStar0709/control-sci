$$q _ {j} ^ {*} (t) = \mathbf {b} _ {j} ^ {\prime} \epsilon^ {- \mathbf {A} ^ {\prime} t} \boldsymbol {\lambda} ^ {*} (0) = 0\dot {q} ^ {*} (t) = \mathbf {b} _ {j} ^ {\prime} \mathbf {A} ^ {\prime} \epsilon^ {- \mathbf {A} ^ {\prime} t} \boldsymbol {\lambda} ^ {*} (0) = 0\ddot {q} ^ {*} (t) = \mathbf {b} _ {j} ^ {\prime} \mathbf {A} ^ {\prime 2} \epsilon^ {- \mathbf {A} ^ {\prime} t} \boldsymbol {\lambda} ^ {*} (0) = 0\bullet \quad \bullet \quad \bullet \quad \bullet \quad \bullet \quad \bullet \quad \bullet \quad \bullet \quad \bullet \quad \bulletq ^ {(n - 1) *} (t) = \mathbf {b} _ {j} ^ {\prime} \mathbf {A} ^ {\prime (n - 1)} \epsilon^ {- \mathbf {A} ^ {\prime} t} \boldsymbol {\lambda} ^ {*} (0) = 0 \tag {7.1.35}$$

which in turn can be written in a compact form as

$$\mathbf {G} _ {j} ^ {\prime} \epsilon^ {- \mathbf {A} ^ {\prime} t} \boldsymbol {\lambda} ^ {*} (0) = 0 \tag {7.1.36}$$

where,

$$
\mathbf {G} _ {j} = \left[ \begin{array}{c c c c c c c c} \mathbf {b} _ {j} & \vdots & \mathbf {A b} _ {j} & \vdots & \mathbf {A} ^ {2} \mathbf {b} _ {j} & \vdots & \dots \vdots & \mathbf {A} ^ {n - 1} \mathbf {b} _ {j} \end{array} \right]
= \left[ \mathbf {B} \vdots \mathbf {A B} \vdots \mathbf {A} ^ {2} \mathbf {B} \vdots \dots \vdots \mathbf {A} ^ {n - 1} \mathbf {B} \right]. \tag {7.1.37}
$$

In the condition (7.1.36), we know that $\epsilon^{-A't}$ is nonsingular, and $\lambda^{*}(0) \neq 0$ , and hence the matrix $G_{j}$ must be singular. Hence, for the STOC system, $G_{j}$ must be singular. Or for the NTOC system, $G_{j}$ must be nonsingular. We know that the matrix $G_{j}$ is nonsingular if and only if the original system (7.1.10) is completely controllable. This leads us to say that the time-optimal control system is normal if the matrix $G_{j}$ is nonsingular or if the system is completely controllable. These results are stated as follows (the proofs are found in books such as [6]).
