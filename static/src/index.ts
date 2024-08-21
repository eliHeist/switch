import Alpine from "alpinejs";
import mask from "@alpinejs/mask"
import collapse from "@alpinejs/collapse"
import 'htmx.org';

import './main.scss';

Alpine.plugin(mask)
Alpine.plugin(collapse)

Alpine.start()



// buttons ===================
const loaderButtons = document.querySelectorAll('.load-btn') as NodeListOf<HTMLButtonElement>

loaderButtons.forEach((button: HTMLElement) => {
    const loader = document.createElement('div') as HTMLDivElement
    loader.classList.add('button--loader')
    loader.innerHTML = `<div></div><div></div><div></div>`
    button.appendChild(loader)
});


