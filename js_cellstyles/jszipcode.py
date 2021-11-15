    from st_aggrid.shared import JsCode

    
    cellsytle_jszipcode = JsCode(
         """

    function(params) {

        if(/^([0-9]{5}|[a-zA-Z][a-zA-Z ]{0,49})$/.test(params.value)){
            return {
                 'color': 'black',
                 'backgroundColor': 'white'
             }
        }
        else {
             return {
                 'color': 'black',
                 'backgroundColor': 'pink'
             }
        } 
         
    };
     """
    )

    