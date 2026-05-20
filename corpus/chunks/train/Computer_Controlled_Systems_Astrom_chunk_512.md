# Operational Aspects

Practically all PID-controllers can run in two modes: manual and automatic. In manual mode the controller output is manipulated directly by the operator, typically by push buttons that increase or decrease the controller output. The controllers may also operate in combination with other controllers, as in a cascade or ratio connection, or with nonlinear elements such as multipliers and selectors. This gives rise to more operational modes. The controllers also have parameters that can be adjusted in operation. When there are changes of modes and parameters, it is essential to avoid switching transients. The way mode switchings and parameter changes are made depends on the structure chosen for the controller.

![](image/f5401c6dd9f47a40a1a23622e396fbe23c091ec72596f1a914b4956ea362c18d.jpg)  
Figure 8.11 Controllers with bumpless transfer from manual to automatic mode. The controller in (a) is incremental. The controllers in (b) and (c) are special forms of position algorithms. The controller in (c) has antiwindup (MCU = Manual Control Unit).

Bumpless transfer. Because the controller is a dynamic system it is necessary to make sure that the state of the system is correct when switching the controller between manual and automatic mode. When the system is in manual mode, the controller produces a control signal that may be different from the manually generated control signal. It is necessary to make sure that the value of the integrator is correct at the time of switching. This is called bumpless transfer. Bumpless transfer is easy to obtain for a controller in incremental form. This is shown in Fig. 8.11(a). The integrator is provided with a switch so that the signals are either chosen from the manual or the automatic increments. Because the switching only influences the increments, there will not be any large transients. A related scheme for a position algorithm is shown in Fig. 8.11(b). In this case the integral action is realized as positive feedback around a first-order system. The transfer function from v to u is

![](image/30957aa20f23da80ee225c0e973198182a649964644b11fcd96dfff4d2f82299.jpg)

<details>
<summary>flowchart</summary>
