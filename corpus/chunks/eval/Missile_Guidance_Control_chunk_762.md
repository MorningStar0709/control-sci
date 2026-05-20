# 7.4.4 Data Correlation Techniques

In Section 7.4.3 the data correlation process was briefly discussed as part of determining vehicle position. In this section we will discuss the terrain correlation technique in more detail. The TERCOM process involves matching the measured contour of the terrain along the ground track of the air vehicle with each downtrack column of the reference matrix that is stored in the vehicle’s onboard digital computer memory prior to flight. Since the TERCOM system is not noiseless, the terrain profile measured during flight will probably never exactly match one of the reference matrix profiles.

A fundamental assumption of the terrain correlation process is that the geographic distance between the measured terrain elevation profile and the best-matching reference matrix column provide an excellent measure of the downtrack and crosstrack position errors of the vehicle as it flies over the reference matrix area.

There are a number of correlation algorithms (e.g., mean squared difference (MSD), mean absolute difference (MAD), the normalized MAD, the normalized MSD, and the product method) of varying complexity and accuracy that can be used to correlate the measured data with the reference data. Furthermore, the MAD algorithm provides the best combination of accuracy and computational efficiency for performing real-time terrain contour matching in an onboard computer environment. Therefore, here we will discuss only the MAD and MSD correlation algorithms.

Suppose now that the first N differences have been acquired. Then, these differences are removed, so that the sample profile is its mean value. Next, this profile is compared with each row of matrix data in the following manner. Let $h _ { n } ( 1 \leq n \leq N )$ denote any row of matrix data and $H _ { n }$ the sequence of required data. Consequently, the MAD algorithm, which is used for correlating the measured terrain elevation file with each downtrack column of the reference matrix, is defined as follows [6]:

$$M A D _ {k, m} = (1 / N) \sum_ {i = 1} ^ {N} | h _ {k, m} - H _ {m, n} |, \tag {7.13}$$

where
