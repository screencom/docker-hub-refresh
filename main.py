import urllib.request
import json
import subprocess

hub_user = 'screencom'

def main():
    json_obj = get_json()
    for image in json_obj['results']:
        image_name = "%s/%s" % (image['namespace'], image['name'])
        refresh(image_name)

def get_json():
    hub_url = 'https://hub.docker.com/v2/repositories/%s/?page_size=1000' % hub_user
    req = urllib.request.Request(hub_url)
    response = urllib.request.urlopen(req)
    json_str = response.read().decode('utf8')
    return json.loads(json_str)

def refresh(image_name):
    print("Pulling image %s..." % image_name)
    subprocess.run(['docker', 'pull', image_name], capture_output=True)

    print("Removing image %s..." % image_name)
    remove_command = "docker image ls | grep %s | awk '{ print $3 }' | xargs docker image rm" % image_name
    ps = subprocess.Popen(remove_command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    ps.communicate()

if __name__ == '__main__':
    main()
