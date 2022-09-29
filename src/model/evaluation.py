from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

def model_evaluation(model, dataset):
    y_pred = model.predict(dataset['x_test'])
    print(classification_report(dataset['y_test'], y_pred, digits=4))
    return accuracy_score(dataset['y_test'], y_pred)
    