// 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
import './index.css'

import { createApp } from 'vue'
import router from './router'
import App from './App.vue'

import {
  Button,
  Card,
  Input,
  setConfig,
  frappeRequest,
  resourcesPlugin,
} from 'frappe-ui'

let app = createApp(App)

setConfig('resourceFetcher', frappeRequest)

app.use(router)
app.use(resourcesPlugin)

app.component('Button', Button)
app.component('Card', Card)
app.component('Input', Input)

app.mount('#app')
