from flask import redirect , url_for , Blueprint, render_template, request, jsonify , app
import joblib
import pandas as pd
from sklearn.metrics.pairwise import linear_kernel

main = Blueprint('main', __name__)

# Load model and data
cosine_sim = joblib.load('./model/recommendation_model.pkl')
df = joblib.load('./model/restaurants_df.pkl')
tfidf = joblib.load('./model/tfidf_vectorizer.pkl')



# Function to get restaurant recommendations
def get_recommendations(cuisine, price_range):
    # Prepare input for recommendation
    input_features = f"{cuisine.lower()} {price_range.lower()}"
    user_tfidf = tfidf.transform([input_features])
    sim_scores = linear_kernel(user_tfidf, tfidf.transform(df['combined_features'])).flatten()
    top_indices = sim_scores.argsort()[-10:][::-1]
    recommendations = df.iloc[top_indices][['Restaurant Name', 'Cuisines', 'Price range']]
    return recommendations


@main.route('/')
def index():
    return render_template('index.html')


# @main.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         cuisine = request.form['cuisine']
#         price_range = request.form['price_range']
#         return redirect(url_for('recommendations.html', cuisine=cuisine, price_range=price_range))
#     return render_template('index.html')


@main.route('/recommend', methods=['POST'])
def recommend():
    
    # RestaurentsName = request.form['Restaurant Name']
    cuisine = request.form['cuisine']
    price_range = request.form['price_range']
    user_input = f"{cuisine} {price_range}"
    # recommendations = get_recommendations(cuisine, price_range)
    user_tfidf = tfidf.transform([user_input])
    sim_scores = linear_kernel(user_tfidf, tfidf.transform(df['combined_features'])).flatten()
    top_indices = sim_scores.argsort()[-10:][::-1]
    
    recommendations = df.iloc[top_indices][['Restaurant Name', 'Cuisines', 'Price range']]
    
    return render_template('recommendations.html', recommendations=recommendations)

# @main.route('/recommend', methods=['GET', 'POST'])
# def recommend():
#     cuisine = request.args.get('cuisine')
#     price_range = request.args.get('price_range')
    
#     if cuisine and price_range:
#         recommendations = get_recommendations(cuisine, price_range)
#         return render_template('recommendations.html', recommendations=recommendations)
#     else:
#         # Handle case where cuisine and/or price_range are not provided
#         return redirect(url_for('main.index'))