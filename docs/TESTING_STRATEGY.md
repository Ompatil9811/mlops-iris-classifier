\# Testing Strategy – MLOps Iris Classifier



\## 1. Introduction



The purpose of this testing strategy is to verify the correctness, reliability, and quality of the MLOps Iris Classifier project. Automated tests are implemented using pytest to check individual pipeline components and model performance.



\## 2. Testing Framework and Tools



\* \*\*Pytest:\*\* Executes automated test cases.

\* \*\*Pytest-Cov:\*\* Measures code coverage.

\* \*\*JUnit XML:\*\* Generates a machine-readable test results report.

\* \*\*Python:\*\* Programming language used for the project.



\## 3. Types of Testing



\### 3.1 Unit Testing



Tests individual functions, including preprocessing, feature engineering, and data validation.



\### 3.2 Model Testing



Checks whether model predictions belong to the expected Iris species labels and whether the model meets the minimum accuracy threshold defined in the test.



\### 3.3 Pipeline Testing



Verifies that model training completes successfully and produces predictions with the expected shape and probability values.



\### 3.4 Data Validation Testing



Checks that valid data passes validation and that invalid data, such as missing columns, invalid species, or out-of-range values, is rejected.



\## 4. Test Execution



The complete test suite is executed using:



```bash

pytest --cov=src --cov-report=term-missing --junitxml=test-results.xml

```



\## 5. Test Results



The test suite contains 16 automated tests across five test files.



\* Total tests: 16

\* Passed: 16

\* Failed: 0

\* Execution time: 3.04 seconds

\* Overall source-code coverage: 27%



\## 6. Test Reports



The `test-results.xml` file stores test execution results in JUnit XML format. The coverage report identifies which source-code statements were executed during testing.



\## 7. Conclusion



All 16 automated tests passed successfully. The tests verify preprocessing, feature engineering, data validation, model training, and model quality. The current overall source-code coverage is 27%, indicating that additional tests could be added to cover more of the project.



