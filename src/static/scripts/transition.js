let gradient_img = document.querySelector("#gradient_img");
if (gradient_img) {
  gradient_img.style.animationDelay = `-${new Date().getTime() % 11000}ms`;
}

const transitionToPage = (href) =>{
    let main_element = document.querySelector("main");
    main_element.style.setProperty('--animate-duration', '0.4s');
    main_element.classList.remove("animate__fadeIn");
    main_element.classList.add('animate__fadeOut');
    main_element.setAttribute('fade_out_clock', new Date().getTime());
    setTimeout(function() { 
        if (href ) {
            window.location.href = href;
        }
        else{
            if( [ '/advanced' ].includes(window.location.pathname) || window.location.href === document.referrer){window.location.href = '/';}
            else{window.location.href = document.referrer;}
        }
    }, 400)
}

let links = document.querySelectorAll('a');
if (links) {
    links.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            transitionToPage(link.href);
        })
    })
}

(function loop() {
    setTimeout(function () {  
        let main_element = document.querySelector("main");
        if (main_element) {
            if( main_element.hasAttribute('fade_out_clock') ){
                let fade_out_clock = main_element.getAttribute('fade_out_clock');
                if( (new Date().getTime() - fade_out_clock) > 3000 ){
                    main_element.classList.remove("animate__fadeOut");
                    main_element.classList.add('animate__fadeIn');
                    main_element.removeAttribute('fade_out_clock');
                }
            }
        }       
    loop();
    }, 500); 
}());
