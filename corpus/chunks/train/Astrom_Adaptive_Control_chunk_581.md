# EXAMPLE 9.7 Titration curve for a strong acid-base pair

Consider neutralization of $m_{A}$ mol of hydrochloric acid HCl by $m_{B}$ mol of sodium hydroxide NaOH in a water solution. The following reaction takes place:

$$\mathrm{HCl} + \mathrm{NaOH} \rightarrow \mathrm{H} ^ {+} + \mathrm{OH} ^ {-} + \mathrm{Na} ^ {+} + \mathrm{Cl} ^ {-}$$

Let the total volume be V. The concentration of chloride ions is then

$$[ \mathrm{Cl} ^ {-} ] = x _ {A} = m _ {A} / V$$

and the concentration of sodium ions is given by

$$\left[ \mathrm{Na} ^ {+} \right] = x _ {B} = m _ {B} / V$$

because the acid and the base are completely ionized. Since the number of positive ions equals the number of negative ions, it follows that

$$x _ {A} + \left[ \mathrm{OH} ^ {-} \right] = x _ {B} + \left[ \mathrm{H} ^ {-} \right]$$

The concentration of hydroxyl ions can be related to the hydrogen ion concentration by Eq. (9.17). Hence

$$x = x _ {B} - x _ {A} = \left[ \mathrm{OH} ^ {-} \right] - \left[ \mathrm{H} ^ {+} \right] = \frac {K _ {w}}{\left[ \mathrm{H} ^ {+} \right]} - \left[ \mathrm{H} ^ {+} \right] = 1 0 ^ {\mathrm{pH} - 1 4} - 1 0 ^ {- \mathrm{pH}} \tag {9.18}$$

Solving for $[H^{+}]$ gives

$$\left[ \mathrm{H} ^ {+} \right] = \sqrt {x ^ {2} / 4 + K _ {w}} - x / 2\left[ \mathrm{OH} ^ {-} \right] = \sqrt {x ^ {2} / 4 + K _ {w}} + x / 2$$

This gives

$$\mathrm{pH} = f (x) = - \log \left(\sqrt {x ^ {2} / 4 + K _ {w}} - x / 2\right) \tag {9.19}$$

![](image/0f96135e51e83daba3e01bdf4c5be7ff7dbd9aa1db35b4ecc5e249a47e410dd9.jpg)

<details>
<summary>line</summary>

| x | f(x) |
| --- | --- |
| -1·10⁻³ | 3.0 |
| -5·10⁻⁴ | 3.0 |
| 0 | 9.0 |
| 5·10⁻⁴ | 10.0 |
| 1·10⁻³ | 10.0 |
</details>

Figure 9.9 Titration curve of Eq. (9.19) for neutralization of a 0.001 M solution of HCl with a 0.001 M solution of NaOH.

The graph of the function $f$ is called the titration curve. It is the fundamental nonlinearity for the neutralization problem. An example of the titration curve is shown in Fig. 9.9, which shows that there is considerable variation in the slope of the titration curve. The abscissa of the titration curve in Fig. 9.9 is given in terms of the concentration difference $x_B - x_A$ . The $x$ -axis can also be recalibrated into the amount of the reagent.

The derivative of the function f is given by

$$f ^ {\prime} (x) = \frac {1 0 \log e}{2 \sqrt {x ^ {2} / 4 + K _ {w}}} = \frac {1 0 \log e}{1 0 \mathrm{pH} ^ {- 1 4} + 1 0 - \mathrm{pH}} \tag {9.20}$$
