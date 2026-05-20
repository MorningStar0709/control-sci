In particular, there are three parameters that are used to describe TERCOM-related terrain, and their values can give an indication of the terrain’s ability to support a successful TERCOM fix. These parameters are (1) sigma-T , (2) sigma-Z $( \sigma _ { Z } )$ , and (3) the terrain correlation length $X _ { T }$ . Note that the correlation length $X _ { T }$ represents the separation distance between two rows or columns of the terrain elevation matrix required to reduce their normalized autocorrelation function to a value of $e ^ { - 1 }$ . It is usually assumed that parallel terrain elevation profiles that are separated by a distance greater than $X _ { T }$ are independent of each other.

Sigma-Z is defined as the standard deviation of the point-to-point changes in terrain elevation (i.e., the slope) as shown in Figure 7.20. Like sigma-T , the value of sigma-Z provides a direct indication of terrain roughness. Sigma-Z has also been shown to be a valid indicator of TERCOM performance. The expression for sigma-Z, assuming a Gaussian autocorrelation function, can be obtained from Figure 7.20. Mathematically, sigma-Z is given by the equation

$$\sigma_ {Z} = \sqrt {[ 1 / (N - 1) ] \sum_ {i = 1} ^ {N} (D _ {i} - D) ^ {2}}, \tag {7.17}$$

where

$$D _ {i} = H _ {i} - H _ {i + 1}, \text { and } D = (1 / (N - 1)) \sum_ {i = 1} ^ {N - 1} D _ {i}.$$

The two parameters sigma-T and sigma-Z are related to the third parameter XT according to the relation

$$\sigma_ {Z} ^ {2} = 2 \sigma_ {T} ^ {2} [ 1 - \exp (- d / X _ {T}) ^ {2} ], \tag {7.18}$$

where d is the cell size (or distance between elevation samples).
