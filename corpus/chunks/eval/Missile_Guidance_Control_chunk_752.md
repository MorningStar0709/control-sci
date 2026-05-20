# 7.4.2 Definitions

At this point, it is appropriate to define some of the terms that the reader will encounter in the discussion of TERCOM.

Cell – One terrain elevation value in a matrix of terrain elevation values.

Cell Size – The geographic distance between TERCOM matrix cells.

Correlation Length – The distance one has to go from a given terrain elevation profile to another parallel terrain elevation profile such that the value of the normalized autocorrelation function for the given profile is reduced to a value of 1/e.

False Fix – A false fix has occurred when the distance between the TERCOM fix was position and the actual vehicle’s position at the time that the TERCOM fix was taken exceeds the terrain correlation length.

Ground Track Signature – The shape or signature of the groundtrack profile is obtained by subtracting the RTS (radar terrain sensor or radar altimeter) measurement from the RAS (radar altimeter sensor) measurement. The subtraction removes the effects of any vertical motion of the airborne vehicle. The mean of the data is removed in the data processing, thus eliminating any requirement for absolute accuracy in the RTS or RAS.

MAD – Mean absolute difference. This is the difference between stored and acquired data, and it is expressed in terms of the difference between the measured terrain elevation and stored reference matrix.

MAD Residue – A measure of the degree of correlation between two one-dimensional sets of data. A MAD residue of zero represents perfect correlation (i.e., identical data). The value of the minimum MAD residue for a matrix represents the amount of noise present in the system.

Map Description Data – These data include the parameters that define the location, orientation, size, and other characteristics of the terrain correlation maps.
