# autoML-fx

*Work in progress*

## Demo

[Click here!](https://automlservice-5gzjmk3g3a-uc.a.run.app/)

## Description

This is my first experiment with combining autoML and MLOps. To create a use case for these two ideas I needed data that I can update each day for free, so I went with [foreign exchange rates](https://freecurrencyapi.net).

You cant always assume that the sample space you trained your model on remains constant, so updating models to reflect the seasonality of the data may be necessary. This presents an issue for businesses who want to leverage their data in a greenfield approach. Automating the collection of new data, training, storage and deployment of models means the data scientist can keep models up to date without interupting users.

This project involves using GitHub Actions to:

1. Download up to date data.
2. Run an AutoML package to find and tune the best model on the up-to-date dataset.
3. Containerize and deploy the resulting app for production.

# Future work

- Set up CRON jobs for data collection/model training
- Store historical models for governence/complience.
- Make the app a little more interesting