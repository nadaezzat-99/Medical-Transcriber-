/**
 * 
 * Manipulating the DOM exercise.
 * Exercise programmatically builds navigation,
 * scrolls to anchors from navigation,
 * and highlights section in viewport upon scrolling.
 * 
 * Dependencies: None
 * 
 * JS Version: ES2015/ES6
 * 
 * JS Standard: ESlint
 * 
*/

/**
 * Define Global Variables
 * 
*/
 let sections = document.querySelectorAll('section');
 const nav_List = document.querySelector('ul');
 let Count_Clicks=4;
 let listItems;
 let navLinks ;

/**
 * End Global Variables
 * Start Helper Functions
 * 
*/

//creat nav_list_item
function nav_list_item(i){
    let htmlTextToAdd_1 =`<li class="navbar__menu li"><a class="active" href="#section${(i+1)}">Section ${(i+1)}</a></li>` ;
    nav_List.insertAdjacentHTML('beforeend',htmlTextToAdd_1 );
}

// build the nav
function buildNav() {
    for (let i = 0; i <4; i++) {
        nav_list_item(i);}
    let htmlTextToAdd_2='<button id="new_section" type="button">Add new section!</button>';
    nav_List.insertAdjacentHTML('beforeend',htmlTextToAdd_2 );
}
     
//  function to ADD new_section
function add_new_section(i)  {
          nav_list_item(i-1)
          nav_List.appendChild(document.getElementById('new_section'));
          const main=document.querySelector('main');
          let htmlTextToAdd_3=` <section id="section${(i)}" data-nav="Section ${(i)}" class="your-active-class"><div class="landing__container"><h2>Section ${(i)}</h2><p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi fermentum metus faucibus lectus pharetra dapibus. Suspendisse potenti. Aenean aliquam elementum mi, ac euismod augue. Donec eget lacinia ex. Phasellus imperdiet porta orci eget mollis. Sed convallis sollicitudin mauris ac tincidunt. Donec bibendum, nulla eget bibendum consectetur, sem nisi aliquam leo, ut pulvinar quam nunc eu augue. Pellentesque maximus imperdiet elit a pharetra. Duis lectus mi, aliquam in mi quis, aliquam porttitor lacus. Morbi a tincidunt felis. Sed leo nunc, pharetra et elementum non, faucibus vitae elit. Integer nec libero venenatis libero ultricies molestie semper in tellus. Sed congue et odio sed euismod.</p><p>Aliquam a convallis justo. Vivamus venenatis, erat eget pulvinar gravida, ipsum lacus aliquet velit, vel luctus diam ipsum a diam. Cras eu tincidunt arcu, vitae rhoncus purus. Vestibulum fermentum consectetur porttitor. Suspendisse imperdiet porttitor tortor, eget elementum tortor mollis non.</ </div></section>`
          main.insertAdjacentHTML('beforeend', htmlTextToAdd_3);
}

//function to calculate number of clicks to add the new section
function num_clicks() {
    Count_Clicks ++;
    add_new_section(Count_Clicks);
}

// Adding class 'active' to section and Activating the navigation item when near top of viewport 
function section_Active(section, index) {
    const { top } = section.getBoundingClientRect();
    if (top <= 100 && top >= -100){
        listItems[index].setAttribute('style', 'background: rgb(96, 203, 245);')
        for (let i = 0; i < listItems.length; i++) {
            if (i !== index) 
                listItems[i].setAttribute('style','color:#fff;')}
        section.classList.add('your-active-class');    
        for (let i = 0; i < sections.length; i++) {                    // remove  style class from other unactive sections 
            if (index !== i) sections[i].classList.remove('your-active-class');
        }
    }
}

function activation() {
    for (let i = 0; i < listItems.length; i++) {
        section_Active(sections[i], i);
    }}

// Scroll to anchor ID using scrollTO event
 function scrollListener(event) {
    //event.preventDefault();
    const section =document.getElementById(event.target.getAttribute("href").split('#')[1]);
    section.scrollIntoView({ behavior: 'smooth' });
  }

// Add 'scroll 'event to nav_items 
 function add_anchor(){
    for (let i = 0; i < navLinks.length; i++) 
    navLinks[i].addEventListener('click', scrollListener);
 }

 // scroll up button clicked
 function scrollToTop() {
    window.scrollTo({top: 0, behavior: 'smooth'});
}
/**
 * End Main Functions
*/
// Build menu 
buildNav();
document.getElementById('new_section').addEventListener('click',num_clicks) ;
listItems = document.querySelectorAll('li');
navLinks=document.querySelectorAll('a');
add_anchor();
document.addEventListener('scroll', activation);
document.getElementById('top_button').addEventListener('click', scrollToTop);



