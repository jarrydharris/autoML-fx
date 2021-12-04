# autoML-fx
 
*Work in progress*
 
## Demo
 
[Click here!](https://automlservice-5gzjmk3g3a-uc.a.run.app/) (Might be slow to boot, currently working on this)
 
## Description
 
This is my first experiment with combining autoML and MLOps. To create a use case for these two ideas I needed data that I can update each day for free, so I went with [foreign exchange rates](https://freecurrencyapi.net).
 
The sample space you trained your model on won't always match the data you are trying to predict. Updating models to reflect the seasonality of the data may be necessary. This presents an issue for businesses who take a greenfield approach to data science. Automating the collection of new data, training, storage and deployment of models keeps applications running with little to no downtime.
 
This project involves using GitHub Actions to:
 
1. Download up to date data.
2. Run an AutoML package to find and tune the best model on the up-to-date dataset.
3. Containerize and deploy the resulting app for production.
 
## Future work

- Speed up the start of a new instance.
- Set up CRON jobs for data collection/model training.
- Store historical models for governance/compliance.
- Make the app a little more interesting.
