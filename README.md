# Ghost Lots
## Introduction
Between 2002 and 2013, the Bloomberg administration rezoned 37% of the New York City as part of a new development policy. Belowis an actual pamphlet from that proposal— The areas in red are those to be rezoned. Many now directly tie this rezoning to rapid, widespread displacement in NYC.

![Noise](https://jblinder.github.io/images/project03/research-1.jpeg)

In the past, vacant lots have been signs of both blight and development potential. Given this recent, dramatic rezoning history, can vacant lots be used as predictors for new development? 

## Data
The main dataset I used for this research is the [NYC PLUTO](https://www1.nyc.gov/site/planning/data-maps/open-data/dwn-pluto-mappluto.page) dataset, which contains tax lot level data about most properties in all 5 boroughs. Brooklyn was the main focus for the first iteration.

## Analysis
One of the first analyses was to see the geographic distribution of vacant lots— here we can see that the majority of the distribution lies in industrial areas like ports, and along the north and northeast neighborhoods.

![Noise](https://jblinder.github.io/images/project03/eda-2.jpeg)

The main outcome I wanted to predict is whether a lot that’s currently vacant will convert to a building in the future. To predict this, I had to engineer a dependent variable that determines if existing buildings in 2017 used to be vacant in the 2013 version of the PLUTO dataset. 

![Noise](https://jblinder.github.io/images/project03/eda-3.jpeg)

## Modeling

Modeling was tricky because of the state of my data. There were vastly fewer vacant lots that converted since 2013 than those that remained vacant, around 3%. Using smote helped a little, but these steps were not very effective.

The two best performing models were Logistic and Random Forest models, the latter proving best on both precision and recall.

There is some trade-off between precision and recall. Since it was key to not miss vacant lots that might convert, recall was more important. Additionally, finding false positives would likely be it wouldn’t hurt their efforts.

![Noise](https://jblinder.github.io/images/project03/performance-1.jpeg)

Among the top important features were the number of buildings on a lot, the total value of assessed land, and building area.

## Predictions

After validating the model, my next step was to run predictions for all of the currently vacant lots in Brooklyn. One area that the model seemed to do well in was Red Hook and Gowanus. Red Hook has been massively developed for a number of years, and Mayor Bill DeBlasio will soon rezone Gowanus for more mixed us and residential building. As we can see here, most of the vacant lots in both neighborhoods were highly predicted as being developed in the next 4 years.


![Noise](https://jblinder.github.io/images/project03/prediction-1.jpeg)

![Noise](https://jblinder.github.io/images/project03/prediction-2.jpeg)

One area where model results seemed a bit more suspect was Downtown Brooklyn, which has also been massively developed in the past decade. Right around the Barclays Center and Fort Greene Park, there were a significant number of lots that were predicted as not being developed in the next 4 years. We’re interested in trying to find what variables might be playing a role in these particular predictions.

## Conclusion

As the city and third-parties release more nuanced types of civic data, it's interesting to consider what might be emerging markers of impending development. For instance, citi bikes, public wifi, potholes, and surveillance cameras might be telling signifiers of urban shifts. A future direction for this project will be exploring these trace data points.