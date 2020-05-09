@app.route('/search', methods=['POST'])
def process():
    tag = request.form['search']

    if tag:        
        istag = False
        isname = False
        isseries = False
        ismovie = False   
        result = []
        final_result = []
        isfinal = False
        named_move = ''
        index = 1;
        movie_index = 1;
        isfound = False; 
        for index in range(17):
            tagvar = 'tag' + str(i)
            equle = session.query(Series).filter_by(tagvar=tag).first()
            if equle != None:               
               istag = True               
               isname = False
               result.append(equle.name)               
            istag = False
        if istag == False:
            search_by_name = session.query(Series).filter_by(name=tag).first()
            if search_by_name != None:
                isname = True
                istag = False
                result.append(search_by_name.name)
            isname = False    
                
        if istag == False and isname == False:
            movie_name = session.query(Movie).filter_by(name=tag).first()
            if movie_name != None:
                ismovie = True
                
            for movie_index in range(17):
               tagm = 'tag' + str(movie_index)
               movie_tag = session.query(Movie).filter_by(tagm=tag).first()
               if movie_tag != None:
                   named_move =  movie_tag.name
                   ismovie = True
                ismovie = False;   
                   
                  
        if result == []:
            isfound = True
        isfound = False

        if isfound == True:
            for i in result:
                final_result.append(result[i])
            if final_result != []:
                isfinal = True            
            isfinal = False
        print(final_result)            
