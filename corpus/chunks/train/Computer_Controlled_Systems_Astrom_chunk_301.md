$$u = \frac {A ^ {+}}{B ^ {+}} \left(\frac {\bar {T}}{\bar {R}} u _ {c} - \frac {\bar {S}}{\bar {R}} y\right)$$

This means that we simply cancel the poles and zeros of the process and design a controller for the reduced system as if the canceled poles were not present. Because $T = t_{0}A_{o}$ , the pulse-transfer function from the command signal to process output is

$$\frac {B T}{A _ {c l}} = \frac {t _ {0} B ^ {+} B ^ {-} A _ {o}}{A _ {c} A _ {o}} = \frac {t _ {0} B ^ {-}}{\bar {A} _ {c}}$$

The canceled factors must correspond to stable modes. If this is not the case the system will have unstable modes that are unreachable or unobservable. In practice it is useful to have more stringent requirements on allowable cancellations. Sometimes cancellation may not be desirable at all. In other cases it may be reasonable to cancel zeros that are sufficiently well damped. One way to express this formally is to introduce a region D in the complex plane that corresponds to modes with sufficient relative and absolute damping. Only zeros inside D may be canceled. An example of a region is shown in Fig. 5.1. From Sec. 2.8 we saw that lines with constant relative damping are logarithmic spirals in the z-plane and that lines with constant absolute damping are circles.

![](image/9c1051f33674f5a0bff463494456769c42258fd22f4d20ed641032cba77ac310.jpg)

<details>
<summary>text_image</summary>

Im
D
1
Re
</details>

Figure 5.1 A region D such that points in the region have a minimum relative damping and a minimum absolute damping.
