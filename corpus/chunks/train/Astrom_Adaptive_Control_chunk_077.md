# EXAMPLE 2.1 Least-squares estimation of static system

Consider the system

$$y (i) = b _ {0} + b _ {1} u (i) + b _ {2} u ^ {2} (i) + e (i)$$

where $e(i)$ is zero mean Gaussian noise with standard deviation 0.1. The system is linear in the parameters and can be written in the form (2.1) with

$$
\varphi^ {T} (i) = \left( \begin{array}{c c c} 1 & u (i) & u ^ {2} (i) \end{array} \right)

\theta^ {T} = \left( \begin{array}{c c c} b _ {0} & b _ {1} & b _ {2} \end{array} \right)
$$

The output is measured for the seven different inputs shown by the dots in Fig. 2.1. In practice the model structure is usually unknown, and the user must decide on an appropriate model. We illustrate this by estimating parameters of the following models:

Model 1: $y(i) = b_0$

Model 2: $y(i) = b_0 + b_1u$

Model 3: $y(i) = b_0 + b_1u + b_2u^2$

Model 4: $y(i) = b_0 + b_1u + b_2u^2 + b_3u^3$

The different models give a polynomial dependence of different orders between $y$ and $u$ .

Table 2.1 shows the least-squares estimates of the different models together with the resulting loss function. Figure 2.1 also shows the estimated relation between u and y for the different models. From the table it is seen that about the same losses are obtained for Models 3 and 4. The fit to the data points is almost the same for these two models, as is seen in Fig. 2.1. □

The example shows that it is important to choose the correct model structure to get a good model. With few parameters it is not possible to get a good fit to the data. If too many parameters are used, the fit to the measured data will be very good but the fit to another data set may be very poor. This latter situation is called overfitting.

Table 2.1 Least-squares estimates and loss functions for the system in Example 2.1 using different model structures.

<table><tr><td>Model</td><td> $\hat{b}_{0}$ </td><td> $\hat{b}_{1}$ </td><td> $\hat{b}_{2}$ </td><td> $\hat{b}_{3}$ </td><td>V</td></tr><tr><td>1</td><td>3.85</td><td></td><td></td><td></td><td>34.46</td></tr><tr><td>2</td><td>0.57</td><td>1.09</td><td></td><td></td><td>1.01</td></tr><tr><td>3</td><td>1.11</td><td>0.45</td><td>0.11</td><td></td><td>0.031</td></tr><tr><td>4</td><td>1.13</td><td>0.37</td><td>0.14</td><td>-0.003</td><td>0.027</td></tr></table>

![](image/0fcb4c6925433056ff72a0d8d8c6072f94fa1a80a00948bd015ada8f419a183e.jpg)

<details>
<summary>scatter</summary>
