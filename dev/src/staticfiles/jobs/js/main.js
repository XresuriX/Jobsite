// grab everything we need
const btn = document.querySelector(".mobile-menu-button");
const sidebar = document.querySelector(".sidebar");
const nav_left_vertical_narrow = document.querySelector(".nav-left-vertical-narrow");

// add our event listener for the click
btn.addEventListener("click", () => {
  sidebar.classList.toggle("-translate-x-full");
});

const btn2 = document.querySelector(".hide-sidebar");

// add our event listener for the click
btn2.addEventListener("click", () => {
  //sidebar.classList.toggle("ease-in-out");
  //sidebar.classList.toggle("duration-1000");
  //sidebar.classList.toggle("hidden");
  //sidebar.classList.toggle("w-64");
  //sidebar.classList.toggle("px-2");
  //sidebar.classList.toggle("space-x-2");
  //sidebar.classList.toggle("md:translate-x-0");
  
  // hides but is still in the DOM so new nav sits after its ghost, damn
  //sidebar.classList.toggle("md:-translate-x-full");
  
  // removes it from the DOM, but puts hidden in the class list that is still there later and causes problem when toggling other menu button, can't bring back original nav
  sidebar.classList.toggle("hidden");
  
  //sidebar.classList.toggle("duration-1000");
  //sidebar.classList.toggle("md:w-0");
  //top-nav-and-content.classList.toggle("md:w-full");
  //top-nav-and-content.classList.toggle("md:w-screen");
  
  // exclude altogether for now
  nav_left_vertical_narrow.classList.toggle("hidden");
  
  
  
  
  
});


// a link for nav with subs
const btn_features = document.querySelector(".features-toggle");

const featuresNavSubs = document.querySelector(".features-nav-subs");

//const nav_left_vertical_narrow = document.querySelector(".nav-left-vertical-narrow");

btn_features.addEventListener("click", () => {
  
  //featuresNavSubs.classList.toggle("hidden");
  //featuresNavSubs.classList.toggle("transition");
  //featuresNavSubs.classList.toggle("delay-150");
  //featuresNavSubs.classList.toggle("duration-300");
  //featuresNavSubs.classList.toggle("ease-in-out");
  
});


function myFunction() {
  // remove what is already there so that transform class can be added in at start 
  featuresNavSubs.classList.remove("features-nav-subs");
  featuresNavSubs.classList.remove("px-6");
  //featuresNavSubs.classList.toggle("hidden");
  
  featuresNavSubs.classList.add("transform");
  featuresNavSubs.classList.add("delay-100");
  //featuresNavSubs.classList.toggle("hidden");
  
  //featuresNavSubs.classList.add("hover");
  //featuresNavSubs.classList.toggle("rotate-90");
  featuresNavSubs.classList.toggle("translate-x-12");
  featuresNavSubs.classList.add("transition");
  featuresNavSubs.classList.add("duration:1000");
  // add back the classes at end of transform classes
  featuresNavSubs.classList.add("features-nav-subs");
  featuresNavSubs.classList.add("px-6");
  //featuresNavSubs.classList.toggle("hidden");
}