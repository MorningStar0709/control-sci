# Data Filters and Excitation

Assume that the process is described by the discrete-time model

$$y (t) = G _ {0} (q) u (t) + v (t) \tag {11.17}$$

Notice that possible anti-aliasing filters appear as part of the process $G_{0}(q)$ . The disturbance $v(t)$ can be the sum of deterministic, piecewise deterministic, and stochastic disturbances. The signal has low-frequency and high-frequency components. In stochastic control problems it is important to design a controller that is tuned to a particular disturbance spectrum. In that case it is, of course, important to estimate the disturbance characteristics. In a deterministic problem we are concerned primarily with the term $G_{0}(q)u(t)$ in the above equation, and we are not particularly interested in the detailed character of the disturbance $v(t)$ . In the following discussion we consider this case.

![](image/317d9a909a204d1a339ce4e78e5b6c45a52bd7ee9e7c67a3bebddec4e1ef66f2.jpg)

<details>
<summary>text_image</summary>

|H_f|
ω_fl
ω_fh
rad/s
</details>

Figure 11.7 Amplitude curve for the data filter $H_{f}(q)$ .

The presence of the disturbance $v(t)$ will, of course, create difficulties in the parameter estimation. However, the effect of $v(t)$ can be reduced by filtering. Assume that we introduce a data filter with the transfer function $H_{f}$ and that we apply this filter to Eq. (11.17). Then

$$y _ {f} (t) = G _ {0} (q) u _ {f} (t) + v _ {f} (t) \tag {11.18}$$

where

$$y _ {f} (t) = H _ {f} (q) y (t) \quad u _ {f} (t) = H _ {f} (q) u (t) \quad \text { and } \quad v _ {f} (t) = H _ {f} (q) v (t)$$

By a proper choice of the data filter we may now make the relative influence of the disturbance term smaller in Eq. (11.18) than in Eq. (11.17). The filtering should also emphasize the frequency ranges that are of primary importance for control design. The disturbance $v(t)$ typically has significant components with low frequencies. Low-frequency components should thus be reduced. Very high frequencies should similarly be attenuated. One reason for this is that if the model

$$A (q) y _ {f} (t) = B (q) u _ {f} (t)$$
