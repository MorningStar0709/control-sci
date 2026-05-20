# Special Design Considerations

Control of fluid removal during dialysis has a direct influence on the patient's well-being. This imposes heavy demands on the control system. Several safety features have been included. Smooth performance from the first moment of control is essential. This can be achieved by a careful choice of certain parameters, as we discuss next.

Filtering. The measured flow signal is corrupted by measurement noise. Since a new value is available every second, it is possible to filter the signal. With a sampling period for control of 5 s, it was found to be suitable to use a first-order filter with a time constant of 30 s to filter flow and accumulated flow before using the values in the control algorithm. This smooths the control signal considerably without preventing fairly quick setpoint changes.

Limits on Setpoint Changes. Both the absolute level and the rates of setpoint changes were limited on the basis of physical constraints. The PID controller was provided with conventional anti-windup protection to avoid problems with saturation. Parameter updating is also interrupted when the pressure setpoint is kept constant at a limit. At startup, when the model parameters may be far from their best values, it is also wise to prevent the control algorithm from changing the control signal (i.e., the pressure setpoint) too rapidly. The rate limit on the pressure setpoint prevents this; experience has shown that this limit is hit only rarely.

Startup. A critical moment for an adaptive controller is the start, before the model parameters have been accurately estimated. It was required that its step response be almost perfect from the beginning. For this reason, most of the development time was spent in adjusting the parameters to ensure a smooth start. The following parameters were then found to be important:

- Initial values of the parameter estimates,   
- Initial values of the covariance matrix $P$ ,   
• The desired closed-loop poles,   
\* The time allowed for signals to settle before estimation and control starts,   
- Limits on the estimated parameters (especially the static gain), and   
• The limit on control changes (and control).
