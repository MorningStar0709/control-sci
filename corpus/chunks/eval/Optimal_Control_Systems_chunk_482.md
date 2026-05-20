# B.2 Linear Matrix Equations

A set of linear simultaneous equations for an unknown matrix P in terms of known matrices A and Q, is written as

$$\mathbf {P} \mathbf {A} + \mathbf {A} ^ {\prime} \mathbf {P} + \mathbf {Q} = 0. \tag {B.2.1}$$

In particular, if Q is positive definite, then there exists a unique positive definite P satisfying the previous linear matrix equation, if and only if A is asymptotically stable or the real part (Re) of $\lambda\{A\} < 0$ . Then (B.2.1) is called the Lyapunov equation, the solution of which is given by

$$\mathbf {P} = \int_ {0} ^ {\infty} e ^ {\mathbf {A} ^ {\prime} t} \mathbf {Q} e ^ {\mathbf {A} t} d t. \tag {B.2.2}$$
