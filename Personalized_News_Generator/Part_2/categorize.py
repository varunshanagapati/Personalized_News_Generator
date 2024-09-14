import spacy
import pandas as pd



nlp = spacy.load("en_core_web_sm")


def preprocess_text(text):
    # Process the text with spaCy
    doc = nlp(text)
    
    # Extract lemmas of tokens, excluding punctuation and stop words
    tokens = [token.lemma_.lower() for token in doc if not token.is_punct and not token.is_stop]
    
    return " ".join(tokens)

def classify_text(text):
    processed_text = preprocess_text(text)
    doc = nlp(processed_text)
    
    # Define keywords for each category
    categories = {
        'world':[ 'world','united states','us','america', 'canada', 'mexico', 'china', 'germany', 'france', 'israel','gaza'
                'united kingdom','uk','england', 'russia', 'brazil', 'australia', 'japan', 'south africa', 'turkey','sri lanka'
                'italy', 'spain', 'nigeria', 'egypt', 'argentina', 'pakistan', 'bangladesh', 'saudi arabia','india'],
        'politics': ['politics','government', 'election', 'policy', 'vote', 'party', 'president', 'congress', 'law', 'politician', 'debate',
                     'protests', 'campaign', 'protest','military','war','fighting','conflict','ceasefire','terrorist','kills','ministry','arrest',
                     'hamas'],
        'business': ['company', 'stock', 'market', 'economy', 'finance', 'investment', 'trade', 'profit', 'ceo', 
                     'startup', 'industry','business'],
        'science & technology': ['technology','software', 'hardware', 'internet', 'app', 'digital', 'computer', 'ai', 'data',
                       'vr', 'cyber', 'tech', 'innovation','electric','ev','science','research', 'study', 'experiment', 'discovery', 'scientist', 'biology', 'physics', 'chemistry',
                    'astronomy', 'theory','climate','evolution','ecosystem','organism','geology','atmosphere','weather','planet',
                    'asteroid','comet','pollution','deforestation'],
        'sports': ['game', 'player', 'team', 'score', 'championship', 'athlete', 'coach', 'tournament', 'league', 'match','sport',
                   'cricket','football','formula 1','f1','rugby','tennis','golf','javelin','cycling'
                   'world cup','t20','league','club','olympic'],
        'entertainment': ['entertainment','movie', 'music', 'celebrity', 'actor', 'film', 'tv', 'show', 'artist',
                           'concert', 'performance','songs','awards','album','producer','director','viral','trend','model']
    }
    
    # Count keyword occurrences for each category
    category_scores = {category: 0 for category in categories}
    
    for token in doc:
        for category, keywords in categories.items():
            if token.lemma_.lower() in keywords:
                category_scores[category] += 1
    
    # Consider named entities
    for ent in doc.ents:
        if ent.label_ in ['ORG', 'PERSON', 'GPE']:
            if ent.label_ == 'ORG':
                category_scores['business'] += 1
            elif ent.label_ == 'PERSON':
                category_scores['politics'] += 1
                category_scores['entertainment'] += 1
            elif ent.label_ == 'GPE':
                category_scores['politics'] += 1
    
    # Find the category with the highest score
    if max(category_scores.values()) > 0:
        return max(category_scores, key=category_scores.get)
    else:
        return "home"




def get_data(published_date,source,scraped_category,title,summary,article_url,output_file_name):
    try:
        category=classify_text(str(title)+" "+str(summary)).capitalize()

        df_dict = {"Publication_date":published_date,"Source":source,"Scraped_category":scraped_category,
                    "Category":category,"Title":title,"Summary":summary,"Article_Url":article_url
                }
        print(df_dict)
        df = pd.DataFrame(df_dict, index=[0], columns=["Publication_date","Source","Scraped_category",
                    "Category","Title","Summary","Article_Url"
                                                    ])

        with open(output_file_name, 'a',encoding='utf-8',newline ='') as f:
            df.to_csv(f, mode='a', header=f.tell()==0,index=False)


    except Exception as e:
        print(e)
    



def main(source_file,output_file_name):
    try:
        data_file=pd.read_csv(source_file)
        for row in data_file.iterrows():
            row=row[1]
            published_date=row["Publication_date"]
            source=row["Source"]
            scraped_category=row["Scraped_category"]
            title=row["Title"]
            summary=row["Summary"]
            article_url=row["Article_Url"]
            get_data(published_date,source,scraped_category,title,summary,article_url,output_file_name)

    except Exception as e:
        print(e)



if __name__ == "__main__":
    source_file="news_articles.csv"
    output_file_name = f"news_articles_5.csv"  
    main(source_file,output_file_name)