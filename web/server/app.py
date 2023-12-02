from flask import Flask, request, render_template
import average

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    user_weights = request.form.to_dict()
    user_weights = {k: int(v) for k, v in user_weights.items()}

    top3_dong = average.calculate_similarity(user_weights)

    return render_template('result.html', top3_dong=top3_dong)

if __name__ == '__main__':
    app.run(debug=True)
