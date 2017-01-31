from setuptools import setup
from setuptools.command.install import install
import os

class MyInstall(install):
    def run(self):
        install.run(self)
        os.system("chmod u+x /usr/local/bin/startup.sh")
        os.system("cd /usr/local/bin")
        os.system("./startup.sh")

setup(name='Tzara---A-Personal-Assistant',
      version='0.1',
      description='A Virtual Personal Assistant',
      url='https://github.com/Suman7495/Tzara---A-Personal-Assistant',
      author='Suman Pal',
      author_email='suman7495@gmail.com',
      license='MIT',
      packages=['tzara'],
      scripts=['bin/startup.sh'],
      cmdclass={'install': MyInstall},
     )
