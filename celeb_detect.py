import boto3
from pprint import pprint
import image_helpers

client = boto3.client('rekognition')

# grab the image from online
imgurl = 'https://images.fandango.com/ImageRenderer/0/0/redesign/static/img/default_poster.png/0/images/masterrepository/performer%20images/p76618/BruceWillis.jpg'

imgbytes = image_helpers.get_image_from_url(imgurl)

rekresp = client.recognize_celebrities(Image={'Bytes': imgbytes})

pprint(rekresp['CelebrityFaces'])

for face in rekresp['CelebrityFaces']:
    print(face['Name'],'confidence:', face['MatchConfidence'], 'url:',face['Urls'])
