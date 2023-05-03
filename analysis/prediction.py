import joblib
from sklearn.feature_extraction.text import TfidfVectorizer

def textclean(tweets):
   
    # Load the SVM model and TF-IDF vectorizer
    svm_model = joblib.load(r"C:\Users\Administrator\OneDrive\Desktop\superbowl_twitter\analysis\svm_model.pkl")
    tfidf_vectorizer = joblib.load(r"C:\Users\Administrator\OneDrive\Desktop\superbowl_twitter\analysis\tfidf_vectorizer.pkl")
    text_vectorized = tfidf_vectorizer.transform([tweets])    
    predicted_class = svm_model.predict(text_vectorized)       
    if predicted_class == 1:
        return("Neutral")
    elif predicted_class == 2:
        return("Negative")
    elif predicted_class == 3:
        return("Positive")
    else:
        return("Unknown value")