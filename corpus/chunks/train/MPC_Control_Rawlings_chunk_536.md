# Solution

Applying the resampling strategy gives the results in Figure 4.23. Notice that resampling prevents the samples from drifting away from the mean of the conditional density. Resampling maintains a high concentration of particles in the 95% probability ellipse. If we repeat this simulation 500 times and compute the fraction of particles within the conditional density’s 95% probability contour, we obtain the results shown in Figure 4.24. Notice the dramatic improvement. Without resampling, fewer than 10% of the particles are in the 95% confidence ellipse after only five time steps. With resampling, about 80% of the samples are inside the 95% confidence ellipse. There is one caution against resampling too frequently, however. If the measurement has a small covariance, then the weights computed from

$$w _ {i} (k) = w _ {i} (k - 1) p (y (k) | x _ {i} (i))$$

![](image/298d84404050510891d2c8b0913b96fb4c8d37271b9da9e0ebcf746301bc28f9.jpg)  
Figure 4.23: Particles’ locations versus time for the simplest particle filter with resampling; 250 particles. Ellipses show the 95% contour of the true conditional densities before and after measurement.

will be dominated by only a few particles whose prediction of y is closest to the measurement. Resampling in this situation gives only those few particles repeated many times in the resample. For a sufficiently small covariance, this phenomenon can produce a single $x _ { i }$ value in the resample. This phenomenon is known as sample impoverishment (Doucet, Godsill, and Andrieu, 2000; Rawlings and Bakshi, 2006). -
