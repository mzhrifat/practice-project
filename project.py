import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix, classification_report, roc_curve, auc
from sklearn.cluster import KMeans
from scipy import stats

# Sample Dataset (Iris dataset for classification, Random dataset for regression)
from sklearn.datasets import load_iris

data = load_iris()
X_class = data.data
y_class = data.target

# Random dataset for regression
np.random.seed(42)
X_reg = np.random.rand(100, 1) * 10  # Random feature
y_reg = 2.5 * X_reg + np.random.randn(100, 1) * 2  # Linear relation with noise

# Mean, Median, Mode Calculation
mean_val = np.mean(y_reg)
median_val = np.median(y_reg)
mode_val = stats.mode(y_reg, keepdims=True)[0][0]
print(f"Mean: {mean_val}, Median: {median_val}, Mode: {mode_val}")

# Standard Deviation & Percentile Calculation
std_dev = np.std(y_reg)
percentile_90 = np.percentile(y_reg, 90)
print(f"Standard Deviation: {std_dev}, 90th Percentile: {percentile_90}")

# Data Splitting
X_train_class, X_test_class, y_train_class, y_test_class = train_test_split(X_class, y_class, test_size=0.2,
                                                                            random_state=42)
X_train_reg, X_test_reg, y_train_reg, y_test_reg = train_test_split(X_reg, y_reg, test_size=0.2, random_state=42)

# Feature Scaling
scaler = StandardScaler()
X_train_class = scaler.fit_transform(X_train_class)
X_test_class = scaler.transform(X_test_class)
X_train_reg = scaler.fit_transform(X_train_reg)
X_test_reg = scaler.transform(X_test_reg)

# Polynomial Regression
poly_features = PolynomialFeatures(degree=2)
X_train_poly = poly_features.fit_transform(X_train_reg)
X_test_poly = poly_features.transform(X_test_reg)
lin_reg = LinearRegression()
lin_reg.fit(X_train_poly, y_train_reg)
y_pred_reg = lin_reg.predict(X_test_poly)

# Scatter Plot for Regression
plt.scatter(X_test_reg, y_test_reg, color='blue', label='Actual')
plt.scatter(X_test_reg, y_pred_reg, color='red', label='Predicted')
plt.xlabel("Feature")
plt.ylabel("Target")
plt.title("Polynomial Regression")
plt.legend()
plt.savefig("pro11.jpg",format='jpg')
#plt.show()

# KNN Classifier
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train_class, y_train_class)
y_pred_class = knn.predict(X_test_class)

# Confusion Matrix
print("Confusion Matrix:")
print(confusion_matrix(y_test_class, y_pred_class))

# Classification Report
print("Classification Report:")
print(classification_report(y_test_class, y_pred_class))

# Cross Validation Score
cv_scores = cross_val_score(knn, X_train_class, y_train_class, cv=5)
print("Cross-Validation Scores:", cv_scores)
print("Mean CV Score:", np.mean(cv_scores))

# Decision Tree
dtree = DecisionTreeClassifier()
dtree.fit(X_train_class, y_train_class)
y_pred_tree = dtree.predict(X_test_class)
print("Decision Tree Classification Report:")
print(classification_report(y_test_class, y_pred_tree))

# Grid Search for Hyperparameter Tuning
param_grid = {'n_neighbors': [3, 5, 7, 9]}
grid_search = GridSearchCV(KNeighborsClassifier(), param_grid, cv=5)
grid_search.fit(X_train_class, y_train_class)
print("Best KNN Parameter:", grid_search.best_params_)

# AUC-ROC Curve (for binary classification, taking class 1 vs rest)
if len(np.unique(y_class)) == 2:
    y_score = knn.predict_proba(X_test_class)[:, 1]
    fpr, tpr, _ = roc_curve(y_test_class, y_score)
    roc_auc = auc(fpr, tpr)

    plt.figure()
    plt.plot(fpr, tpr, color='blue', lw=2, label=f'ROC curve (area = {roc_auc:.2f})')
    plt.plot([0, 1], [0, 1], color='gray', linestyle='--')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver Operating Characteristic')
    plt.legend(loc='lower right')
    plt.savefig("pro3.png",format='png')
    #plt.show()

# K-Means Clustering
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X_class)
cluster_labels = kmeans.labels_
plt.scatter(X_class[:, 0], X_class[:, 1], c=cluster_labels, cmap='viridis')
plt.title("K-Means Clustering")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.savefig("pro.png",format='png')
plt.savefig("pro1.png",format='png')
#plt.show()