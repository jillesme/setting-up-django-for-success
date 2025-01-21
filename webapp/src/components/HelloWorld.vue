<script setup lang="ts">
import { ref, inject } from 'vue'

const props = defineProps<{ isAuthenticated: boolean, count?: number }>()
const csrfToken = inject<string>('csrfToken')
const count = ref(props.count || 0)

async function increment() {
  if (!props.isAuthenticated || !csrfToken) return;

  try {
    await fetch('/api/me/count', {
      credentials: 'include',
      method: 'PATCH',
      headers: {
        'mode': 'same-origin',
        'X-CSRFToken': csrfToken
      },
    })
    count.value++
  } catch (error) {
    console.error(error)
  }
}
</script>

<template>
    <button type="button" @click="increment" :disabled="!isAuthenticated">count is {{ count }}</button>
</template>
