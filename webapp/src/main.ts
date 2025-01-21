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

createApp(HelloWorld, getComponentProps('#homepage-count-button-props'))
    .mount('#homepage-count-button')
