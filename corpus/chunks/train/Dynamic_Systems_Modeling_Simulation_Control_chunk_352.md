# Example 7.3

Figure 7.2 shows a three-way spool valve used to meter flow in a hydraulic system. Given the following I/O equation for the valve, determine (a) the characteristic equation and characteristic roots and (b) the transfer function and poles of the transfer function.

$$0. 0 4 \ddot {y} + 1 6 \dot {y} + 7 0 0 0 y = f (t) \tag {7.16}$$

Equation (7.16) is the governing mathematical model of the spool valve, which consists of a single mass, a linear viscous friction force, and a linear spring force. Variable y(t) is the displacement of the spool valve, and f (t) is the force from an electromagnetic actuator (i.e., solenoid) that can push on the valve. We assume that there is no hydraulic fluid pressure imbalance on the valve, and that flow forces are neglected; hence, the electromagnetic force f (t) is the sole applied force acting on the valve mass.

![](image/36536098a237300e60223bde17eac6fcb496db5856c108cffc8dca988e81bb18.jpg)

<details>
<summary>text_image</summary>

Supply pressure
Drain
Return spring
Electromagnetic force, f(t)
Spool-valve mass, m
y
Fluid flow
</details>

Figure 7.2 Three-way spool valve for Example 7.3.

We see that by comparing the general I/O equation (7.1) with its corresponding characteristic equation (7.6), the characteristic equation of the valve model (7.16) can be written by using the left-hand side $a _ { i }$ coefficients

$$0. 0 4 r ^ {2} + 1 6 r + 7 0 0 0 = 0 \tag {7.17}$$

Equation (7.17) is the characteristic equation of the valve model. In summary, the characteristic equation of an I/O equation is an nth-order polynomial in $r ,$ where the nth derivative $y ^ { ( n ) }$ is replaced by $r ^ { n } , y ^ { ( n - 1 ) }$ is replaced by $r ^ { n - 1 }$ , etc. The characteristic roots are determined by setting the characteristic equation to zero. We can use MATLAB’s roots command to determine the roots of this second-order polynomial:

$$> > r = \text { roots } ([ 0. 0 4 1 6 7 0 0 0 ])$$

where the row vector [0.04 16 7000] contains the $a _ { i }$ coefficients of the characteristic polynomial in descending order from the second- to zeroth-order terms. The two characteristic roots are

$$r _ {1} = - 2 0 0 + j 3 6 7. 4 2 \quad r _ {2} = - 2 0 0 - j 3 6 7. 4 2$$

These roots are called complex conjugates as they have the same real part (−200), but the imaginary parts (j367.42 and −j367.42) have equal magnitudes but opposite signs (we use $j = \sqrt { - 1 }$ as the imaginary number).
