import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

# ==========================================
# LOAD DATASET
# ==========================================

data = pd.read_csv("health_dataset.csv")

# ==========================================
# REMOVE PERSON ID
# ==========================================

data.drop("Person ID", axis=1, inplace=True)

# ==========================================
# CONVERT ALL COLUMNS TO STRING
# ==========================================

for column in data.columns:
    data[column] = data[column].astype(str)

# ==========================================
# LABEL ENCODING
# ==========================================

label_encoder = LabelEncoder()

for column in data.columns:
    data[column] = label_encoder.fit_transform(
        data[column]
    )

# ==========================================
# INPUT FEATURES
# ==========================================

X = data.drop("Sleep Disorder", axis=1)

# ==========================================
# OUTPUT
# ==========================================

y = data["Sleep Disorder"]

# ==========================================
# TRAIN TEST SPLIT
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# ==========================================
# MODEL
# ==========================================

model = RandomForestClassifier()

# ==========================================
# TRAIN MODEL
# ==========================================

model.fit(X_train, y_train)

# ==========================================
# TEST MODEL
# ==========================================

predictions = model.predict(X_test)

accuracy = accuracy_score(
    y_test,
    predictions
)

print(
    "\nModel Accuracy:",
    round(accuracy * 100, 2),
    "%"
)

# ==========================================
# SAVE MODEL
# ==========================================

pickle.dump(
    model,
    open("model.pkl", "wb")
)

print("\nModel saved successfully")
