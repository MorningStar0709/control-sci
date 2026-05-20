# EXAMPLE 5–1

Consider the system shown in Figure 5–6, where $\zeta = 0 . 6$ and $\omega _ { n } = 5$ radsec. Let us obtain the rise time t , peak time $t _ { p } ,$ maximum overshoot $M _ { p } { \mathrm { : } }$ , and settling time t when the system is subjected to a unit-step input.

From the given values of $\zeta$ and $\omega _ { n }$ , we obtain $\omega _ { d } = \omega _ { n } \sqrt { 1 - \zeta ^ { 2 } } = 4 \mathrm { a n d } \sigma = \zeta \omega _ { n } = 3 .$

Rise time $t _ { r } \colon$ The rise time is

$$t _ {r} = \frac {\pi - \beta}{\omega_ {d}} = \frac {3 . 1 4 - \beta}{4}$$

where b is given by

$$\beta = \tan^ {- 1} \frac {\omega_ {d}}{\sigma} = \tan^ {- 1} \frac {4}{3} = 0. 9 3 \mathrm{rad}$$

The rise time t is thus

$$t _ {r} = \frac {3 . 1 4 - 0 . 9 3}{4} = 0. 5 5 \mathrm{sec}$$

Peak time $t _ { p } \colon$ : The peak time is

$$t _ {p} = \frac {\pi}{\omega_ {d}} = \frac {3 . 1 4}{4} = 0. 7 8 5 \mathrm{sec}$$

Maximum overshoot $M _ { p } { \mathrm { : } }$ : The maximum overshoot is

$$M _ {p} = e ^ {- (\sigma / \omega_ {d}) \pi} = e ^ {- (3 / 4) \times 3. 1 4} = 0. 0 9 5$$

The maximum percent overshoot is thus 9.5%.

Settling time t : For the 2% criterion, the settling time is

$$t _ {s} = \frac {4}{\sigma} = \frac {4}{3} = 1. 3 3 \mathrm{sec}$$

For the 5% criterion,

$$t _ {s} = \frac {3}{\sigma} = \frac {3}{3} = 1 \sec$$

Servo System with Velocity Feedback. The derivative of the output signal can be used to improve system performance. In obtaining the derivative of the output position signal, it is desirable to use a tachometer instead of physically differentiating the output signal. (Note that the differentiation amplifies noise effects. In fact, if discontinuous noises are present, differentiation amplifies the discontinuous noises more than the useful signal. For example, the output of a potentiometer is a discontinuous voltage signal because, as the potentiometer brush is moving on the windings, voltages are induced in the switchover turns and thus generate transients. The output of the potentiometer therefore should not be followed by a differentiating element.)

![](image/eae3cc3c62b4a78e0a801b6e712c2bb746662f2a1cabb90f41d2b4be58998b0f.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    R["s"] --> |+| Sum1
    Sum1 --> |+| Sum2
    Sum2 --> |K/(Js+B)| A1["1/s"]
    A1 --> C["s"]
    C --> |K_h| Sum1
    Sum1 --> |+| Sum2
    Sum2 --> |+| Sum1
```
</details>

(a)

![](image/111939dcbc96d9d633468b7d7186d6fd12acf3a7bfa0f12b41c510e534a3095e.jpg)
