# 2.7.2 Different Types of Systems

We now obtain different cases depending on the statement of the problem regarding the final time $t_{f}$ and the final state $\mathbf{x}(t_{f})$ (see Figure 2.9).

\- Type (a): Fixed-Final Time and Fixed-Final State System: Here, since $t_f$ and $\mathbf{x}(t_f)$ are fixed or specified (Figure 2.9(a)), both $\delta t_f$ and $\delta \mathbf{x}_f$ are zero in the general boundary condition (2.7.32), and there is no extra boundary condition to be used other than those given in the problem formulation.

\- Type (b): Free-Final Time and Fixed-Final State System: Since $t_f$ is free or not specified in advance, $\delta t_f$ is arbitrary, and since $\mathbf{x}(t_f)$ is fixed or specified, $\delta \mathbf{x}_f$ is zero as shown in Figure 2.9(b). Then, the coefficient of the arbitrary $\delta t_f$ in the general boundary condition (2.7.32) is zero resulting in

$$\boxed {\left(\mathcal {H} + \frac {\partial S}{\partial t}\right) _ {* t _ {f}} = 0.} \tag {2.7.33}$$

\- Type (c): Fixed-Final Time and Free-Final State System: Here $t_f$ is specified and $\mathbf{x}(t_f)$ is free (see Figure 2.9(c)). Then $\delta t_f$ is zero and $\delta \mathbf{x}_f$ is arbitrary, which in turn means that the coefficient of $\delta \mathbf{x}_f$ in the general boundary condition (2.7.32) is zero. That is

$$\left(\frac {\partial S}{\partial \mathbf {x}} - \boldsymbol {\lambda} ^ {*} (t)\right) _ {* t _ {f}} = 0 \longrightarrow \boxed {\boldsymbol {\lambda} ^ {*} (t _ {f}) = \left(\frac {\partial S}{\partial \mathbf {x}}\right) _ {* t _ {f}}.} \tag {2.7.34}$$

![](image/f89eb4e0252999afe3d2a95bbe9a0c2d16e20ed062a06ba2c6cafb30771acaf2.jpg)

<details>
<summary>line</summary>

| t | x*(t) | x*(t)+δx(t) |
| --- | --- | --- |
| 0 | x₀ | x₀ |
| t₀ | x₀ | x₀ |
| t_f | x_f | x_f |
</details>

(a)

![](image/76aea0f8013e1dc8be5aa269a38c20e1799fd8743c4b98112aa02bfad83d152d.jpg)

<details>
<summary>line</summary>

| t | x*(t) | x*(t)+δx(t) |
| --- | --- | --- |
| 0 | x₀ | x₀ |
| t₀ | x₀ | x₀ |
| t_f | x_f | x_f |
</details>

(b)

![](image/7de4a96eb1f16687806a75e8d0b67268db038b62aa90124eaa03b0a615075509.jpg)

<details>
<summary>line</summary>

| t | x*(t) | x*(t)+δx(t) |
| --- | --- | --- |
| t₀ | x₀ | x₀ |
| t_f | x₀ | x₀ |
</details>

(c)

![](image/98d23a8f45ba7d1ee096be8b2bed3d3710aa6382369c675f94a1969ef57ea41d.jpg)

<details>
<summary>line</summary>

| t | x*(t) | x*(t)+δx(t) |
| --- | --- | --- |
| 0 | x₀ | x₀ |
| t₀ | x₀ | x₀ |
| t_f | x₀ | x₀ |
</details>

(d)   
Figure 2.9 Different Types of Systems: (a) Fixed-Final Time and Fixed-Final State System, (b) Free-Final Time and Fixed-Final State System, (c) Fixed-Final Time and Free-Final State System, (d) Free-Final Time and Free-Final State System
