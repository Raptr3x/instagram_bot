import requests

graph_url = 'https://graph.facebook.com/v16.0/'

def post_image(caption='test', image_url='https://i.redd.it/i0mkepzpetfa1.jpg',instagram_account_id='17841409151659064',access_token='EAAG8CWtzsYIBAMgTvzHyPiqIU6ZC5KpZC9PWvoEr2ps5Jrf6b1JI7F8qzYLXOIpZAs7m7ZB9dZASf8rAY5wClZCIN7OlBdFaiD8vzPvuoHdhRBeF80TLi7iwHlsOdHirLWUsd2KEMImZBZAkVhCTOQPbkb01EJrUJoZCz4kfDDZBl3T7CjdCx6uviW7OtwvtpNocearhOEA6chjOkN9CLGhV3W4APAkGN6i4gZD'):
    url = graph_url + instagram_account_id + '/media'
    param = dict()
    param['access_token'] = access_token
    param['caption'] = caption
    param['image_url'] = image_url
    response = requests.post(url, params=param)
    return response

def publish_container(creation_id,instagram_account_id='17841409151659064',access_token='EAAG8CWtzsYIBAMgTvzHyPiqIU6ZC5KpZC9PWvoEr2ps5Jrf6b1JI7F8qzYLXOIpZAs7m7ZB9dZASf8rAY5wClZCIN7OlBdFaiD8vzPvuoHdhRBeF80TLi7iwHlsOdHirLWUsd2KEMImZBZAkVhCTOQPbkb01EJrUJoZCz4kfDDZBl3T7CjdCx6uviW7OtwvtpNocearhOEA6chjOkN9CLGhV3W4APAkGN6i4gZD'):
    url = graph_url + instagram_account_id + '/media_publish'
    param = dict()
    param['access_token'] = access_token
    param['creation_id'] = creation_id
    response = requests.post(url,params=param)
    response = response.json()
    return response

# print(post_image().text)
print(post_image().json())

id = post_image().json()['id']

print(publish_container(id).json())