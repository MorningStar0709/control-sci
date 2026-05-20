# Example 5.2

Consider the simple single-mass mechanical system shown in Fig. 5.1, which involves both stiffness and damping elements. Determine the state-variable equations.

The position of the mass is denoted by $z ,$ which is measured from the static equilibrium position when applied force $F _ { a } ( t ) = 0$ . Stiffness is modeled by a nonlinear spring, which exhibits the following nonlinear force-displacement relationship:

$$f _ {k} (z) = k _ {1} z + k _ {3} z ^ {3} \tag {5.6}$$

Damping force is assumed to be a linear function of viscous friction coefficient b and velocity. The applied force $F _ { a } ( t )$ is the input to the system.

We start with the mathematical model, which is derived using a free-body diagram and the methods of which are presented in Chapter 2. The modeling equation is identical to the mass–spring–damper model in Example 2.1, except that the nonlinear spring force (5.6) must be used:

$$m \ddot {z} + b \dot {z} + k _ {1} z + k _ {3} z ^ {3} = F _ {a} (t) \tag {5.7}$$

Equation (5.7) is a second-order (nonlinear) ODE. Hence $n = 2$ and it requires two state variables. We select position z and velocity ż as the two state variables because knowledge of these variables will determine the total (potential + kinetic) energy of the system. The applied force is the single system input. Therefore, using our convention where $x _ { i }$ are state variables and $u _ { j }$ are input variables, we have $x _ { 1 } = z , x _ { 2 } = \dot { z }$ , and $u = F _ { a } ( t )$ .

1 2 Once we have defined the state variables, we simply write the first-order differential equations by taking time derivatives of each state variable. The state-variable equations are

$$\dot {x} _ {1} = \dot {z} \tag {5.8}\dot {x} _ {2} = \ddot {z} = \frac {1}{m} \left(- b \dot {z} - k _ {1} z - k _ {3} z ^ {3} + F _ {a} (t)\right) \tag {5.9}$$

Notice that we have solved the mathematical model (5.7) for acceleration z̈ and substituted it into the second statevariable equation (5.9). Our standard convention for state-variable equations presented by Eq. (5.1) shows that the right-hand side functions must solely involve states $x _ { i }$ and inputs $u _ { j }$ . Therefore, we substitute $x _ { 1 } = z , x _ { 2 } = \dot { z } ,$ and $u = F _ { a } ( t )$ into Eqs. (5.8) and (5.9) to produce the final form of the state-variable equations:

$$\dot {x} _ {1} = x _ {2} \tag {5.10}\dot {x} _ {2} = - \frac {k _ {1}}{m} x _ {1} - \frac {k _ {3}}{m} x _ {1} ^ {3} - \frac {b}{m} x _ {2} + \frac {1}{m} u \tag {5.11}$$
