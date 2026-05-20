$$\frac {\omega_ {1}}{\omega_ {3}} = \frac {\omega_ {3}}{\omega_ {2}}$$

On the Bode diagram,

$$\log \omega_ {1} - \log \omega_ {3} = \log \omega_ {3} - \log \omega_ {2}$$

Thus, the $\omega _ { 3 }$ point is just midway between the $\omega _ { 2 }$ and $\omega _ { 1 }$ points. The damping ratio $\zeta$ of the system is then

$$\zeta = \frac {F}{2 \sqrt {K J}} = \frac {\omega_ {2}}{2 \omega_ {3}}$$

Determination of Static Acceleration Error Constants. Consider the unityfeedback control system shown in Figure 7–16. Figure 7–19 shows an example of the log-magnitude plot of a type 2 system. The intersection of the initial –40-dBdecade segment (or its extension) with the v=1 line has the magnitude of 20 log $K _ { a }$ . Since at low frequencies

$$G (j \omega) = \frac {K _ {a}}{(j \omega) ^ {2}}, \quad \text { for } \omega \ll 1$$

it follows that

$$2 0 \log \left| \frac {K _ {a}}{(j \omega) ^ {2}} \right| _ {\omega = 1} = 2 0 \log K _ {a}$$

![](image/b500f7d5cf06485a6e3d1852c43a29977d9101670acae458f10e2320b642b20c.jpg)

<details>
<summary>line</summary>

| ω in log scale | dB |
| --- | --- |
| 0 | -40 dB/decade |
| 20 log Ka | -60 dB/decade |
| ωₐ = √(Kₐ) | 0 |
| ω = 1 | 0 |
</details>

Figure 7–19 Log-magnitude curve of a type 2 system.

The frequency $\omega _ { a }$ at the intersection of the initial –40-dBdecade segment (or its extension) with the 0-dB line gives the square root of $K _ { a }$ numerically. This can be seen from the following:

$$2 0 \log \left| \frac {K _ {a}}{\left(j \omega_ {a}\right) ^ {2}} \right| = 2 0 \log 1 = 0$$

which yields

$$\omega_ {a} = \sqrt {K _ {a}}$$

Plotting Bode Diagrams with MATLAB. The command bode computes magnitudes and phase angles of the frequency response of continuous-time, linear, timeinvariant systems.

When the command bode (without left-hand arguments) is entered in the computer, MATLAB produces a Bode plot on the screen. Most commonly used bode commands are

```txt
bode(num,den)
bode(num,den,w)
bode(A,B,C,D)
bode(A,B,C,D,w)
bode(A,B,C,D,iu,w)
bode(sys) 
```

When invoked with left-hand arguments, such as

$$[ \text { mag }, \text { phase }, w ] = \text { bode } (\text { num }, \text { den }, w)$$
