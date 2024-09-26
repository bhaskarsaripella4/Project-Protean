from sklearn.pipeline import Pipeline
from pandas import read_csv
from pycaret.datasets import get_data



insurance = read_csv('../Datasets/insurance_dataset_kaggle.csv')

from pycaret.regression import *
r1 = setup(insurance, target = 'charges', session_id=123, normalize=True,
           polynomial_features=True, feature_selection=True,
           bin_numeric_features=['age','bmi'])

lr = create_model('lr') #automatically picks the r1 variable
save_model(lr,model_name = 'pycaret_pipeline_Nov12023')

y = insurance['charges']
X = insurance.drop(columns = ['charges'])
ratio = int(len(X)*0.8)

X_train,X_test = X[:ratio],X[ratio:]
y_train,y_test = y[:ratio],y[ratio:]

print(X.head())
print(y.head())
print(X_train.shape,X_test.shape, y_train.shape,y_test.shape)