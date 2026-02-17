from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

# Dummy Data
TALKS = [
    {
        "id": 1,
        "title": "Keynote: The Future of Cloud Computing",
        "speakers": [
            {"first_name": "Sundar", "last_name": "Pichai", "linkedin": "https://www.linkedin.com/in/sundarpichai/"}
        ],
        "category": "Keynote",
        "description": "Join us for an inspiring keynote on the future of cloud technology and AI innovation.",
        "time": "09:00 AM - 10:00 AM"
    },
    {
        "id": 2,
        "title": "Scaling with Kubernetes",
        "speakers": [
            {"first_name": "Kelsey", "last_name": "Hightower", "linkedin": "https://www.linkedin.com/in/kelseyhightower/"},
            {"first_name": "Alice", "last_name": "Dev", "linkedin": "#"}
        ],
        "category": "Infrastructure",
        "description": "Learn best practices for scaling applications using Kubernetes on Google Cloud.",
        "time": "10:15 AM - 11:00 AM"
    },
    {
        "id": 3,
        "title": "BigQuery for Data Warehousing",
        "speakers": [
            {"first_name": "Felipe", "last_name": "Hoffa", "linkedin": "https://www.linkedin.com/in/felipehoffa/"}
        ],
        "category": "Data & Analytics",
        "description": "Discover how BigQuery can revolutionize your data analytics strategy with serverless scaling.",
        "time": "11:15 AM - 12:00 PM"
    },
    {
        "id": 4,
        "title": "Serverless on GCP",
        "speakers": [
            {"first_name": "Guillaume", "last_name": "Laforge", "linkedin": "https://www.linkedin.com/in/glaforge/"}
        ],
        "category": "App Development",
        "description": "Build and deploy scalable applications without managing infrastructure using Cloud Run and Functions.",
        "time": "12:15 PM - 01:00 PM"
    },
    # Lunch Break Placeholder (Logic handled in template or list structure)
    {
        "id": 5,
        "title": "AI and Machine Learning with Vertex AI",
        "speakers": [
            {"first_name": "Dale", "last_name": "Markowitz", "linkedin": "https://www.linkedin.com/in/dale-markowitz/"},
             {"first_name": "Kaz", "last_name": "Sato", "linkedin": "https://www.linkedin.com/in/kazunori-sato/"}
        ],
        "category": "AI/ML",
        "description": "Get hands-on with Vertex AI to build, deploy, and scale machine learning models.",
        "time": "02:00 PM - 02:45 PM"
    },
    {
        "id": 6,
        "title": "Security in the Cloud",
        "speakers": [
            {"first_name": "Maya", "last_name": "Kaczorowski", "linkedin": "https://www.linkedin.com/in/mayakaczorowski/"}
        ],
        "category": "Security",
        "description": "Understand the shared responsibility model and how to secure your workloads on GCP.",
        "time": "03:00 PM - 03:45 PM"
    },
    {
        "id": 7,
        "title": "Networking Deep Dive",
        "speakers": [
            {"first_name": "Priyanka", "last_name": "Vergadia", "linkedin": "https://www.linkedin.com/in/pvergadia/"}
        ],
        "category": "Infrastructure",
        "description": "Explore the networking foundations of Google Cloud, from VPCs to Load Balancing.",
        "time": "04:00 PM - 04:45 PM"
    },
    {
        "id": 8,
        "title": "Closing Remarks & Networking",
        "speakers": [
          {"first_name": "Thomas", "last_name": "Kurian", "linkedin": "https://www.linkedin.com/in/thomas-kurian-5b51311/"}
        ],
        "category": "Keynote",
        "description": "Wrap up the day with key takeaways and networking opportunities.",
        "time": "05:00 PM - 05:30 PM"
    }
]

# Lunch is handled as a static entry in the template or inserted here if strict ordering is needed.
# For simplicity, we can insert it into the list or handle it in the template loop (e.g., after the 4th talk).

@app.route('/')
def index():
    query = request.args.get('q', '').lower()
    filtered_talks = []

    if query:
        for talk in TALKS:
            # Search by title
            if query in talk['title'].lower():
                filtered_talks.append(talk)
                continue
            
            # Search by category
            if query in talk['category'].lower():
                filtered_talks.append(talk)
                continue
            
            # Search by speaker name
            speaker_match = False
            for speaker in talk['speakers']:
                full_name = f"{speaker['first_name']} {speaker['last_name']}".lower()
                if query in full_name:
                    speaker_match = True
                    break
            if speaker_match:
                filtered_talks.append(talk)
    else:
        filtered_talks = TALKS

    current_year = datetime.now().year
    
    return render_template('index.html', talks=filtered_talks, year=current_year, query=query)

if __name__ == '__main__':
    app.run(debug=True)
