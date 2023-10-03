# -*- coding: utf-8 -*-

import base64

def encode_file(file_path):
    with open(file_path, 'rb') as file:
        file_content = file.read()
        return base64.b64encode(file_content).decode('utf-8')

# Replace 'your_image.jpg' with the path to the image file you want to encode
image_base64 = encode_file('your_image.jpg')

with open('body.json', 'w') as body_file:
    body_file.write('''
{
  "mimeType": "JPEG",
  "languageCodes": ["*"],
  "model": "page",
  "content": "%s"
}
''' % image_base64)

# After running the code, enter the following command in the terminal:

# export IAM_TOKEN=<IAM_token>
# curl -X POST \
#     -H "Content-Type: application/json" \
#     -H "Authorization: Bearer ${IAM_TOKEN}" \
#     -H "x-folder-id: <catalog ID>" \
#     -H "x-data-logging-enabled: true" \
#     -d "@body.json" \
#     https://ocr.api.cloud.yandex.net/ocr/v1/recognizeText \
#     -o output.json

# To get the <IAM_token> and <catalog ID>, see the instructions on the official website:
# https://cloud.yandex.com/en/docs/iam/operations/iam-token/create 
# https://cloud.yandex.com/en/docs/resource-manager/operations/folder/get-id
# https://cloud.yandex.com/en/docs/vision/quickstart?from=int-console-empty-state