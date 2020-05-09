@app.route('/mform')
def index():
	return render_template('form.html')   


    
    
@app.route('/process', methods=['POST'])
def showprocess():    
    
    mytag = request.form['search']

    if mytag:
        myseries =  session.query(Series).filter_by(name=mytag).first()
        mymovie =  session.query(Movie).filter_by(name=mytag).first()
        if myseries:
            message = '1 Result Found for %s .' %myseries.name
            myurl = '%s/' %myseries.url
            print(myurl)
            return jsonify({'search' : message, 'url' : myurl})
        if mymovie:
            message = '1 Result Found for %s .' %mymovie.name
            myurl = '%s/' %mymovie.url
            return jsonify({'search' : message, 'url' : myurl})
   
    return jsonify({'error' : 'No Result Found!'})
