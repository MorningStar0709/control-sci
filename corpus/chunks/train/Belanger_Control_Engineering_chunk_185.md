| Frequency (rad/s) | Magnitude (db) |
| --- | --- |
| 0.1 | -20 |
| 1 | 10 |
| 10 | 0 |
| 100 | 0 |
</details>

(b)   
Figure 4.7 Typical frequency-domain specifications on: a) The reference output transmission and b) The disturbance-output transmission

Figure 4.9a shows the magnitudes $|B_k(j\omega)|$ . It can be shown (see Problem 4.4) that

$$\left| B _ {k} (j \omega) \right| = \frac {1}{\left[ 1 + \left(\frac {\omega}{\omega_ {0}}\right) ^ {2 k} \right] ^ {1 / 2}} \tag {4.10}$$

so that

$$\left| B _ {k} (j \omega_ {0}) \right| = \frac {1}{\sqrt {2}}$$

for all k. Thus, $\omega_{0}$ is the so-called 3-db bandwidth, because $20\log(1/\sqrt{2}) = -3$ . Note the rolloff rate, equal to 20 kdb/decade.

Figure 4.9b shows $|1 - B_k(j\omega)|$ , the magnitude of the Butterworth high-pass filter. It is easy to show (see Problem 4.5) that the denominator of $1 - B_k(s)$ is the same as that of $B_k(s)$ , and that the numerator is just the denominator without the constant term.

![](image/675d148afafba1c1e9dc42e777231be6fb68e9d1bfb3de7ae710f5e789852a86.jpg)

<details>
<summary>text_image</summary>

φk
φk
1/2 φk
φk
1/2 φk
</details>

Figure 4.8 A Butterworth pole pattern   
![](image/47c4d102651e11b96b12c0bda4d8d97d9ec5d502f387072ade592f7e126d8551.jpg)

<details>
<summary>line</summary>

| Frequency/ω₀ | Magnitude (db) |
| --- | --- |
| 0.1 | 0 |
| 1 | -5 |
| 10 | -60 |
</details>

(a)

![](image/8b6d8e05afaba7f0a9431bea6782a7e9ce5c92a321d09ca1d1718e09232e5d9e.jpg)

<details>
<summary>line</summary>

| Frequency/ω₀ | Magnitude (db) - Solid Line | Magnitude (db) - Dashed Line | Magnitude (db) - Dotted Line |
| --- | --- | --- | --- |
| 0.1 | -20 | -15 | -13 |
| 1 | -5 | 2 | 4 |
| 10 | 0 | 0 | 0 |
</details>

(b)   
Figure 4.9 Frequency responses for Butterworth filters: a) Low-pass and b) High-pass
