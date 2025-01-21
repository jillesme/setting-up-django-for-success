import { createApp } from 'vue'
import HelloWorld from "./components/HelloWorld.vue";

function getComponentProps(selector: string) {
    const element = document.querySelector(selector);
    if (!element?.textContent) return {};
    try {
        return JSON.parse(element.textContent)
    } catch (e) {
        return {}
    }
}

const csrfToken = document.querySelector('meta[name="csrf-token"]')?.getAttribute('content');

createApp(HelloWorld, getComponentProps('#homepage-count-button-props'))
    .provide('csrfToken', csrfToken)
    .mount('#homepage-count-button')
