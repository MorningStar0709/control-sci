The interstitial distance or cell size is denoted by d, and L = N d is the length of the profile used for correlation. In a typical application, d = 800 ft and N = 32, so that $L = 2 5 { , } 6 0 0$ ft. As the air vehicle approaches the fix area, TERCOM begins to acquire two altitude measurements during every interval d. One of the two is altitude above MSL, whereas the other is the altitude above the terrain. Acquisition of these measurements is continued until the vehicle is well past the fix area. Each pair is differenced, with the result that the sequence of differences yields an estimate of terrain profile along the vehicle track. There are two general approaches to TERCOM fix taking. One is referred to as long sample–short matrix (LSSM), and the other is referred to as short sample–long matrix (SSLM). These two concepts are illustrated in Figure 7.16.

In both cases, the matrix is made wide enough to accommodate the crosstrack arrival uncertainty. For LSSM, the acquired sample is long enough to accommodate the downtrack uncertainty, whereas for SSLM the stored matrix is long enough to accommodate the downtrack uncertainty. The LSSM is used whenever the vehicle arrival uncertainty is relatively large or if only small fix areas are available. The SSLM is also employed during a multiple fix-taking mode. In this latter mode, faster updating is achieved, provided the search area (i.e., navigation uncertainty) is kept small, and data for a longer matrix are available. The length L of the data interval is the same for either mode. For SSLM, only one sample set of length L is used. For LSSM, the first sample set is correlated, and the result (minimum residue and location) is saved. The first point that was gathered is then dropped, and another point is collected, and the correlation process is repeated until the correlation is complete. Some of the TERCOM characteristics can be summarized as follows:

![](image/6a44075465450614d379bec2b5eaae4e8ebfe9442f5e5987563a861f1d327ad0.jpg)

<details>
<summary>text_image</summary>

d
Nd
Vehicle track
</details>

Fig. 7.15. Definition of fix area and cell size.

![](image/7651da1b1f79c393ea830368b88901d124415a946228c909bb6662c9ef62bba4.jpg)

<details>
<summary>text_image</summary>

Acquired data
Tercom matrix
Downtrack uncertainty
Acquired data
Crosstrack uncertainty
(a) Long sample-short matrix
(b) Short sample-long matrix
</details>
