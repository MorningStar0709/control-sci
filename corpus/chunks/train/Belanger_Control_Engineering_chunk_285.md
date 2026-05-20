# 5.6.4 Unstructured Uncertainties

A parametric model is based upon consideration of some physical phenomena thought to represent the salient features of the plant. In practice, a model used for control system design does not include all physical effects, for two reasons: (i) the design model is a simplified version of a more complex simulation model, and (ii) secondary physical effects are excluded because of complexity and engineering study costs. Such effects are incorporated in the unstructured uncertainty. We consider the model

$$P (s) = [ 1 + \Delta (s) ] P _ {0} (s) \tag {5.25}$$

where $P_{0}(s)$ is the nominal model and $\Delta(s)$ is a transfer function with a known magnitude bound; i.e.,

$$| \Delta (j \omega) | \leq \ell (j \omega) \tag {5.26}$$

where $\ell(j\omega)$ is a real, nonnegative number. It is assumed that no phase information on $\Delta$ is available, so $\neq \Delta(j\omega)$ may have any value between $0^{\circ}$ and $360^{\circ}$ .

Figure 5.29 illustrates the multiplicative term $1 + \Delta(j\omega)$ , which is a complex number represented by a vector drawn from the origin to some point on or within the circle. For $\ell(j\omega) < 1$ ,

$$1 - \ell (j \omega) \leq | 1 + \Delta (j \omega) | \leq 1 + \ell (j \omega) \tag {5.27}$$

and

$$- \arcsin \ell (j \omega) \leq \not \prec [ 1 + \Delta (j \omega) ] \leq \arcsin \ell (j \omega). \tag {5.28}$$

![](image/34b572e0d8dcb6940c7acbe41d2f465590083fa058e7f9db2d42eaf34b961200.jpg)

<details>
<summary>text_image</summary>

1 + \u0394(jw)
1 - \u0394(jw)
\u0394(jw)
1
1 + \u0394(jw)
</details>

Figure 5.29 Illustration of transfer function uncertainty

For $\ell(j\omega) > 1$ ,

$$0 \leq | 1 + \Delta (j \omega) | \leq 1 + \ell (j \omega) \tag {5.29}$$

and

$$0 ^ {\circ} \leq \neq [ 1 + \Delta (j \omega) ] \leq 3 6 0 ^ {\circ}. \tag {5.30}$$

Note that $|1 + \Delta(j\omega)|$ , expressed in decibels, is added to the log magnitude of $P_0(j\omega)$ , and that the phase of $[1 + \Delta(j\omega)]$ is added to the phase of $P_0(j\omega)$ . In particular, Equation 5.30 shows that, if $\ell(j\omega) > 1$ , the phase of $P(j\omega)$ may have any value between $0^\circ$ and $360^\circ$ , i.e., is completely uncertain.

It is often easier to include parametric uncertainties in an unstructured uncertainty because the latter is expressible by one real function, $\ell(j\omega)$ . Solving Equation 5.25 yields

$$\Delta (j \omega) = \frac {P (j \omega)}{P _ {0} (j \omega)} - 1 \tag {5.31}$$

and $\ell(j\omega)$ , the upper bound on $|\Delta(j\omega)|$ , is

$$\ell (j \omega) = \max _ {\mathcal {P}} \left| \frac {P (j \omega)}{P _ {0} (j \omega)} - 1 \right|. \tag {5.32}$$
