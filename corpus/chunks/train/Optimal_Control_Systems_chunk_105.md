$$
\begin{array}{l} u ^ {*} (t) = \dot {x} ^ {*} (t) + x ^ {*} (t) \\ = C _ {1} (1 - \sqrt {2}) e ^ {- \sqrt {2} t} + C _ {2} (1 + \sqrt {2}) e ^ {\sqrt {2} t}. \tag {2.6.45} \\ \end{array}
$$

Thus, we get the same results as in direct method. The constants $C_1$ and $C_2$ , evaluated using the boundary conditions (2.6.26) are the same as given in (2.6.34).

The solution for the set of differential equations (2.6.32) with the boundary conditions (2.6.26) for Example 2.11 using Symbolic Toolbox of the MATLAB $^{©}$ , Version 6, is shown below.

```txt
\*  
x=dsolve('D2x-2*x=0', 'x(0)=1, x(1)=0')  
x =  
-(exp(2^(1/2))^2+1)/(exp(2^(1/2))^2-1)*sinh(2^(1/2)*t)+cosh(2^(1/2)*t)  
    1/2 2    1/2  
    (exp(2 ) + 1) sinh(2 t)    1/2  
    -  
    1/2 2  
    exp(2 ) - 1  
u =  
-(exp(2^(1/2))^2+1)/(exp(2^(1/2))^2-1)*cosh(2^(1/2)*t)*2^(1/2)+sinh(2^(1/2)*t)*2^(1/2)-(exp(2^(1/2))^2+1)/(exp(2^(1/2))^2-1)*sinh(2^(1/2)*t)+cosh(2^(1/2)*t)  
    1/2 2    1/2 1/2  
    (exp(2 ) + 1) cosh(2 t) 2    1/2 1/2  
    -  
    1/2 2  
    exp(2 ) - 1  
    1/2 2    1/2  
    (exp(2 ) + 1) sinh(2 t)    1/2  
    -  
    1/2 2  
    exp(2 ) - 1
```

It is easy to see that the previous solution for optimal $x^{*}(t)$ is the same as given in (2.6.33) and (2.6.34).

Let us note once again that the Lagrange multiplier $\lambda(t)$ helped us to treat the augmented functional (2.6.38) as if it contained independent variables $x(t)$ and $u(t)$ , although they are dependent as per the plant equation (2.6.36).
