# 11.3 SOLENOID ACTUATOR–VALVE SYSTEM

The second case study involves the analysis and design of a solenoid actuator that is often used to position valves for metering flow [3, 4]. The basic principles of a solenoid have been described and analyzed in Chapters 2, 3, 5, and 6. Figure 11.13 shows the electromechanical system, which consists of a solenoid coil, an armature mass (plunger), a spool valve, and a return spring. When current flows through the coil, the resulting electromagnetic force pulls the plunger (to the right) toward the center of the coil, which pushes on the spool valve in order to properly meter hydraulic fluid flow. When the voltage source is switched off and current is dissipated, the electromagnetic force goes to zero and the compressed spring returns the armature to the seated position.

Our objective is to determine the solenoid system parameters that minimize the settling time for the armature–valve mass to reach a displacement of 2 mm. We will modify our integrated Simulink model for the solenoid actuator that was developed in Chapter 6 and include physical models for the electrical inductance and electromagnetic force of the solenoid coil.

![](image/d34fc30d3c6836eb676dc08e71e96eb572777331d73413d2818bfe1dcd7a5093.jpg)

<details>
<summary>text_image</summary>

Seated position
Coil
Air gap
Supply pressure
Spool valve
Drain
Return spring
Electrical input
Armature (plunger)
Push rod
Fluid flow
</details>

Figure 11.13 Solenoid actuator–valve system.
