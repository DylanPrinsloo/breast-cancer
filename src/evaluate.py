# evaluation
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import f1_score, roc_auc_score, roc_curve, classification_report, accuracy_score

def evaluate_model(model, data_gen, steps):
    y_true = []
    y_pred = []
    for i in range(steps):
        x_batch, y_batch = next(data_gen)
        predictions = model.predict(x_batch)
        predictions_bin = (predictions >= 0.5).astype(np.int32)
        y_true.extend(y_batch.flatten())
        y_pred.extend(predictions_bin.flatten())
        if i % 20 == 0:
            plot_single_prediction(x_batch, y_batch, predictions_bin)
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    if np.array_equal(np.unique(y_true), [0, 1]) and np.array_equal(np.unique(y_pred), [0, 1]):
        f1 = f1_score(y_true, y_pred)
        auc = roc_auc_score(y_true, y_pred)
        print(f'F1-Score: {f1}')
        print(f'AUC: {auc}')
        fpr, tpr, _ = roc_curve(y_true, y_pred)
        plt.figure()
        plt.plot(fpr, tpr, marker='.')
        plt.title('ROC Curve')
        plt.xlabel('False Positive Rate')
        plt.ylabel('True Positive Rate')
        plt.show()
        print(classification_report(y_true, y_pred))
    else:
        print("Error: y_true or y_pred is not in the expected binary format.")
