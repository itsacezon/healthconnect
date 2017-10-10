# healthconnect

HealthConnect aims to help local government units and NGOs manage their health programs while keeping their constituents informed by using SMS.

This was an entry to #ThinkOpenHealth Hackathon 2016.

## Screenshots

![Landing page](/screenshots/index.png)

![Program page](/screenshots/program.png)

## Running the app

### Requirements

- `python3`
- `node`

### Django app
1. Run `virtualenv ENV -p /usr/local/bin/python3` to create a separate environment for the app.
2. Then, install all the dependencies inside the `requirements.txt` by running `pip install -r requirements.txt`
3. To run the Django app, `python manage.py runserver`

### Vue app (for development)
1. Install the dependencies: `npm install`
2. To watch, run `npm run dev`
3. To build, run `npm run build`

## Developers
Django app was written by ![Andie Rabino](https://github.com/heyandie), Vue app was written by me.
