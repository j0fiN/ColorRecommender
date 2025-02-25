# Interactive Color Recommender

## What is it?
This project is a simple **Color** recommendation system 
where the user needs to select the color from the palette
based on the random ratings coming on the screen. The ratings 
is from 1 to 3 where,
- 1 depicts bad
- 2 depicts okay
- 3 depicts good

And the user gets their favorite color in few generation cylces.
(minimum of 10 generation required)
## Use cases
This project is mainly developed to show **Dynamic Model Training** 
and **Deployment of ML Models To Production**.

- The model trains and predicts your(possible) favorite color as soon 
as you click the *Generate* button in the website.

- The model is put into production(or deployed) using Flask framework.

### Disclaimer
- The Website was developed giving more importance to 
server-side development.So the website is **NOT reponsive**. For best results,
use computer. And getting your name in the first page was for personal education
purpose and it has nothing to do with data collection.

- This is just a simple model and strictly not for production purpose.

## How to run
```commandline
git clone https://github.com/j0fiN/ColorRecommender.git
cd ColorRecommender
pip install -r requirements.txt
python app.py
```
## References
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [P5*.js](https://p5js.org/)
- [Bootstrap](https://getbootstrap.com/)
- [Scikit-learn](https://scikit-learn.org/stable/)
- [Unittesting](https://docs.python.org/3/library/unittest.html)



