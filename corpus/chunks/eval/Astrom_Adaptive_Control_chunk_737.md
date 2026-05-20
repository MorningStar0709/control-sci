Principle. The adaptive control unit used in Firstloop and Firstline is based on recursive estimation of a transfer function model and a control law based on indirect pole placement. The controller also admits feedforward. The main advantage of using an indirect pole placement algorithm is that the system can be applied to nonminimum-phase systems and systems with time-varying time delays. This also implies that short sampling periods can be used. (Compare the discussion in Section 6.9.) The adaptive module comes in two versions, a standard module and an expert module. The standard module is intended for use by ordinary instrument engineers who are not specialists in adaptive control. The expert module shown in Fig. 12.5 is intended for specialists in adaptive control. Many parameters are given default values in the standard module. The variables that must be specified are shown in Fig. 12.5. The signal connections are measured value MV, setpoint SP, external control signal UE, feedforward FF1, FF2, and controller output U. The mode switches ON, AUTO, and ADAPT are for on/off, auto/normal, and adaptation on/off, respectively.

![](image/a2d05da7ecc7793e5e81b3f9fc2aebe42d1b4f31b7aa19b044c88ea921b2e62d.jpg)

<details>
<summary>text_image</summary>

Signals
ON
AUTO
ADAPT
LOAD
MODEL
MV
SP
UE
FF1
FF2
HI
LO
DUP
DUM
U
Parameters
NA
NB
NC
MD
DMP
SAMP
UMAX
UMIN
RESU
RESY
KINIT
BMPLVL
POLE
SFF1
SFF2
Integer
Real
Logical
Output
</details>

Figure 12.5 The expert module STREGX in Firstloop.

Parameters UMAX and UMIN define the actuator range. Variables HI, LO, DUP, and DUM specify the limits on the control signal that are used internally in the controller. The performance-related parameters are POLE, which gives the desired closed-loop pole, and BMPLVL, which gives the admissible initial change of the control variable at mode switches.

The desired closed-loop pole is the major variable to be selected. The choice of this variable clearly requires knowledge of the time scales of the process. The recommended rule of thumb is to start with a large value and gradually decrease it.
