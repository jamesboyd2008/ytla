# YTLA Data Persistence and Visualization

This decoupled application stores telescope data and makes graphs.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Install [Anaconda](https://docs.anaconda.com/anaconda/install/).

### Installing

Create an environment

```
conda create --name ytla
```

Activate that environment

```
source activate ytla
```

Install dependencies:

```
conda install --yes --file requirements.txt
```

In the likely event that you want to run this program with simulated data, you'll want to run a MongoDB server, locally (perhaps in another terminal tab):

```
sudo mongod
```

Seed the database:

```
python seed_database.py
```

Run the application:

```
python run_app.py
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

You must SSH into the server on Mauna Loa to connect to the DB.

## Built With

* [Python](http://www.dropwizard.io/1.0.2/docs/) - for science
* [Flask](https://maven.apache.org/) - Microframework
* [MongoDB](https://rometools.github.io/rome/) - DB

## Authors

* **Billie Thompson** - *README template author* - [PurpleBooth](https://github.com/PurpleBooth)
* **Eonasdan** - *Creator of datetimepicker* - [Eonasdan](https://github.com/eonasdan)
* **Marc Brinkman** - *Flask-Bootstrap* - [Marc Brinkman](https://github.com/mbr/flask-bootstrap)

See also the list of [contributors](https://github.com/jamesboyd2008/ytla/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

Mahalo to all the following for making this project possible:

* [Akamai Workforce Initiave](https://akamaihawaii.org/)
* [TMT]()
* funders
