# Tube-based model predictive controller.

Initialization: At time $i \ : = \ : 0$ , set $x = z = x ( 0 )$ in which $x ( 0 )$ is the current state.

Step 1 (Compute control): At time i and current state $( x , z )$ , solve the nominal optimal control problem $\bar { \mathbb { P } } _ { N } ( z )$ to obtain the nominal control action $\upsilon = \bar { \kappa } _ { N } ( z )$ and the control action $u = \nu + K ( x - z )$ .

Step 2 (Check): If $\bar { \mathbb { P } } _ { N } ( z )$ is infeasible, adopt safety/recovery procedure.

Step 3 (Apply control): Apply the control u to the system being controlled.

Step 4 (Update): Measure the successor state $x ^ { + }$ of the system being controlled and compute the successor state $z ^ { + } = f ( z , \nu )$ of the nominal system.

Step 5: Set $( x , z ) = ( x ^ { + } , z ^ { + } )$ , set $i = i + 1$ , and go to Step 1.

In this algorithm, $\bar { \kappa } _ { N } ( z )$ is, of course, the first element in the control sequence $\mathbf { v } ^ { 0 } ( z )$ obtained by solving the nominal optimal control problem $\bar { \mathbb { P } } _ { N } ( z )$ . Step 2, the check step, is not activated if the assumptions made previously are satisfied and, therefore, is ignored in our analysis.

Computation of Z and V. To implement the tube-based controller, we need inner approximations Z and V to be, respectively, the sets $\hat { \mathbb { Z } } : = \mathbb { X } \Theta$ $S _ { K } ( \infty )$ and $\hat { \mathbb { V } } : = \mathbb { U } \ominus K S _ { K } ( \infty )$ ; computation of the set $S _ { K } ( \infty )$ , a difficult task, is not necessary. Suppose we have a single state constraint

$$y := c ^ {\prime} x \leq d$$

so that $\mathbb { X } = \{ x \in \mathbb { R } ^ { n } \mid c ^ { \prime } x \leq d \}$ . Then, since, for all $i \in \mathbb { I } _ { \geq 0 } , x ( i ) =$ $z ( i ) + e ( i )$ where $e ( i ) \in S _ { K } ( \infty ) \mathrm { i f } e ( 0 ) \in S _ { K } ( \infty )$ , it follows that $c ^ { \prime } x ( i ) \leq$ d if

$$c ^ {\prime} z (i) \leq d - \max \{c ^ {\prime} e \mid e \in S _ {K} (\infty) \}$$

Let $\phi _ { \infty }$ be defined as follows

$$\phi_ {\infty} := \max _ {e} \left\{c ^ {\prime} e \mid e \in S _ {K} (\infty) \right\}$$

Hence

$$\hat {\mathbb {Z}} = \{z \in \mathbb {R} ^ {n} \mid c ^ {\prime} z \leq d - \phi_ {\infty} \}$$
