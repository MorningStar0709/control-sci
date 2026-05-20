MATLAB Program 5–25   
```matlab
t = 0:0.2:12;
    for n = 1:6;
    num = [1];
    den = [1 2*(n-1)*0.2 1];
    [y(1:61,n),x,t] = step(num,den,t);
    end
plot(t,y)
grid
title('Unit-Step Response Curves')
xlabel('t Sec')
ylabel('Outputs')
gtext('\zeta = 0'),
gtext('0.2')
gtext('0.4')
gtext('0.6')
gtext('0.8')
gtext('1.0')

% To draw a three-dimensional plot, enter the following command: mesh(y) or mesh(y').
% We shall show two three-dimensional plots, one using "mesh(y)" and the other using "% "mesh(y)". These two plots are the same, except that the x axis and y axis are % interchanged.

mesh(y)
title('Three-Dimensional Plot of Unit-Step Response Curves using Command "mesh(y)"')
xlabel('n, where n = 1,2,3,4,5,6')
ylabel('Computation Time Points')
zlabel('Outputs')

mesh(y')
title('Three-Dimensional Plot of Unit-Step Response Curves using Command "mesh(y transpose)"')
xlabel('Computation Time Points')
ylabel('n, where n = 1,2,3,4,5,6')
zlabel('Outputs') 
```

Figure 5–64

(a) Two-dimensional plot of unit-step response curves; (b) three-dimensional plot of unit-step response curves using command “mesh(y)”; (c) three-dimensional plot of unit-step response curves using command “mesh(y¿)”.

![](image/c43f733020aaa53b4d00fbc6058544b6f9a6f6afa2a22359c6a614de9ce848ca.jpg)

<details>
<summary>line</summary>

| t Sec | ζ = 0 | ζ = 0.2 | ζ = 0.4 | ζ = 0.6 | ζ = 0.8 | ζ = 1.0 |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| 2 | ~1.5 | ~1.2 | ~1.0 | ~0.9 | ~0.8 | ~0.7 |
| 4 | ~2.0 | ~1.5 | ~1.2 | ~1.0 | ~0.9 | ~0.8 |
| 6 | ~0.0 | ~0.7 | ~0.9 | ~1.0 | ~1.0 | ~1.0 |
| 8 | ~1.5 | ~1.2 | ~1.0 | ~1.0 | ~1.0 | ~1.0 |
| 10 | ~2.0 | ~1.5 | ~1.2 | ~1.0 | ~1.0 | ~1.0 |
| 12 | ~0.2 | ~0.2 | ~0.2 | ~0.2 | ~0.2 | ~0.2 |
</details>

Three-Dimensional Plot of Unit-Step Response Curves using Command “mesh(y)”   
Three-Dimensional Plot of Unit-Step Response Curves using Command “mesh(y transpose)”   
![](image/09a57153492c3e6925f6cdd38c8b0560dec0b81576e2c973d1a0ed1cc2264002.jpg)  
(b)

![](image/a68e44cac2f49f0747afa5847aa6faec09ef93dd1c53e15257416936b9ef1e0e.jpg)

<details>
<summary>surface_3d</summary>

| Computation Time Points | n=1 | n=2 | n=3 | n=4 | n=5 | n=6 |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 10 | 0 | 0 | 0 | 0 | 0 | 0 |
| 20 | 0 | 0 | 0 | 0 | 0 | 0 |
| 30 | 0 | 0 | 0 | 0 | 0 | 0 |
| 40 | 0 | 0 | 0 | 0 | 0 | 0 |
| 50 | 0 | 0 | 0 | 0 | 0 | 0 |
| 60 | 0 | 0 | 0 | 0 | 0 | 0 |
| 70 | 0 | 0 | 0 | 0 | 0 | 0 |
</details>

(c)
