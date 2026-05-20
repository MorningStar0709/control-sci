One free gain parameter in each of the two inner loops is then calculated. A specification on the dominant break frequency $\omega _ { 1 }$ , obtained from analyses of miss distance and attitude-loop stability, is then used to calculate a free gain parameter of the accelerometer loop. Finally, as a check, the coefficients $b _ { 1 } , b _ { 2 }$ , and $b _ { 3 }$ are then calculated, and the cubic polynomial is factored in order to check the autopilot poles. The design method discussed above achieves the required dominant break frequency ω1 and maximizes $\omega _ { 2 }$ and $\zeta _ { 2 }$ within stability constraints.

As discussed earlier, each autopilot must have feedback from an accelerometer. The rate-damping loop must have a wide bandwidth for damping the poles of the airframe, while the synthetic stability loop stabilizes the poles of an unstable bare frame. In reference to Figure 3.36, some other useful transfer functions are as follows:

![](image/fdc763c0bb094b13909e24b81783e0e9e35153b6b4da8ee4a64a180bdf855fe7.jpg)

<details>
<summary>line</summary>

| Mach number | Band 1 Altitude | Band 2 Altitude | Band 3 Altitude |
| --- | --- | --- | --- |
| Constant Mδ | Low | High | Medium |
| Constant Mδ | High | Medium | High |
</details>

Fig. 3.37. Curves of constant $M _ { \delta }$ for band-switching of autopilot gains.

$$G _ {1} = A _ {L} / \delta = K _ {1} (1 + a _ {1 1} s + a _ {1 2} s ^ {2}) / (1 + b _ {1 1} s + b _ {1 2} s ^ {2}),G _ {1} \cong G _ {2},G _ {3} = (1 / \delta) [ K _ {3} (1 + A _ {3 1} s) ] / (1 + b _ {1 1} s + b _ {1 2} s ^ {2})\cong M _ {\delta} [ s + (1 / A _ {3 1}) ] / [ s ^ {2} + (b _ {1 1} / b _ {1 2}) s - M _ {\alpha} ].$$

(Note that $A _ { 3 1 } \equiv \tau$ as in $\tau = \alpha / \dot { \gamma } )$ .

Figure 3.37 shows the typical contours of constant $M _ { \delta }$ for band-switching on the plane of altitude versus Mach number for a hypothetical missile. As a final step in the design process, the effects of high-frequency structural modes on autopilot stability are checked by a digital computer frequency-response program. It should be pointed out that the autopilot can tolerate some bare-airframe instability (i.e., some maximum positive value of $M _ { \alpha } )$ . This parameter $M _ { \alpha }$ tends to be most troublesome at sea level (i.e., low altitude and corresponding low angles of attack) and maximum Mach number.
