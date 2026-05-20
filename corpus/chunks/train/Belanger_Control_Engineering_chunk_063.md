2.9 Chemical reactor Figure 2.24 illustrates a so-called continuous stirred tank reactor (CSTR). An aqueous solution of temperature $T_0$ , containing a material $A$ at a concentration $c_{A0}$ kg-moles/m³, flows into the reactor at a rate $F$ m³/s. A controlled quantity of heat is fed to (or taken from) the reactor, at a rate $Q$ watts. At a sufficiently high temperature, a chemical reaction, $A \to B + C$ , takes place. The reactor is well mixed, so the concentrations of $A, B$ , and $C$ are uniform over the (constant) volume $V$ of the tank. Density is assumed constant, as is the heat capacity, and the outlet flow is taken to be $F$ . Some relevant principles are as follows: (i) The reaction proceeds at a rate of $r$ kg-moles/s. (ii) In the reaction, one mole of $A$ is converted to one mole each of $B$ and $C$ . (iii) The reaction liberates heat (is exothermic) at a rate proportional to $r$ . The rate of reaction is given by $r = VAc_A e^{-E/RT}$ , where $V$ is the volume, $c_A$ is the concentration of $A$ in kilogram-moles per cubic meter, $T$ is the temperature in degrees Kelvin, and $A, E$ , and $R$ are constants. The rate of heat liberated is $\Delta Hr$ , where $\Delta H$ is a positive constant.

![](image/10d109c91b4fc9ebd068ffa2d96b8da75dc3c3dbb99a534b34e5dbe0517bfb39.jpg)

<details>
<summary>text_image</summary>

F, T₀, cₐ₀ →
cₐ, cₑ, c꜀, T → F
Q ↑
</details>

Figure 2.24 Chemical reactor

a. Derive a model for the reactor. Suggested steps are:

i. Mass balance. Let $N_{A}(t) = \text{number of kg-moles of } A$ in the reactor at time t. Between t and $t + \Delta t$ , $Fc_{A0} \Delta t$ kg-moles of A flow in, $Fc_{A} \Delta t$ kg-moles flow out, and $r \Delta t$ kg-moles are converted to B and C. Write $N_{A}(t + \Delta t)$ as $N_{A}(t) + \text{net increase of } A$ between t and $t + \Delta t$ .   
ii. Obtain a differential equation for $N_A$ . Since $c_A = N_A / V$ , obtain a differential equation for $c_A$ .   
iii. Repeat for $c_{B}$ and $c_{C}$ . Note that none of B or C flows into the tank; amounts $r \Delta t$ kg-moles of each are created during $\Delta t$ , and $Fc_{B} \Delta t(Fc_{C} \Delta t)$ kg-moles are removed.
