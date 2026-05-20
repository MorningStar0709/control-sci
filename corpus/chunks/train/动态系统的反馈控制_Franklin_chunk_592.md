![](image/ea16c9d2bc9c80acc891886626996069f718c2ef3b33df30127723430a714a2a.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    e --> |+| Sum1["Σ"]
    Sum1 --> |k_P| Sum2["Σ"]
    Sum2 --> |u_I| Sum3["Σ"]
    Sum3 --> |u_c| Sum4["Σ"]
    Sum4 --> |u_min| UU["u"]
    Sum4 --> |u_max| UC["u_C"]
    UU --> |u| Output["u"]
    UC --> |u| Output
    K_a --> |-| Sum1
    K_a --> |+| Sum2
    K_a --> |-| Sum4
```
</details>

b)

![](image/1cafa66dbcc334e25fe0279ac042e6b18a15310b8d8d3df9434be13ee8b4d2eb.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    e --> |+| Sum1["Σ"]
    Sum1 --> |k_I/s| Sum2["Σ"]
    Sum2 --> |+| Sum3["Σ"]
    Sum3 --> |+| Sum4["Σ"]
    Sum4 --> |+| Sum5["Σ"]
    Sum5 --> |+| Sum6["Σ"]
    Sum6 --> |+| Sum7["Σ"]
    Sum7 --> |+| Sum8["Σ"]
    Sum8 --> |+| Sum9["Σ"]
    Sum9 --> |+| Sum10["Σ"]
    Sum10 --> |+| Sum11["Σ"]
    Sum11 --> |+| Sum12["Σ"]
    Sum12 --> |+| Sum13["Σ"]
    Sum13 --> |+| Sum14["Σ"]
    Sum14 --> |+| Sum15["Σ"]
    Sum15 --> |+| Sum16["Σ"]
    Sum16 --> |+| Sum17["Σ"]
    Sum17 --> |+| Sum18["Σ"]
    Sum18 --> |+| Sum19["Σ"]
    Sum19 --> |+| Sum20["Σ"]
    Sum20 --> |+| Sum21["Σ"]
    Sum21 --> |+| Sum22["Σ"]
    Sum22 --> |+| Sum23["Σ"]
    Sum23 --> |+| Sum24["Σ"]
    Sum24 --> |+| Sum25["Σ"]
    Sum25 --> |+| Sum26["Σ"]
    Sum26 --> |+| Sum27["Σ"]
    Sum27 --> |+| Sum28["Σ"]
    Sum28 --> |+| Sum29["Σ"]
    Sum29 --> |+| Sum30["Σ"]
    Sum30 --> |+| Sum31["Σ"]
    Sum31 --> |+| Sum32["Σ"]
    Sum32 --> |+| Sum33["Σ"]
    Sum33 --> |+| Sum34["Σ"]
    Sum34 --> |+| Sum35["Σ"]
    Sum35 --> |+| Sum36["Σ"]
    Sum36 --> |+| Sum37["Σ"]
    Sum37 --> |+| Sum38["Σ"]
    Sum38 --> |+| Sum39["Σ"]
    Sum39 --> |+| Sum40["Σ"]
    Sum40 --> |+| Sum41["Σ"]
    Sum41 --> |+| Sum42["Σ"]
    Sum42 --> |+| Sum43["Σ"]
    Sum43 --> |+| Sum44["Σ"]
    Sum44 --> |+| Sum45["Σ"]
    Sum45 --> |+| Sum46["Σ"]
    Sum46 --> |+| Sum47["Σ"]
    Sum47 --> |+| Sum48["Σ"]
    Sum48 --> |+| Sum49["Σ"]
    Sum49 --> |+| Sum50["Σ"]
    Sum50 --> |+| Sum51["Σ"]
    Sum51 --> |+| Sum52["Σ"]
    Sum52 --> |+| Sum53["Σ"]
    Sum53 --> |+| Sum54["Σ"]
    Sum54 --> |+| Sum55["Σ"]
    Sum55 --> |+| Sum56["Σ"]
    Sum56 --> |+| Sum57["Σ"]
    Sum57 --> |+| Sum58["Σ"]
    Sum58 --> |+| Sum59["Σ"]
    Sum59 --> |+| Sum60["Σ"]
    Sum60 --> |+| Sum61["Σ"]
    Sum61 --> |+| Sum62["Σ"]
    Sum62 --> |+| Sum63["Σ"]
    Sum63 --> |+| Sum64["Σ"]
    Sum64 --> |+| Sum65["Σ"]
    Sum65 --> |+| Sum66["Σ"]
    Sum66 --> |+| Sum67["Σ"]
    Sum67 --> |+| Sum68["Σ"]
    Sum68 --> |+| Sum69["Σ"]
    Sum69 --> |+| Sum70["Σ"]
    Sum70 --> |+| Sum71["Σ"]
    Sum71 --> |+| Sum72["Σ"]
    Sum72 --> |+| Sum73["Σ"]
    Sum73 --> |+| Sum74["Σ"]
    Sum74 --> |+| Sum75["Σ"]
    Sum75 --> |+| Sum76["Σ"]
    Sum76 --> |+| Sum77["Σ"]
    Sum77 --> |+| Sum78["Σ"]
    Sum78 --> |+| Sum79["Σ"]
    Sum79 --> |+| Sum80["Σ"]
    Sum80 --> |+| TotalSum
```
</details>

c)

![](image/7988e87be97922842c35b0f5f7387a661f611e3741e84cbbedf0f6db41fd4e0b.jpg)  
d)   
图 9.21 积分器抗饱和技术

抗饱和的作用是减小反馈系统中的超调和控制作用。在任何积分控制的实际应用中都有必要实施这样的抗饱和方案，忽略这种技术将会导致响应的严重恶化。从稳定性的角度看，饱和的影响就是断开反馈环使得开环对象输入为常值，控制器成为一个以系统误差为输入的开环系统。

抗饱和的目的是：当主回路由于信号饱和而断开时，为控制器提供局部反馈使得其自身稳定，任何这样的回路都会起到抗饱和的作用。
