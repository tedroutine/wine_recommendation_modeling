# Data Processing
import pandas as pd

# Machine Learning
from sklearn.metrics.pairwise import cosine_similarity 

# mongodb
import pymongo

import flask
from flask import *

app = flask.Flask(__name__)
app.config["DEBUG"] = True

from flask_cors import CORS
CORS(app)

# main index page route
@app.route('/')
def home():
    return '<h1>API is working.. </h1>'

@app.route('/main')
def main():
    return render_template("webservice.html")

@app.route('/predict',methods=['GET'])
def predict():

    def find_wine(question1_answer, question2_answer, question3_answer, question4_answer, question5_answer, result):
        path = "/home/ubuntu/python3/notebook/workspace/project/Wine_Recommendation_Modeling/kakao/static/data"
        wine_data = pd.read_csv('{}/wine_data.csv'.format(path))
        wine_data.drop('Unnamed: 0', axis=1, inplace=True)
        customer_data = pd.read_csv('{}/customer_data.csv'.format(path))
        customer_data.drop('Unnamed: 0', axis=1, inplace=True)

        # 1. 설문조사 만들기
        question1 = {0 : 'black', 1 : 'milk_sweet', 2: 'tea'}
        question2 = {0 : 'acid', 1 : 'body'}
        question3 = {0 : 'meat', 1 : 'cheese', 2: 'seafood', 3 : 'vegetables', 4 : 'dessert'}
        question5 = 0
        # 중복 선택 가능
        question4 = {0 : 'floral', 1 : 'fruit', 2 : 'citrus', 3 : 'oriental_spice', 4 : 'oriental_leather', 5: 'earth'} 
        questions = [question1, question2, question3, question4, question5]

        # 2. 설문조사 답에 따른 와인 특성 값
        question1_result = list(question1.values())[question1_answer]
        question2_result = list(question2.values())[question2_answer]
        question3_result = list(question3.values())[question3_answer]
        question4_result = [list(question4.values())[int(i)] if question4_answer >= 10 else list(question4.values())[question4_answer]
                    for i in str(question4_answer)]
        question5_result = question5_answer

        # 3. question1, 2(survey) 에 따른 wine_data 나누기

        if (question1_result, question2_result) == ('black', 'acid'):
            customer_data = customer_data[customer_data['type'] =='a']
        elif (question1_result, question2_result) == ('black', 'body'):
            customer_data = customer_data[customer_data['type'] =='b']
        elif (question1_result, question2_result) == ('milk_sweet', 'acid'):
            customer_data = customer_data[customer_data['type'] =='c']
        elif (question1_result, question2_result) == ('milk_sweet', 'body'):
            customer_data = customer_data[customer_data['type'] =='d']
        elif (question1_result, question2_result) == ('tea', 'acid'):
            customer_data = customer_data[customer_data['type'] =='e']
        elif (question1_result, question2_result) == ('tea', 'body'):
            customer_data = customer_data[customer_data['type'] =='f']

        # 4. question3(food)에 따른 데이터프레임 나누기

        if question3_result == 'meat':
            customer_data = customer_data[customer_data['meat'] == 1]
        elif question3_result == 'cheese':
            customer_data = customer_data[customer_data['cheese'] == 1]
        elif question3_result == 'seafood':
            customer_data = customer_data[customer_data['seafood'] == 1]
        elif question3_result == 'vegetables':
            customer_data = customer_data[customer_data['vegetables'] == 1]
        elif question3_result == 'dessert':
            customer_data = customer_data[customer_data['dessert'] == 1]

        # 5. question4(aroma)에 따른 데이터프레임 나누기

        if 'floral' in question4_result:
            customer_data = customer_data[customer_data['floral'] == 1]
        elif 'fruity' in question4_result:
            customer_data = customer_data[customer_data['fruity'] == 1]
        elif 'citrus' in question4_result:
            customer_data = customer_data[customer_data['citrus'] == 1]
        elif 'oriental_spice' in question4_result:
            customer_data = customer_data[customer_data['oriental_spice'] == 1]
        elif 'oriental_leather' in question4_result:
            customer_data = customer_data[customer_data['oriental_leather'] == 1]
        elif 'earth' in question4_result:
            customer_data = customer_data[customer_data['earth'] == 1]

        # 6. 투표 가장 많이 받은 아이템 sort

        customer_data_counts = customer_data['title'].value_counts()

        customer_data = pd.merge(customer_data, customer_data_counts, how='left', left_on ='title',
        right_on =customer_data_counts.index)

        customer_data.rename(columns = {'title_y' : 'counts'}, inplace=True)
        customer_data.rename(columns = {'title_x' : 'title'}, inplace=True)

        customer_data = customer_data.sort_values(by='counts', ascending=False)
        customer_data.drop_duplicates(keep='first', inplace=True)
        customer_data = customer_data.iloc[:,1:]

        # 7. 가격을 무시한 베스트 상품 찾기

        best_review = pd.DataFrame(columns=['title', 'alcohol', 'sweetness', 'acidity', 'body_rate', 'tannin_rate', 
                              'meat', 'cheese', 'seafood', 'vegetables', 'dessert', 'floral', 'fruit', 'citrus', 'oriental_spice',
                             'oriental_leather', 'earth', 'europe_a', 'europe_b', 'north_america', 'south_america', 
                              'new_world', 'korea','price', 'link'])

        data =list(customer_data.iloc[0,:][['title','alcohol', 'sweetness', 'acidity', 'body_rate', 'tannin_rate', 
                              'meat', 'cheese', 'seafood', 'vegetables', 'dessert', 'floral', 'fruit', 'citrus', 'oriental_spice',
                             'oriental_leather', 'earth', 'europe_a', 'europe_b', 'north_america', 'south_america', 
                              'new_world', 'korea', 'price', 'link']])

        data = pd.Series(data, index=best_review.columns)
        best_review = best_review.append(data, ignore_index=True)
        best_review.set_index('title', drop=False, inplace=True)

        # 8. price 적용한 데이터프레임

        if best_review['price'][0] > question5_answer:
            if len(customer_data[customer_data['price'] <= question5_answer]) >= 1:
                customer_data_price = customer_data[customer_data['price'] <= question5_answer]
                customer_data_price = customer_data_price[['title', 'alcohol', 'sweetness', 'acidity', 'body_rate', 'tannin_rate', 
                                      'meat', 'cheese', 'seafood', 'vegetables', 'dessert', 'floral', 'fruit', 'citrus', 'oriental_spice',
                                     'oriental_leather', 'earth', 'europe_a', 'europe_b', 'north_america', 'south_america', 
                                      'new_world', 'korea']]
                best_review.drop(['price', 'link'], axis=1, inplace=True)
                best_review = best_review.append(customer_data_price)
                best_review.set_index('title', inplace=True)

                # 커피취향, 음식, 아로마, 가격대가 모두 맞고 베스트 상품과 유사도가 가장 높은 와인
                recommend_wine = cosine_similarity(best_review, best_review)
                recommend_wine_df = pd.DataFrame(data=recommend_wine, index = best_review.index, columns=best_review.index)
                recommend_wine_name = recommend_wine_df.iloc[0,:].sort_values(ascending=False)[1:2]
                for i in range(len(customer_data)):
                    if customer_data['title'].iloc[i] == recommend_wine_name.index:
                        result["link"] = customer_data['link'].iloc[i]
                        return result
                        break
            else:
                result["code"] = 201
                result["msg"] = "₩{} 가격대에는 적절한 와인이 없는 것 같아요 😭. 가끔은 평소와 다른 와인이 하루를 더 특별하게 만들어준답니다:)".format(question5_answer)
                return result

        elif best_review['price'][0] <= question5_answer:
            recommend_wine_df = best_review
            result["link"] = recommend_wine_df['link'][0]
            return result
    
    result = find_wine(int(request.args['Coffee_Preference']), 
                     int(request.args['Coffee_Bean']),
                     int(request.args['Food_Pairing']),
                     int(request.args['Aroma']), 
                     int(request.args['Price']), {"code": 200})
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
