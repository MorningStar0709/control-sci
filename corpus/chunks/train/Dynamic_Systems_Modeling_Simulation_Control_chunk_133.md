# Electrostatic Microactuator

Motors and solenoid actuators are driven by the current–magnetism interaction that is governed by Faraday’s laws. However, for tiny devices at the microscale, there is no room for coils and electromagnetic induction [3]. Microelectromechanical systems (MEMS) often use electrostatic forces for actuation, and applications include surgical microgrippers and optical microshutters [3–5]. The electrostatic driving force is the electrical force of repulsion or attraction between charged particles.

Figure 3.25 shows a MEMS device commonly known as a comb-drive actuator [3–5]. Comb-drive actuators consist of two interlocking “finger” structures that have the appearance of two intertwined combs. The interlocking fingers are misaligned parallel plates that act as a series of capacitors where the movable drive and stationary closure plates carry opposite charges. An input voltage $e _ { \mathrm { i n } } ( t )$ is applied to the comb structure that establishes the electrostatic force that attempts to realign the parallel plates of the interconnected comb. Hence, the electrostatic force attracts the drive arm toward the stationary closure arm. Movement of the comb structure could actuate the extension arms of a microgripper device. Deflections for these MEMS devices are on the order of microns, where $1 \mu \mathrm { m } = 1 0 ^ { - 6 }$ m. A stiffness element (modeled by spring constant k) is used to retract the drive arm when the electrostatic force is removed.

Figure 3.26 shows a schematic diagram for a comb-drive actuator where the intertwined parallel plates are replaced by a lumped capacitor C(x). The comb circuit consists of the voltage source $e _ { \mathrm { i n } } ( t )$ , comb capacitance C(x), and resistance R. A single lumped mass m represents the movable drive-comb structure that experiences stiffness and friction forces modeled by kx and bẋ , respectively. Charging the misaligned parallel plates of the comb produces an electrostatic force $F _ { \mathrm { e s } }$ that pulls the drive arm to the left in order to realign the plates.

The equivalent capacitance of the comb is

$$C (x) = \frac {n \varepsilon_ {0} A}{d} = \frac {n \varepsilon_ {0} (x _ {0} + x) w}{d} \tag {3.105}$$

![](image/72ca81426c1d9644b7afaf3f3103d078913b5dc5377a3e55a1cc1ff19840c72e.jpg)

<details>
<summary>text_image</summary>

Microgripper
Drive arm
Closure arm
e_in(t)
+
-
I
k
b
</details>
