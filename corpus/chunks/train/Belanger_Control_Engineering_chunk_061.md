i. Write the total volume $V_{T}$ in the tank at $t + \Delta t$ , in terms of the volume at t and the flows in and out of the tank during the interval t to $t + \Delta t$ . Note that a flow $F m^{3}/s$ carries $F \Delta t m^{3}$ of material during $\Delta t$ . With $V_{T} = A\ell(A = \text{cross-sectional area})$ , write a differential equation for $\ell$ in terms of the variables $F_{A}, F_{B}$ , and $F_{0}$ .   
ii. Proceed as in (i) to write a differential equation for $V_{A}$ , the volume of substance A in the tank. Note that, if the tank is well mixed, the concentration of A is $C_{A} = V_{A}/V_{T}$ , and the rate of outflow of A is $C_{A}F_{0}$ .

b. Write the state equations for the specific value $A = 0.1 \, m^{2}$ .   
c. Simulate for $\ell(0) = 0.2\mathrm{m}$ , $C_A(0) = 0.5$ , $F_A = F_B = 0.0002\mathrm{m}^3/\mathrm{s}$ , $F_0 = 0.0003\mathrm{m}^3/\mathrm{s}$ . The simulation interval is $0 \leq t \leq 60\mathrm{s}$ . (Note: You will need to calculate $V_T(0)$ from $l(0)$ and $C_A(0)$ .)

![](image/b8928de7f1df3d36a0c3bcc0a741e1e2eecfd2e5adde313e37f42ab3efb57bdc.jpg)

2.8 Heat exchanger Figure 2.22 illustrates a counterflow heat exchanger. A hot liquid flows leftward at a rate $F_{H}$ and transfers heat through a pipe to a cold liquid flowing rightward at a rate $F_{C}$ . This is actually a distributed system; it is approximated by the system of Figure 2.23, where the fluids are assumed to flow between well-mixed tanks with uniform temperatures. The tanks appear in pairs, and heat is conducted across the separating surfaces.

The basic physical principles are that (i) the heat contained in a mass M of liquid is $Mc_{v}T$ , where $c_{v}$ is the heat capacity and T is the temperature, and (ii) the rate of heat conduction across a surface is proportional to the temperature difference across it. All tanks have volume V, and both liquids have density $\rho$ and heat capacity $c_{v}$ .

![](image/985855b06a7382cfa74ea116e6cd2dc95f07a33af431f7fdc0aa9b244f5dff62.jpg)

<details>
<summary>text_image</summary>

F_C →
F_H
</details>

Figure 2.22 Counterflow heat exchanger

![](image/f4a811425a8a64394196d669e0ae35fb747572e43296c10d258b4a06b494bcfd.jpg)

<details>
<summary>flowchart</summary>
