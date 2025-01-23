from flask import Flask, request, render_template
import joblib
import pandas as pd
import nltk
import re
import string
import dill as pickle
import pandas as pd
from flask import Flask, request, render_template, redirect, url_for

# Load necessary components
model_filename = 'rf_model.pkl'
vectorizer_filename = 'tfidf_vect.pkl'

with open(model_filename, 'rb') as model_file:
    loaded_model = pickle.load(model_file)

with open(vectorizer_filename, 'rb') as vectorizer_file:
    loaded_vectorizer = pickle.load(vectorizer_file)


# Initialize Flask app
app = Flask(__name__)

stopwords = nltk.corpus.stopwords.words('english')
ps = nltk.PorterStemmer()

def count_punct(text):
    count = sum([1 for char in text if char in string.punctuation])
    return round(count / (len(text) - text.count(" ")), 3) * 100



@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        user_input = request.form['text']
        
        # Preprocess the input text
        input_df = pd.DataFrame({
    'body_text': [user_input],
    'body_len': [len(user_input) - user_input.count(" ")],
    'punct%': [count_punct(user_input)] 
})
        tfidf_input_tf = loaded_vectorizer.transform(input_df['body_text'])
        input_vect = pd.concat([input_df[['body_len', 'punct%']].reset_index(drop=True), pd.DataFrame(tfidf_input_tf.toarray())], axis=1)
        input_vect.columns = input_vect.columns.astype(str)
        
        # Make prediction
        prediction = loaded_model.predict(input_vect)[0]
        
        return redirect(url_for('result', prediction=prediction, text=user_input))
    
    return render_template('index.html')

@app.route('/result')
def result():
    prediction = request.args.get('prediction')
    text = request.args.get('text')
    return render_template('result.html', prediction=prediction, text=text)

if __name__ == '__main__':
    app.run(debug=True)
