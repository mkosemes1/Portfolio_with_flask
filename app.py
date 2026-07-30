import os
from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mail import Mail, Message
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')

app.config['MAIL_SERVER'] = os.environ.get('MAIL_SERVER', 'smtp.gmail.com')
app.config['MAIL_PORT'] = int(os.environ.get('MAIL_PORT', 587))
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME', '')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD', '')

mail = Mail(app)

PROFESSIONAL_DATA = {
    'name': 'M.Moustapha Souane',
    'title': 'Junior Data Scientist & ML | Pentester',
    'profile_photo': 'IMG_1853.JPG',
    'tagline': 'Big Data | Machine Learning | IOT & Robotique | Intelligence Artificielle',
    'email': 'malickoseme@gmail.com',
    'phone': '+221 77 590 87 46',
    'location': 'Dakar, SENEGAL',
    'linkedin': 'https://linkedin.com/in/mkosemes',
    'github': 'https://github.com/mkosemes1',
    'about': """Passionné par la technologie et l'innovation, je suis etudiant de 3 ieme annee en informatique spécialisé
    dans le Big Data, le Machine Learning en plus de cela j'ai un interet particulier a la Robotique et dans l'IOT ce qui ma permis d'evoluer en autoaprentissage dans ce domaine. Avec plusieurs années d'expérience
    dans la conception et le déploiement de solutions intelligentes, je transforme les données
    en actions concrètes et les problèmes complexes en solutions elegantes.""",
    'about_detail': """Mon parcours m'a permis de développer une expertise transversale, allant
    de l'analyse de données massives à la conception de systèmes embarques et robotiques autonomes.
    Je crois fermement que la technologie doit servir l'humain et résoudre des problèmes concrets.
    Chaque projet est une opportunité d'apprendre et de repousser les limites du possible.""",
    'experience_years': '3+',
    'projects_completed': '11+',
    'clients_satisfied': '5+',
}

SKILLS = {
    'Big Data': {
        'icon': 'database',
        'items': [
            {'name': 'Apache Spark', 'level': 95},
            {'name': 'Hadoop Ecosystem', 'level': 90},
            {'name': 'Kafka', 'level': 88},
            {'name': 'Hive / HBase', 'level': 85},
            {'name': 'Elasticsearch', 'level': 82},
            {'name': 'Airflow', 'level': 90},
        ]
    },
    'Machine Learning': {
        'icon': 'brain',
        'items': [
            {'name': 'TensorFlow / Keras', 'level': 95},
            {'name': 'PyTorch', 'level': 92},
            {'name': 'Scikit-learn', 'level': 95},
            {'name': 'NLP / Transformers', 'level': 88},
            {'name': 'Computer Vision', 'level': 85},
            {'name': 'Reinforcement Learning', 'level': 80},
        ]
    },
    'IOT & Robotique': {
        'icon': 'cpu',
        'items': [
            {'name': 'ROS / ROS2', 'level': 90},
            {'name': 'Navigation Autonome', 'level': 88},
            {'name': 'Perception & SLAM', 'level': 85},
            {'name': 'Gazebo / Simulation', 'level': 82},
            {'name': 'Arduino / Raspberry Pi', 'level': 90},
            {'name': 'Computer Vision for Robotics', 'level': 85},
        ]
    },
    'Programmation': {
        'icon': 'code',
        'items': [
            {'name': 'Python', 'level': 98},
            {'name': 'C++', 'level': 85},
            {'name': 'R', 'level': 80},
            {'name': 'SQL / NoSQL', 'level': 80},
            {'name': 'JavaScript', 'level': 75},
            {'name': 'Java', 'level': 60},
        ]
    },
    'Cloud & DevOps': {
        'icon': 'cloud',
        'items': [
            {'name': 'AWS (SageMaker, EMR, Lambda)', 'level': 90},
            {'name': 'GCP (Vertex AI, BigQuery)', 'level': 88},
            {'name': 'Docker / Kubernetes', 'level': 85},
            {'name': 'CI/CD Pipelines', 'level': 82},
            {'name': 'Terraform', 'level': 78},
            {'name': 'MLOps', 'level': 88},
        ]
    },
    'Outils & Frameworks': {
        'icon': 'tools',
        'items': [
            {'name': 'Git / GitHub', 'level': 95},
            {'name': 'Linux / Bash', 'level': 90},
            {'name': 'Pandas / NumPy', 'level': 98},
            {'name': 'Matplotlib / Seaborn', 'level': 90},
            {'name': 'Jupyter / VS Code', 'level': 95},
            {'name': 'MLflow / Kubeflow', 'level': 82},
        ]
    },
}

