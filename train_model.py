# model/train_model.py
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import joblib

# Load dataset
df = pd.read_csv('C:\\Users\\HP\\OneDrive\\Desktop\\Machine Learning Projects\\Restaurant_Recommendation_using_ML\\data\\Dataset .csv')

# Handle missing values
df.fillna('', inplace=True)

# Combine features for content-based filtering
df['combined_features'] = df['Cuisines'] + ' ' + df['Price range']

# Create TF-IDF matrix
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['combined_features'])

# Compute cosine similarity matrix
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

# Save the model and other components
joblib.dump(cosine_sim, './model/recommendation_model.pkl')
joblib.dump(df, './model/restaurants_df.pkl')
joblib.dump(tfidf, './model/tfidf_vectorizer.pkl')
