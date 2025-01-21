<script setup lang="ts">
import { ref, inject } from 'vue'

const props = defineProps<{ isAuthenticated: boolean, count?: number }>()
const csrfToken = inject<string>('csrfToken')
const count = ref(props.count || 0)

async function increment() {
  try {
    const response = await fetch('/api/me/count', {
      credentials: 'same-origin',
      mode: 'same-origin',
      method: 'PATCH',
      headers: {
        'X-CSRFToken': csrfToken as string
      },
    })
    if (response.ok) {
      const data: { updatedCount: number } = await response.json()
      count.value = data.updatedCount
    }
  } catch (error) {
    console.error(error)
  }
}
</script>

<template>
    <button type="button" @click="increment" :disabled="!isAuthenticated">count is {{ count }}</button>
</template>
