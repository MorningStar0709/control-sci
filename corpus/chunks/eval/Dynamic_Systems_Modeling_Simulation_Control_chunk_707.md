# Linear Maglev Model

We wish to design a feedback control scheme for position control of the ball using the electromagnetic force. In Chapter 10, we investigated various methods for analyzing and designing control systems. All of these techniques are based on linear, time-invariant (LTI) plant models. Therefore, we must first develop a linear model of the maglev system; once we have an LTI system, we can apply control-design techniques such as the root-locus method. If we can arrive at a satisfactory control system design using the approximate LTI plant model, we must eventually test its performance with the full nonlinear maglev system.

Our nonlinear maglev system is third order, so let us begin by defining three nonlinear state-variable equations for the state vector ${ \bf x } = [ I { \bf \Xi } z \dot { \bf \Xi } ] ^ { T }$ with the input vector $\mathbf { u } = \left[ e _ { \mathrm { i n } } ( t ) \quad g \right] ^ { T }$ . Using Eqs. (11.65) and (11.68) we can write three first-order ODEs

$$\dot {x} _ {1} = \frac {- R}{L} x _ {1} + \frac {1}{L} u _ {1} = f _ {1} (\mathbf {x}, \mathbf {u}) \tag {11.69}\dot {x} _ {2} = x _ {3} = f _ {2} (\mathbf {x}, \mathbf {u}) \tag {11.70}\dot {x} _ {3} = \frac {K _ {F} x _ {1} ^ {2}}{m (d - x _ {2}) ^ {2}} - u _ {2} = f _ {3} (\mathbf {x}, \mathbf {u}) \tag {11.71}$$
