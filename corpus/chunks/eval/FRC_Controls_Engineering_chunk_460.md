# 17.3.2 Nonlinear MPC

Here’s an example problem formulation for a nonlinear system x˙ = f(xk, uk).

$$\min _ {\mathbf {x} _ {0: N}, \mathbf {u} _ {0: N - 1}} \mathbf {x} _ {N} ^ {\top} \mathbf {Q} \mathbf {x} _ {N} + \sum_ {k = 0} ^ {N - 1} \left(\mathbf {x} _ {k} ^ {\top} \mathbf {Q} \mathbf {x} _ {k} + \mathbf {u} _ {k} ^ {\top} \mathbf {R} \mathbf {u} _ {k}\right)$$

subject to x = current state

$$\mathbf {x} _ {k + 1} = \operatorname{RK4} (f, \mathbf {x} _ {k}, \mathbf {u} _ {k}, \Delta T)\mathbf {u} _ {\text { min }} \leq \mathbf {u} _ {k} \leq \mathbf {u} _ {\text { max }}$$

where N is the number of samples, Q and R are weighting factors, and RK4 is a numerical integration method from section 7.9 chosen for its simplicity. The controller solves this problem at each timestep and returns u0.

Snippet 17.2 shows a nonlinear MPC class in Python.

```python
import frccontrol as fct
from sleipnir.optimization import Problem, bounds 
```

```python
class NonlinearMPC:
    def __init__(self, states, inputs, f, Q, R, dt, u_min, u_max, horizon):
    self.states, self.inputs = states, inputs 
```

```python
self.f = f
self.Q, self.R = Q, R
self.dt = dt
self.u_min, self.u_max = u_min, u_max
self.N = int(horizon / dt)

def calculate(self, x, r):
    problem = Problem()
    X = problem.decision_variable(self.states, self.N + 1)
    U = problem.decision_variable(self.inputs, self.N)

    J = 0
    for k in range(self.N + 1):
    J += (r - X[:, k : k + 1]).T @ self.Q @ (r - X[:, k : k + 1])
    for k in range(self.N):
    J += U[:, k : k + 1].T @ self.R @ U[:, k : k + 1]
    problem.minimize(J)

    problem.subject_to(X[:, :1] == x)
    for k in range(self.N):
    x_k, u_k = X[:, k : k + 1], U[:, k : k + 1]
    problem.subject_to(
    X[:, k + 1 : k + 2] == fct.rk4(self.f, x_k, u_k, self.dt)
    )
    problem.subject_to(bounds(self.u_min, u_k, self.u_max))

    problem.solve()
    return U.value()[ :, :1] 
```  
Snippet 17.2. Nonlinear MPC class in Python
