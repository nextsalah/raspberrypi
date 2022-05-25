
function change_language( language ) {
    console.log( "Chaning Language: " + language );
    switch( language ){
        case 'en':
            translate_text = [
                "Monday",
                "Tuesday",
                "Wednesday",
                "Thursday",
                "Friday",
                "Saturday",
                "Sunday",
                "January",
                "February", 
                "March",
                "April",
                "May",
                "June",
                "July",
                "August",
                "September",
                "October",
                "November",
                "December",
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
        case 'se':
            translate_text = översätt_text = översätt_text = [
                "Måndag",
                "Tisdag",
                "Onsdag",
                "Torsdag",
                "Fredag",
                "Lördag",
                "Söndag",
                "Januari",
                "Februari",
                "Mars",
                "April",
                "Maj",
                "Juni",
                "Juli",
                "Augusti",
                "September",
                "Oktober",
                "November",
                "December",
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
        case 'ba':
            translate_text = [
                "Ponedjeljak", 
                "Utorak", 
                "Srijeda", 
                "Četvrtak", 
                "Petak", 
                "Subota", 
                "Nedjelja", 
                "Januar",
                "Februar",
                "Mart",
                "April",
                "Maj",
                "Juni",
                "Juli",
                "Avgust",
                "Septembar",
                "Oktobar",
                "Novembar",
                "Decembar",
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
    }
    catch( e ){
        console.log( e );
    }

}