import cohere
from cohere.classify import Example
co = cohere.Client('RfibZy93rfGcosxAdDkWiPrJ4SY5F29aTGRcxYyY')
classifications = co.classify(
  model='2ba87422-f96a-4e9a-ab85-a3d9e181f19f-ft',
  inputs=["the movie is good"])

print('The confidence levels of the labels are: {}'.format(classifications.classifications)[1])