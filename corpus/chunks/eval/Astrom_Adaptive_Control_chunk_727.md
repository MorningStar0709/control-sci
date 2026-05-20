# SattControl ECA40 and Fisher Control DPR 900

This is the original auto-tuner based on relay oscillations, as described in Chapter 8. It was first introduced in a small (about 45 loops) DDC system for industrial process control SDM20. In this application the tuner can be connected to tune any loop in the system. Relay auto-tuning is also available in single-loop PID controllers (SattControl ECA40 and Fisher Control DPR900). In these controllers, tuning is done on demand by pushing a button on the front panel, so-called one-button tuning. The controllers are also provided with facilities for gain scheduling. There is a table with three controller settings.

Parameter Estimation. The ultimate period and the ultimate gain are determined by an experiment with relay feedback. The fluctuations in the output signal are measured, and the hysteresis of the relay is set slightly wider than the noise band. The initial relay amplitude is fixed. The amplitude and period are measured for each half-period. A feedback adjusts the relay amplitude so that the limit cycle oscillation has a given amplitude. When two successive half-periods are sufficiently close, PID parameters are computed, and PID control is initiated automatically.

Control Design. When the ultimate gain and the ultimate period are known, the parameters of a PID controller can be determined by a modified Ziegler-

Nichols rule. There is also a limited amount of logic to determine whether derivative action is needed.

Prior Information. A major advantage of the auto-tuner is that no parameters have to be set a priori. To use the tuner, the process is simply brought to an equilibrium by setting a constant control signal in manual mode. The tuning is then activated by pushing the tuning button. The controller is automatically switched to automatic mode when the tuning is complete. Different control objectives may be obtained by modifying the parameters in the Ziegler-Nichols rule. One mode is chosen by default, but the user can request a slower or an extra-fast response.
