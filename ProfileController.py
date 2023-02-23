from flask import Flask, render_template
import json

app = Flask(__name__, template_folder='templates')


@app.route('/')
def home():
    app.debug = True
    name = "Neha Raj"
    position = "Current MSCS Graduate Student"
    website = "www.neharaj.com"
    linkedin = "https://www.linkedin.com/in/neha-raj-scu/"
    github = "https://github.com/NA0724"
    with open('skills.json') as sk:
        skills = json.load(sk)
    with open('school.json') as sc:
        school = json.load(sc)
    with open('projects.json') as p:
        projects = json.load(p)
    with open('projects.json') as pr:
        projects = json.load(pr)
    with open('experience.json') as e:
        experience = json.load(e)
    return render_template('index.html', name=name, website=website, linkedin=linkedin, github=github, skills=skills,
                           school=school, experience=experience, position=position, projects=projects)


@app.route('/contact')
def contact():
    email = "nraj@scu.edu"
    phone = "+1(813)934-8365"
    address = "Santa Clara, CA, 95051"
    return render_template('contact.html', email=email, phone=phone, address=address)


if __name__ == '__main__':
    app.run()
