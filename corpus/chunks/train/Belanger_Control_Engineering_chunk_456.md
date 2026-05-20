7.25 High-wire artist A pole-placement controller was designed in Problem 7.14. We wish to design a LQ controller to satisfy the following specifications: for $\theta(0) = 0.5$ rad, the response must satisfy $|\theta(t)| \leq 0.5$ rad, $|\phi(t)| \leq 0.5$ rad, $|\omega_{\phi}(t)| \leq 0.5$ rad/s, $|\tau(t)| \leq 75$ Nm.

a. Use the linearized model of Problem 2.18 with a LQ law that minimizes

$$J \int_ {0} ^ {\infty} [ Q _ {1 1} \theta^ {2} + Q _ {3 3} \phi^ {2} + Q _ {4 4} \omega_ {\psi} ^ {2} + R _ {1 1} \tau^ {2} ] d t$$

To start, use $Q_{11} = Q_{33} = Q_{44} = 1/0.25$ , $R_{11} = 1/75^{2}$ , and compute the gain matrix.

b. Adjust the weights until the specifications are met.

c. Simulate your control law with the nonlinear model of Problem 2.12, for the initial states of Problem 7.14.

M

7.26 Crane A pole-placement controller was designed for the crane of Problem 2.11 (Chapter 2). We now wish to study an LQ design, in part because pole placement does not take into account the size of the control input $|F|$ , which is to be held below $1500\mathrm{N}$ , or of $|\theta|$ , which is to be less than 0.2 rad (for safety reasons).

a. Use the linearized model of Problem 2.17 to regulate to a set point $x_{d}$ , with an LQ control law that minimizes

$$J = \int_ {0} ^ {\infty} [ Q _ {1 1} (x - x _ {d}) ^ {2} + Q _ {3 3} \theta^ {2} + R _ {1 1} F ^ {2} ] d t.$$

To start, use $Q_{11} = 1/10^{2}$ , $Q_{33} = 1/0.2^{2}$ , and $R_{11} = 1/1500^{2}$ , and calculate the gain matrix.

b. Adjust $Q_{33}$ and $R_{11}$ so that, for $x_{d} = 10 \, m$ , $\theta(0) = 0$ , and zero linear and angular velocities, the constraints on $\theta$ and F are met and the speed of response of x is approximately maximized.

c. Try the linear control law on the nonlinear model of Problem 2.11, for the same conditions.

M

7.27 Two-pendula problem A linear model for the two-pendula problem was developed in Problem 2.19 (Chapter 2).

a. This system is unstable and requires a minimum of control effort in order to become stable. For $\ell_{1}=1$ m and $\ell_{2}=0.5$ m, solve the LQ gain for

$$J = \int_ {0} ^ {\infty} F ^ {2} d t.$$

b. Solve for the responses $\theta_{1}(t)$ , $\theta_{2}(t)$ , and $F(t)$ with the initial state $\theta_{1}(0)=0.1$ rad, $\theta_{2}(0)=-0.1$ rad, $\omega_{1}(0)=\omega_{2}(0)=x(0)=v(0)=0$ . Find the maximum value of $|F(t)|$ and the maximum power $F(t)v(t)$ supplied to the system.
