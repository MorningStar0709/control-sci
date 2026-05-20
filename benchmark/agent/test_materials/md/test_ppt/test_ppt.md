第6章 无限冲激响应(IIR）滤波器设计

## **A1**

6.1  滤波器的基本概念；

6.2  模拟低通滤波器设计；

6.3  模拟高通、带通及带阻滤波器设计；

6.4   冲激响应不变法；

6.5   双线性Z变换法；

6.6  数字高通、带通及带阻滤波器设计；

6.5 用双线性Z变换法设计 IIR DF

放弃上一节的线性转换关系，找新的关系

**A1**

这种关系应该保证：

![](image/632e5045eb8cb1dac89ea6106f121844666f179080789a435190d78628ab0699.jpg)

双线性z变换

满足上述4个条件的映射关系为

双线性z变换

即

![](image/9cefeef1cbfc78f664bf6e77394dfad976fdfb1d100765baee32cbb325b202ef.png)

(6.5.3)

(6.5.4)

非线性关系，但是一对一的转换

![](image/46fd8242faefe5aa732276070c1273104c5875eb54acec5b1d8861749c377a17.jpg)

数字低通滤波器的设计步骤：

Step1.

Step2.  频率转换：

Step3.

Step4.

![](image/1598533d3833dd9c05085e4e7174133e672389607939b8ebbd81fdd090a87310.jpg)

所以：

这样：系数         可以省略，因此，双线性Z变换又可定义为 ：

这一组定义和前面的定义，对最后的 DF 而言，结果是一样的，差别是中间设计的 AF， 由于缺少了频率定标

![](image/1a8ce284e63a1a5da2749991fbbbc3a822e37b748a33f9f0982fabcd072ba928.jpg)

![](image/94d89c3ae5e76547cf658e7c7cb60be50db1d80035f2ca9c3d4057b4aacbfed4.jpg)

![](image/9f75d0c99bc84609b2c91abbad4c5aa9681dff8758e77f54f7c290c1f4fab1cd.jpg)

![](image/80235e6da533e2982acc1b0163a5c131c33666d6f130b0d4f56869028e3086a7.jpg)

![](image/e787f94d454e89fa7bd28165f6f99e6bd2cf38a878d6a7393792ca8c4ebf38ed.png)

![](image/2ef8294e276375df88d17d25174319954aceff49e303b3c8b609ec5ffae01442.jpg)

![](image/77b397521fe6c8cb1be5d4f861e72adaf36eaf764be2ad2d08398a210b6f5985.png)

![](image/adfd834866aa395f14a6a110bf9b5dfc340137ba7d3f5c5616001b7855685d89.jpg)

![](image/3e3f1dddc248c9618a75923f5aaa014f534756f0adb9853a9313ac60325f9458.jpg)

![](image/c9305645643a93d4b586aaaf990fb8bfada11859d0fd9cd3e0a67a054dafa53c.jpg)

![](image/765e65b72ed2bab2b26e4e2b01f3bd0bbefd5365ca8de4fd163412fe690cac13.jpg)

![](image/0087035f8f5da753608f741749ebadafd1fc7a0416e4d7fb57592bd05b284d15.png)

![](image/0819da535e8754da09f89598d7b1a631612ad630fa894171047fafa74ea2d4c3.jpg)

![](image/0e9bdce754ae5200481a6308a0fc0444b6ef96682a200cb1b85ad6eaca9428e9.jpg)

![](image/cd8301879ce15552d128e52988a275d4b0e3f99bf82278578bbe7209ec345f5e.jpg)

![](image/fd0f1cb90ecbfa272f3c82dfe9b5ac0a5aa06d38079a4973f2cb761b76240b96.jpg)

![](image/b2cea6a2cfdbef33d31fe6c73171b11eeb34c36460ad0112a8dbff3cd51f8ad2.jpg)

![](image/9956bb4b238c9f7de5ca6904efd5d949d1fa0b7f78c9f90ddbc97dc7c5946a72.jpg)

![](image/5085a0a302067b7b5a5a3a31302dce7c86610287ab57ad49b4c9ab67dd063fb7.png)

6.6 数字高通滤波器的设计

**给出**

**数字高通**

**的技术要求**

**得到**

**模拟高通**

**的技术要求**

**得到**

**模拟低通**

**的技术要求**

**最后得到**

**数字高通转移**

**函数**

**得到**

**模拟高通转移**

**函数**

**设计出**

数字高通滤波器设计步骤

![](image/5aa772a3921f7aac8ff75d4100a70207dc8c8a0b748ae64f05ecc42887b0597d.jpg)

![](image/bac4e1818c778e46f49e85691197905519c7844598b6780350f912da21cbcd28.jpg)

![](image/a9dafd86df140ff77fda62fc7713edba6f637690accc2e9d794a35995736c804.jpg)

![](image/d8feed394679e6970c6e85d0a2e60dcbe74badad20d7788d6c358d5853cd2190.jpg)

![](image/546a22eef78d6e1ddb83607fae99d324efc3452a91972e880fc312cc77e9ab87.jpg)

![](image/d3492a0b7e013e912226584f80074045ee262d50e9ede566aad054854292172c.jpg)

![](image/c7dc8f8615a90f0f06aef44a9984a7f49d186e1d3652683f91ec7a5c82b44962.jpg)

![](image/ee67baf88cdd29452b0307082b4506f09e8cef7b489f2bd73e1e12c05126cded.jpg)