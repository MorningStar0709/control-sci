We shall first give detailed discussions of the principle by which proportional controllers operate. Then we shall treat methods for obtaining derivative and integral control actions. Throughout the discussions, we shall place emphasis on the fundamental principles, rather than on the details of the operation of the actual mechanisms.

Pneumatic Systems. The past decades have seen a great development in lowpressure pneumatic controllers for industrial control systems, and today they are used extensively in industrial processes. Reasons for their broad appeal include an explosionproof character, simplicity, and ease of maintenance.

Resistance and Capacitance of Pressure Systems. Many industrial processes and pneumatic controllers involve the flow of a gas or air through connected pipelines and pressure vessels.

Consider the pressure system shown in Figure 4–4(a). The gas flow through the restriction is a function of the gas pressure difference $p _ { i } - p _ { o }$ . Such a pressure system may be characterized in terms of a resistance and a capacitance.

The gas flow resistance R may be defined as follows:

$$R = \frac {\text { change in gas pressure difference, lb } _ {\mathrm{f}} / \mathrm{ft} ^ {2}}{\text { change in gas flow rate, lb / sec }}$$

or

$$R = \frac {d (\Delta P)}{d q} \tag {4-8}$$

where is a small change in the gas pressure difference and dq is a small changed(¢P) in the gas flow rate. Computation of the value of the gas flow resistance R may be quite time consuming. Experimentally, however, it can be easily determined from a plot of the pressure difference versus flow rate by calculating the slope of the curve at a given operating condition, as shown in Figure 4–4(b).

The capacitance of the pressure vessel may be defined by

$$C = \frac {\text { change in gas stored, lb }}{\text { change in gas pressure, lb } _ {\mathrm{f}} / \mathrm{ft} ^ {2}}$$

or

$$C = \frac {d m}{d p} = V \frac {d \rho}{d p} \tag {4-9}$$

Figure 4–4 (a) Schematic diagram of a pressure system; (b) pressuredifference-versusflow-rate curve.   
![](image/49a3e27af6dc87d097bd0dc52fd0392caa3af058a100a6ecafb2bb463425e94b.jpg)

<details>
<summary>text_image</summary>

Resistance
R
q
P̄ + p₀
P̄ + pᵢ
Capacitance
C
</details>

(a)

![](image/fd814a926308a9cf8462b7d7ed7c26ba80672702e96d6066ffd2f41f1a584549.jpg)

<details>
<summary>line</summary>

| q | ΔP |
| --- | --- |
| 0 | 0 |
| >0 | >R |
</details>

(b)
