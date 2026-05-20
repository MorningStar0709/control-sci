# 1. 模糊化接口(Fuzzy Interface)

模糊控制器的输入必须通过模糊化才能用于控制输出,因此,它实际上是模糊控制器的输入接口,其主要作用是将真实的确定量输入转换为一个模糊向量。对于一个模糊输入变量 e, 其模糊子集通常可以按如下方式划分:

![](image/79675a1bd0e8d78ddeb188e7a1328c0697c72101e623034dc53705fc363a05dc.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["输入"] --> B["模糊化接口"]
    B --> C["推理机"]
    C --> D["解模糊接口"]
    D --> E["输出"]
    F["数据库"] --> C
    G["规则库"] --> C
    H["知识库"] --> C
```
</details>

图 4-2 模糊控制器的组成框图

① $e=\{负大,负小,零,正小,正大\}=\{NB,NS,ZO,PS,PB\}$

② $e = \{\text{负大,负中,负小,零,正小,正中,正大}\} = \{\mathrm{NB},\mathrm{NM},\mathrm{NS},\mathrm{ZO},\mathrm{PS},\mathrm{PM},\mathrm{PB}\}$

③ $e=\{负大,负中,负小,零负,零正,正小,正中,正大\}=\{NB,NM,NS,NZ,PZ,PS,PM,PB\}$

将方式 ③ 用三角形隶属度函数表示, 如图 4-3 所示。

![](image/a3cabdf3fc110d818f3667b2cc5c92825cc18e95d2fa8ea86f9a708be35e15c8.jpg)

<details>
<summary>line</summary>

| Position | Value |
| --- | --- |
| -12 | 0 |
| -10 | 0 |
| -8 | 0 |
| -6 | 0 |
| -4 | 0 |
| -2 | 0 |
| 0 | 0 |
| 2 | 0 |
| 4 | 0 |
| 6 | 0 |
| 8 | 0 |
| 10 | 0 |
| 12 | 0 |
u(e) for NB and NM; u(e) for NS; u(e) for NZ; u(e) for PZ; u(e) for PS; u(e) for PM; u(e) for PB.
</details>

图 4-3 模糊子集和模糊化等级
