import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle

def train_model():
    df = pd.read_csv('data/sample_training_data.csv')
    
    df['os_type'] = df['os_type'].astype('category').cat.codes
    
    X = df.drop('vulnerable', axis=1)
    y = df['vulnerable']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    
    model = RandomForestClassifier(n_estimators=100)
    model.fit(X_train, y_train)
    
    with open('ml_model/vuln_predictor.pkl', 'wb') as f:
        pickle.dump(model, f)
    
    print("[+] Model trained and saved as 'ml_model/vuln_predictor.pkl'.")

if __name__ == "__main__":
    train_model()