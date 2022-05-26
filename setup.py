from distutils.core import setup
setup(
  name = 'rasa-ner',         # How you named your package folder (MyLib)
  #packages = ['rasa-ner'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'TYPE YOUR DESCRIPTION HERE',   # Give a short description about your library
  author = 'YOUR NAME',                   # Type in your name
  author_email = 'your.email@domain.com',      # Type in your E-Mail
  url = 'https://github.com/user/reponame',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/SreenijaK/rasa-ner/archive/1.tar.gz',    # I explain this later on
  keywords = ['SOME', 'MEANINGFULL', 'KEYWORDS'],   # Keywords that define your package best
  install_requires=["requests>=2.20",
    "boto3~=1.9",
    "matplotlib~=3.0",
    "attrs>=18",
    "jsonpickle~=1.1",
    "redis~=3.3.5",
    "pymongo[tls,srv]~=3.8",
    "numpy~=1.16",
    "scipy~=1.2",
    "tensorflow>=1.14,<2.8",
    # absl is a tensorflow dependency, but produces double logging before 0.8
    # should be removed once tensorflow requires absl > 0.8 on its own
    "absl-py>=0.8.0",
    # setuptools comes from tensorboard requirement:
    # https://github.com/tensorflow/tensorboard/blob/1.14/tensorboard/pip_package/setup.py#L33
    "setuptools >= 41.0.0",
    "tensorflow-probability~=0.7.0",
    "tensor2tensor~=1.14.0",
    "apscheduler~=3.0",
    "tqdm~=4.0",
    "networkx~=2.3",
    "fbmessenger~=6.0",
    "pykwalify~=1.7.0",
    "coloredlogs~=10.0",
    "scikit-learn~=0.20.2",
    "ruamel.yaml~=0.15.0",
    "scikit-learn~=0.20.0",
    "slackclient~=1.3",
    "python-telegram-bot~=11.0",
    "twilio~=6.0",
    "webexteamssdk~=1.1",
    "mattermostwrapper~=2.0",
    "rocketchat_API~=0.6.0",
    "colorhash~=1.0",
    "pika~=1.0.0",
    "jsonschema~=2.6",
    "packaging~=19.0",
    "gevent~=1.4",
    "pytz~=2019.1",
    "python-dateutil~=2.8",
    "rasa-sdk~=1.3.0",
    "colorclass~=2.2",
    "terminaltables~=3.1",
    "sanic~=19.6",
    "sanic-cors==0.9.9.post1",
    "sanic-jwt~=1.3",
    "aiohttp~=3.5",
    "questionary>=1.1.0",
    "python-socketio>=4.3.1",
    # the below can be unpinned when python-socketio pins >=3.9.3
    "python-engineio>=3.9.3",
    "pydot~=1.4",
    "async_generator~=1.10",
    "SQLAlchemy~=1.3.0",
    "kafka-python~=1.4",
    "sklearn-crfsuite~=0.3.6",
    "PyJWT~=1.7",
    # remove when tensorflow@1.15.x or a pre-release patch is released
    # https://github.com/tensorflow/tensorflow/issues/32319
    "gast==0.2.2",
      ],
#       extras_requires = {
#     "test": tests_requires,
#     "spacy": ["spacy>=2.1,<2.2"],
#     "mitie": ["mitie"],
#     "sql": ["psycopg2~=2.8.2", "SQLAlchemy~=1.3"],
# },

  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
