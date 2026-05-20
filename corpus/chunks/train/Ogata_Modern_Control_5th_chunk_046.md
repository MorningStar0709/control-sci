Consider the liquid-level control system shown in Figure 2–8(a), where the electromagnetic valve shown in Figure 2–8(b) is used for controlling the inflow rate.This valve is either open or closed.With this two-position control, the water inflow rate is either a positive constant or zero. As shown in Figure 2–9, the output signal continuously moves between the two limits required to cause the actuating element to move from one fixed position to the other. Notice that the output curve follows one of two exponential curves, one corresponding to the filling curve and the other to the emptying curve. Such output oscillation between two limits is a typical response characteristic of a system under two-position control.

Figure 2–8 (a) Liquid-level control system; (b) electromagnetic valve.   
![](image/eac59cc1b0141426c395b1e4c76d9851f284cb678b0f7faa2e12f214b1bc838e.jpg)

<details>
<summary>text_image</summary>

q_i
115 V
Float
C
h
R
</details>

(a)

![](image/c884df1b24aa531014d27fac0945a1e29cd1ac1ac7d1a1f505ff2d9ac6ac149b.jpg)

<details>
<summary>text_image</summary>

Movable iron core
Magnetic coil
</details>

![](image/3b07f9f0e27287cb7259f4838c8ba2ddab7f058cf569727f9013be2cdf6fcd6f.jpg)

<details>
<summary>line</summary>

| t | h(t) |
| --- | --- |
| 0 | 0 |
| Peak | High |
| Low | Low |
</details>

Figure 2–9 Level h(t)-versus-t curve for the system shown in Figure 2–8(a).

From Figure 2–9, we notice that the amplitude of the output oscillation can be reduced by decreasing the differential gap. The decrease in the differential gap, however, increases the number of on–off switchings per minute and reduces the useful life of the component. The magnitude of the differential gap must be determined from such considerations as the accuracy required and the life of the component.

Proportional Control Action. For a controller with proportional control action, the relationship between the output of the controller $u ( t )$ and the actuating error signal $e ( t )$ is

$$u (t) = K _ {p} e (t)$$

or, in Laplace-transformed quantities,

$$\frac {U (s)}{E (s)} = K _ {p}$$

where $K _ { p }$ is termed the proportional gain.

Whatever the actual mechanism may be and whatever the form of the operating power, the proportional controller is essentially an amplifier with an adjustable gain.
