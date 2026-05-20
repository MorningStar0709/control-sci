证明 由图7-26得

$$C (s) = G _ {2} (s) E _ {1} ^ {*} (s)E _ {1} (s) = G _ {1} (s) E ^ {*} (s)$$

对 $E_{1}(s)$ 离散化，有

$$E _ {1} ^ {*} (s) = G _ {1} ^ {*} (s) E ^ {*} (s)C (s) = G _ {2} (s) G _ {1} ^ {*} (s) E ^ {*} (s)$$

考虑到 $E(s) = R(s) - H(s)C(s)$

$$= R (s) - H (s) G _ {2} (s) G _ {1} ^ {*} (s) E ^ {*} (s)$$

离散化后，有

$$E ^ {*} (s) = R ^ {*} (s) - H G _ {2} ^ {*} (s) G _ {1} ^ {*} (s) E ^ {*} (s)$$

即 $E^{*}(s) = \frac{R^{*}(s)}{1 + G_{1}^{*}(s)HG_{2}^{*}(s)}$

所以，输出信号的采样拉氏变换

$$C ^ {*} (s) = G _ {2} ^ {*} (s) G _ {1} ^ {*} (s) E ^ {*} (s) = \frac {G _ {1} ^ {*} (s) G _ {2} ^ {*} (s) R ^ {*} (s)}{1 + G _ {1} ^ {*} (s) H G _ {2} ^ {*} (s)}$$

对上式进行 z 变换, 证得

$$\Phi (z) = \frac {C (z)}{R (z)} = \frac {G _ {1} (z) G _ {2} (z)}{1 + G _ {1} (z) H G _ {2} (z)}$$

对于采样器在闭环系统中具有各种配置的闭环离散系统典型结构图,及其输出采样信号的z变换函数 $C(z)$ ,可参见表7-3。

表 7-3 典型闭环离散系统及输出 z 变换函数

<table><tr><td>序号</td><td>系统结构图</td><td>C(z)计算式</td></tr><tr><td>1</td><td><img src="image/002728ff106242a52bb6af0213a4bff518754f4f4f3559f8039f22d1ed204f7f.jpg"/></td><td> $\frac{G(z)R(z)}{1+GH(z)}$ </td></tr><tr><td>2</td><td><img src="image/611f18b47f960340873c00583b4321ca9441049ea6458069b553920a7c7a9da8.jpg"/></td><td> $\frac{RG_1(z)G_2(z)}{1+G_2HG_1(z)}$ </td></tr><tr><td>3</td><td><img src="image/6610159bd641ee4acd0224c7bf322afe40423b74fd6c5b2277191ad057593493.jpg"/></td><td> $\frac{G(z)R(z)}{1+G(z)H(z)}$ </td></tr><tr><td>4</td><td><img src="image/e0b3df3bb6540b2ba2dbae900884f7fecfc21ec52f675beabd6ba452037d0de4.jpg"/></td><td> $\frac{G_1(z)G_2(z)R(z)}{1+G_1(z)G_2H(z)}$ </td></tr><tr><td>5</td><td><img src="image/3d53d6eadaa8292252032de6e21061b799190ada53db9af2a38c79c5ccffb81f.jpg"/></td><td> $\frac{RG_1(z)G_2(z)G_3(z)}{1+G_2(z)G_1G_3H(z)}$ </td></tr><tr><td>6</td><td><img src="image/ea056e44cab670f2c6dee7c89bc1742f5afc2b2d78b9bc799f01e95e2c327ccc.jpg"/></td><td>RG(z)/1+HG(z)</td></tr><tr><td>7</td><td><img src="image/07894177421be7d2714ef82f864c6fabb2a94599c603dbb69e3d5c75a501ec6b.jpg"/></td><td>R(z)G(z)/1+G(z)H(z)</td></tr><tr><td>8</td><td><img src="image/dd0a92bea326d36896195712ce6bbc35747f77066f3b5fe517ba5a39392484bd.jpg"/></td><td>G1(z)G2(z)R(z)/1+G1(z)G2(z)H(z)</td></tr></table>
