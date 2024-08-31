from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)
summarizer = pipeline("summarization")

@app.route('/scan', methods=['POST'])
def scan_job_description():
    data = request.json
    job_description = data['jobDescription']
    summary = summarizer(job_description, max_length=130, min_length=30, do_sample=False)[0]['summary_text']
    return jsonify({"summary": summary})

@app.route('/apply', methods=['POST'])
def apply_for_job():
    # Logic to modify and enhance resume based on job description
    return jsonify({"status": "success", "message": "Resume updated and job application filled."})

if __name__ == '__main__':
    app.run(debug=True)
