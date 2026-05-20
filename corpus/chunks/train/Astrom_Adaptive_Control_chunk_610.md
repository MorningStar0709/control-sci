# Design of an SOAS

The self-oscillating adaptive system is a simple nonlinear feedback system that is capable of adapting rapidly to gain variations. The system has a continuous limit cycle oscillation. This is not suitable when valves or other mechanical parts are used as actuators. However, an SOAS may conveniently be used with thyristors as actuators. The presence of the limit cycle oscillation may also cause other inconveniences. Since the system will automatically adjust to an amplitude margin $A_{m} = 2$ , it is also necessary that the characteristics of the process be such that this design principle gives suitable closed-loop properties. The key problem in the design of the SOAS is the compromise between the limit cycle amplitude and the response speed. This compromise is influenced by the selection of the linear compensator, $G_{i}(s)$ , and of the relay amplitude. (Compare Fig. 10.7.) The design for an SOAS can be described by the following procedure.

Step 1: The relay amplitude is first determined such that the desired control authority (tracking rate, force, speed, etc.) is obtained. This can be estimated by analyzing the response of the process to constant control signals.

Step 2: When the relay amplitude is specified, the desired limit cycle frequency can be determined from the condition

$$d \left| G _ {p} (i \omega_ {u}) \right| = e _ {0}$$

where $e_{0}$ is the tolerable limit cycle amplitude in the error signal and $G_{p}(s)$ is the transfer function of the process. It is necessary to check that the frequency obtained is reasonable. For example, the frequency $\omega_{u}$ may become so high that the process dynamics become uncertain.

Step 3: The final step is to determine the transfer function $G_{f}$ of the linear compensator such that

$$\arg G _ {f} (i \omega_ {u}) + \arg G _ {p} (i \omega_ {u}) = - \pi$$

A large phase lead may be necessary, but this may not be realizable because of noise sensitivity.

Step 4: Check that the linear closed-loop system with the loop gain $G_{0} = KG_{f}G_{p}$ will work well when the gain K is adjusted so that the amplitude margin is 2. If this is not the case, the compensator $G_{f}$ must be modified. ☐

Notice that it is necessary to have an estimate of the magnitude of the process transfer function in Steps 1 and 2. Knowledge of the phase curve of the process transfer function is necessary in the third step. Also notice that it may not be possible to resolve the compromises in all steps. It is then necessary to add additional loops for changing the gain.
