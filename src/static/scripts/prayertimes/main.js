const send_data = async ( form ) => {
    let data_form  = new FormData( form );
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
        timeout:1000000,
        body: JSON.stringify(data),
    } );
    if ( response.status === 200 ) {
        const data_res = await response.json();
        if ( data_res.status){
            hide_loader(data_res.status);
            return true;
        }
    }
    hide_loader(false);
    return false;
}

const hide_loader = ( status ) => {
    document.getElementById('loading').style.display = 'none';
    if ( status ) {
        alert('Prayer times saved successfully');
    }
    else{
        alert('Error saving prayer times');
    }
    window.location.href = '/';
}

const forms  = document.querySelectorAll('form');
forms.forEach(form => {
    form.addEventListener('submit', (e) => {
        e.preventDefault();
        document.getElementById('loading').style.display = 'flex';
        send_data(form);

    }

    , false);
});
