function animate() {
  // Only animate elements in the currently visible/active view
  const activeView = document.querySelector('.view.active')
  const scope = activeView || document
  const animateElements = scope.querySelectorAll('.animate')

  animateElements.forEach((element, index) => {
    setTimeout(() => {
      element.classList.add('show')
    }, index * 150)
  });
}

document.addEventListener("DOMContentLoaded", animate)
document.addEventListener("astro:after-swap", animate)