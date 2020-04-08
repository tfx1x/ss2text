from aip import AipOcr

config = {
    'appId': '*******',
    'apiKey': '******',
    'secretKey': '******'
}

options = {}
options["language_type"] = "CHN_ENG"
options["detect_direction"] = "true"
options["detect_language"] = "true"
options["probability"] = "true"

client = AipOcr(**config)

def get_file_content(file):
    with open(file, 'rb') as fp:
        return fp.read()

def transIm_baidu(image_path):
    image = get_file_content(image_path)
    result = client.basicGeneral(image, options)
    if 'words_result' in result:
        return '\n'.join([w['words'] for w in result['words_result']])
