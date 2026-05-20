# 10.2.1 Performance Functions

The python method cost\_pid() uses several functions which compute the performance measures from the step response.

Settling Time: $T _ { S }$

Settling time $( T _ { S } )$ is the time from the start of step input until the response stays within 2% of its nal value (not necessarily the desired nal value if SSE is non zero).

Percent Overshoot: P OS

P OS is the percentage by which the step response exceeds its nal value.

Steady State Error: SSE

SSE is the dierence between the nal value of the step response and the amplitude of the input step (we use 1.0).

Actuator Eort: $U _ { M A X }$

Actuator eort (same as control eort) is the amount of output from your actuator which is given to the plant. A controller design must achieve its step response specs without requiring excessive output from its actuator. By including actuator eort into the cost function, we make sure that the controller we design is practical. The measure of actuator eort will be the peak value during the simulation time, max u(t).

Gain Margin: gm

Gain Margin is described in Section 6.7.1. In brief, if a system has gain margin GM (usually expressed in dB), then the magnitude of the loop gain $( | C P H ( s ) | )$ can be increased by that amount of gain while still remaining stable. For example, for a gain margin of 20dB, we can add +19dB of gain to $C \bar { P } H ( s )$ and the system will still be stable (but the new gain margin will be only 1dB).

We will specify a target or desired value for each performance measure, for example $T _ { s d } = 0 . 2 5$ means we set a goal to nd a design with a settling time of 0.25sec. We will measure one aspect of how good is our design by minimizing the dierence between our design's performance and the desired value, in this case

$$\left| \left(T _ {s} - T _ {s d}\right) \right|$$

If we only care about settling time, then our goal is to minimize this quantity.
