In many weapon delivery cases, one calculates the miss distance frequency distribution. In order to do this, we need to define the intercept plane. The intercept plane (see Section 5.1, Figure 5.6, and Section 5.9, Figures 5.23 and 5.24) is the plane that contains the miss distance vector from the target aim point to the closest point of approach (CPA) and is normal to the bomb or missile path (relative to a stationary aircraft). Let the distance from the aircraft aim point $( \mathrm { i . e . }$ , the origin of the coordinate system and normally the aircraft centroid) to any $( x , y )$ pair be the miss distance for that particular launch (or bomb throw), and the distances x and y be the coordinate errors. If there is no correlation between the x and y components of the miss distances, the frequency distribution of the miss distance $\rho ( x , y )$ can be expressed by the bivariate normal distribution

$$\rho (x, y) = \frac {1}{2 \pi \sigma_ {x} \sigma_ {y}} \exp \{[ - (x - \mu_ {x}) ^ {2} / 2 \sigma_ {x} ^ {2} ] - [ (y - \mu_ {y}) ^ {2} / 2 \sigma_ {y} ^ {2} ] \},$$

where the sample means $\mu _ { x }$ and $\mu _ { y }$ and the standard deviations $\sigma _ { x }$ and $\sigma _ { y }$ are related to the sample means M and variances $\sigma ^ { 2 }$ by

$$\mu = M \quad \mathrm{and} \quad \sigma^ {2} = [ N / (N - 1) ] S ^ {2}$$

(note that $\sigma ^ { 2 }$ is sometimes set equal to $S ^ { 2 }$ , particularly when N is large compared to unity). The sample means $M _ { x }$ and $M _ { y }$ are given by

$$M _ {x} = \frac {1}{N} \sum_ {i = 1} ^ {N} x _ {i} \quad \text { and } \quad M _ {y} = \frac {1}{N} \sum_ {i = 1} ^ {N} y _ {i},$$

where $x _ { i }$ and $y _ { i }$ denote the x and y locations of the miss distance for the ith launch, and the sample variances $S _ { x } ^ { 2 }$ and $\dot { S } _ { y } ^ { 2 }$ are computed using

$$S _ {x} ^ {2} = \frac {1}{N} \sum_ {i = 1} ^ {N} (x _ {i} - M _ {x}) ^ {2} \quad \text { and } \quad S _ {y} ^ {2} = \frac {1}{N} \sum_ {i = 1} ^ {N} (y _ {i} - M _ {y}) ^ {2}.$$

If the two means are found or assumed to be equal to zero, and if the two standard deviations are found or assumed to be equal, the bivariate distribution simplifies to the circular normal distribution given by

$$\rho (r) = \frac {1}{2 \pi \sigma_ {r} ^ {2}} \exp [ - r ^ {2} / 2 \sigma_ {r} ^ {2} ],$$

where r is the radial miss distance from the target aim point, and $\sigma _ { r }$ is the circular standard deviation, which is equal to both $\sigma _ { x }$ and $\sigma _ { y }$ . The circular miss distance within which 50% of the shots fall (the CEP) is given by [7]
