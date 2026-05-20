Note that the third closed-loop pole of the designed system is found by dividing the characteristic equation by the known factors as follows:

$$s ^ {3} + 5. 6 4 6 s ^ {2} + 1 6. 9 3 3 s + 2 3. 8 7 5 = (s + 1. 5 + j 2. 5 9 8 1) (s + 1. 5 - j 2. 5 9 8 1) (s + 2. 6 5)$$

The foregoing compensation method enables us to place the dominant closed-loop poles at the desired points in the complex plane. The third pole at $s = - 2 . 6 5$ is fairly close to the added zero at 1.9432. Therefore, the effect of this pole on the transient response is relatively small. Since no restriction has been imposed on the nondominant pole and no specification has been given concerning the value of the static velocity error coefficient, we conclude that the present design is satisfactory.

Method 2. If we choose the zero of the lead compensator at s = 1 so that it will cancel the plant pole at $s = - 1$ , then the compensator pole must be located at s = 3. (See Figure 6–44.) Hence the lead compensator becomes

$$G _ {c} (s) = K _ {c} \frac {s + 1}{s + 3}$$

The value of $K _ { c }$ can be determined by use of the magnitude condition.

$$\left| K _ {c} \frac {s + 1}{s + 3} \frac {1 0}{s (s + 1)} \right| _ {s = - 1. 5 + j 2. 5 9 8 1} = 1$$

Figure 6–44 Compensator pole and zero.   
![](image/e4b79ee353df025a782ff828034926997a6eee7d61b999e86b821ad838b621db.jpg)

<details>
<summary>text_image</summary>

Desired
closed-loop pole
Compensator
pole
60°
Compensator
zero
jω
j3
j2
j1
j1
120°
-4
-3
-2
-1
σ
-j1
-j2
</details>

or

$$K _ {c} = \left| \frac {s (s + 3)}{1 0} \right| _ {s = - 1. 5 + j 2. 5 9 8 1} = 0. 9$$

Hence

$$G _ {c} (s) = 0. 9 \frac {s + 1}{s + 3}$$

The open-loop transfer function of the designed system then becomes

$$G _ {c} (s) G (s) = 0. 9 \frac {s + 1}{s + 3} \frac {1 0}{s (s + 1)} = \frac {9}{s (s + 3)}$$

The closed-loop transfer function of the compensated system becomes

$$\frac {C (s)}{R (s)} = \frac {9}{s ^ {2} + 3 s + 9}$$

Note that in the present case the zero of the lead compensator will cancel a pole of the plant, resulting in the second-order system, rather than the third-order system as we designed using Method 1.

The static velocity error constant for the present case is obtained as follows:

$$
\begin{array}{l} K _ {v} = \lim _ {s \rightarrow 0} s G _ {c} (s) G (s) \\ = \lim _ {s \rightarrow 0} s \left[ \frac {9}{s (s + 3)} \right] = 3 \\ \end{array}
$$
