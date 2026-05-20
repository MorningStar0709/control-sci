# 7.3.1 Taylor series

![](image/1f20190fedad146a7c524266bc863b3cb6e08f99794b5540cedd8581b65510b8.jpg)

Watch the “Taylor series” video from 3Blue1Brown’s Essence of calculus series for an explanation of how the Taylor series expansion works.

The definition for the matrix exponential and the approximations below all use the Taylor series expansion. The Taylor series is a method of approximating a function like $e ^ { t }$ via the summation of weighted polynomial terms like $t ^ { k } , \ e ^ { t }$ has the following Taylor series around t = 0.

![](image/a221d037b33b2844ccee7e54a86a1960e4660dbcdc8627da66a5d0ed06c8db65.jpg)  
“Taylor series” (22 minutes)   
3Blue1Brown   
https://www.3blue1brown.com/lessons/taylor-series

$$e ^ {t} = \sum_ {n = 0} ^ {\infty} \frac {t ^ {n}}{n !}$$

where a finite upper bound on the number of terms produces an approximation of $e ^ { t }$ . As n increases, the polynomial terms increase in power and the weights by which they are multiplied decrease. For $e ^ { t }$ and some other functions, the Taylor series expansion equals the original function for all values of t as the number of terms approaches infinity.[3] Figure 7.6 shows the Taylor series expansion of $e ^ { t }$ around $t = 0$ for a varying number of terms.

We’ll expand the first few terms of the Taylor series expansion in equation (7.3) for ${ \bf X } = { \bf A } T$ so we can compare it with other methods.

$$\sum_ {k = 0} ^ {3} \frac {1}{k !} (\mathbf {A} T) ^ {k} = \mathbf {I} + \mathbf {A} T + \frac {1}{2} \mathbf {A} ^ {2} T ^ {2} + \frac {1}{6} \mathbf {A} ^ {3} T ^ {3}$$

Table 7.2 compares discretization methods for the matrix case, and table 7.3 compares their Taylor series expansions. These use a more complex formula which we won’t present here.

Each of them has different stability properties. The bilinear transform preserves the (in)stability of the continuous time system.
