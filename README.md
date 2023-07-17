# Least-squares-regression
In this assignment we were asked to create a dataset with the noise and then fit it using linear regression. It was found out thta as the number of points in the dataset (N) increases, r - correlation coefficient decreases and plot becomes more recognizable. 

## Introduction
This assignment focuses on simulating sparse and noisy observations of a physical phenomenon that follows an exponential decay, represented by the equation y=y0exp(-kx). The task involves generating random measurements of x within a specified range, with varying data points and fixed y0 values. The data is then subject to random noise, with the maximum absolute noise specified as input. The goal is to study the effectiveness of the least square regression procedure in analyzing the data. The main hypothesis for the first part is that as the number of elements increases plot should have a better fit. And the main hypothesis for the second part is the as the noise level decrease, data should be less distorted and have a higher value of correlation coefficient R.

## Methods
Plotting data with different N's


Part 1.1
![image](https://github.com/leilaakisheva/Least-squares-regression/assets/128895782/b85ec066-d12a-4d97-b6ea-e14805706dfb)
![image](https://github.com/leilaakisheva/Least-squares-regression/assets/128895782/d78b6023-d358-428f-8325-361f2c3664a3)

R squared: 0.863416464072008
Relative error: 0.00969077463711626


Part 1.2
![image](https://github.com/leilaakisheva/Least-squares-regression/assets/128895782/5da809bc-b555-41eb-a871-31ec161c4b82)
![image](https://github.com/leilaakisheva/Least-squares-regression/assets/128895782/1f270be5-98a1-4361-9948-c5832ef24f19)

R squared: 0.9221551940265046
Relative error: 0.08197397600919082


Part 1.3
![image](https://github.com/leilaakisheva/Least-squares-regression/assets/128895782/d4d2f10d-5d6e-4e94-b1f9-7f065c23141a)
![image](https://github.com/leilaakisheva/Least-squares-regression/assets/128895782/b575de98-a23e-4024-ba46-5c4a0bd65754)

R squared: 0.9332871565780241
Relative error: 0.21199319862439356


Part 1.4
![image](https://github.com/leilaakisheva/Least-squares-regression/assets/128895782/16208131-7c6d-47b2-9c2f-422dc84e317b)
![image](https://github.com/leilaakisheva/Least-squares-regression/assets/128895782/7b77fcfa-d9ba-4f85-87ab-a4059ccde965)

R squared: 0.9493953939384118
Relative error: 0.018424882279282285

Part 2.1
![image](https://github.com/leilaakisheva/Least-squares-regression/assets/128895782/8a0a7e4d-4734-4f76-9463-d321431f028e)
![image](https://github.com/leilaakisheva/Least-squares-regression/assets/128895782/e417398e-2c8a-4b4a-ad5b-ccc919a1de97)

Noise 2.0451527187306624, 


Part 2.2
![image](https://github.com/leilaakisheva/Least-squares-regression/assets/128895782/1c01faa0-4c9c-469f-b40c-bc272f2deb74)
![image](https://github.com/leilaakisheva/Least-squares-regression/assets/128895782/18256113-f5cb-473e-8b98-77ebf80750c3)

Noise 1.434543926925878


Part 2.3
![image](https://github.com/leilaakisheva/Least-squares-regression/assets/128895782/496b6fbb-a575-432b-a149-a5bf6dec9aad)
![image](https://github.com/leilaakisheva/Least-squares-regression/assets/128895782/f95e26d1-8c48-400f-bb20-1826834f2ba2)

Noise 0.9216610230621303


Part 2.4
![image](https://github.com/leilaakisheva/Least-squares-regression/assets/128895782/effab363-9ce4-4f91-bbb6-861cefaabf3c)
![image](https://github.com/leilaakisheva/Least-squares-regression/assets/128895782/bd890bd0-3c57-4553-80a6-7d0f154e6d0f)

Noise 0.060559856063391496


## Results
As it can be seen in the plot 1.1-1.4 as the number of elements in the dataset increases, out exponential fit becomes better. Moreover the Table-1, values of the R-squared slightly increases with the number of elements, so the correlation becomes better. This can be explained by the fact that as the number of points increases, there is a higher probability that more points will be at the best fit line.

In the plot 2.1-2.4 it can be seen that for N=30 and decreasing noise levels, R-squared also decreases. However, comparing with the first part, there is a dramatic increase in correlation with the decrease of noise. And in the Table-2 one can see numerical results of this. Also, relative error drops from 22% to 0.01%.

 N    R squared    Rel. error
---  -----------  ------------
 20      0.86342       0.00969
 30      0.92216       0.08197
 40      0.93329       0.21199
100      0.9494        0.01842

In this assignment it was asked to complete linear regression on the exponential decay function and compare results as the number of points and noise levels vary. The results are consistent with the hypothesis, so the method is successful
