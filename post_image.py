import requests
import constants as con

'''
Ovaj kod radi 100%, post_image ti vraca creation_id, taj id korsitis u publish_container da zapravo postavis sliku

korisni linkovi:
    https://developers.facebook.com/tools/explorer/?method=POST&path=17841409151659064%2Fmedia&version=v16.0&image_url=https%3A%2F%2Fi.redd.it%2Fi0mkepzpetfa1.jpg&caption=test%20123
    https://developers.facebook.com/docs/instagram-api/guides/content-publishing
'''

def post_img(link,caption):
    '''
    Takes in link, caption, other vals are in constants and posts the img to Instagram
    Uses facebook graph api
    '''
    
    url = con.GRAPH_URL + con.INSTA_ACC_ID + '/media'

    param = dict()
    param['access_token'] = con.ACCESS_TOKEN
    param['caption'] = caption
    param['image_url'] = link
    
    response = requests.post(url, params=param)
    try:
        creation_id = response.json()['id'] # Should return a dict id:id_val if it fails, break func
    except Exception as e:
        print(e)
        return -1

    post_url = con.GRAPH_URL + con.INSTA_ACC_ID + '/media_publish'

    post_param = dict()
    post_param['access_token'] = con.ACCESS_TOKEN
    post_param['creation_id'] = creation_id

    response = requests.post(post_url,params=post_param)
    print(response.json())
    if(response.status_code!='200'):
        return -1
    else:
        return 0