PROJECTS = [
    {
        'id': 1,
        'title': 'Pipeline Big Data - Environement Monitoring',
        'description': 'Analyse et visualisation de la qualite de l\'aire en temps reel avec des donnees collectes sur OPen Meteo',
        'category': 'Big Data',
        'technologies': ['Apache Kafka', 'Spark Streaming', 'Minio', 'Python', 'Docker'],
        'image': 'bigdata.jpg',
        'github': 'https://github.com/mkosemes/bigdata-pipeline',
        'demo': '#',
    },
    {
        'id': 2,
        'title': 'Robot Autonome - Navigation Intelligente',
        'description': 'Développement d\'un robot autonome capable de naviguer dans des environnements complexes grâce au SLAM et au Deep Learning pour la perception.',
        'category': 'IOT & Robotique',
        'technologies': ['ROS2', 'Python', 'C++', 'TensorFlow', 'Gazebo'],
        'image': 'robot.jpg',
        'github': 'https://github.com/mkosemes/autonomous-robot',
        'demo': '#',
    },
    {
        'id': 3,
        'title': 'Système de Recommandation IA',
        'description': 'Plateforme de recommandation personnalisée utilisant des réseaux de neurones profonds et le traitement du langage naturel.',
        'category': 'Machine Learning',
        'technologies': ['PyTorch', 'Transformers', 'FastAPI', 'PostgreSQL', 'Redis'],
        'image': 'ml.jpg',
        'github': 'https://github.com/mkosemes/ai-recommender',
        'demo': '#',
    },
    {
        'id': 4,
        'title': 'Prédiction de Séries Temporelles',
        'description': 'Modèle de prédiction financière basé sur les Transformers et les LSTM pour l\'analyse de marchés boursiers en temps réel.',
        'category': 'Machine Learning',
        'technologies': ['TensorFlow', 'Pandas', 'Plotly', 'Flask', 'AWS'],
        'image': 'timeseries.jpg',
        'github': 'https://github.com/mkosemes/time-series-prediction',
        'demo': '#',
    },
    {
        'id': 5,
        'title': 'Cluster Spark - Analyse de Sentiment',
        'description': 'Pipeline distribué pour l\'analyse de sentiment de millions de tweets en temps réel avec Apache Spark sur cluster Hadoop.',
        'category': 'Big Data',
        'technologies': ['Apache Spark', 'Hadoop', 'NLP', 'Python', 'Kafka'],
        'image': 'spark.jpg',
        'github': 'https://github.com/mkosemes/spark-sentiment',
        'demo': '#',
    },
    {
        'id': 6,
        'title': 'Bras Robotique - Manipulation d\'Objets',
        'description': 'Système de contrôle intelligent pour un bras robotique utilisant la vision par ordinateur et le reinforcement learning.',
        'category': 'IOT & Robotique',
        'technologies': ['ROS', 'Python', 'OpenCV', 'PyBullet', 'Arduino'],
        'image': 'arm.jpg',
        'github': 'https://github.com/mkosemes/robotic-arm',
        'demo': '#',
    },
]

CERTIFICATIONS = [
    {'name': 'Informatique et internet', 'issuer': 'FORCE N'},
    {'name': 'Introduction en Cybersecurite', 'issuer': 'CISCO'},
    {'name': 'Data analyst ( en cours )', 'issuer': 'CISCO'},
    {'name': 'Data Science ( en cours )', 'issuer': 'CISCO'},
]

@app.route('/')
def index():
    return render_template('index.html', data=PROFESSIONAL_DATA)

@app.route('/about')
def about():
    return render_template('about.html', data=PROFESSIONAL_DATA, certifications=CERTIFICATIONS)

@app.route('/skills')
def skills():
    return render_template('skills.html', data=PROFESSIONAL_DATA, skills=SKILLS)

@app.route('/projects')
def projects():
    return render_template('projects.html', data=PROFESSIONAL_DATA, projects=PROJECTS)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name', '')
        email = request.form.get('email', '')
        subject = request.form.get('subject', '')
        message = request.form.get('message', '')

        if not all([name, email, subject, message]):
            flash('Veuillez remplir tous les champs.', 'error')
            return redirect(url_for('contact'))

        try:
            msg = Message(
                subject=f'Portfolio Contact: {subject}',
                sender=email,
                recipients=[PROFESSIONAL_DATA['email']],
                body=f'Nom: {name}\nEmail: {email}\n\nMessage:\n{message}'
            )
            mail.send(msg)
            flash('Message envoyé avec succès!', 'success')
        except Exception:
            flash('Erreur lors de l\'envoi. Essayez par email direct.', 'error')

        return redirect(url_for('contact'))

    return render_template('contact.html', data=PROFESSIONAL_DATA)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
