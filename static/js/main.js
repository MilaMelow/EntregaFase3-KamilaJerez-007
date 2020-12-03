/*Aquí se muestra el menú*/

const showMenu = (toggleId, navId) =>{
    const toggle = document.getElementById(toggleId)
        nav = document.getElementById(navId)

    if(toggle && nav){
        toggle.addEventListener('click', ()=>{
            nav.classList.toggle('show')
        })   
    }
}

showMenu('nav-toggle', 'nav-menu')

/*Menú movil*/
const navLink = document.querySelectorAll('.nav__link')

function linkAction(){
    //Este es el click activador
    navLink.forEach(n => n.classList.remove('active'))
    this.classList.add('active')

    /*Aquí se remueve el menù movil*/
    const navMenu = document.getElementById('nav-menu')
    navMenu.classList.remove('show')
}   

navLink.forEach(n => n.addEventListener('click', linkAction))


/*Carrusel*/
document.addEventListener('DOMContentLoaded', ()=> {
    const elementosCarousel = document.querySelectorAll('.carousel');
    M.Carousel.init(elementosCarousel, {
        duration: 150,
        dist: -80,
        shift: 5,
        padding: 5,
        numVisible: 3,
        indicators: true,
        noWrap: false
    })
})