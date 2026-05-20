$$
\begin{array}{l} \frac {b ^ {4}}{(\delta + 1 + a) ^ {4}} = \frac {b ^ {4}}{(\delta + b) ^ {4}} = \frac {b ^ {4}}{\delta^ {4} + 4 b \delta^ {3} + 6 b ^ {2} \delta^ {2} + 4 b ^ {3} \delta + b ^ {4}} \\ = \frac {b ^ {4}}{\delta^ {4} + b _ {1} \delta^ {3} + b _ {2} \delta^ {3} + b _ {3} \delta + b _ {4}} \\ \end{array}
$$

where $b = 1 + a$ . Notice that $b$ is a small number when $a$ is close to -1. The system is implemented using (9.21), where $\bar{F}$ and $\bar{G}$ have the same form as for the shift-operator companion form in Listing 9.3. The implementation in $\delta$ -companion form is given in Listing 9.6, where $b_i$ are the coefficients in the characteristic polynomial.

The implementation of the discrete-time system also includes a monitor system that runs the program each sampling period. Notice that the code contains only addition, multiplication, and assignment statements; thus it can easily be implemented using many computer languages. Because assignment statements only transfer data, they will not introduce any numerical errors. This means that 0 and 1 in a standard matrix representation are represented exactly.

Listing 9.6 Computer code for implementing (9.25) based on $\delta$ -operator controllable canonical form.   
```txt
begin
    y:=b*b*b*b*x4
    s:=-b1*x1-b2*x2-b3*x3-b4*x4+u
    x4:=x4+x3
    x3:=x3+x2
    x2:=x2+x1
    x1:=x1+s
end 
```

![](image/6b389a81b6ce38ee659bd2d0d830c13e924711eabc41f23a09a278d50ba8099d.jpg)

<details>
<summary>line</summary>

| x | Output |
| --- | --- |
| 0 | 0 |
| 500 | 1 |
| 1000 | 1 |
</details>

![](image/00103cf528aa11de9d372365f02ec3199eb15e42fe797742ff568e720b472639.jpg)

<details>
<summary>line</summary>

| x | Output |
| --- | --- |
| 0 | 0 |
| 500 | 1 |
| 1000 | 1 |
</details>

![](image/afa5a6043608b7a2edc38a8a642a9bb7303c2a6e7e486789cd656fc80489cfef.jpg)

<details>
<summary>line</summary>

| Time | Output (Solid Line) | Output (Dashed Line) |
| --- | --- | --- |
| 0 | 0 | 0 |
| 500 | ~1 | ~0.8 |
| 1000 | 1 | ~0.6 |
</details>

![](image/6f91bb8ad9a091c8e5361f41669bc9ca20bab55b446b8f36f056cc44f39d5e50.jpg)

<details>
<summary>line</summary>

| Time | Output (Solid Line) | Output (Dashed Line) |
| --- | --- | --- |
| 0 | 0 | 0 |
| 500 | ~0.8 | ~0.9 |
| 1000 | 1 | ~0.2 |
</details>
