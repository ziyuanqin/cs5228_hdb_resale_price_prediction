# cs5228_hdb_resale_price_prediction

Overall, all preprocessing and feature engineering steps seem meaningful, including the creation of new location/distance-based features.

Probably not a big deal, but it is not obvious where the ranking for FLAT_TYPE comes from. For example, "executive" flats have 3-4 bedrooms, so it's not obvious why they have a higher rank than "5-room" flats.

General comment for the final report. You want to ensure that the plots are readable and have sufficient font size.

Slide 10: A correlation analysis is never a bad idea, but in your project you may want to add some discussion about what information you get out of this. This includes that this figure only shows a linear correlation, and why this might be some limitation.

Slide 11: Similarly, it's not clear how you use the information about outliers. Are you removing them?

Slide 12 (next steps)

- Depending on your total number of models you may consider, you could limit hyperparameter tuning to only the most promising one. No need to tune a model that just performs poorly.
- Apart from just bringing the RSME, you may also want to explore any other insights the data or the model(s) tell you. A good model is not just one that makes good predictions.
- You may not have enough time to explore all possibilities – not worries, this is by design. So you may need to make informed decisions which directions could be more promising than others.

Lastly, as a general comment, always keep an eye on the deadline. You want to start early with your final report to avoid rushing it. After all, the final report is the main assessment component. There is no need to spend too much time just to squeeze out a slightly better ranking in Kaggle.
