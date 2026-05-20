The ISE (rms error) will be small if $|H_w|$ is small at frequencies where $w$ has substantial energy (power). As for the other terms in Equation 4.6, if the sensor noise $v(t) \neq 0$ , the transfer function $H_v$ should also be small in magnitude at frequencies where $|v(j\omega)|$ is large. In the case of the reference to output transfer function $H_d$ , Equation 4.6 shows that $|1 - H_d(j\omega)|$ should be small where $|y_d(j\omega)|$ is large; another way of saying this is that $H_d(j\omega) \sim 1$ where $|y_d(j\omega)|$ is relatively large.

The phase of $H_{d}(j\omega)$ is important. In Figure 4.6a, the circular arc is the locus of complex numbers $|H_{d}| = 1$ ; as the diagram shows, the complex number $1 - H_{d}$ is quite different from zero if $\neq H_{d}$ is not near $0^{\circ}$ . Therefore, a specification on $H_{d}(j\omega)$ must include magnitude and phase. The specification of phase is avoided if we work with $1 - H_{d}(j\omega)$ ; as Figure 4.6b shows, $H_{d}(j\omega)$ is near 1 if $|1 - H_{d}(j\omega)|$ is close to zero.

In practice, reference and disturbance signals are typically concentrated at low frequencies. Therefore, it is normally desirable to have $H_{d}(j\omega) \sim 1$ and $H_{w}(j\omega) \sim 0$ at low frequencies. It turns out to be undesirable to maintain these values at all frequencies. As we shall see, in a practical design, $H_{d}(j\omega)$ tends to zero and $H_{w}(j\omega)$ to one at high frequencies. The design objective is to make $H_{d}(j\omega) \sim 1$ and $H_{w}(j\omega) \sim 0$ over the frequency range 0 to $\omega_{b}$ , where $y_{d}$ and $w$ have significant spectral constant. That frequency range is the system passband, and $\omega_{b}$ is the bandwidth, which can be defined in a number of ways, depending on the application.

![](image/e5fb4373b760e05a92258a6e60ec85a4e6758ff270ec9726bd3ae296832bcad9.jpg)

<details>
<summary>text_image</summary>

H_d
1 - H_d
1
</details>

(a)

![](image/fa5bea20658b577be12af00155d86f45b0dbfc5ee646d14d10faa1ce0f2b2dd4.jpg)

<details>
<summary>text_image</summary>

H_d
1 - H_d
1
</details>

(b)   
Figure 4.6 Showing the importance of phase differences
