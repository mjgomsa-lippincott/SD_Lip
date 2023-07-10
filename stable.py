import base64
import os
import requests
import config
import json

api_host = 'https://api.stability.ai'
api_key = config.api_key
engine_id = 'stable-diffusion-xl-beta-v2-2-2'


def getModelList():
    url = f"{api_host}/v1/engines/list"
    response = requests.get(url, headers={"Authorization": f"Bearer {api_key}"})

    if response.status_code == 200:
        payload = response.json()
        print(payload)


def generateSDImg(prompt, height, width, steps):
    url = f"{api_host}/v1/generation/{engine_id}/text-to-image"
    head = {
        "Content-Type": "application/json",
        "Accept": "application/json", #png?
        "Authorization": f"Bearer {api_key}"
    }
    payload = {}
    payload['text_prompts'] = [ {"text": f"{prompt}"}]
    payload['cfg_scale'] = 7
    payload['clip_guidance_preset'] = 'FAST_BLUE'
    payload['height'] = height
    payload['width'] = width
    payload['samples'] = 1
    payload['steps'] = steps

    response = requests.post(
        url,
        headers = head,
        json = payload,
    )

    # Processing the response
    if response.status_code == 200:
        data = response.json()
        for i, image in enumerate(data["artifacts"]):
            with open(f"./output/v1_txt2img_{i}.png", "wb") as f:
                f.write(base64.b64decode(image["base64"]))





    

    









