$$G (j \omega) = \frac {K (T _ {a} j \omega + 1) (T _ {b} j \omega + 1) \cdots (T _ {m} j \omega + 1)}{(j \omega) ^ {N} (T _ {1} j \omega + 1) (T _ {2} j \omega + 1) \cdots (T _ {p} j \omega + 1)}$$

Figure 7–17 shows an example of the log-magnitude plot of a type 0 system. In such a system, the magnitude of $G ( j \omega )$ equals $K _ { p }$ at low frequencies, or

$$\lim _ {\omega \to 0} G (j \omega) = K = K _ {p}$$

It follows that the low-frequency asymptote is a horizontal line at 20 log $K _ { p }$ dB.

Figure 7–16 Unity-feedback control system.   
![](image/7c0ab3e1a12292dd064295c368c0ce92e7d07d453c9a20abecf295bf238a2b89.jpg)

<details>
<summary>line</summary>

| Parameter | Value |
| --- | --- |
| Frequency ω | -20 log Kp |
| Frequency ω | -40 dB/decade |
| Frequency ω | 20 log Kp |
</details>

Figure 7–17 Log-magnitude curve of a type 0 system.

Determination of Static Velocity Error Constants. Consider the unity-feedback control system shown in Figure 7–16. Figure 7–18 shows an example of the log-magnitude plot of a type 1 system. The intersection of the initial –20-dBdecade segment (or its extension) with the line $\omega = 1$ has the magnitude 20 log $K _ { v } .$ . This may be seen as follows: In a type 1 system

$$G (j \omega) = \frac {K _ {v}}{j \omega}, \quad \text { for } \omega \ll 1$$

Thus,

$$2 0 \log \left| \frac {K _ {v}}{j \omega} \right| _ {\omega = 1} = 2 0 \log K _ {v}$$

The intersection of the initial –20-dBdecade segment (or its extension) with the 0-dB line has a frequency numerically equal to $K _ { v } .$ . To see this, define the frequency at this intersection to be $\omega _ { 1 } ;$ ; then

$$\left| \frac {K _ {v}}{j \omega_ {1}} \right| = 1$$

or

$$K _ {v} = \omega_ {1}$$

As an example, consider the type 1 system with unity feedback whose open-loop transfer function is

$$G (s) = \frac {K}{s (J s + F)}$$

If we define the corner frequency to be $\omega _ { 2 }$ and the frequency at the intersection of the –40-dBdecade segment (or its extension) with 0-dB line to be $\omega _ { 3 }$ , then

$$\omega_ {2} = \frac {F}{J}, \quad \omega_ {3} ^ {2} = \frac {K}{J}$$

![](image/e9b8a3f35344454c9064be5cb471be1ba01134e57595e76645d5155fe8636c75.jpg)

<details>
<summary>line</summary>

| ω in log scale | Frequency (dB) |
| --- | --- |
| ω₂ | -20 |
| ω₃ | 20 log Kᵥ |
| ω₁ | 0 |
| ω = 1 | -40 |
</details>

Figure 7–18 Log-magnitude curve of a type 1 system.

Since

$$\omega_ {1} = K _ {v} = \frac {K}{F}$$

it follows that

$$\omega_ {1} \omega_ {2} = \omega_ {3} ^ {2}$$

or
