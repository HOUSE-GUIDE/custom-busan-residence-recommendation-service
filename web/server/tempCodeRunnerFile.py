from flask import Flask, request, render_template
import average

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    user_weights = request.form.to_dict()
    user_weights = {k: int(v) for k, v in user_weights.items()}  # 입력은 문자열이므로 숫자로 변환해줍니다.

    top3_dong = average.calculate_similarity(user_weights)  # average.py에서 함수를 호출하여 결과를 얻습니다.

    return render_template('result.html', top3_dong=top3_dong)

if __name__ == '__main__':
    app.run(debug=True)
