#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
FastAPI server to display some {{ cookiecutter.__project_slug }}.
"""

import os
import pandas as pd

from fastapi import FastAPI, HTTPException


# variables
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "..", "data")
data_file = os.path.join(DATA_DIR, 'data.csv')

# API configuration
app = FastAPI(
    title="My {{ cookiecutter.__project_slug }} title",
    description="L'API pour les {{ cookiecutter.__project_slug }}",
    version="0.1.0",
    openapi_tags=[
        {
            'name': '{{ cookiecutter.__project_slug }}',
            'description': "Deals with {{ cookiecutter.__project_slug }}"}
    ]
)


data = pd.read_csv(data_file)
data = data.rename(columns={
    'Something': 'something', # placez ici les colonnes à renommer !
})
data = data.fillna('')


def random_{{ cookiecutter.__project_slug }}(number: int):
    """
    Get given number of random records from {{ cookiecutter.__project_slug }}.

    **number**: quantity of random records you want to display.

    Return:
    - random records (dataFrame)
    - or raise an HTTPException
    """
    length = data.shape[0]
    if length < number:
        raise HTTPException(
            status_code=400,
            detail=f'Not enough records in database: {length}')
    return data.sample(number)


@app.get('/{{ cookiecutter.__project_slug }}', name="Get all {{ cookiecutter.__project_slug }}", tags=['{{ cookiecutter.__project_slug }}'])
def get_{{ cookiecutter.__project_slug }}():
    """
    Return all {{ cookiecutter.__project_slug }}
    """
    return data.to_dict(orient='records')


@app.get(
    "/{{ cookiecutter.__project_slug }}/random/{number:int}",
    name="Get X random {{ cookiecutter.__project_slug }}",
    tags=['{{ cookiecutter.__project_slug }}'])
def {{ cookiecutter.__project_slug }}(number: int):
    """
    Return X {{ cookiecutter.__project_slug }} regarding X (as int)
    """
    return random_{{ cookiecutter.__project_slug }}(number).to_dict(orient='records')


@app.get(
    "/{{ cookiecutter.__project_slug }}/random",
    name="Get 5 random {{ cookiecutter.__project_slug }}",
    tags=['{{ cookiecutter.__project_slug }}'])
def get_random_{{ cookiecutter.__project_slug }}():
    """
    Return 5 random {{ cookiecutter.__project_slug }}
    """
    return random_{{ cookiecutter.__project_slug }}(5).to_dict(orient='records')


@app.get(
    "/{{ cookiecutter.__project_slug }}/{element}",
    name="Get element from {{ cookiecutter.__project_slug }}",
    tags=['{{ cookiecutter.__project_slug }}'])
def get_element(element: str):
    """
    Return what given element is
    """
    res = data.query(f'code == "{element}"')
    if res.empty:
        raise HTTPException(status_code=404, detail="Element not found")
    return res.to_dict(orient='records')
