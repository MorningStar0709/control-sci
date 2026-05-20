# Kirchhoff’s Voltage Law

Kirchhoff’s voltage (or “loop”) law states that the algebraic sum of all voltages across the elements for any closed path (loop) is equal to zero. Figure 3.5 shows a circuit that consists of a single loop with voltage source $e _ { \mathrm { i n } } ( t )$ and three passive elements. These three elements can be any combination of resistors, capacitors, or inductors. The positive current flow I is shown in the figure, where current flows through each passive element from the positive terminal to the negative terminal. The convention is to assign a negative sign for a “voltage drop” (moving with the current across a passive element, or moving from + to – across an active voltage source) and a positive sign for a “voltage rise” (moving against the current across a passive element, or moving from – to + across a voltage source). Summing the voltages in the loop (moving with the current in a clockwise direction) results in

$$\text { Clockwise: } \quad - e _ {1} - e _ {2} - e _ {3} + e _ {\text { in }} (t) = 0 \tag {3.13}$$

![](image/200cb6a3cd149e6b1bc24a41947c944c5f5da46514a6a6d9873c2d1d9afebfed.jpg)

<details>
<summary>text_image</summary>

+
e₁
-
Element 1
I
eᵢₙ(t)
+
-
Element 2
+
e₂
-
-
e₃
+
Element 3
</details>

Figure 3.5 Example of Kirchhoff’s voltage (loop) law.

Of course, we could sum voltages around the loop moving in a counterclockwise (against the current) direction

$$\text { Counterclockwise: } \quad - e _ {\text { in }} (t) + e _ {3} + e _ {2} + e _ {1} = 0 \tag {3.14}$$

which yields the same algebraic result as Eq. (3.13).
