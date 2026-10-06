import pandas as pd
import mlflow
import mlflow.sklearn

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
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

model = RandomForestClassifier(random_state=42)

param_grid = {
    "n_estimators": [50, 100, 200],
    "max_depth": [3, 5, 10, None],
    "min_samples_split": [2, 5, 10],
    "max_features": ["sqrt", "log2"],
}

grid_search = GridSearchCV(
    estimator=model,
    param_grid=param_grid,
    cv=5,
    scoring="f1_macro",
    n_jobs=-1,
)

grid_search.fit(X_train, y_train)

best_model = grid_search.best_estimator_

y_pred = best_model.predict(X_test)
test_accuracy = accuracy_score(y_test, y_pred)

mlflow.set_experiment("iris-hyperparameter-tuning")

with mlflow.start_run(run_name="grid_search_random_forest"):
    mlflow.log_param("model", "RandomForestClassifier")
    mlflow.log_param("search_type", "GridSearchCV")
    mlflow.log_param("cv_folds", 5)
    mlflow.log_param("total_fits", len(grid_search.cv_results_["params"]) * 5)

    mlflow.log_params(grid_search.best_params_)
    mlflow.log_metric("cv_f1_macro_mean", grid_search.best_score_)
    mlflow.log_metric("test_accuracy", test_accuracy)

    mlflow.sklearn.log_model(best_model, "model")

    print("Grid Search Random Forest")
    print(f"Best Parameters: {grid_search.best_params_}")
    print(f"CV F1 Macro: {grid_search.best_score_:.4f}")
    print(f"Test Accuracy: {test_accuracy:.4f}")
    print(f"Total Fits: {len(grid_search.cv_results_['params']) * 5}")