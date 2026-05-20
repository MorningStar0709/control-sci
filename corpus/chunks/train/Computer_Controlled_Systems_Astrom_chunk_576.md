# An Example

An example illustrates the properties of the different realizations. Consider a system with the pulse-transfer function

$$H (z) = \frac {b ^ {4}}{(z + a) ^ {4}} \tag {9.25}$$

where $b = 1 + a$ . The system has multiple poles that are close to one when a is close to -1. The previous discussion then shows that the system is very sensitive to coefficient perturbations.

To obtain the computer program, a state-space realization of the pulse-transfer function is first determined. The computer code is then obtained as a direct implementation of the difference equations. There are many possible choices of the coordinate system in the state-space realization. A controllable canonical form in shift and $\delta$ -operator and a Jordan canonical form are chosen to demonstrate that the numerical properties may differ considerably. For the shift-operator controllable form we implement

Listing 9.3 Computer code for implementation of (9.25) based on the shift-controllable canonical form.   
```txt
begin
    y:=b*b*b*b*x4
    s:=-a1*x1-a2*x2-a3*x3-a4*x4+u
    x4:=x3
    x3:=x2
    x2:=x1
    x1:=s
end 
```

$$\frac {b ^ {4}}{(z + a) ^ {4}} = \frac {b ^ {4}}{z ^ {4} + 4 a z ^ {3} + 6 a ^ {2} z ^ {2} + 4 a ^ {3} z + a ^ {4}}$$

The code is given in Listing 9.3. The numerical values of the parameters for the controllable canonical form when a = -0.99 are given by

$$
\begin{array}{l} a _ {1} = 4 a = - 3. 9 6 \\ a _ {2} = 6 a ^ {2} = 5. 8 8 0 6 \\ a _ {3} = 4 a ^ {3} = - 3. 8 8 1 1 9 6 \\ a _ {4} = a ^ {4} = 0. 9 6 0 5 9 6 0 1 \\ \end{array}
$$

Listing 9.4 gives an implementation based on the Jordan canonical form. By rewriting the Jordan form as (9.21) Listing 9.5 is obtained. Notice that this slight modification gives a significant improvement over the form in Listing 9.4, because the state is now obtained by adding a small correction to the previous state.

Listing 9.4 Computer code for implementing (9.25) based on the Jordan canonical form.   
```txt
begin
x4:=-a*x4+b*u
x3:=-a*x3+b*x4
x2:=-a*x2+b*x3
x1:=-a*x1+b*x2
y:=x1
end 
```

Listing 9.5 Rearrangement to short-sampling-interval modification of the code in Listing 9.4.   
```txt
begin
x4:=x4+b*(u-x4)
x3:=x3+b*(x4-x3)
x2:=x2+b*(x3-x2)
x1:=x1+b*(x2-x1)
y:=x1
end 
```

For the $\delta$ -form we implement (in controllable canonical form)
