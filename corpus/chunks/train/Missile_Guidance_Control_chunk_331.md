# (b) Discrete-Time Kalman Filtering

Consider the linear stochastic system given in state-space description [4], [25]:

$$\mathbf {x} (k + 1) = A (k) \mathbf {x} (k) + B (k) \mathbf {w} (k), \tag {4.109}\mathbf {z} (k) = H (k) \mathbf {x} (k) + \mathbf {v} (k), \tag {4.110}\text { with initial state } \mathbf {x} (k) = 0, k = 0, 1, 2, \dots ,$$

where $A ( k ) , B ( k ) , H ( k )$ are known $n \times n , n \times p$ , and $q \times n$ constant matrices, respectively, with $1 \leq p , q \leq n$ , and k identified as time (i.e., kth instant). Furthermore, {w} and {v} are zero-mean Gaussian white noise sequences with prior statistics [30]

$$
\begin{array}{l} E \{\mathbf {w} (k) \mathbf {w} ^ {T} (k) \} = Q (k) \delta_ {k l}, \\ E \{\mathbf {v} (k) \mathbf {v} ^ {T} (k) \} = R (k) \delta_ {k l}, \\ E \{\mathbf {w} (k) \mathbf {v} ^ {T} (k) \} = \mathbf {0}, \\ \forall k, l = 0, 1, \dots , \\ \delta_ {k l} = \left\{ \begin{array}{l} 1 \text {   if   } k = l, \\ 0 \text {   if   } k \neq l, \end{array} \right. \\ \end{array}
$$

where $Q ( k )$ and $R ( k )$ are known $p \times p$ and $q \times q$ nonnegative and positive symmetric matrices, respectively, independent of $k .$ . The vector $\mathbf { z } ( k )$ is called, as before, the measurement or observation vector and is of dimension $q \times 1$ .

Now let ${ \hat { \mathbf { x } } } ( k \mid j )$ be the (optimal) least-squares estimate of $\mathbf { x } ( k )$ when all measurements up to the jth sample are available. Then,

for $j = k , \quad \hat { \mathbf { x } } ( k ) = \hat { \mathbf { x } } ( k \mid k )$ : that is, the estimation process is called a digital filtering process;

$j < k , { \hat { \mathbf { x } } } ( k \mid j )$ : the process is called optimal prediction of $\mathbf { x } ( \mathrm { k } )$

$j > k , { \hat { \mathbf { x } } } ( k | j )$ : this is called a smoothing estimate of $\mathbf { x } ( \mathrm { k } )$ , and the process a digital smoothing process.

In order to compute ${ \hat { \mathbf { x } } } ( k )$ in real time, the following recursive equations are needed:

$$\hat {\mathbf {x}} (k \mid k - 1) = A (k - 1) \hat {\mathbf {x}} (k - 1), \tag {4.111}\hat {\mathbf {x}} (k \mid k) = \hat {\mathbf {x}} (k \mid k - 1) + K (k) [ \mathbf {z} (k) - H (k) \hat {\mathbf {x}} (k \mid k - 1) ], \tag {4.112a}$$

or

$$\hat {\mathbf {x}} (k \mid k) = A (k - 1) \hat {\mathbf {x}} (k - 1) + K (k) [ \mathbf {z} (k) - H (k) A (k - 1) \hat {\mathbf {x}} (k - 1) ], \tag {4.112b}\hat {\mathbf {x}} (0) = E \{\mathbf {x} (0) \},$$
