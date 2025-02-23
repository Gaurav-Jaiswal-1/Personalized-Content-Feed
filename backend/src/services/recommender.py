from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import spacy

nlp = spacy.load("en_core_web_md")

def filter_recommended_videos(user_input, videos):
    input_doc = nlp(user_input)
    scored_videos = [(video, nlp(video).similarity(input_doc)) for video in videos]
    return sorted(scored_videos, key=lambda x: x[1], reverse=True)


def filter_videos(videos, keyword):
    keyword = keyword.lower()
    corpus = [video['snippet']['title'].lower() + " " + video['snippet'].get('description', '').lower() for video in videos]

    # Apply TF-IDF
    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform(corpus)

    # Convert keyword into a vector
    keyword_vector = vectorizer.transform([keyword])

    # Compute cosine similarity
    cosine_similarities = (tfidf_matrix * keyword_vector.T).toarray().flatten()

    # Rank videos by similarity
    ranked_videos = sorted(zip(videos, cosine_similarities), key=lambda x: x[1], reverse=True)

    return [video for video, score in ranked_videos if score > 0.1]
