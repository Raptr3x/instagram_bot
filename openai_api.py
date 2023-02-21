import requests
import openai
import os

openai.api_key = os.getenv("OPENAI_API")

prompt = '''Short article or text, maximum 1800 characters, that provides a brief overview of a topic: 
"How to make your pc setup feel comfortable for gaming and working"
followed by a pros and cons discussion or different aspects of that topic.
in the end write 15 hashtags regarding the subject but add two new epmpty lines before the hashtags.
'''

response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    max_tokens=500
)


print(response)
print("-"*40)
print(response.choices[0].text)

with open('tmp.txt', 'w') as f:
    f.write(str(response))

# {
#     "id": "cmpl-GERzeJQ4lvqPk8SkZu4XMIuR",
#     "object": "text_completion",
#     "created": 1586839808,
#     "model": "text-davinci:003",
#     "choices": [
#         {
#             "text": "\n\nThis is indeed a test",
#             "index": 0,
#             "logprobs": null,
#             "finish_reason": "length"
#         }
#     ],
#     "usage": {
#         "prompt_tokens": 5,
#         "completion_tokens": 7,
#         "total_tokens": 12
#     }
# }



#pcsetup #graphicscard #upgrade #gamingexperience #gamingperformance #motherboard #ram #gpu #coolingpad #thermallimits #pcsetupideas #gamingPC #desktopgaming #dualGPU #PCcomponents #shadowRAM #maximumperformance #keepyourpcclean #PCcoolling #gaminghardware