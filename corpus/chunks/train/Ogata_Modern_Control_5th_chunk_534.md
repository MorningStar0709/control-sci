instantaneously transfer energy from the input to the output. In addition, since noise is almost always present in one form or another, a system with a unity transfer function is not desirable. A desired control system, in many practical cases, may have one set of dominant complex-conjugate closed-loop poles with a reasonable damping ratio and undamped natural frequency. The determination of the significant part of the closed-loop pole-zero configuration, such as the location of the dominant closed-loop poles, is based on the specifications that give the required system performance.

Cancellation of Undesirable Complex-Conjugate Poles. If the transfer function of a plant contains one or more pairs of complex-conjugate poles, then a lead, lag, or lag–lead compensator may not give satisfactory results. In such a case, a network that has two zeros and two poles may prove to be useful. If the zeros are chosen so as to cancel the undesirable complex-conjugate poles of the plant, then we can essentially replace the undesirable poles by acceptable poles. That is, if the undesirable complexconjugate poles are in the left-half s plane and are in the form

$$\frac {1}{s ^ {2} + 2 \zeta_ {1} \omega_ {1} s + \omega_ {1} ^ {2}}$$

then the insertion of a compensating network having the transfer function

$$\frac {s ^ {2} + 2 \zeta_ {1} \omega_ {1} s + \omega_ {1} ^ {2}}{s ^ {2} + 2 \zeta_ {2} \omega_ {2} s + \omega_ {2} ^ {2}}$$

will result in an effective change of the undesirable complex-conjugate poles to acceptable poles. Note that even though the cancellation may not be exact, the compensated system will exhibit better response characteristics. (As stated earlier, this approach cannot be used if the undesirable complex-conjugate poles are in the righthalf s plane.)

Familiar networks consisting only of RC components whose transfer functions possess two zeros and two poles are the bridged-T networks. Examples of bridged-T networks and their transfer functions are shown in Figure 7–117. (The derivations of the transfer functions of the bridged-T networks were given in Problem A–3–5.)

![](image/042ca4ad58d5d8e479501c6c7f59d1752595b12654e2c9537c226d312d378f16.jpg)

<details>
<summary>chemical</summary>

Electrical circuit diagram with resistors and capacitors, showing equivalent resistance formula for RC components
</details>

(a)
