# 7–12 LAG COMPENSATION

In this section we first discuss the Nyquist plot and Bode diagram of the lag compensator. Then we present lag compensation techniques based on the frequency-response approach.

Characteristics of Lag Compensators. Consider a lag compensator having the following transfer function:

$$G _ {c} (s) = K _ {c} \beta \frac {T s + 1}{\beta T s + 1} = K _ {c} \frac {s + \frac {1}{T}}{s + \frac {1}{\beta T}} \quad (\beta > 1)$$

Figure 7–101 Polar plot of a lag compensator $K _ { c } \beta ( j \omega T + 1 ) / ( j \omega \beta T + 1 ) .$ .   
![](image/afe7b2d06faac883b689127cd3e5d557256e98b9fba1640f551d95c0c553c4c5.jpg)

<details>
<summary>text_image</summary>

Im
Kc
ω = ∞
Kcβ
0
Re
ω = 0
</details>

Figure 7–102 Bode diagram of a lag compensator $\beta ( j \omega T + 1 ) / ( j \omega \beta T + 1 ) .$ with b=10.   
![](image/f236794150be6ae528e7d725817f6d0ee5818c86ec37782b4acedd00ddd47f8d.jpg)

<details>
<summary>line</summary>

| ω in rad/sec | dB |
| --- | --- |
| 0.01/T | 0° |
| 0.1/T | 20° |
| 1/T | 0° |
| 10/T | 0° |
</details>

In the complex plane, a lag compensator has a zero at $s = - 1 / T$ and a pole at $s = - 1 / ( \beta T )$ . The pole is located to the right of the zero.

Figure 7–101 shows a polar plot of the lag compensator. Figure 7–102 shows a Bode diagram of the compensator, where $K _ { c } = 1$ and $\beta = 1 0$ . The corner frequencies of the lag compensator are at $\omega = 1 / T$ and $\omega = 1 / ( \beta T )$ . As seen from Figure 7–102, where the values of $K _ { c }$ and $\beta$ are set equal to 1 and 10, respectively, the magnitude of the lag compensator becomes 10 (or 20 dB) at low frequencies and unity (or 0 dB) at high frequencies. Thus, the lag compensator is essentially a low-pass filter.

Lag Compensation Techniques Based on the Frequency-Response Approach. The primary function of a lag compensator is to provide attenuation in the highfrequency range to give a system sufficient phase margin. The phase-lag characteristic is of no consequence in lag compensation.

The procedure for designing lag compensators for the system shown in Figure 7–93 by the frequency-response approach may be stated as follows:

1. Assume the following lag compensator:

$$G _ {c} (s) = K _ {c} \beta \frac {T s + 1}{\beta T s + 1} = K _ {c} \frac {s + \frac {1}{T}}{s + \frac {1}{\beta T}} \quad (\beta > 1)$$

Define

$$K _ {c} \beta = K$$

Then

$$G _ {c} (s) = K \frac {T s + 1}{\beta T s + 1}$$

The open-loop transfer function of the compensated system is
