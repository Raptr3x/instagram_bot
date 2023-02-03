import requests

QUERY_URL = "https://api.openai.com/v1/engines/gpt-3/jobs"

def generate_description(image_url):
    model = "text-davinci-003"
    prompt = f"Write Instagram description for image located at {image_url}."
    api_key = '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'

    response = requests.post(
        QUERY_URL,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        },
        json={
            "model": model,
            "prompt": prompt,
            "max_tokens": 100,
            "temperature": 0.5
        }
    )

    if response.status_code == 200:
        description = response.json()["choices"][0]["text"]
        print(description)
        print('\n')
        print(response.json())
        return description
    else:
        raise Exception("Failed to generate description")


# def generate_description(image_url):
#     model = "image-alpha-001"
#     prompt = f"Write Instagram description for image located at {image_url}"
#     api_key = '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'

#     response = requests.post(
#         QUERY_URL,
#         headers={
#             "Content-Type": "application/json",
#             "Authorization": f"Bearer {api_key}"
#         },
#         json={
#             "model": model,
#             "prompt": prompt,
#             "num_images":1,
#             "size":"1024x1024",
#             "response_format":"url"
#         }
#     )

#     if response.status_code == 200:
#         description = response.json()["data"]
#         print(description)
#         print('\n')
#         print(response.json())
#         return description
#     else:
#         raise Exception("Failed to generate description")


generate_description('https://i.postimg.cc/wTM7BZZT/116336732-1003207993470070-3363504100969961476-n.jpg')