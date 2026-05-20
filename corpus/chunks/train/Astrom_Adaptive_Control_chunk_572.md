The controller is thus highly nonlinear. Figure 9.6 shows the output and the control signal when the controller of Eq. (9.3) is used and when a fixed-gain controller

$$u (t) = - l _ {1} x _ {1} (t) - l _ {2} x _ {2} (t) + m u _ {c} (t) \tag {9.4}$$

is used. The parameters $l_{1}, l_{2}$ , and $m$ are chosen to give the characteristic equation (Eqs. 9.2) when the system is linearized around $x_{1} = \pi$ , that is, the upright position.

Notice that Eq. (9.3) can be used for all angles except for $x_{1} = \pm\pi/2$ , that is, when the pendulum is horizontal. The magnitude of the control signal increases without bounds when $x_{1}$ approaches $\pm\pi/2$ . The linearized model is not controllable at this operating point.

The following example illustrates how to use the method of nonlinear transformations for a second-order system.
