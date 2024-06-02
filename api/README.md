# API Details

This template doesn't contain Database

## API Structure

```bash

├── src                          # directory for source code for the whole API logic 
│    ├── routes                  # dir for routes and init fo flask app
│    ├── config                  # dir for any project configuration
│    ├── DS                      # dir to store data science models
│    ├── schemas                 # dir for app types
│    └── main.py                 # runner file : to start the server using it.
├── env                          # directory for virtual env, It's required for docker compose 
├── Dockerfile                   # docker file for production
├── flake8                       # config file for linting
├── Makefile                     # Make file to help create docker images 
├── requirements.txt             # requirements file for all dependencies
└── README.md                    # ...
```
