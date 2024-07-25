import os

from dotenv import load_dotenv

from django.shortcuts import render
from django.http import HttpResponse

from myapp.client.requests_client import RequestsClient
from myapp.client.gql_client import GqlClient
from myapp.runner import GraphQLClientRunner
from myapp.queries.repository import repository_issues_query



def individual_post(request):
    return HttpResponse('Hi, this is where an individual post will be.')

load_dotenv()  # take environment variables from .env

GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
GITHUB_GRAPHQL_ENDPOINT = os.environ.get("GITHUB_GRAPHQL_ENDPOINT")

def main():
    r_client = RequestsClient(
        endpoint=GITHUB_GRAPHQL_ENDPOINT, token=GITHUB_TOKEN
    )
    r_runner = GraphQLClientRunner(client=r_client)

    gql_client = GqlClient(
        endpoint=GITHUB_GRAPHQL_ENDPOINT, token=GITHUB_TOKEN
    )
    gql_runner = GraphQLClientRunner(client=gql_client)

    data = r_runner.execute(repository_issues_query, {})
    print(data)



if __name__ == "__main__":
    main()