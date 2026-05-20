Use the mathematical model developed in Problem 4.15a for an incompressible fluid where we can assume that the flow in/out of the chambers is $Q = A { \dot { x } }$ . Develop a Simulink model and simulate the damper’s response to the pulse input. Plot piston position x(t) and $\bar { \boldsymbol { F } } _ { d } ( t )$ , which is the total force (due to friction and pressure) that opposes motion. Let the simulation time be 1 s [Hint: use a fixed-step integration method with a small step size].

6.27 Consider again the hydraulic damper in Fig. P6.26 and Problem 6.26. Use the mathematical model developed in Problem 4.15b for a compressible fluid where we cannot assume that $Q = A { \dot { x } }$ always holds. Develop an integrated Simulink model and simulate the damper’s response to the pulse input and initial conditions described in Problem 6.26. Plot piston position $x ( t )$ and pressure $P _ { 1 } ( t )$ . Let the simulation time be 1 s [Hint: use a fixed-step integration method with a very small step size].

6.28 Figure P6.28 shows the electropneumatic clutch actuator described in Problem 4.20 in Chapter 4. The system parameters are [6]

Rod and piston mass $m = 10\mathrm{kg}$ Viscous friction $b = 2000\mathrm{N - s / m}$ Clutch load force $F_{L} = 4000(1 - e^{-500x}) - 20,000x\mathrm{N}(x$ in $\mathfrak{m})$ Area $A_{1} = 0.0123\mathrm{m}^{2}$ Area $A_{2} = 0.0115\mathrm{m}^{2}$ Valve orifice area (open) $A_0 = 7(10^{-6})\mathrm{m}^2$ Discharge coefficient $C_d = 0.8$ Chamber volume $V = V_{0} + A_{1}x$ Half-cylinder volume $V_{0} = 1.48(10^{-4})\mathrm{m}^{3}$ Gas constant (air) $R = 287\mathrm{N - m / kg - K}$ Air temperature $T = 298\mathrm{K}$ Isothermal process with choked flow through both valves   
Supply pressure $P_{S} = 9.5(10^{5})\mathrm{Pa}$ Ambient pressure $P_{\mathrm{atm}} = 1.013(10^{5})\mathrm{Pa}$

The initial piston position is x = 0 and the initial chamber pressure is $P = P _ { \mathrm { a t m } } A _ { 2 } / A _ { 1 }$ . Develop an integrated Simulink model and simulate the pneumatic clutch actuator response to a supply valve pulse opening that lasts 0.1 s (the exhaust valve remains closed). Plot piston position x(t) and chamber pressure $P ( t )$ responses. Use the pressure response to validate the assumption that the valve flow is always choked.

![](image/dcb9311800dd3b35179b291c42fff02c482fc46911a60e3e07ef574fad5431c9.jpg)

<details>
<summary>text_image</summary>

Supply
P_S
Supply valve
Area, A_1
x
Area, A_2
Exhaust valve
P, V
P_atm
Piston mass, m
Viscous friction, b
Clutch load force, F_L
</details>

Figure P6.28
