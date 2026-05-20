In the application of modern optimal control and estimation theory to modeling of the seeker and missile/target dynamics, glint and scintillation errors are commonly modeled using filtered Gaussian white noise input in order to produce correlated noise output. The new noise treatment replaces the fourth-order Runge–Kutta approximation with the method of conditional probability density function (pdf ). This new technique allows random draws of correlated errors to be made directly, thus eliminating the need to make white noise input draws and to filter this input before output draws are made. The probability density function of the correlated output error is found in closed form in terms of the previous value of the correlated output and the correlation coefficient. The new method provides accurate statistics and satisfies the necessary correlation properties. Its computational simplicity translates into substantial savings in computer processing time. The correlated output terms for glint and scintillation are computed using the same form of the conditional probability density function. The pdf is derived from the spectral density and autocorrelation function and is given by the expression

$$p (g _ {2} | g _ {1}) = \frac {1}{\sqrt {2 \pi (1 - \rho^ {2}) \cdot \sigma_ {c} ^ {2}}} \cdot \exp \left(- \frac {1}{2 \sigma_ {c} ^ {2} \cdot (1 - \rho^ {2})} (g _ {2} - \rho g _ {1}) ^ {2}\right) \tag {3.88}$$

where

$$g _ {1} = \text { previous value of the error term },g _ {2} = \text { current value of the error term },\sigma_ {c} = \text { standard deviation of correlated noise },\rho = \text { correlation coefficient }.$$

This is a Gaussian density with mean $\rho$ and variance $\sigma _ { c } ^ { 2 } \ ( 1 - \rho ^ { 2 } )$ . Error terms are computed using the radar error covariance function $\mathrm { R A D E V } ( \sigma _ { c } )$ , which returns a normally distributed random number with zero mean and standard deviation $\sigma _ { c }$ . The expression for computing the glint and scintillation is

$$g _ {2} = \rho \cdot g _ {1} + \text {RADEV} (\sigma_ {c}), \tag {3.89}$$

where appropriate statistics are substituted into the above expression for glint or scintillation.
