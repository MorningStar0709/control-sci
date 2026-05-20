# Bandwidth

The cutoff frequency $\omega _ { B }$ is defined as the maximum input frequency at which the output of the system will follow an input sinusoid in a satisfactory manner. Typically, “satisfactory tracking” includes all frequencies up to the cutoff frequency where the amplitude ratio is attenuated (reduced) from its low-frequency value by a factor of 0.7071 or $1 / { \sqrt { 2 } } .$ . This 70.7% factor arises from electrical circuit theory and represents a one-half power loss because power is typically a squared quantity. In decibels, attenuation by a factor of 0.7071 is equal to a 3-dB drop from the low-frequency magnitude and, therefore, the cutoff frequency can be read directly from the Bode magnitude plot. The frequency range $0 \leq \omega \leq \omega _ { B }$ where the magnitude of G( j??) remains within 3 dB of the DC gain is called the bandwidth of the system.

Figure 9.27 shows the magnitude plot (dB) from the Bode diagram for the rotational mechanical system from Example 9.8. The low-frequency magnitude (DC gain) is −36.3 dB and is labeled on Fig. 9.27.

![](image/01bf371891a0e7a3c80a1412009e6c0043fe7d3bb8bcda4457f317fb67af5ac8.jpg)

<details>
<summary>line</summary>

| Frequency, ω, rad/s | Magnitude, dB |
| --- | --- |
| 10^0 | -36.3 |
| 10^1 | -39.3 |
| 10^2 | -60 |
</details>

Figure 9.27 Magnitude plot showing bandwidth and cutoff frequency $\omega _ { B }$ of the rotational mechanical system from Example 9.8.

The bandwidth is determined by the cutoff frequency $\omega _ { B }$ where the magnitude plot has dropped to −39.3 dB (or, 3 dB below the DC gain value). We can estimate the cutoff frequency by reading the Bode diagram or we can use the MATLAB command bandwidth:

```matlab
>> sysG = tf(5, [18325]) % create transfer function G(s)
>> wB = bandwidth(sysG) % compute the bandwidth of system G(s) 
```

MATLAB returns bandwidth wB in units of rad/s, and executing the above commands yields the cutoff frequency $\omega _ { B } = 2 7 . 0 2 3 \mathrm { r a d / s }$ . This cutoff frequency is also depicted in Fig. 9.27. Bandwidth is sometimes presented in hertz (cycles per second), which is $\omega _ { B } / ( 2 \pi ) = 4 . 3$ Hz for this example.

In general, high bandwidth corresponds to a fast system response because the output can satisfactorily track a high-frequency input. For example, we might require an electromechanical actuator (solenoid) to possess a very high bandwidth so that it can quickly position a hydraulic valve and improve the overall system performance. However, we do not want the solenoid and valve to respond to undesirable high-frequency noise and, therefore, we might choose to send the voltage input signal through a low-pass filter in order to eliminate the high-frequency components.
