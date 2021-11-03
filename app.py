# app.py
from flask import Flask, render_template, jsonify
import requests
app = Flask(__name__)

url = "https://api.themoviedb.org/3/movie/popular"
service_key = "b3574ad4d1429f3dd3841d2b6658110d"
language_kr = "ko"


# HTML을 주는 부분
@app.route('/')
def home():
  return render_template('index.html')

## API 역할을 하는 부분
@app.route('/test', methods=['GET'])
def read_reviews():
  vote_average_movies_over_8 = []
  params = {
    'api_key' : service_key,
    'language' : language_kr
  }
  
  # 1.TMDB API url과 KEY 합치기
  res = requests.get(url=url, params=params)
  print(res.status_code,res.url)

  # 2.합쳐진 url를 json -> dictionary 형태로 변환
  movie_dict = res.json()

  # 3. `movie_dict`에서 영화 데이터를 담고 있는  `results`를 리스트로 받아온다. 
  movie_details = movie_dict.get('results', None)

  # 4. movie_details 반복
  for movie_detail in movie_details:
    # 5. 개별 영화들의 평점 확인
    vote_average_movies_over_8.append(movie_detail)

  # 6. 평점 8 이상인 영화들의 목록을 담은 리스트를 반환한다.
  return jsonify({'api_loading': vote_average_movies_over_8})

if __name__ == '__main__':
  app.run('0.0.0.0',port=5000,debug=True)