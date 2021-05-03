from configuration import collection


def insert_quote(quote, author, tag1=None, 
tag2=None, tag3=None, tag4=None, tag5=None, tag6=None):
    dict_insert = {"quote": quote,
    "author": author,
    "tag1": tag1,
    "tag2": tag2,
    "tag3": tag3,
    "tag4": tag4,
    "tag5": tag5,
    "tag6": tag6, 
    }
    collection.insert_one(dict_insert)

def insert_quote_dic(df):
    df_dic = df.to_dict(orient="records")
    collection.insert_many(df_dic)