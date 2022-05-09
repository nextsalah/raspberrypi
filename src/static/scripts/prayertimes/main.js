const sendData = async ( form ) => {
    let data_form  = new FormData( form );
    let output_form  = new FormData();
    let data = {};
    data_form.forEach( ( value, key ) => {
        if ( key !== 'source' ) {
            data['data'] = {
                ...data['data'],[key]: value
            }
            return;
        }
        data['source'] = value;
    });

    const response = await fetch( "/api/prayertimes", {
        headers: {
            'Content-Type': 'application/json'
        },
        method: 'POST',
        body: JSON.stringify(data),
    } );
    if ( response.status === 200 ) {
        const data = await response.json();
        return data;
    }
    return false;
}

const forms  = document.querySelectorAll('form');
forms.forEach(form => {
    form.addEventListener('submit', (e) => {
        e.preventDefault();
        sendData(form);
    }

    , false);
});
