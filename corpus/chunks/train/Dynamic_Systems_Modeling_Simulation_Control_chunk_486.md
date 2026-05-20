<table><tr><td>Input Frequency, ω (rad/s)</td><td>Magnitude |G(jω)|</td><td>Magnitude |G(jω)|dB (dB)</td><td>Phase ∠G(jω)</td></tr><tr><td>0.1</td><td>1.4995</td><td>3.52</td><td>-1.43°</td></tr><tr><td>0.5</td><td>1.4884</td><td>3.45</td><td>-7.13°</td></tr><tr><td>1</td><td>1.4552</td><td>3.26</td><td>-14.04°</td></tr><tr><td>2</td><td>1.3416</td><td>2.55</td><td>-26.57°</td></tr><tr><td>4</td><td>1.0607</td><td>0.51</td><td>-45.00°</td></tr><tr><td>10</td><td>0.5571</td><td>-5.08</td><td>-68.20°</td></tr><tr><td>20</td><td>0.2942</td><td>-10.63</td><td>-78.69°</td></tr><tr><td>50</td><td>0.1196</td><td>-18.44</td><td>-85.43°</td></tr><tr><td>100</td><td>0.0600</td><td>-24.44</td><td>-87.70°</td></tr></table>

![](image/6a514d46ae29ffe80a3367e3bf773eaa6c713f6c1c2fd91597fa755270c52a46.jpg)

<details>
<summary>line</summary>

| Frequency, ω, rad/s | Magnitude of G(jω), dB |
| --- | --- |
| 0.1 | 3.0 |
| 0.3 | 3.0 |
| 1.0 | 3.0 |
| 2.0 | 2.0 |
| 5.0 | 0.0 |
| 10.0 | -5.0 |
| 20.0 | -10.0 |
| 50.0 | -18.0 |
| 100.0 | -25.0 |
</details>

![](image/38054fad766ae27fb90b2a0d64b7cb3c43cd532286759cd14e9f694a0e6ffdb7.jpg)

<details>
<summary>line</summary>

| Frequency, ω, rad/s | Phase of G(jω), deg |
| --- | --- |
| 0.1 | 0 |
| 0.3 | -5 |
| 1 | -15 |
| 3 | -28 |
| 10 | -45 |
| 30 | -68 |
| 100 | -88 |
</details>

Figure 9.15 Bode diagram of first-order transfer function $G ( s ) = 6 / ( s + 4 )$ with data points from Table 9.1.

Once we have constructed the Bode diagram it can be used to efficiently compute the frequency response. The basic steps are summarized below:

1. Given the input sinusoid $u ( t ) = U _ { 0 }$ sin ??t, read the magnitude $| G ( j \omega ) | _ { \mathrm { d B } }$ and phase $\phi$ (degrees) |directly from the Bode diagram for the known input frequency ??.   
2. Convert the magnitude $| G ( j \omega ) | _ { \mathrm { d B } }$ from decibels to an absolute-value magnitude using Eq. (9.43).   
3. Convert the phase ?? from degrees to radians.   
4. Using the amplitudes $U _ { 0 }$ and $| G ( j \omega ) |$ and phase ?? compute the frequency response $y _ { \mathrm { s s } } ( t ) =$ $| G ( j \omega ) | U _ { 0 } \sin ( \omega t + \phi )$ .

The following example illustrates how to utilize the Bode diagram.
