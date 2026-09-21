# Data Pipeline Documentation

## 1. Collect

**Purpose:** Collect the Iris dataset.

**Input:** Iris dataset from scikit-learn.

**Output:** `data/raw/iris_raw.csv`

The collect stage loads the Iris dataset, maps target values to species names, adds the collection timestamp, and saves the raw dataset.

## 2. Preprocess

**Purpose:** Preprocess the collected dataset.

**Input:** `data/raw/iris_raw.csv`

**Output:** `data/processed/iris_preprocessed.csv`

**Validation/Processing Rules:**
- Remove duplicate records.
- Coerce numeric columns to numeric types.
- Impute missing numeric values using the column median.
- Drop rows with missing species.
- Remove the `collected_at` column.

## 3. Features

**Purpose:** Perform feature engineering.

**Input:** `data/processed/iris_preprocessed.csv`

**Output:** `data/processed/iris_features.csv`

The feature engineering stage creates:
- `sepal_area`
- `petal_area`
- `sepal_to_petal_length_ratio`
- `petal_length_bin`

## 4. Validate

**Purpose:** Validate the engineered dataset.

**Input:** `data/processed/iris_features.csv`

**Output:** Validation result.

**Validation Rules:**
- Check that the expected columns are present.
- Check that species values are valid.
- Check that feature values are within the expected ranges.
- Raise a validation error if any check fails.

## Pipeline Flow

```text
Collect
   |
   v
data/raw/iris_raw.csv
   |
   v
Preprocess
   |
   v
data/processed/iris_preprocessed.csv
   |
   v
Features
   |
   v
data/processed/iris_features.csv
   |
   v
Validate