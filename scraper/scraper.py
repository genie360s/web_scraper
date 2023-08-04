import functools
import requests

from bs4 import BeautifulSoup

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from scraper.db import get_db

sp = Blueprint('scraper', __name__, url_prefix='/scraper')


@sp.route('/home')
def home():
    URL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia'
    page = requests.get(URL)
    print(page)
    context = {
        page : page
    }
    return render_template('scraper/home.html', context)
