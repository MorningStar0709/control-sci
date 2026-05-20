# 7.3.2 Matrix exponential

![](image/19cebf938714af67da9ada22bca450e4825d792134ad179f489dcf845ff14e96.jpg)

Watch the “How (and why) to raise e to the power of a matrix” video from 3Blue1Brown’s Essence of linear algebra series for a visual introduction to the matrix exponential.

![](image/11cc264d55dda11725840b6c04a3c73a69386a90c5078e0a9f2605d468813c41.jpg)

<details>
<summary>line</summary>

| t | e^t | Taylor series of e^t (n = 5) | Taylor series of e^t (n = 4) | Taylor series of e^t (n = 3) | Taylor series of e^t (n = 2) | Taylor series of e^t (n = 1) | Taylor series of e^t (n = 0) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| -5 | 0.0 | -4.0 | 13.5 | -4.0 | 8.0 | -2.0 | 1.0 |
| -4 | 0.0 | -3.0 | 6.0 | -3.0 | 4.0 | -1.0 | 1.0 |
| -3 | 0.0 | -2.0 | 2.0 | -2.0 | 2.0 | 0.0 | 1.0 |
| -2 | 0.0 | -1.0 | 0.5 | -1.0 | 1.0 | 0.5 | 1.0 |
| -1 | 0.0 | 0.0 | 0.0 | 0.0 | 0.5 | 1.0 | 1.0 |
| 0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.0 | 1.0 |
| 1 | 0.0 | 1.0 | 2.0 | 1.0 | 2.0 | 3.0 | 1.0 |
| 2 | 0.0 | 3.0 | 5.0 | 3.0 | 4.0 | 4.5 | 1.0 |
| 3 | 0.0 | 6.0 | 9.0 | 6.0 | 7.5 | 6.5 | 1.0 |
| 4 | 0.0 | 12.0 | 16.0 | 12.5 | 14.5 | 9.5 | 1.0 |
| 5 | 0.0 | 24.0 | 28.0 | 24.5 | 22.5 | 13.5 | 1.0 |
</details>

Figure 7.6: Taylor series expansions of $e ^ { t }$ around $t = 0$ for n terms

![](image/ed6648c3d89f09aeb2167ce1bcc3d5a186422892d95db7621cc6c95b8c2927ce.jpg)  
“How (and why) to raise e to the power of a matrix” (27 minutes) 3Blue1Brown   
https://www.3blue1brown.com/lessons/matrix-exponents

Definition 7.3.1 — Matrix exponential. Let X be an $n \times n$ matrix. The exponential of X denoted by $e ^ { \mathbf { X } }$ is the $n \times n$ matrix given by the following power series.

$$e ^ {\mathbf {X}} = \sum_ {k = 0} ^ {\infty} \frac {1}{k !} \mathbf {X} ^ {k} \tag {7.3}$$

where $\mathbf { X } ^ { 0 }$ is defined to be the identity matrix I with the same dimensions as $\mathbf { X } .$ .

To understand why the matrix exponential is used in the discretization process, consider the scalar differential equation ${ \dot { x } } = a x$ . The solution to this type of differential equation
