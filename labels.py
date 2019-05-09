import boto3
from pprint import pprint
import image_helpers

client = boto3.client('rekognition')

#imgurl = 'https://www.parrots.org/images/uploads/dreamstime_C_47716185.jpg'
#imgurl = 'http://www.drummerworld.com/drummerworld1/glensobel840112.jpg'
imgurl = 'https://upload.wikimedia.org/wikipedia/commons/7/7d/Air_Force_One_over_Mt._Rushmore.jpg'
#imgurl = 'http://www.idothat.us/images/idothat-img/features/pool-patio-lanai/ft-pool-patio-lanai-2.jpg'

# grab the image from URL
imgbytes = image_helpers.get_image_from_url(imgurl)

rekresp = client.detect_labels(Image={'Bytes': imgbytes},
                               MinConfidence=95)

#pprint(rekresp)
pprint(rekresp['Labels'])
