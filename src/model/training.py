import mlflow

def model_training(dataset, sklearn_model, mlflow_experiment_name = "iris_dataset"):
    mlflow.set_experiment(mlflow_experiment_name)
    mlflow.sklearn.autolog()

    # Initial the model
    if sklearn_model == "RandomForestClassifier":
        from sklearn.ensemble import RandomForestClassifier
        model = RandomForestClassifier(n_estimators = 100)
    elif sklearn_model == "DecisionTreeClassifier":
        from sklearn import tree
        model = tree.DecisionTreeClassifier()
    
    # Training the model.
    with mlflow.start_run() as run:
        model = model.fit(dataset['x_train'], dataset['y_train'])
        
    return model, run