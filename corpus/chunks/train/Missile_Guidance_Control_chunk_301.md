# Summary

Because of the important role that proportional navigation (PN) plays in missile guidance, we will summarize here for the reader some of the most important concepts.

Intercept Geometry

Figure 4.23 will be used to summarize the concepts of proportional navigation.

Classical PN Equation (Normal Interceptor Acceleration)

$$a _ {n} = N v _ {c} \left(\frac {d \lambda}{d t}\right) \tag {4.24}$$

or

$$a _ {n} = (N / t _ {g o} ^ {2}) [ \mathbf {R} (t) + \mathbf {v} _ {m} (t) t _ {g o} ],$$

where R(t) is the missile–target range vector, and the term in brackets is the zero effort miss.

Closing Velocity

$$v _ {c} = - \frac {d R}{d t},$$

where R is the range (or distance) between interceptor missile and target $( R \cong v _ { c } t _ { g o } )$ .

![](image/3232eee7bf3ab197678c166dc52081f8be73160015af4557af38e37c405989ad.jpg)

<details>
<summary>line</summary>

| Time (sec) | Thrust (k pounds) |
| --- | --- |
| 0 | 3 |
| 5 | 6 |
| 10 | 1 |
| 15 | 0 |
</details>

(a) Thrust profile (sea level thrust variation with time)

![](image/113356eb43fdb6c0315c703813805063d864b6a0c5b365dbf123b8a59043dac1.jpg)

<details>
<summary>line</summary>

| Time (sec) | Mach no. |
| --- | --- |
| 0 | 10 |
| 20 | 30 |
| 40 | 20 |
| 60 | 15 |
| 80 | 12 |
| 100 | 10 |
</details>

(b) Velocity profile (Note: $\mathbf { M } _ { \mathrm { l a u n c h } } = M _ { T }$ h = 40,000 ft)

Fig. 4.21. MK-58 motor characteristics.   
![](image/e0bf103d71694590d42688cb045dcddca858d6b524a33cf83c093edaa53dcfc8.jpg)

<details>
<summary>text_image</summary>

Axial g's
Lateral g's
θH
θH = Heading aim angle
</details>

Fig. 4.22. Missile axial compensation diagram.

Navigation Constant, N

$$N = - N ^ {\prime} \left[ \left(\frac {d R}{d t}\right) / v _ {m} \cos (\gamma_ {m} - \lambda) \right] = N ^ {\prime} [ v _ {c} / v _ {m} \cos (\gamma_ {m} - \lambda) ]. \tag {4.32a}$$

Effective Navigation Constant, $N ^ { \prime }$

$$N ^ {\prime} = N \left[ v _ {m} \cos (\gamma_ {m} - \lambda) / \left(\frac {d R}{d t}\right) \right]. \tag {4.32b}$$

Equation of Motion

$$\frac {d y _ {m}}{d t} = v _ {m} \sin \gamma ,\frac {d ^ {2} y _ {m}}{d t ^ {2}} = N ^ {\prime} [ s / (1 + \tau s) ] [ (y _ {t} - y _ {m}) / t _ {g o} ],$$

where γ is the missile heading or attitude angle. (Note: Heading and attitude may not be the same, unless the angle of attack is neglected, that is, assumed to be zero.)

![](image/cac606c637e79bc97af0e89fd70e17a62e59144eff497288ad472b1cccc4c1f9.jpg)

<details>
<summary>text_image</summary>
