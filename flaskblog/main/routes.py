from flask import render_template, request, Blueprint, url_for, redirect
from flaskblog.models import Post
from flask_login import login_required

main = Blueprint('main', __name__)


@main.route("/")
def achintyajha():
    return render_template('achintyajha.html', title='Home')


@main.route("/home")
def home():
    return render_template('home.html', title='Home')


@main.route("/blog")
def blog():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('blog.html', posts=posts, title='Blog')


@main.route("/highschool")
def highschool():
	return render_template('hs.html', title='High School')


@main.route("/FAQs")
def faq():
	return render_template('faqs.html', title='FAQs')


@main.route("/Programming")
def programming():
	return render_template('programming.html', title='Python and Stuff')


@main.route("/resume")
def resume():
	return redirect(url_for('static', filename="resources/Achintya's Resume.pdf"))

	