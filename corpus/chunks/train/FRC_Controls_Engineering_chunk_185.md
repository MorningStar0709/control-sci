# 7.1.3 Nyquist frequency

To completely reconstruct a signal, the Nyquist-Shannon sampling theorem states that it must be sampled at a frequency at least twice the maximum frequency it contains. The highest frequency a given sample rate can capture is called the Nyquist frequency, which is half the sample frequency. This is why recorded audio is sampled at 44.1 kHz. The maximum frequency a typical human can hear is about 20 kHz, so the Nyquist frequency is 20 kHz and the minimum sampling frequency is 40 kHz. (44.1 kHz in particular was chosen for unrelated historical reasons.)

Frequencies above the Nyquist frequency are folded down across it. The higher frequency and the folded down lower frequency are said to alias each other.[2] Figure 7.5 demonstrates aliasing.

The effect of these high-frequency aliases can be reduced with a low-pass filter (called an anti-aliasing filter in this application).

![](image/cd1c2a261e8787952d9af5e47856886ce2fc4913f3d90dbcc233271e4da7ab5f.jpg)

<details>
<summary>line</summary>

| t | Original signal at 1.5 Hz | Samples at 2 Hz | Aliased signal at 0.5 Hz |
| --- | --- | --- | --- |
| 0.0 | 0.00 | 0.00 | 0.00 |
| 0.5 | -1.00 | -1.00 | -1.00 |
| 1.0 | 0.00 | 0.00 | 0.00 |
| 1.5 | 1.00 | 1.00 | 1.00 |
| 2.0 | 0.00 | 0.00 | 0.00 |
| 2.5 | -1.00 | -1.00 | -1.00 |
| 3.0 | 0.00 | 0.00 | 0.00 |
| 3.5 | 1.00 | 1.00 | 1.00 |
| 4.0 | 0.00 | 0.00 | 0.00 |
</details>

Figure 7.5: The original signal is a 1.5 Hz sine wave, which means its Nyquist frequency is 1.5 Hz. The signal is being sampled at 2 Hz, so the aliased signal is a 0.5 Hz sine wave.
