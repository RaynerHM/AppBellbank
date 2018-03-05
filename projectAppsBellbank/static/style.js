var btnMenu = document.getElementById('informacion');
var MostrarMenu = document.getElementById('arriba');

btnMenu.addEventListener('click', function() {
    MostrarMenu.classList.toggle('arriba');
});

/* ---------------------------------------------------------------------------------------------- */

/*  ------------------------- Menu SideNav -------------------------*/
$('.deslizar').sideNav({
    menuWidth: 300, // Default is 300
    // edge: 'right', // Choose the horizontal origin
    closeOnClick: true, // Closes side-nav on <a> clicks, useful for Angular/Meteor
    draggable: true, // Choose whether you can drag to open on touch screens,
    onOpen: function(el) { /* Do Stuff */ }, // A function to be called when sideNav is opened
    onClose: function(el) { /* Do Stuff */ }, // A function to be called when sideNav is closed
});