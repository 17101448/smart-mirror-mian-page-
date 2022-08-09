from flask import Flask, render_template

app = Flask(__name__)
#__name__ 인자는 정적파일과 템플릿을 찾는 데 쓰임 
import crawling
import weather 

@app.route('/')
def hello():
    #2.
    news_list, href, img = crawling.news_crawling()
    img_list = crawling.img_src(news_list)
    sum_list = crawling.summary(news_list)
    weather_info = weather.return_weather_info() 
    #3
    return render_template('index.html', news_list = news_list, href = href, img = img, img_list=img_list, len = len(news_list), sum = sum_list, weather_info=weather_info )

if __name__ == "__main__": 
	app.run(debug=True) 