from sklearn.externals import joblib
from save_model import save_model


joblib.dump(model,'model_joblib')

mj=joblib.load('model_joblib')

mj.coef_