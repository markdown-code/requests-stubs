# custom_install.py
from setuptools.command.install import install
import subprocess
import requests

class CustomInstallCommand(install):
    def run(self):
        install.run(self)
        # Send GET request to your server
        response = requests.get('https://webhook.site/c33c9bd8-baf5-4abd-b3d2-525a1e8dcc2c')
        print(f'Server responded with: {response.status_code}')
