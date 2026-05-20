# Build matrices
A = np.array([[0, 1, 0, 0],
    [0, 0, -m*g/M, 0],
    [0, 0, 0, 1],
    [0, 0, (M+m)*g/(M*1), 0]])
B = np.array([[0], [1/M], [0], [-1/(M*1)]])
rho = 0.1
Q = np.matrix([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 100, 0],
    [0, 0, 0, 100]])
R = rho * np.eye(1) # control size is 1 
```

Then we define the LQR controller as following, where X is the solution to the Riccati equations solved via the Python library SciPy. The closed loop gain K is then defined as:

$$K = R ^ {- 1} B ^ {T} X \tag {389}$$

Python code:   
```python
def LQR(A,B,Q,R):
    """Solve the continuous time lqr controller.
    dx/dt = A x + B u
    cost = integral x.T*Q*x + u.T*R*u
    """
    #ref Bertsekas, p.151

# First, try to solve the Riccati equation
    X = np.matrix(scipy.linalg.solve_continuous_are(A, B, Q, R))

# Compute the LQR gain
    K = np.matrix(scipy.linalg.inv(R)*(B.T*X))

eigVals, eigVecs = scipy.linalg.eig(A-B*K)

return K, X, eigVals

K, X, eigVals = LQR(A, B, Q, R) 
```

By running the code with our designed controller we get:

$$K = \left[ - 3. 1 6 2 2 7 7 6 6 - 9. 2 6 5 9 4 0 7 1 - 1 4 6. 9 4 2 6 5 7 6 9 - 8 0. 1 3 7 7 6 7 6 5 \right] \tag {390}$$

In order to simulate the system, we design a class simulating the inverted pendulum and its physical behavior in time, which is discretized in steps of τ = 0.02s:

```python
class ControlledPendulum():
    ''' Continuous version of the OpenAI Gym cartpole '''
def __init__(self, M, m, l, tau=0.02, g=9.81):
    self.gravity = g
    self.masscart = M
    self.masspole = m
    self.total_mass = (self.masspole + self.masscart)
    self.length = l  # actually half the pole's length
    self.polemass_length = (self.masspole * self.length)
    self.force_mag = 30.0
    self.tau = tau  # seconds between state updates
    self.state = None  # Initialize through reset

def step(self, force):
    x, x_dot, theta, theta_dot = self.state
    costtheta = math.cos(theta)
    sintheta = math.sin(theta)
    temp = (force + self.polemass_length * theta_dot \
    * theta_dot * sintheta) / self.total_mass
    thetaacc = (self.gravity * sintheta - costtheta * temp) / \
    (self.length * (4.0/3.0 - self.masspole * \
    costtheta * costtheta / self.total_mass))
    xacc = temp - self.polemass_length * thetaacc * \
    costtheta / self.total_mass
    x = x + self.tau * x_dot
    x_dot = x_dot + self.tau * xacc
    theta = theta + self.tau * theta_dot
    theta_dot = theta_dot + self.tau * thetaacc
    self.state = x, x_dot, theta, theta_dot # save state
    return np.array(self.state, dtype='float64').reshape(4,1)
