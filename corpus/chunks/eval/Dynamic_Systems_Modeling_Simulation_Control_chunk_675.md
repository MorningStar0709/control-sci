Both orifice-flow equations depend on the supply pressure $P _ { S }$ and the valve area, $A _ { \nu } = h y$ . Hence, the supply pressure $P _ { S }$ and valve displacement y are the two free input variables for the air-brake system. In reality, the valve displacement y is proportional to the driver’s brake-pedal force (see Fig. 11.22).

Figure 11.25 shows the Simulink model of the integrated air-brake system. Note that the two system inputs are the driver’s brake-pedal force (step input) and the constant supply pressure. Valve displacement y is proportional to the brake-pedal force. The orifice-flow subsystem, Eqs. (11.29) and (11.30), has $y , P _ { S } ,$ , and P as its input variables and mass-flow rate w as the single output. The chamber pressure subsystem, Eq. (11.27), has mass flow w, piston position x, and piston velocity ẋ as its input variables and chamber pressure as the single output. Finally, the mechanical subsystem, Eq. (11.24), has pressure P as the single input and piston displacement and velocity as its two output variables.

Figure 11.26 shows the inner details of the orifice subsystem block. Because the orifice-flow equations (11.29) and (11.30) are complicated, they are contained in an M-file instead of explicitly shown as a simulation diagram. The Interpreted MATLAB Fcn block, found in the User-Defined Functions Simulink library, allows the user to write a customized script (M-file) that is a function of several input variables. Note that the three inputs $( P _ { S } , y _ { : }$ , and P) in Fig. 11.26 are sent to the multiplexer Mux, which combines the three inputs into a $3 \times 1$ column vector (Mux is found in the Signal Routing library). MATLAB M-file 11.2 shows the customized M-file Valve.m, which contains the necessary equations, (11.29)– (11.31), to compute either choked or unchoked flow.

![](image/d4afa0cce1d7faf2368ebaf77d189bf12eb71700b58ac78a94515dc02bb04f77.jpg)

<details>
<summary>flowchart</summary>
