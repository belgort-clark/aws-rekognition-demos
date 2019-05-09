import boto3
import image_helpers
from pprint import pprint

client = boto3.client('rekognition')

imgurl = 'https://s3.amazonaws.com/ctec280/pictures/bruce_drums.jpg'
#imgurl = 'https://pbs.twimg.com/profile_images/1012000737289629698/Jx1uL9qf_400x400.jpg'
#imgurl = 'https://bruceelgort.files.wordpress.com/2014/09/domino_cannon_beach.jpg'
#imgurl = 'http://www.clark.edu/Library/Images/chimes24_onlinenw2007_crop400.jpg'
#imgurl = 'https://cdn.pixabay.com/photo/2017/09/25/13/12/dog-2785074_1280.jpg'
#imgurl = 'http://www.clark.edu/about/news-and-media/releases/images/DwightHughes.jpg'
#imgurl = 'http://littlejoe.typepad.com/photos/orlando1003/groupobriens.jpg'

imgbytes = image_helpers.get_image_from_url(imgurl)

rekresp = client.detect_labels(Image={'Bytes': imgbytes})

pprint(rekresp)
