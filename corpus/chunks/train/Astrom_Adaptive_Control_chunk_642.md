# Controller Windup

Linear theory is adequate to deal with many problems in control system design. There is, however, one nonlinear problem that we must deal with in almost all practical control systems, and that is actuator saturation. The feedback will be broken when the actuator saturates. Large deviation may then occur if the process or the controller is unstable. A simple case in which this occurs is when the controller has integral action. The phenomenon was first observed in connection with PID control. It is therefore often called integrator windup because the integral term "winds up" when the actuator is saturated. Since integral action was also called reset, the phenomenon is also called reset windup. It is necessary to include a scheme for avoiding windup in systems in which the process and/or the controller is unstable.

There are many different ways to introduce anti-reset windup. One simple way is based on the interpretation of a controller as a combination of a state estimator and state feedback. Such a system is shown in Fig. 11.3. The controller is composed of two components, a state estimator and a state feedback. The state estimator determines an estimate of the state based on the process input and output. The state feedback generates the control signal based on the estimated state. It is intuitively clear from the figure that the state estimator will perform poorly when the actuator saturates because it is uses a wrong value of the control signal applied to the process. This interpretation also suggests that the problem can be avoided by feeding back the actual process input, $u_{a}$ , or an estimate of it as in Fig. 11.3(b).

![](image/e2d610e60759849c286263c122f2558f5a131e46e1e60e34ea5fd388a5d096c4.jpg)  
Figure 11.3 Block diagrams of controllers based on state feedback and state estimation with a process having a nonlinear actuator.

Since we are using polynomial representations of the controller in this book, we also give a polynomial interpretation of the scheme. Consider the controller

$$R (q) u (t) = T (q) u _ {c} (t) - S (q) y (t)$$

where the polynomial $R(q)$ is assumed to be monic. The controller can be written in observer form as

$$A _ {o} (q) u (t) = T (q) u _ {c} (t) - S (q) y (t) + \left(A _ {o} (q) - R (q)\right) u (t)$$

where $A_{o}(q)$ is the observer polynomial. Let the saturating actuator be described by the nonlinear function $f(u)$ . A controller that avoids windup is then given by
