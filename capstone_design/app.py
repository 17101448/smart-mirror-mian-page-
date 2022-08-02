from flask import Flask, render_template

app = Flask(__name__)
#__name__ 인자는 정적파일과 템플릿을 찾는 데 쓰임 
import crawling


@app.route('/')
def hello():
    news_list, href, img = crawling.news_crawling()
    img_list = crawling.img_src(news_list)
    sum_list = crawling.summary(news_list)
    return render_template('index.html', news_list = news_list, href = href, img = img, img_list=img_list, len = len(news_list), sum = sum_list )

if __name__ == "__main__": 
	app.run(debug = True ) 