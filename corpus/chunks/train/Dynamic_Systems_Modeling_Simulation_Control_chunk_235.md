which is the nominal pressure or operating point of the hydraulic system. The perturbation variables are defined as $\delta P = P - P ^ { * }$ and $\bar { \delta Q } _ { \mathrm { i n } } = Q _ { \mathrm { i n } } - \bar { Q } _ { \mathrm { i n } } ^ { * }$ . Next, we use Eq. (5.62), the first-order Taylor-series expansion

$$\delta \dot {P} = \left. \frac {\partial f}{\partial P} \right| _ {*} \delta P + \left. \frac {\partial f}{\partial Q _ {\mathrm{in}}} \right| _ {*} \delta Q _ {\mathrm{in}} \tag {5.72}$$

where the first-order partial derivatives can be determined using Eq. (5.70)

$$\left. \frac {\partial f}{\partial P} \right| _ {*} = \frac {- K _ {T}}{2 C \sqrt {P ^ {*} - P _ {\mathrm{atm}}}} \quad \left. \frac {\partial f}{\partial Q _ {\mathrm{in}}} \right| _ {*} = \frac {1}{C}$$

Substituting Eq. (5.71) for the nominal $P ^ { * }$ yields the first-order derivative

$$\left. \frac {\partial f}{\partial P} \right| _ {*} = \frac {- K _ {T} ^ {2}}{2 C Q _ {\mathrm{in}} ^ {*}}$$

This derivative is a known constant, given numerical values for turbulent flow coefficient $K _ { T }$ , fluid capacitance C, and nominal input flow rate $Q _ { \mathrm { i n } } ^ { \ast }$ . Finally, the linear hydraulic model is

$$\delta \dot {P} = \frac {- K _ {T} ^ {2}}{2 C Q _ {\mathrm{in}} ^ {*}} \delta P + \frac {1}{C} \delta Q _ {\mathrm{in}} \tag {5.73}$$

The solution to the linear model will produce the pressure perturbation $\delta P ( t )$ . We revisit this problem in Chapter 6 when we compare the system responses of the linear and nonlinear hydraulic models using numerical simulations.

The linearization method can be generalized and applied to the nth-order vector of nonlinear state equations

$$\dot {\mathbf {x}} = \mathbf {f} (\mathbf {x}, \mathbf {u}) \tag {5.74}$$

The nominal input vector time history ${ \bf u } ^ { * } ( t )$ will produce a nominal state vector history ${ \bf x } ^ { * } ( t )$ , sometimes called the state trajectory. For example, a predefined program for motor torque inputs for a robotic system will produce nominal trajectories for the positions and velocities of the robot linkages. The three-step linearization process previously described can be applied to the nonlinear vector system (5.74), and the result is

$$\delta \dot {\mathbf {x}} = \left. \frac {\partial \mathbf {f}}{\partial \mathbf {x}} \right| _ {*} \delta \mathbf {x} + \left. \frac {\partial \mathbf {f}}{\partial \mathbf {u}} \right| _ {*} \delta \mathbf {u} \tag {5.75}$$
