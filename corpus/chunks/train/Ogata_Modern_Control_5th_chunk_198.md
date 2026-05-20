Second-Order Systems and Transient-Response Specifications. In the following, we shall obtain the rise time, peak time, maximum overshoot, and settling time of the second-order system given by Equation (5–10). These values will be obtained in terms of $\zeta$ and $\omega _ { n }$ . The system is assumed to be underdamped.

Rise time $t _ { r }$ : Referring to Equation (5–12), we obtain the rise time $t _ { r }$ by letting $c \big ( t _ { r } \big ) = 1$ .

$$c (t _ {r}) = 1 = 1 - e ^ {- \zeta \omega_ {n} t _ {r}} \left(\cos \omega_ {d} t _ {r} + \frac {\zeta}{\sqrt {1 - \zeta^ {2}}} \sin \omega_ {d} t _ {r}\right) \tag {5-18}$$

Since $e ^ { - \zeta \omega _ { n } t _ { r } } \neq 0$ we obtain from Equation (5–18) the following equation:,

$$\cos \omega_ {d} t _ {r} + \frac {\zeta}{\sqrt {1 - \zeta^ {2}}} \sin \omega_ {d} t _ {r} = 0$$

Since $\omega _ { n } \sqrt { 1 - \zeta ^ { 2 } } = \omega _ { d }$ and $\zeta \omega _ { n } = \sigma$ , we have

$$\tan \omega_ {d} t _ {r} = - \frac {\sqrt {1 - \zeta^ {2}}}{\zeta} = - \frac {\omega_ {d}}{\sigma}$$

Thus, the rise time $t _ { r }$ is

$$t _ {r} = \frac {1}{\omega_ {d}} \tan^ {- 1} \left(\frac {\omega_ {d}}{- \sigma}\right) = \frac {\pi - \beta}{\omega_ {d}} \tag {5-19}$$

where angle $\beta$ is defined in Figure 5–9. Clearly, for a small value of $t _ { r } , \omega _ { d }$ must be large.

![](image/55c4c4c870efb93d680a3747c5f5fb8c0b32dc2a4294cdc465eb681e6c46808a.jpg)

<details>
<summary>text_image</summary>

jω
jωd
ωn√(1−ζ²)
ωn
β
-σ
0
σ
ζωn
</details>

Figure 5–9 Definition of the angle $\beta .$

Peak time $t _ { p } \colon$ Referring to Equation (5–12), we may obtain the peak time by differentiating c(t) with respect to time and letting this derivative equal zero. Since

$$
\begin{array}{l} \frac {d c}{d t} = \zeta \omega_ {n} e ^ {- \zeta \omega_ {n} t} \left(\cos \omega_ {d} t + \frac {\zeta}{\sqrt {1 - \zeta^ {2}}} \sin \omega_ {d} t\right) \\ + e ^ {- \zeta \omega_ {n} t} \left(\omega_ {d} \sin \omega_ {d} t - \frac {\zeta \omega_ {d}}{\sqrt {1 - \zeta^ {2}}} \cos \omega_ {d} t\right) \\ \end{array}
$$

and the cosine terms in this last equation cancel each other, $d c / d t ,$ , evaluated at $t = t _ { p } .$ can be simplified to

$$\left. \frac {d c}{d t} \right| _ {t = t _ {p}} = (\sin \omega_ {d} t _ {p}) \frac {\omega_ {n}}{\sqrt {1 - \zeta^ {2}}} e ^ {- \zeta \omega_ {n} t _ {p}} = 0$$

This last equation yields the following equation:

$$\sin \omega_ {d} t _ {p} = 0$$

or

$$\omega_ {d} t _ {p} = 0, \pi , 2 \pi , 3 \pi , \dots$$
