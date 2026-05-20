# Example 5.1

Determine the state-variable equations for the system modeled by the following ODEs, where z and w are the dynamic variables and v is the input

$$2 \ddot {z} + 0. 8 z - 0. 4 w + 0. 2 \dot {z} w = 0 \tag {5.2}4 \dot {w} + 3 w + 0. 1 w ^ {3} - 6 z = 8 v \tag {5.3}$$

The first step is to determine the order of the system. Equation (5.2) is a second-order nonlinear ODE in dynamic variables z and w, while Eq. (5.3) is a first-order nonlinear ODE in dynamic variables w and z and input v. Hence the complete system is third order, and we need three state variables. We define the state variables $x _ { 1 } = z ,$ , $x _ { 2 } = \dot { z }$ , and $x _ { 3 } = w$ and the single input u = v. Next, we write the three first-order time derivatives of the three state variables

$$\dot {x} _ {1} = \dot {z}\dot {x} _ {2} = \ddot {z} = 0. 5 (- 0. 8 z + 0. 4 w - 0. 2 \dot {z} w)\dot {x} _ {3} = \dot {w} = 0. 2 5 (- 3 w - 0. 1 w ^ {3} + 6 z + 8 v) \tag {5.4}$$

Note that we have substituted the second-order ODE (5.2) for z̈, and the first-order ODE (5.3) for ẇ . Because we want all three right-hand sides of Eq. (5.4) to be functions of the states $x _ { i }$ and input u, we substitute $x _ { 1 } = z , x _ { 2 } = \dot { z } ,$ $x _ { 3 } = w$ , and u = v to yield

$$\dot {x} _ {1} = x _ {2}\dot {x} _ {2} = - 0. 4 x _ {1} + 0. 2 x _ {3} - 0. 1 x _ {2} x _ {3}\dot {x} _ {3} = - 0. 7 5 x _ {3} - 0. 0 2 5 x _ {3} ^ {3} + 1. 5 x _ {1} + 2 u \tag {5.5}$$

Equations (5.5) are the state-variable equations of the system described by Eqs. (5.2) and (5.3). All three righthand sides of the state-variable equations are functions of the states $x _ { i }$ and input u. Two of the three state-variable equations are nonlinear, due to the nonlinear terms $- 0 . 1 x _ { 2 } x _ { 3 }$ (second state-variable equation) and $- 0 . 0 2 5 x _ { 3 } ^ { 3 }$ (third 3 state-variable equation). The reader should note that the assignment of the state variables is arbitrary; for example, we could have swapped the definitions of states $x _ { 1 }$ and $x _ { 3 }$ and used $x _ { 1 } = w$ and $x _ { 3 } = z$ .
