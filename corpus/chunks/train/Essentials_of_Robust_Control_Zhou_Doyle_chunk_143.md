Despite the simplicity of this statement, feedback design is by no means trivial. This is true because loop gains cannot be made arbitrarily high over arbitrarily large frequency ranges. Rather, they must satisfy certain performance tradeoff and design limitations. $\mathrm { A }$ major performance tradeoff, for example, concerns commands and disturbance error reduction versus stability under the model uncertainty. Assume that the plant model is perturbed to $( I + \Delta ) P$ with $\Delta$ stable, and assume that the system is nominally stable (i.e., the closed-loop system with $\Delta = 0$ is stable). Now the perturbed closed-loop system is stable if

$$\det (I + (I + \Delta) P K) = \det (I + P K) \det (I + \Delta T _ {o})$$

has no right-half plane zero. This would, in general, amount to requiring that $\| \Delta T _ { o } \|$ be small or that $\bar { \sigma } ( T _ { o } )$ be small at those frequencies where $\Delta$ is significant, typically at high-frequency range, which, in turn, implies that the loop gain, $\overline { { \sigma } } ( L _ { o } )$ , should be small at those frequencies.

Still another tradeoff is with the sensor noise error reduction. The conflict between the disturbance rejection and the sensor noise reduction is evident in equation (6.1). Large $\underline { { \sigma } } ( L _ { o } ( j \omega ) )$ values over a large frequency range make errors due to d small. However, they also make errors due to n large because this noise is “passed through” over the same frequency range, that is,

$$y = T _ {o} (r - n) + S _ {o} P d _ {i} + S _ {o} d \approx (r - n)$$

Note that n is typically significant in the high-frequency range. Worst still, large loop gains outside of the bandwidth of $P -$ that is, $\underline { { \sigma } } ( L _ { o } ( j \omega ) ) \gg 1$ or $\underline { { \sigma } } ( L _ { i } ( j \omega ) ) \gg 1$ while $\overline { { \sigma } } ( P ( j \omega ) ) \ll 1 -$ can make the control activity (u) quite unacceptable, which may cause the saturation of actuators. This follows from

$$u = K S _ {o} (r - n - d) - T _ {i} d _ {i} = S _ {i} K (r - n - d) - T _ {i} d _ {i} \approx P ^ {- 1} (r - n - d) - d _ {i}$$

Here, we have assumed $P$ to be square and invertible for convenience. The resulting equation shows that disturbances and sensor noise are actually amplified at u whenever the frequency range significantly exceeds the bandwidth of $P ,$ , since for $\omega$ such that $\overline { { \sigma } } ( P ( j \omega ) ) \ll 1$ we have
