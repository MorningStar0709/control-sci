where $\tau _ { 1 }$ is the head tracking time constant (typically 0.1 second for an air-to-air missile during the terminal phase, and 0.2 second during the preterminal guidance phase). An approximate knowledge of closing velocity is necessary for the optimum solution of the navigation problem because the optimum value of the acceleration command to the autopilot is proportional to the closing velocity. The Doppler frequency, representing closing velocity, is used to control the multiplication of the error signal, which is proportional to the line-of-sight rate. In the actual mechanization, the acceleration command to the autopilot $( a _ { c } )$ is generated as a constant (K) multiplied by the product of radar error (ε) and closing velocity $V _ { c }$ :

$$a _ {c} = K \varepsilon V _ {c}.$$

In this manner, the missile trajectory is optimized as a function of missile and target velocity variations.

In terms of their contribution to proportional navigation, the principal functions of the major circuits in the guidance and control system are as follows:

RF and Microwave Section: The front antenna is typically a flat-plate slotted array antenna. Directional information for the missile flight is obtained by conical scanning the target’s reflected energy using ferrite phase shifters. The radar antenna that receives RF energy from the launching aircraft is used for automatic frequency controlling.

Rear Receiver: The rear receiver acquires and tracks illuminator transmission for use as a reference for extracting the Doppler signal.

Front Receiver and Video Amplifier: The front receiver and video amplifier amplify and AGC (automatic gain control) the front signal to a level compatible with the dynamic range of the speedgate.

Speedgate: The speedgate acquires and tracks the Doppler signal, using AGC to adjust the signal to a constant level, so that AM directional information (ε) can be extracted at a known scale factor (10% modulation is equal to $1 ^ { \circ }$ of direction error off antenna boresight (see also Section 3.6)).

Head Control: The head control establishes proportionality between antenna error (ε) and line-of-sight rate (dλ/dt). Whenever error is not equal to the tracking time constant $\left( \tau _ { 1 } \right)$ multiplied by the head rate in space $[ ( d \lambda / d t ) + ( d \varepsilon / d t ) ]$ ], the head servo must adjust the head rate and position.
