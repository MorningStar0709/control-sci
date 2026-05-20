Principle. The ABB adaptive controller is a direct self-tuning regulator similar to Algorithm 4.1 in Section 4.3. The parameters of a discrete-time model are estimated by using recursive least squares. The control design is a minimum-variance controller, which is extended to admit positioning of one pole and a penalty on the control signal. The block diagrams in Fig. 12.3 show two of the adaptive modules. The ABB adaptive controller system has three adaptive modules: STAR1, STAR2, and STAR3. STAR3 is the most complicated. The simpler ones have fewer inputs and have default values on some of the parameters in STAR3. In the block diagram the input signals are shown on the left and top sides of the box, the output signals on the right, and the parameters on the bottom. The parameters can be changed at configuration time. The parameters PL, T, and PN can also be changed on-line.

The simplest module, STAR1, has three input signals: the manual input UEXT, the measured value FB, and the setpoint REF. It has three parameters. The variable PY is the smallest relevant change in the feedback signal; the adaptation is inhibited for changes less than PY. The parameters MAX and MIN denote the bounds on the control variable, and T is the sampling period.

The module STAR2 has more input signals. It admits a feedforward signal FF. There are also four signals, HI, LO, DH, and DL, that admit dynamic changes on the bounds of the control variable and its rate of change. There are also additional parameters: PN, for a penalty on the control variable, and KD, which specifies the prediction horizon. The module also has two additional mode switches: REGAD, which turns off adaptation when false, and SOFT, which allows a soft start.

The module STAR3 has an additional function LOAD, which admits parameters stored in an EEPROM to be loaded. It also has several additional parameters, which admit positioning of one pole PL and specification of controller structure NA, NB, NC, and INT.

Parameter Estimation. The parameter estimation is based on the model

$$
\begin{array}{l} (1 - P L q ^ {- 1}) y (t + K D) - (1 - P L) y (t) \\ = A ^ {*} (q ^ {- 1}) \Delta y (t) + B ^ {*} (q ^ {- 1}) \Delta u (t) + C ^ {*} (q ^ {- 1}) \Delta v (t) \\ \end{array}
$$
