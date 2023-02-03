import requests
import openai


openai.api_key = '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'
# openai.Model.list()

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Give social media description of this image from the link: https://postimg.cc/WhR2WWsQ",
  max_tokens=200,
  stop=["11."]
)

print(response)

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

