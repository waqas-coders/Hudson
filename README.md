# DOCKER GUIDESE

STEP 1: UP
RUN COMMAND : docker-compose up --build

STEP 2: RUN MIGRATION
RUN COMMAND : docker-compose run web python manage.py migrate

STEP 3: DOWN:
RUN CAMMAND: docker-compose down