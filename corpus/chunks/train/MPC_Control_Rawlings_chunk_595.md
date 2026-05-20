But the estimator state {x(t) ˆ } is influenced by the disturbance ψ (see (5.6)), so it cannot be precisely controlled. The problem of controlling the system described by (5.6) is the same type of problem studied in Chapter 3, where the system was described by $x ^ { + } = f ( x , u , w )$ with the estimator state ${ \hat { x } } ,$ , which is accessible, replacing the actual state x. Hence we may use the techniques presented in Chapter 3 to choose a control that forces $\hat { x }$ to lie in another tube $\{ \{ z ( t ) \} \oplus \mathbb { S } ( t ) \}$ where the set sequence $\{ \mathbb { S } ( t ) \}$ that defines the cross section of the tube is precomputed, and $\{ z ( t ) \}$ } that defines the center of the tube is the state trajectory of the nominal (deterministic) system defined by

$$z ^ {+} = \phi (z, u, 0) \tag {5.8}$$

which is the nominal version of (5.6). Equations (5.8) is obtained by replacing ψ by 0 in the original equations. Thus we get two tubes, one embedded in the other. At time t the estimator state ${ \hat { x } } ( t )$ lies in the set $\{ z ( t ) \} \oplus \mathbb { S } ( t )$ , and $x ( t )$ lies in the set $\{ \hat { x } ( t ) \} \oplus \mathbb { \Sigma } ( t )$ , so that for all t

$$x (t) \in \{z (t) \} \oplus \mathbb {T} (t) \quad \mathbb {T} (t) := \Sigma (t) \oplus \mathbb {S} (t)$$

The tubes $\{ \{ z ( t ) \} \oplus \mathbb { S } ( t ) \}$ , in which the trajectory $\{ \hat { x } ( t ) \}$ lies, and $\{ \{ z ( t ) \} \oplus \mathbb { T } ( t ) \}$ , in which the state trajectory $\{ x ( t ) \}$ lies, are shown in Figure 5.2. The tube $\{ \{ z ( t ) \} \oplus \mathbb { S } ( t ) \}$ is embedded in the larger tube $\{ \{ z ( t ) \} \oplus \mathbb { T } ( t ) \}$ .

![](image/ec66dcf615bfb6080553b5f30e21755a3505b8aedf9c486c14f1b601e2593909.jpg)

<details>
<summary>text_image</summary>

{z(0)} ⊕ S
{z(0)} ⊕ Γ
x₂
z(k)
x₁
</details>

Figure 5.2: State tube.
