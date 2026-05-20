# 11.6 FEEDBACK CONTROL OF A MAGNETIC LEVITATION SYSTEM

Our fifth and last case study involves a feedback control system design for a magnetic levitation (“maglev”) system. Maglev systems are used to suspend and propel trains without contact with a rail. Magnetic levitation is also used to support rotating bearings for high-performance machines in order to eliminate friction and the need for lubrication [9]. A laboratory experiment demonstrating magnetic levitation is shown in Fig. 11.49 (see also Problems 3.33 and 5.34). Passing a current through the coil produces an electromagnet that provides an attraction force on the metal ball. The electromagnetic force balances the gravity force at steady state. The constant d in Fig. 11.49 is the nominal air gap between the electromagnet tip and the ball for a nominal electromagnetic force. Ball displacement z is measured positive upward from a fixed static equilibrium position that corresponds to the nominal electromagnetic force, and consequently $d - z$ is the air gap between the ball and the electromagnet. Our goal is to design a control system for the coil circuit so that the ball can be held in static equilibrium at a desired reference position; or, moved from one position to another position.

![](image/f969b1788c341fb2e7eeea98172d61852152a70cbda31878a6c49d2a974961fa.jpg)

<details>
<summary>text_image</summary>

Electromagnet
Coil, L
R
e_in(t)
+
-
Nominal air gap, d
(for z = 0)
Metal ball, m
z
</details>

Figure 11.49 Magnetic levitation system.
