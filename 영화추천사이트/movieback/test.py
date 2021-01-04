from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
import nltk 
import urllib
from nltk import tokenize
from bs4 import BeautifulSoup
from nltk.tokenize import sent_tokenize

from wordcloud import WordCloud
from wordcloud import STOPWORDS
import matplotlib.pyplot as plt

import json
import requests

from .models import Movie
from .models import M_data
from .serializers import MovieListSerializer
from .serializers import MovieSerializer
from .serializers import M_dataSerializer

