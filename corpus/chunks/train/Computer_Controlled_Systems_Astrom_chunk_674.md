# Example 11.4 Ship steering

The linearized dynamics that describe the steering of ships can be described by the equation

$$
\frac {d}{d t} \left( \begin{array}{l} v \\ r \\ \Psi \end{array} \right) = \left( \begin{array}{c c c} a _ {1 1} & a _ {1 2} & 0 \\ a _ {2 1} & a _ {2 2} & 0 \\ 0 & 1 & 0 \end{array} \right) \left( \begin{array}{l} v \\ r \\ \Psi \end{array} \right) + \left( \begin{array}{l} b _ {1} \\ b _ {2} \\ 0 \end{array} \right) \delta \tag {11.41}
$$

where $\delta$ is rudder angle, $\Psi$ is the heading angle, r is the turning rate, and v the sway velocity. The relative increase in the drag due to steering may be approximated by the expression

$$\frac {\Delta R}{R} = \frac {\alpha}{T} \int_ {0} ^ {T} (v r + \rho \delta^ {2}) d t \tag {11.42}$$

The first term represents the Coriolis force due to coupling of sway velocity and turning rate. The second term represents the drag induced by the rudder deflections.

In many cases it is difficult to find natural quadratic loss functions. LQ-control theory has found considerable use even when this cannot be done. In such cases the control designer chooses a loss function. The feedback law is obtained directly by solving the Riccati equation. The closed-loop system obtained is then analyzed with respect to transient response, frequency response, robustness, and so on. The elements of the loss function are modified until the desired result is obtained. Such a procedure may seem like a strange use of optimization theory.

The fact that other methods, such as direct search over the feedback gain or pole placement, are not used instead might be questioned. It has been found empirically that LQ-theory is quite easy to use in this way. The search will automatically guarantee stable closed-loop systems with reasonable margins.

It is often fairly easy to see how the weighting matrices should be chosen to influence the properties of the closed-loop system. Variables $x_{i}$ , which correspond to significant physical variables, are chosen first. The loss function is then chosen as a weighted sum of $x_{i}$ . Large weights correspond to small responses. The responses of the closed-loop system to typical disturbances are then evaluated. A particular difficulty is to find the relative weights between state variables and control variables, which can be done by trial and error.
