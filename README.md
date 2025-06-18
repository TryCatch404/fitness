# DYFitness App



## 🏋️ Fitness Regime Flask App
A modular Flask application that provides customized fitness regimes based on user profile attributes such as height, weight, gender, age, and activity level. The app stores recommended diet and exercise plans and supports user authentication and geolocation tracking.

🚀 Features
User authentication with Flask-Login

Custom fitness regime generation

Diet and exercise plan storage

Location mapping support

Enum-based classification for:

Gender

Age groups

Activity levels

## 📦 Models Overview
User
Stores application users and integrates with Flask-Login.

Field	Type	Description
id	Integer	Primary key
email	String	Unique email
password	String	Hashed password
first_name	String	User's first name

Regime
Represents a personalized fitness regime based on a user's profile.

Field	Type	Description
from_height	Float	Height lower bound
to_height	Float	Height upper bound
from_weight	Float	Weight lower bound
to_weight	Float	Weight upper bound
gender	Enum	Gender enum
age	Enum	Age group enum
active	Enum	Activity level enum
diet	Relation	Associated diet entries
exercise	Relation	Associated exercise plans

Diet
Stores general or regime-specific diet plans.

Field	Type	Description
data	String	Diet plan text
regime_id	FK	Linked Regime ID

Exercise
Stores exercise plan data.

Field	Type	Description
data	String	Exercise plan text
regime_id	FK	Linked Regime ID

Locations
Stores geographical data for mapping or location-based services.

Field	Type	Description
name	String	Location or place name
street	String	Street info
zip	String	ZIP/postal code
city	String	City name
country	String	Country name
long	Float	Longitude
lat	Float	Latitude

## 🧪 Setup Instructions & Installtion


Make sure you have the latest version of Python installed.

```bash
git clone <repo-url>
```

```bash
pip install -r requirements.txt
```

## Running The App

```bash
python main.py
```

## Viewing The App

Go to `http://127.0.0.1:5000`
