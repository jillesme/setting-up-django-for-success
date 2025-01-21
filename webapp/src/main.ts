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

function getCsrfToken() {
    const csrfToken = document.querySelector('meta[name="csrf-token"]')?.getAttribute('content');
    if (!csrfToken) {
        throw new Error('CSRF token not found');
    }
    return csrfToken;
}

createApp(HelloWorld, getComponentProps('#homepage-count-button-props'))
    .provide('csrfToken', getCsrfToken())
    .mount('#homepage-count-button')
