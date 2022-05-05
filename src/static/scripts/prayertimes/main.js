var socket = io();

const  send_source_info = (source, data) => {
    let all_buttons  = document.querySelectorAll('button');
    all_buttons.forEach(button => {
        button.disabled = true;
        button.style.opacity = 0.5;
    });

    if (data.length > 0){
        console.log("Sending data to server");
        socket.emit('get_new_prayertimes', {
            'source': source,
            'data' : data
        });
    }
}
const get_prayertimes = ( source ) => {
    if (source == 'islamiska-forbundet'){
        let city = document.querySelector('#islamiska_forbundet_city').value;
        send_source_info(source, city);
    }
    else if (source == 'vaktijaba'){
        let city_id = document.querySelector('#vaktijaba_city').value;
        send_source_info(source, city_id);
    }
    else if (source == 'vaktijaeu'){
        let slug = document.querySelector('#vaktija_eu_city').value;
        send_source_info(source, slug);
    }

}

// Alert the user the result of the prayertimes request
socket.on('alert', (data) => {
    let all_buttons  = document.querySelectorAll('button');

    all_buttons.forEach(button => {
        button.disabled = false;
        button.style.opacity = 1;
    });

    alert(data.message);
});
