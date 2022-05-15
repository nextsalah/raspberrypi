let gradient_img = document.querySelector("#gradient_img");
if (gradient_img) {
  gradient_img.style.animationDelay = `-${new Date().getTime() % 11000}ms`;
}

const transitionToPage = (href) =>{
    let main_element = document.querySelector("main");
    main_element.style.setProperty('--animate-duration', '0.4s');
    main_element.classList.add('animate__fadeOut');

    setTimeout(function() { 
        if (href ) {
            window.location.href = href;
        }
        else{
            history.back(-1);
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

