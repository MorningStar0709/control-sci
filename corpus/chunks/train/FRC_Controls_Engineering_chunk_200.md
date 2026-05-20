# 7.7.1 The intuition

We can demonstrate the basic idea behind the linear-quadratic regulator with the following flywheel model.

$$\dot {x} = a x + b u$$

where a is a negative constant representing the back-EMF of the motor, x is the angular velocity, b is a positive constant that maps the input voltage to some change in angular velocity (angular acceleration), u is the voltage applied to the motor, and x˙ is the angular acceleration. Discretized, this equation would look like

$$x _ {k + 1} = a _ {d} x + b _ {d} u _ {k}$$

If the angular velocity starts from zero and we apply a positive voltage, we’d see the motor spin up to some constant speed following an exponential decay, then stay at that speed. If we throw in the control law $u _ { k } = k _ { p } ( r _ { k } - x _ { k } )$ , we can make the system converge to a desired state $r _ { k }$ through proportional feedback. In what manner can we pick the constant $k _ { p }$ that balances getting to the target angular velocity quickly with getting there efficiently (minimal oscillations or excessive voltage)?

We can solve this problem with something called the linear-quadratic regulator. We’ll

define the following cost function that includes the states and inputs:

$$J = \sum_ {k = 0} ^ {\infty} (Q (r _ {k} - x _ {k}) ^ {2} + R u _ {k} ^ {2})$$

We want to minimize this while obeying the constraint that the system follow our flywheel dynamics $x _ { k + 1 } = a _ { d } x _ { k } + b _ { d } u _ { k }$ .

The cost is the sum of the squares of the error and the input for all time. If the controller gain $k _ { p }$ we pick in the control law $u _ { k } = k _ { p } ( r _ { k } - x _ { k } )$ is stable, the error $\boldsymbol { r } _ { k } - \boldsymbol { x } _ { k }$ and the input $u _ { k }$ will both go to zero and give us a finite cost. Q and R let us decide how much the error and input contribute to the cost (we will require that $Q \geq 0$ and $R > 0$ for reasons that will be clear shortly[6]). Penalizing error more will make the controller more aggressive, while penalizing the input more will make the controller less aggressive. We want to pick a $k _ { p }$ that minimizes the cost.
