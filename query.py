"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# # Start here.


# Part 2: Write queries

# 1. Get the brand with the **id** of 8.
db.session.query(Brand).filter(Brand.id == 8).one()


# 2. Get all models with the **name** Corvette and the **brand_name** Chevrolet.
db.session.query(Model).filter_by(name="Corvette", brand_name="Chevrolet").all()

# 3. Get all models that are older than 1960.
db.session.query(Model).filter(Model.year == 1960)

# 4. Get all brands that were founded after 1920.
db.session.query(Brand).filter(Model.year > 1920)

# 5. Get all models with names that begin with "Cor".
db.session.query(Model).filter(Model.name.like('%Cor%')).all()

# 6. Get all brands with that were founded in 1903 and that are not yet discontinued.
db.session.query(Brand).filter((Brand.founded == 1903) & (Brand.discontinued.isnot("null")))

# 7. Get all brands with that are either discontinued or founded before 1950.
db.session.query(Brand).filter((Brand.founded < 1950) | (Brand.discontinued.isnot("null")))

# 8. Get any model whose brand_name is not Chevrolet.
db.session.query(Model).filter(Model.brand_name.isnot("Chevrolet"))

# Fill in the following functions. (See directions for more info.)


def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    car_model = Model.query.filter_by(year=year)
    for car in car_model:
        print car_model.model, car_model.brand_name, car_model.headquarters


def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

    print"Querying database"

    brands_summary = Model.query.all()
    brands_summary_list = []

    for brands in brands_summary:
        brands_summary_list.append(brand.brand_name)
        brands_list = set(brands_summary_list)

    for brand in brands_list:
        print "Brand: {}".format(brand.brand_name)
        for model in brands_summary:
            if model.brand_name == brand:
                print " Model: {} ({})".format(model.name, model.year)


    # model table
    # brand_name
    # name

    # brand
    # name

    # # .join for this one




# -------------------------------------------------------------------


# Part 2.5: Advanced and Optional
def search_brands_by_name(mystr):
    pass


def get_models_between(start_year, end_year):
    pass

# -------------------------------------------------------------------

# Part 3: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?

# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?
