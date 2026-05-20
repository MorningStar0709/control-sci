# 7.4.5 Terrain Roughness Characteristics

One of the factors that is used in selecting an update area is the roughness and uniqueness of the terrain. The variation in terrain elevation provides what can be considered as the TERCOM signal, and the quality of this signal increases directly with increasing amplitude, frequency, and randomness of the terrain. It should be noted that the TERCOM concept will not work over all types of terrain. For instance, the rougher the terrain, the better TERCOM works. However, good terrain must be more than just rough, it must be unique (i.e., a given profile out of the TERCOM map must not resemble any other map. Terrain roughness is defined as the standard deviation of the terrain elevation samples (see Figure 7.19). It is usually referred to as “sigma-T” (or σ T ).

Sigma-T is defined by the equation

$$\sigma_ {T} = \sqrt {(1 / N) \sum_ {i = 1} ^ {N} (H _ {i} - \bar {H}) ^ {2}}, \tag {7.16}$$

where $\bar { H } = ( 1 / N ) \Sigma _ { i = 1 } ^ { N } H _ { i }$

Thus, $\sigma _ { T }$ is a measure of the variation of the terrain elevation about its average elevation. Note that the minimum value of σT required to support TERCOM operation is approximately 25 ft (7.62 m). Areas that have sigma-T values of fifty or greater are usually considered as good candidates for TERCOM fix areas. Obviously, lakes and very flat or smooth areas have low values of sigma-T . Therefore, they are not suitable as fix areas. However, sigma-T is not the only criterion for determining whether a given area is suitable for TERCOM operation.

![](image/73cb3fd1706066a269ef45af79b60692d8538e29428e926600f576f6b9a92dba.jpg)

<details>
<summary>text_image</summary>

Mean elevation
Terrain profile
H₁
H̅
Mean sea level
</details>

Fig. 7.19. Terrain standard deviation $( \sigma _ { T } )$ .

![](image/da43b55beb426e54081241eb73c7cf4d12dbabee53c1df54acb4c4302350c3a5.jpg)

<details>
<summary>text_image</summary>

Terrain profile
D_i
H_i
H_{i+1}
Mean sea level
</details>

Fig. 7.20. Definition of sigma-Z.
