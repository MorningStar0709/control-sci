# EXAMPLE 5.9 Linear system with sup norm

Consider a stable linear system with impulse response $h(t)$ . We have

$$y (t) = \int_ {0} ^ {\infty} h (\tau) u (t - \tau) d \tau$$

Using the sup norm, we get

$$| y (t) | = \left| \int_ {0} ^ {\infty} h (\tau) u (t - \tau) d \tau \right| \leq \sup _ {t} | u (t) | \int_ {0} ^ {\infty} | h (\tau) | d \tau$$

This gives

$$\sup _ {t} | y (t) | \leq \gamma (G) \cdot \sup _ {t} | u (t) |$$

where the gain of the system is given by

$$\gamma (G) = \int_ {0} ^ {\infty} | h (\tau) | d \tau$$

![](image/e2a7865783e1b5bbf8c9843edc800bc62cf956037859edd8b6272ca6b2013ba6.jpg)

<details>
<summary>text_image</summary>

f(x)
f = γx
x
f = -γx
</details>

Figure 5.15 Illustration of the gain of a static nonlinearity.

If we let $u_0 = \max_t |u(t)|$ , the maximum is assumed for the signal

$$u (s) = u _ {0} \operatorname{sign} (h (t - s))$$

However, this signal is not in $L_{2e}$ . Since the system is stable, we can get arbitrarily close with a signal in $L_{2e}$ by making T sufficiently large. ☐
