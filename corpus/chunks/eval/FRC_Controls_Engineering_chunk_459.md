# 17.3.1 Linear MPC

Here’s an example problem formulation for a linear system $\mathbf { x } _ { k + 1 } = \mathbf { A } \mathbf { x } _ { k } + \mathbf { B } \mathbf { u } _ { k }$ .

$$\min _ {\mathbf {x} _ {0: N}, \mathbf {u} _ {0: N - 1}} \mathbf {x} _ {N} ^ {\top} \mathbf {Q} \mathbf {x} _ {N} + \sum_ {k = 0} ^ {N - 1} \left(\mathbf {x} _ {k} ^ {\top} \mathbf {Q} \mathbf {x} _ {k} + \mathbf {u} _ {k} ^ {\top} \mathbf {R} \mathbf {u} _ {k}\right)$$

subject to x0 = current state

$$\mathbf {x} _ {k + 1} = \mathbf {A x} _ {k} + \mathbf {B u} _ {k}\mathbf {u} _ {\text { min }} \leq \mathbf {u} _ {k} \leq \mathbf {u} _ {\text { max }}$$

where N is the number of samples and Q and R are weighting factors. The controller solves this problem at each timestep and returns u0.

![](image/42d0733008b57a18939f1e694527ea095a5d0220b61f487321d5732c131d4fae.jpg)

This optimization problem is a generalization of finite-horizon LQR to linear equality and inequality constraints.

Snippet 17.1 shows a linear MPC class in Python.

import frccontrol as fct from sleipnir.optimization import Problem, bounds

class LinearMPC: def \_init\_\_(self, A, B, Q, R, dt, u\_min, u\_max, horizon): self.A\_d, self.B\_d = fct.discretize\_ab(A, B, dt) self.Q, self.R = Q, R

```python
self.u_min, self.u_max = u_min, u_max
self.N = int(horizon / dt)

def calculate(self, x, r):
    problem = Problem()
    X = problem.decision_variable(self.A_d.shape[0], self.N + 1)
    U = problem.decision_variable(self.B_d.shape[1], self.N)

    J = 0
    for k in range(self.N + 1):
    J += (r - X[:, k : k + 1]).T @ self.Q @ (r - X[:, k : k + 1])
    for k in range(self.N):
    J += U[:, k : k + 1].T @ self.R @ U[:, k : k + 1]
    problem.minimize(J)

    problem.subject_to(X[:, :1] == x)
    for k in range(self.N):
    x_k, u_k = X[:, k : k + 1], U[:, k : k + 1]
    problem.subject_to(X[:, k + 1 : k + 2] == self.A_d @ x_k + self.B_d @ u_k)
    problem.subject_to bounds(self.u_min, u_k, self.u_max))

    problem.solve()
    return U.value()[:, :1] 
```  
Snippet 17.1. Linear MPC class in Python
