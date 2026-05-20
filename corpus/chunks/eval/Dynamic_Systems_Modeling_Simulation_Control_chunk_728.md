# Complex Variables

Complex variables can be entered by simply typing their real and imaginary parts. MATLAB assigns both i and j as the imaginary number √ −1. Complex variables can defined, added, and multiplied as shown here:

```matlab
>> x = 2 - j * 5 % define complex variable x = 2 - j5
>> y = -4 + j * 8 % define complex variable y = -4 + j8
>> z = x + y % add complex variables x and y
>> w = x * y % multiply complex variables x and y 
```

The MATLAB commands abs and angle can be used to compute the absolute value (magnitude) and phase angle of a complex variable:

```txt
>> x = 2 - j*5 % define complex variable x = 2 - j5
>> Mag_x = abs(x) % magnitude of x
>> Phase_x = angle(x) % phase angle of x (in rad) 
```

Table B.1 summarizes the basic MATLAB built-in functions described in this section as well as other common functions, such as trigonometric and logarithmic functions.

Table B.1 Basic MATLAB Built-In Functions 

<table><tr><td>MATLAB Command</td><td>Description</td></tr><tr><td>abs (x)</td><td>Absolute value of x (magnitude if x is complex)</td></tr><tr><td>angle (x)</td><td>Phase angle (in rad) of complex variable x</td></tr><tr><td>cos (x)</td><td>Cosine of x (input angle in rad)</td></tr><tr><td>sin (x)</td><td>Sine of x (input angle in rad)</td></tr><tr><td>tan (x)</td><td>Tangent of x (input angle in rad)</td></tr><tr><td>acos (x)</td><td>Inverse cosine of x (answer in rad)</td></tr><tr><td>asin (x)</td><td>Inverse sine of x (answer in rad)</td></tr><tr><td>atan (x)</td><td>Inverse tangent of x (answer in rad)</td></tr><tr><td>exp (x)</td><td>Exponential of x (base e)</td></tr><tr><td>log (x)</td><td>Natural logarithm of x</td></tr><tr><td>log10 (x)</td><td>Base 10 logarithm of x</td></tr><tr><td>max (x)</td><td>Maximum element of vector x</td></tr><tr><td>min (x)</td><td>Minimum element of vector x</td></tr><tr><td>size (x)</td><td>Size (dimension) of vector or matrix x</td></tr><tr><td>sqrt (x)</td><td>Square root of x</td></tr><tr><td>sum (x)</td><td>Sum of the elements of vector x</td></tr></table>
