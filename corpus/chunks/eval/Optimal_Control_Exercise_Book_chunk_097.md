In this case, we have: $$
A = \left[ \begin{array}{l l} 0 & 1 \\ 0 & 0 \end{array} \right], \quad B = \left[ \begin{array}{l} 0 \\ 1 \end{array} \right], \quad Q = \left[ \begin{array}{l l} 1 & 0 \\ 0 & 1 \end{array} \right], \quad R = [ 1 ] \tag {398}
$$ We can now use the Python’s library SciPy to solve the ARE: ```python # Importing the packages import numpy as np from scipy.linalg import solve_continuous_are # Build matrices A = np.matrix([[0, 1], [0, 0]]) B = np.matrix([[0], [1]]) Q = np.eye(2) # Identity matrix, dim = 2 R = np.eye(1) # Identity matrix, dim = 1 # Solve the ARE P = solve_continuous_are(A, B, Q, R) print(P) ``` By which we get $$
P = \left[ \begin{array}{c c} 1.
7 3 2 0 5 0 8 1 & 1 \\ 1 & 1.
7 3 2 0 5 0 8 1 \end{array} \right] \sim \left[ \begin{array}{c c} \sqrt {3} & 1 \\ 1 & \sqrt {3} \end{array} \right] \tag {399}
$$ The formula for Riccati Differential Equation is as following: $$\dot {P} (t) = - P (t) A - A ^ {\top} P (t) - Q + P (t) B R ^ {- 1} B P (t) \tag {400}$$ So, based on the previous result we can get ${ \dot { P } } ( t )$ as following 1 # Calculate the steady-state derivative 2 P\_dot = A.T\*P + P\*A + Q -P\*B\*R\*B.T\*P 3 print(P\_dot) By which we get $$
\dot {P} = \left[ \begin{array}{l l} 0 & 0 \\ 0 & 0 \end{array} \right] \tag {401}
$$ hence proving P is indeed the steady-state solution of the RDE.
# Exercise 6.24 Consider the infinite-horizon LQR problem $$u ^ {*} := \underset {u: [ 0, \infty) \rightarrow \mathbb {R}} {\operatorname{argmin}} J (u) := \int_ {0} ^ {\infty} \left(q x (t) ^ {2} + r u (t) ^ {2}\right) d t \tag {402}$$ subject to (403) $$\dot {x} (t) = a x (t) + b u (t), \quad t \in [ t _ {0}, \infty) \tag {404}x \left(t _ {0}\right) = x _ {0} \tag {405}$$ where $a , q , r > 0$ and $b \in \mathbb { R }$ is arbitrary.
Find the optimal control law.
Moreover, show that $f o r \ r 0$ , the eigenvalue of the optimal closed-loop system moves off to $- \infty$ , while for $r \infty$ , the eigenvalue of the optimal closed-loop system tends $t o - a$ # Solution: Recalling the ARE as: $$0 = A ^ {\top} P + P A + Q - P B R ^ {- 1} B ^ {\top} P \tag {406}$$ the optimal control law will be given by: $$u ^ {*} (t) = K x ^ {*} (t) \tag {407}$$ ${ \mathrm { w h e r e ~ t h e ~ g a i n ~ } } K = - R ^ { - 1 } B ^ { \top } P$ (408) with P being the solution to the ARE.
