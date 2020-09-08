# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) 'The Mix, the Master and the Model'
Classifying Spotify tracks by decade using auditory features

# Contents
- [Summary](#summary)
- [Data](#data)
- [Analysis and Cleaning](#analysis)
- [Modelling](#modelling)
- [Conclusions](#conclusions)

<a id='summary'></a>
# Summary

This project aims to predict the decade of a song's release based on auditory features determined by Spotify. As with most classification problems, my main metrics were accuracy, precision and recall. Along the way I aimed to study the changing tastes of music, and I found that some events in the history of music production were reflected in the data. For instance, music has got measurably 'louder' over time, as better technology allows mastering engineers to normalize a track closer to the maximum output of a speaker. The main blockers I found were sampling bias in selecting tracks, class imbalance in the song decades, duplication in the different versions of a song, and the fact that genre is often more distinguishing than period.

<a id='data'></a>
# Data

Spotify API does not allow users to access the audio files of their tracks (for obvious reasons), but rather gives developers a range of features they have extracted from analysis of those files, namely:

    danceability, key, energy, mode, loudness, speechiness,
    acousticness, instrumentalness, liveness, valence, tempo, duration_ms
    
While attributes such as key, tempo, duration and loudness are more objective (although Spotify's low-level analysis includes confidence intervals for them, to account for things like tempo/key changes), the majority are somewhat subjective and stem from the Spotify team's own signal processing techniques. The more obvious descriptive data, such as release dates and artist/album/song names, were easily accessible, and I got my target from taking the start of the decade of release date.

Through scraping the Billboard top 100 artists' tracks, I found that my data overwhelmingly came from the 2010s, so I addressed this by adding the top 10 artists of every key genre since 1950. However, there was still a large class imbalance towards tracks released later. In the end, I addressed this by oversampling with the Synthetic Minority Over-sampling Technique (SMOTE).

<a id='analysis'></a>
# Analysis and Cleaning

Preliminary EDA showed that some unintended outliers had presented themselves: there was an album from the 1930s (outside the scope of this study), as well as a track that was louder than possible. The 'loudness' feature is represented with 'digital full scale', meaning a negative system where 0dB represents a signal's maximum representable value. Any louder than this and a track produces a form of distortion known as clipping, which is never permitted in professional production. However, Eminem's 'So Bad' came out at 0.496dB loudness; as a professionally produced track and an extreme outlier, I decided this was likely a Spotify analysis error and discounted it.

Additionally, I found that there were many instances of wrongly dated tracks. These included compilations, 'best of' albums, greatest hits, remasters, deluxe and anniversary editions, all of which were dated much later than their actual release. Since this would logically lead to misclassifications, I removed all of the above from the dataset.

<a id='modelling'></a>
# Modelling

The various cleaning techniques I used only got me to an 11.6% increase in accuracy over the baseline. In early tests, Logistic Regression outperformed K-Nearest Neighbours and Decision Tree Classifiers (DTCs), so I optimized by tuning the parameters of the logit model with gridsearching. I experimented with bagging the logistic regression models to reduce variance, but this did not impact results significantly. In addition, the confusion matrix showed that my model was mainly predicting the largest classes (2000 and 2010), so I had to address the class imbalance. My chosen method was Synthetic Minority Over-sampling Technique for Nominal and Continuous (SMOTE-NC), which was the only oversampler allowing me to mix both continuous variables (like loudness) with categorical ones (such as time signature). While raising the precision of the worst-represented classes, this reduced the overall accuracy score. In the end, random forest models generalised the best, as they combine bagging and random feature selection to reduce the variance inherent in decision trees, which are prone to overfitting.

I then approached the data from different angles to gain new insights. Running linear regression on loudness alone to predict months since 1984 (when [Pro Tools](https://en.wikipedia.org/wiki/Pro_Tools) brought professional production to the masses) rendered a lowly score of 5.1%, but one which still implies a positive trend.

Restricting the data to the middle 7 years of each decade, to greater distinguish the classes, did not end up providing significant advantages over existing models (only 1.6% difference from the earlier random forest). Finally, binarizing the problem into predicting pre-2000 and post-2000 songs did bear fruit, with 77.5% accurate predictions (18.8% above the baseline).

<a id='conclusions'></a>
# Conclusions

- We can achieve 33% accuracy over the baseline in classifying the decades of songs based on their features. Random forest algorithms handle this problem most effectively, especially oversampling with SMOTE-NC.
- We can predict, with 77.5% accuracy (18.8% above the baseline), whether a song was released pre- or post-2000.
- Loudness is the defining feature in determining how the sound of music has changed over the epochs. As we initially hypothesized, it all comes down to the master!
- For modern producers, whether you like the new production standards or not, a loud master is now the default for popular tracks, and you may need to stick to it to earn success.
