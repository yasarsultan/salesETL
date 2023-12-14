import re
import pandas as pd 
import analysis
from db_tasks import *

def split_users(row):
    splitted_text = re.split(',(?!,| |Tcr|Soopy)', row)
    return splitted_text

## Extracting data from csv file
dataframe = pd.read_csv('data/amazon.csv')
# print(dataframe.head())


## Selecting relevant columns for multiple dataframes
products = dataframe[["product_id", "product_name", "category", "discounted_price", "actual_price", "discount_percentage", "rating", "rating_count", "about_product", "img_link", "product_link"]]
reviews = dataframe[["product_id", "review_id", "review_title", "review_content"]]
users = dataframe[["product_id", "user_id", "user_name"]]


## Saving products dataframe as a csv file
products.to_csv('data/products.csv', index=False)


## Performing Sentiment Analysis on reviews
# reviews = reviews.iloc[:100]
reviews[['negative', 'neutral', 'positive', 'compound']] = reviews['review_content'].apply(analysis.sentiment_scoring).apply(pd.Series)
## Saving reviews dataframe as a csv file
reviews.to_csv('data/reviews.csv', index=False)


## Transforming Users dataframe
users['user_id'] = users['user_id'].str.split(',')
users_name = users['user_name'].apply(split_users).explode().reset_index(drop=True)


# unames = users['user_name'].apply(split_users)
# for row in unames:
#     if len(row) > 8:
#         print(row)
# Problem causing values: ["Jayesh Rajesh k.,Soopy", "Pradeep,Tcr"]

users = users.explode('user_id').reset_index(drop=True)
users = pd.DataFrame({
    'product_id': users['product_id'],
    'user_id': users['user_id'],
    'user_name': users_name
})
## Saving users dataframe as a csv file
users.to_csv('data/users.csv', index=False)



## Establishing connection with database
connector = create_connection()
# create_database(connector)

## Loading products dataframe into products table
create_table(connector, "products", product_structure)
insert_data(connector, 'products', products)
print("Loaded products data successfully.")

## Loading reviews dataframe into reviews table
create_table(connector, 'reviews', review_structure)
print("Loaded reviews data successfully.")

## Loading users dataframe into users table
create_table(connector, 'users', user_structure)
print("Loaded users data successfully.")

close_connection(connector)