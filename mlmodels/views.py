from django.shortcuts import render
from django.http import HttpResponse 
import os
import cohere
from cohere.classify import Example


def index(request):
    return render(request, "mlmodelmain.html")
# setup cohere api
co = cohere.Client('RfibZy93rfGcosxAdDkWiPrJ4SY5F29aTGRcxYyY')

def fakenews(request):
	return render(request, "fakenews.html")

def fakenewsresult(request):
  input_text_title = request.GET["Title"]
  input_text_body = request.GET["Body"]
  input_combined = input_text_title + " " + input_text_body
  classifications = co.classify(
  model='4fbf93e1-e48c-42d5-9cd7-b3aa859b529c-ft',
  inputs=[input_combined])


  return render(request, "fakenewsresult.html",{'ans': classifications,'lis':input_combined})

