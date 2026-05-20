Figure 7–1 Stable, linear, timeinvariant system.   
![](image/515fa231c820cb43ebfdc39c4da000a0172c47141326fd789655817295e983ba.jpg)

where a and the $b _ { i }$ (where $i = 1 , 2 , \ldots , n )$ are constants and $\bar { a }$ is the complex conjugate of $a .$ The inverse Laplace transform of Equation (7–2) gives

$$y (t) = a e ^ {- j \omega t} + \bar {a} e ^ {j \omega t} + b _ {1} e ^ {- s _ {1} t} + b _ {2} e ^ {- s _ {2} t} + \dots + b _ {n} e ^ {- s _ {n} t} \quad (t \geq 0) \tag {7-3}$$

For a stable system, $- s _ { 1 } , - s _ { 2 } , \ldots , - s _ { n }$ have negative real parts.Therefore, as t approaches infinity, the terms $e ^ { - s _ { 1 } t } , e ^ { - s _ { 2 } t } , \ldots ,$ and, $e ^ { - s _ { n } t }$ approach zero.Thus, all the terms on the righthand side of Equation $( 7 - 3 )$ , except the first two, drop out at steady state.

If $Y ( s )$ involves multiple poles $s _ { j }$ of multiplicity $m _ { j }$ , then $y ( t )$ will involve terms such as $t ^ { h _ { j } } e ^ { - s _ { j } i } \left( h _ { j } = 0 , 1 , 2 , \dots , \dots 1 \right)$ For a stable system, the terms. $t ^ { h _ { j } } e ^ { - s _ { j } t }$ approach zero as t approaches infinity.

Thus, regardless of whether the system is of the distinct-pole type or multiple-pole type, the steady-state response becomes

$$y _ {\mathrm{ss}} (t) = a e ^ {- j \omega t} + \bar {a} e ^ {j \omega t} \tag {7-4}$$

where the constant a can be evaluated from Equation (7–2) as follows:

$$a = G (s) \frac {\omega X}{s ^ {2} + \omega^ {2}} (s + j \omega) \Bigg | _ {s = - j \omega} = - \frac {X G (- j \omega)}{2 j}$$

Note that

$$\bar {a} = G (s) \frac {\omega X}{s ^ {2} + \omega^ {2}} (s - j \omega) \Bigg | _ {s = j \omega} = \frac {X G (j \omega)}{2 j}$$

Since $G ( j \omega )$ is a complex quantity, it can be written in the following form:

$$G (j \omega) = | G (j \omega) | e ^ {j \phi}$$

where $\left| G ( j \omega ) \right|$ @ represents the magnitude and $\phi$ represents the angle of $G ( j \omega )$ ; that is,

$$\phi = \underline {{G (j \omega)}} = \tan^ {- 1} \left[ \frac {\text { imaginary part of } G (j \omega)}{\text { real part of } G (j \omega)} \right]$$

The angle $\phi$ may be negative, positive, or zero. Similarly, we obtain the following expression for $G ( - j \omega )$ :

$$G (- j \omega) = | G (- j \omega) | e ^ {- j \phi} = | G (j \omega) | e ^ {- j \phi}$$

Then, noting that

$$a = - \frac {X | G (j \omega) | e ^ {- j \phi}}{2 j}, \quad \bar {a} = \frac {X | G (j \omega) | e ^ {j \phi}}{2 j}$$

Equation (7–4) can be written
