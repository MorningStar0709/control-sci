$$u ^ {*} := \underset {u: [ 0, \infty) \rightarrow \mathbb {R}} {\operatorname{argmin}} J (u) := \int_ {0} ^ {\infty} [ q y (t) ^ {T} y (t) + u (t) ^ {2} ] d t \tag {421}$$ subject to (422) $$\dot {x} (t) = A x (t) + B u (t), \quad t \in [ t _ {0}, \infty) \tag {423}y (t) = C x (t) + D u (t), \quad t \in [ t _ {0}, \infty) \tag {424}x \left(t _ {0}\right) = x _ {0} \tag {425}$$ Tasks: 1.
Find an optimal policy for the LQR problem by solving ARE using Python or Matlab functions.
2.
Plot trajectories of y(t) and u(t).
3.
In the answer, please include your Python or Matlab codes.
# Solution: First of all, we need to find the matrix Q.
We can see that, given D = 0, then $$y (t) = C x (t) \tag {426}\Longrightarrow J (u) := \int_ {0} ^ {\infty} [ x ^ {T} (t) (C ^ {T} q C) x (t) + u (t) ^ {2} ] d t \tag {427}$$ hence we can consider $Q = C ^ { T } q C$ .
We solve the problem in Python.
The first step is declaring all the variables: ```python import numpy as np import torch import scipy.linalg # Build matrices A = np.matrix([[-10, 0, 0, 0, 0, 0], [0.0729, -0.0558, -0.997, 0.0802, 0.0415, 0], [-4.75, 0.598, -0.115, -0.0318, 0, 0], [1.53, -3.05, 0.388, -0.465, 0, 0], [0, 0, 0.0805, 1, 0, 0], [0, 0, 1, 0, 0, -0.3333]]) B = np.matrix([[1], [0], [0], [0], [0], [0]]) C = np.matrix([0, 0, 1, 0, 0, -0.3333]) D = 0*np.eye(1) # Choose Q and R matrices q = 9.527 Q = C.T*q*C R = np.eye(1) ``` Then we define the LQR controller as following, where X is the solution to the Riccati equations solved via the Python library SciPy.
The closed loop gain K is then defined as: $$K = R ^ {- 1} B ^ {T} X \tag {428}$$ Python code: ```python def LQR(A,B,Q,R): """Solve the continuous time lqr controller.
