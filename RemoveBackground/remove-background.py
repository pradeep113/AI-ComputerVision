# Remove the background from the image or generate a foreground matte
print('\nRemoving background from image...')
    
url = "{}computervision/imageanalysis:segment?api-version={}&mode={}".format(endpoint, api_version, mode)

headers= {
    "Ocp-Apim-Subscription-Key": key, 
    "Content-Type": "application/json" 
}

image_url="https://github.com/MicrosoftLearning/mslearn-ai-vision/blob/main/Labfiles/01-analyze-images/Python/image-analysis/{}?raw=true".format(image_file)  

body = {
    "url": image_url,
}
    
response = requests.post(url, headers=headers, json=body)

image=response.content
with open("backgroundForeground.png", "wb") as file:
    file.write(image)
print('  Results saved in backgroundForeground.png \n')