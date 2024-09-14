from django.shortcuts import render
from django.http import HttpResponse
import os
from django.conf import settings
import csv
from pathlib import Path
from datetime import datetime


csv_file_path = Path(settings.BASE_DIR) / 'news_articles_5.csv'


def home(request):
    articles = []  
      # Path to the CSV file
    try:
        with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['Category'].lower() == 'home':
                    articles.append(row)
                        
    except FileNotFoundError:
        print(f"CSV file not found at {csv_file_path}")

    return render(request, 'articles/home.html', {'articles': articles})

def world(request):
    articles = []  
      # Path to the CSV file
    try:
        with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['Category'].lower() == 'world':
                    articles.append(row)
                        
    except FileNotFoundError:
        print(f"CSV file not found at {csv_file_path}")

    return render(request, 'articles/home.html', {'articles': articles})


def politics(request):
    articles = []  
      # Path to the CSV file
    try:
        with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['Category'].lower() == 'politics':
                    articles.append(row)
                        
    except FileNotFoundError:
        print(f"CSV file not found at {csv_file_path}")

    return render(request, 'articles/home.html', {'articles': articles})


def business(request):
    articles = []  
      # Path to the CSV file
    try:
        with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['Category'].lower() == 'business':
                    articles.append(row)
                        
    except FileNotFoundError:
        print(f"CSV file not found at {csv_file_path}")

    return render(request, 'articles/home.html', {'articles': articles})


def science_tech(request):
    articles = []  
      # Path to the CSV file
    try:
        with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['Category'].lower() == 'science & technology':
                    articles.append(row)

                        
    except FileNotFoundError:
        print(f"CSV file not found at {csv_file_path}")

    return render(request, 'articles/home.html', {'articles': articles})


def entertainment(request):
    articles = []  
      # Path to the CSV file
    try:
        with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['Category'].lower() == 'entertainment':
                    articles.append(row)
                        
    except FileNotFoundError:
        print(f"CSV file not found at {csv_file_path}")

    return render(request, 'articles/home.html', {'articles': articles})


def sports(request):
    articles = []  
      # Path to the CSV file
    try:
        with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['Category'].lower() == 'sports':
                    articles.append(row)
                        
    except FileNotFoundError:
        print(f"CSV file not found at {csv_file_path}")

    return render(request, 'articles/home.html', {'articles': articles})
    

def all(request):
    articles = []  
      # Path to the CSV file
    try:
        with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                articles.append(row)
                        
    except FileNotFoundError:
        print(f"CSV file not found at {csv_file_path}")

    return render(request, 'articles/home.html', {'articles': articles})




