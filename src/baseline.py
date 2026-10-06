import pandas as pd
import mlflow
import mlflow.sklearn

from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

DATA_PATH = "data/processed/iris_features.csv"

FEATURE_COLS = [
    "sepal length (cm)",
    "sepal width (cm)",
    "petal length (cm)",
    "petal width (cm)",
    "sepal_area",
    "petal_area",
    "sepal_to_petal_length_ratio",
]

TARGET_COL = "species"

df = pd.read_csv(DATA_PATH)

X = df[FEATURE_COLS]
y = df[TARGET_COL]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y,
)

model = DecisionTreeClassifier(random_state=42)

cv_scores = cross_val_score(
    model,
    X_train,
    y_train,
    cv=5,
    scoring="f1_macro",
)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)
test_accuracy = accuracy_score(y_test, y_pred)

mlflow.set_experiment("iris-hyperparameter-tuning")

with mlflow.start_run(run_name="baseline_decision_tree"):
    mlflow.log_param("model", "DecisionTreeClassifier")
    mlflow.log_param("cv_folds", 5)

    mlflow.log_metric("cv_f1_macro_mean", cv_scores.mean())
    mlflow.log_metric("test_accuracy", test_accuracy)

    mlflow.sklearn.log_model(model, "model")

    print("Baseline Decision Tree")
    print(f"CV F1 Macro: {cv_scores.mean():.4f}")
    print(f"Test Accuracy: {test_accuracy:.4f}")