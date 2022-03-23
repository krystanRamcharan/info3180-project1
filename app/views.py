"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""
import os
from app import app,db
from flask import render_template, request, redirect, url_for, flash, jsonify
from app.forms import PropertyForm
from app.models import Properties
from werkzeug.utils import secure_filename

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Properties")


@app.route('/properties/create', methods=['POST','GET'])
def property_form():
    propertyform=PropertyForm()
    if request.method == 'POST' and propertyform.validate_on_submit():
        title= request.form['title']
        description=request.form['description']
        room=request.form['rooms']
        bathroom=request.form['bathrooms']
        price=request.form['price']
        proptype=request.form['proptype']
        location=request.form['location']
        

        photo=request.files['photo']
        filename=secure_filename(photo.filename)
        photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        
        upload=Properties(title=title,description=description,No_of_rooms=room,No_of_bathrooms=bathroom,price=price,property_type=proptype,location=location,photo_filename=filename)
        db.session.add(upload)
        db.session.commit()
        return redirect(url_for("properties"))
        flash('Property Saved', 'success')
    return render_template('propform.html',form=propertyform)



@app.route('/properties', methods=['GET','POST'])
def properties():
    properties=Properties.query.filter_by().all()
    return render_template('properties.html', properties=properties)


@app.route('/uploads/<filename>', methods=['GET','POST'])

def get_image(filename):
    return send_from_directory(os.path.join(os.getcwd(),app.config['UPLOAD_FOLDER']),filename)


@app.route('/properties/<propertyid>', methods=['GET','POST'])

def property(propertyid):
    json={}
    prop=Properties.query.filter_by(id=propertyid).first()
    if request.method == 'POST':
        json={'propertyid':prop.id, 'title':prop.title, 'Description':prop.description, '  Number of Bedrooms':prop.No_of_rooms,
              'Number of Bathrooms':prop.No_of_bathrooms,  'price':prop.price,   'property type':prop.property_type,
              'location':prop.location, 'photo':prop.photo_filename}
        return jsonify(json)
    elif request.method == 'GET' and prop:
        return render_template('individualproperty.html',prop=prop)

    return render_template('propform.html')
            
    

    


###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
