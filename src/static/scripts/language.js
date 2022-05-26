
function change_language( language ) {
    console.log( "Chaning Language: " + language );
    switch( language ){
        case 'en':
            translate_text = [
                "Fajr",
                "Sunrise",
                "Dhuhr",
                "Asr",
                "Maghrib",
                "Isha",
                "Begins",
                "Prayer",
                "Iqamah",
                "Next...",
                "Please, turn off your phones"
            ];
            break;
        case 'sv':
            translate_text = översätt_text = översätt_text = [
                "Fajr",
                "Soluppgång",
                "Dhuhr",
                "Asr",
                "Maghrib",
                "Isha",
                "Börjar",
                "Bön",
                "Iqamah",
                "Nästa...",
                "Snälla, stäng av dina telefoner"
            ];
            break;
        case 'bs':
            translate_text = [
                "Zora", 
                "Izlazak sunca" , 
                "Podne", 
                "Ikindija", 
                "Akšam", 
                "Jacija",
                "Namaz", 
                "Ikamet", 
                "Počinje",  
                "Sljedeći...", 
                "Isključite telefone"
            ];
            break;
        }

    let inputs = document.getElementsByTagName( 'input' );
    try{
        for( let i = 0; i < inputs.length; i++ ){
            inputs[i].value = translate_text[i];
        }
        document.querySelector("#language_code").value = language;
    }
    catch( e ){
        console.log( e );
    }

}